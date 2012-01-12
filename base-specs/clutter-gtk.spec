#
# spec file for package clutter-gtk
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%define OSR 12687:0.8.3

Summary:      clutter-gtk - GTK+ integration library for clutter
Name:         clutter-gtk
Version:      0.10.8
Release:      1
License:      LGPLv2.1
Group:        System/Libraries
Distribution: Java Desktop System
Vendor:       clutter-project.org
Source:	      http://www.clutter-project.org/sources/clutter-gtk/0.10/clutter-gtk-%{version}.tar.bz2
Patch1:	      clutter-gtk-01-introspection.diff
URL:          http://www.clutter-project.org/
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n clutter-gtk-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
./configure --prefix=%{_prefix}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --disable-static
make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*

%changelog
* Fri Oct 22 2010 - brian.cameron@oracle.com
- Bump to 0.10.8.
* Tue Jun 01 2010 - brian.cameron@oracle.com
- Bump to 0.10.4.
* Thu Mar 18 2010 - christian.kelly@sun.com
- Add clutter-gtk-01-deprecated.diff.
* Tue Aug 25 2009  lin.ma@sun.com
- Bump to 0.10.2
* Fri Jun 26 2009  chris.wang@sun.com
- Change patch and spec owner to lin
* Mon Feb 23 2009  chris.wang@sun.com
- Bump to 0.8.3 version
* Tue Jul  1 2008  chris.wang@sun.com
- Initial build.


