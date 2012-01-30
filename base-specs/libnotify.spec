#
# spec file for package libnotify
#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
# bugdb: http://trac.galago-project.org/
#

%define OSR 5892:0.4

Name:         libnotify
Version:      0.4.5
Release:      1
Summary:      libnotify is a notification system for the GNOME desktop environment.

Group:        System/Libraries
License:      LGPLv2
URL:          http://www.galago-project.org/news/index.php
Distribution: java-desktop-system
Vendor:       Galago
Source:       http://www.galago-project.org/files/releases/source/libnotify/libnotify-%{version}.tar.bz2
# date:2009-01-20 owner:jedy type:feature bugid:176
Patch1:       libnotify-01-uninstalled-pc.diff

BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%define gtk2_version 2.6.0
%define dbus_version 0.36

BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: dbus-devel >= %{dbus_version}
Requires: gtk2 >= %{gtk2_version}
Requires: dbus >= %{dbus_version}

%description
Libnotify is a notification system for the GNOME desktop environment.

%prep
%setup -q
%patch1 -p1

%build
%ifos linux
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f 
autoconf
./configure --prefix=%{_prefix} \
		--bindir=%{_bindir} \
		--libdir=%{_libdir}
make -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr (-, root, root)
%doc README AUTHORS COPYING
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/pkgconfig/*
%{_includedir}/libnotify/*
%{_datadir}/gtk-doc/*

%changelog
* Mon Jun 20 2010 - yuntong.jin@sun.com
- Change owner to jouby
* Tue Dec 29 2009 - jedy.wang@sun.com
- Add 64-bit support.
* Tue Jan 20 2009 - brian.cameron@sun.com
- Add libnotify-01-uninstalled-pc.diff.
* Wed Dec 03 2008 - jedy.wang@sun.com
- Bump to 0.4.5.
* Thu Mar 25 2007 - jedy.wang@sun.com
- Initial spec
