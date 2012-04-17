#
# spec file for package SUNWgnome-keyring
#
# includes module(s): gnome-keyring
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc
%use gnomekeyring = gnome-keyring.spec

Name:                    SUNWgnome-keyring
License: GPL v2, LGPL v2
IPS_package_name:        gnome/gnome-keyring
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Sessions
Summary:                 GNOME keyring libraries
Version:                 %{gnomekeyring.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: system/library/security/libgcrypt
Requires: service/gnome/desktop-cache
Requires: library/libtasn1
Requires: system/library/dbus
Requires: library/glib2
Requires: library/desktop/gtk2
BuildRequires: system/library/security/libgcrypt
BuildRequires: library/libtasn1
BuildRequires: system/library/dbus
BuildRequires: library/glib2
BuildRequires: library/desktop/gtk2

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc
Requires: service/postrun

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir %name-%version
%gnomekeyring.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED
export PKG_CONFIG_PATH=../gnome-keyring-%{gnomekeyring.version}/library
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"
export CFLAGS="%optflags -I/usr/sfw/include -DANSICPP"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib -norunpath"
%gnomekeyring.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gnomekeyring.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man1/*.1

rm -rf $RPM_BUILD_ROOT%{_libdir}/gnome-keyring/devel
rm -rf $RPM_BUILD_ROOT%{_libdir}/gnome-keyring/standalone
rm -rf $RPM_BUILD_ROOT%{_libdir}/gnome-keyring/*.la

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%post root
( echo 'xmlcatalog --noout --add "rewriteSystem" \' ;
  echo '"http://scrollkeeper.sourceforge.net/dtds/scrollkeeper-omf-1.0" \' ;
  echo '"file://%{_datadir}/xml/scrollkeeper/dtds" %{_sysconfdir}/xml/catalog'
) | $BASEDIR/var/lib/postrun/postrun -c JDS

%preun root
test -x $BASEDIR/var/lib/postrun/postrun || exit 0
( echo 'xmlcatalog --noout --del \' ;
  echo '"http://scrollkeeper.sourceforge.net/dtds/scrollkeeper-omf-1.0" \' ;
  echo '%{_sysconfdir}/xml/catalog'
) | $BASEDIR/var/lib/postrun/postrun -i -c JDS

%postun root
rm -rf $BASEDIR/var/lib/scrollkeeper

%files
%doc(bzip2) gnome-keyring-%{gnomekeyring.version}/COPYING
%doc(bzip2) gnome-keyring-%{gnomekeyring.version}/COPYING.LIB
%doc(bzip2) gnome-keyring-%{gnomekeyring.version}/NEWS
%doc(bzip2) gnome-keyring-%{gnomekeyring.version}/ChangeLog
%doc gnome-keyring-%{gnomekeyring.version}/AUTHORS
%doc gnome-keyring-%{gnomekeyring.version}/README
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gnome-keyring-daemon
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/gnome-keyring/*
%{_libdir}/gnome-keyring-prompt
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/dbus-1
%dir %attr (0755, root, bin) %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.gnome.keyring.service
%{_datadir}/dbus-1/services/org.freedesktop.secrets.service
%dir %attr (0755, root, other) %{_datadir}/gcr
%dir %attr (0755, root, other) %{_datadir}/gcr/ui
%{_datadir}/gcr/ui/*
%dir %attr (0755, root, other) %{_datadir}/gnome-keyring
%dir %attr (0755, root, other) %{_datadir}/gnome-keyring/introspect
%{_datadir}/gnome-keyring/introspect/*
%dir %attr (0755, root, other) %{_datadir}/gnome-keyring/ui
%{_datadir}/gnome-keyring/ui/*

%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc/*
%dir %attr(0755, root, bin) %{_mandir}

%files root
%attr (0755, root, sys) %dir %{_sysconfdir}
%defattr (-, root, sys)
%{_sysconfdir}/gconf/schemas/gnome-keyring.schemas
%{_sysconfdir}/xdg/autostart/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Jun 22 2010 - jeff.cai@sun.com
- Ship secret.service file
* Tue Jan 26 2010 - christian.kelly@sun.com
- Fix %files.
* Tue Jan 26 2010 - jeff.cai@sun.com
- Split SUNWgnome-keyring from SUNWgnome-libs


