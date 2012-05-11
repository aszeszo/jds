#
# spec file for package SUNWat-spi2-core
#
# includes module(s): at-spi2-core
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan

%include Solaris.inc

Name:                    SUNWat-spi2-core
IPS_package_name:        gnome/accessibility/at-spi2-core
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
License:                 LGPL v2, MIT/X
Summary:                 Accessibility implementation on D-Bus
Version:                 2.4.1
Source:	                 http://ftp.gnome.org/pub/GNOME/sources/at-spi2-core/2.4/at-spi2-core-%{version}.tar.xz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Patch1:	                 at-spi2-core-01-configure.diff

%include default-depend.inc
%include gnome-incorporation.inc
Requires:       SUNWglib2
Requires:       SUNWdbus
Requires:       SUNWdbus-glib
Requires:       SUNWgtk2
BuildRequires:  SUNWglib2-devel
BuildRequires:  SUNWdbus-devel
BuildRequires:  SUNWdbus-glib-devel
BuildRequires:  SUNWgtk2-devel

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

%prep
%setup -q -n at-spi2-core-%{version}
%patch1 -p1

%build
#libtoolize -f
aclocal -I . -I ./m4 $ACLOCAL_FLAGS
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
            --enable-xevie=no			\
            --with-dbus-daemondir=/usr/lib      \
            %{gtk_doc_option}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d  at-spi2-core-%{version}/AUTHORS
%doc -d  at-spi2-core-%{version}/COPYING
%doc -d  at-spi2-core-%{version}/README
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/girepository-1.0/*
%{_libdir}/at-spi*
%{_libdir}/libatspi*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/at-spi2/accessibility.conf
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop

%changelog
* Thu May 03 2012 - brian.cameron@oracle.com
- Bump to 2.4.1.
* Mon Oct 24 2011 - brian.cameron@oracle.com
- Bump to 2.2.1.
* Mon Aug 15 2011 - lee.yuan@oracle.com
- Bump to 2.1.4.
* Mon Aug 23 2010 - christian.kelly@oracle.com
- Bump to 0.3.90.
* Thu Jul 01 2010 - li.yuan@sun.com
- Bump to 0.3.4.
* Fri Jun 11 2010 - li.yuan@sun.com
- Bump to 0.3.3.
* Fri Jun 04 2010 - li.yuan@sun.com
- Bump to 0.3.2
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
- Bump to 0.1.3.
* Fri Nov 20 2009 - li.yuan@sun.com
- Initial version.
