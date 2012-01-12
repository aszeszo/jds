#
# spec file for package SUNWat-spi2-atk
#
# includes module(s): at-spi2-atk
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan

%include Solaris.inc

Name:                    SUNWat-spi2-atk
IPS_package_name:        gnome/accessibility/at-spi2-atk
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
License:                 LGPL v2, MIT/X
Summary:                 Accessibility implementation on D-Bus for GNOME
Version:                 2.2.1
Source:	                 http://ftp.gnome.org/pub/GNOME/sources/at-spi2-atk/2.2/at-spi2-atk-%{version}.tar.bz2
Patch1:                  at-spi2-atk-01-configure.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires:       SUNWglib2
Requires:       SUNWdbus
Requires:       SUNWdbus-glib
Requires:       SUNWgtk2
Requires:       SUNWlxml
Requires:       SUNWlibatk
Requires:       SUNWat-spi2-core
BuildRequires:  SUNWglib2-devel
BuildRequires:  SUNWdbus-devel
BuildRequires:  SUNWdbus-glib-devel
BuildRequires:  SUNWgtk2-devel
BuildRequires:  SUNWlxml
BuildRequires:  SUNWlibatk-devel


%if %build_l10n
%package l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}
%endif

%prep
%setup -q -n at-spi2-atk-%{version}
%patch1 -p1

%build
libtoolize -f
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f
autoconf
CFLAGS="%optflags"

LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix}			\
            --libdir=%{_libdir}			\
            --bindir=%{_bindir}			\
            --sysconfdir=%{_sysconfdir}		\
            --mandir=%{_mandir}			\
            --libexecdir=%{_libexecdir}		\
            %{gtk_doc_option}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/modules/*.la

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d  at-spi2-atk-%{version}/AUTHORS
%doc -d  at-spi2-atk-%{version}/COPYING
%doc -d  at-spi2-atk-%{version}/README
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/gtk-2.0/modules/*.so
%{_libdir}/gtk-3.0/modules/*.so
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/glib-2.0/*

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Mon Oct 24 2011 - brian.cameron@oracle.com
- Bump to 2.2.1.
* Mon Aug 15 2011 - lee.yuan@oracle.com
- Bump to 2.1.4.
* Mon Aug 23 2010 - christian.kelly@oracle.com
- Bump to 0.3.90.
* Wed Aug  4 2010 - christian.kelly@oracle.com
- Bump to 0.3.6.
* Tue Aug  3 2010 - christian.kelly@oracle.com
- Fix %files.
* Thu Jul 22 2010 - li.yuan@sun.com
- Bump to 0.3.5.
* Thu Jul 01 2010 - li.yuan@sun.com
- Bump to 0.3.4.
* Fri Jun 11 2010 - li.yuan@sun.com
- Bump to 0.3.3.
* Fri Jun 04 2010 - li.yuan@sun.com
- Bump to 0.3.2.
* Sat Apr  3 2010 - christian.kelly@sun.com
- Bump to 0.1.8.
* Tue Feb 23 2010 - li.yuan@sun.com
- Bump to 0.1.7.
* Wed Feb 10 2010 - li.yuan@sun.com
- Bump to 0.1.6.
* Tue Jan 12 2010 - li.yuan@sun.com
- Bump to 0.1.5.
* Tue Dec 22 2009 - li.yuan@sun.com
- Bump to 0.1.4.
* Tue Dec 01 2009 - li.yuan@sun.com
- Bump to 0.1.3, remove at-spi2-atk-01-bridge-init.diff.
* Thu Nov 26 2009 - ke.wang@sun.com
- Added patch at-spi2-atk-01-bridge-init.diff
* Fri Nov 20 2009 - li.yuan@sun.com
- Initial version.
