#
# spec file for package pangomm
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         pangomm
License:      LGPL
Group:        System/Libraries
Version:      2.26.1
Release:      1
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      pangomm - C++ Interfaces for pango 
Source:       http://download.gnome.org/sources/pangomm/2.26/pangomm-%{version}.tar.bz2
URL:          http://www.gtkmm.org/
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n pangomm-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags -D_XPG4_2 -D_RWSTD_NO_WSTR -D__EXTENSIONS__"

aclocal -Ibuild
automake --add-missing
autoconf
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}
make -j$CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*


%changelog
* Tue Apr 20 2010 - christian.kelly@oracle.com
- Bump to 2.26.1.
* Thu Oct 22 2009 - dave.lin@sun.com
- Bump to 2.26.0.
- Removed the patch 01-ignore-defs.diff.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change spec and patch owner to gheet
* Fri Mar 13 2009 - dave.lin@sun.com
- Bump to 2.24.0
* Mone Feb 16 2009 - chris.wang@sun.com
- Bump to 2.14.1
* Thu Jan 08 2009 - christian.kelly@sun.com
- Bump to 2.14.0.
* Mon Nov 17 2008 - chris.wang@sun.com
- Add _RWSTD_NO_WSTR to CXXFLAG to pass SS12 build
* Fri Aug 08 2008 - damien.carbery@sun.com
- Remove reference to upstream patch glibmm-02-m4-macro.diff.
* Tue Aug 05 2008 - damien.carbery@sun.com
- Bump to 2.13.7.
* Thu Jul 24 2008 - chris.wang@sun.com
- create
