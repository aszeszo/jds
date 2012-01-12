#
# spec file for package SUNWlibgnomekbd
#
# includes module(s): libgnomekbd
#
# Copyright (c) 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner ja208388
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define _sysconfdir /etc/%{_arch64}
%use libgnomekbd_64 = libgnomekbd.spec
%endif

%include base.inc
%use libgnomekbd = libgnomekbd.spec

Name:                    SUNWgnome-keyboard-libs
IPS_package_name:        library/gnome/libgnomekbd
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                 GNOME kbd library
Version:                 %{libgnomekbd.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{libgnomekbd.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include gnome-incorporation.inc
%include default-depend.inc
Requires: SUNWgtk2
Requires: SUNWlibart
Requires: SUNWlibmsr
Requires: SUNWlibxklavier
Requires: SUNWgnome-config
BuildRequires: SUNWlibm
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWlibart-devel
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWlibxklavier

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %{name}

%description devel
The libgnomekbd-devel package contains libraries and header files for
developing applications that use libgnomekbd.

%package l10n
Summary:                 %{summary} - l10n content
Requires: %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libgnomekbd_64.prep -d %name-%version/%_arch64
%endif

mkdir -p %name-%version/%{base_arch}
%libgnomekbd.prep -d %name-%version/%{base_arch}
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%ifarch amd64 sparcv9
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="$FLAG64"
export PKG_CONFIG_PATH="%{_pkg_config_path64}"
%libgnomekbd_64.build -d %name-%version/%_arch64
%endif

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH="%{_pkg_config_path}"
%libgnomekbd.build -d %name-%version/%{base_arch}

%install
%ifarch amd64 sparcv9
%libgnomekbd_64.install -d %name-%version/%_arch64
%endif

%libgnomekbd.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT 

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d  %{base_arch} libgnomekbd-%{libgnomekbd.version}/README
%doc -d  %{base_arch} libgnomekbd-%{libgnomekbd.version}/AUTHORS
%doc(bzip2) -d  %{base_arch} libgnomekbd-%{libgnomekbd.version}/COPYING.LIB
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/girepository-1.0
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%{_libdir}/%{_arch64}/girepository-1.0
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0
%{_datadir}/gir-1.0
%{_datadir}/GConf
%{_datadir}/libgnomekbd/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %dir %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %dir %{_datadir}

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %dir %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Fix packaging for libgnomekbd 3.0.0 release.
* Thu May 12 2011 - javier.acosta@oracle.com
- Fix 64-bit support
* Mon Dec 13 2010 - christian.kelly@oracle.com
- Add dep on gnome-config.
* Wed Aug 04 2010 - javier.acosta@sun.com
- Add 64-bit support and man pages
* Mon Aug 02 2010 - javier.acosta@sun.com
- second version for release plus corrections and modifications
* Fri Sep 04 2009 - suresh.chandrasekharan@sun.com
- initial version

