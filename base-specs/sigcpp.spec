#
# spec file for package sigcpp
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet 
#

%define OSR 8309:2.x

Name:                    libsigc++
License:                 LGPL v2.1
Group:                   System/Libraries
Version:                 2.2.8
Release:                 1
Distribution:            Java Desktop System
Vendor:                  Sourceforge
Summary:                 Libsigc++ - a library that implements a typesafe callback system for standard C++
URL:                     http://libsigc.sourceforge.net
Source:                  http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.2/%{name}-%{version}.tar.bz2
#Patch1:                  sigcpp-01-build-fix.diff
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n libsigc++-%version
#%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
perl -pi -e 's/(\s*#define SIGC_TYPEDEF_REDEFINE_ALLOWED.*)/\/\/$1/' \
    sigc++/macros/signal.h.m4
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}       \
            --sysconfdir=%{_sysconfdir}
make -j$CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 2.2.8.
* Tue Apr 20 2010 - christian.kelly@oracle.com
- bump to 2.2.6.
* Sat Apr  3 2010 - christian.kelly@sun.com
- Bump to 2.2.5.
* Fri Sep 04 2009 - brian.lu@sun.com
- Change owner to gheet since Elaine is on vacation
* Thu Sep 03 2009 - dave.lin@sun.com
- Bump to 2.2.4.2
* Tue Sep 01 2009 - dave.lin@sun.com
- Bump to 2.2.4.1
* Thu Aug 27 2009 - christian.kelly@sun.com
- Bump to 2.2.4.
* Mon Nov 17 2008 - elaine.xiong@sun.com
- Bump to 2.2.3.
* Mon Mar 10 2008 - damien.carbery@sun.com
- Bump to 2.2.2.
* Fri Feb 29 2008 - elaine.xiong@sun.com
- Bump to 2.2.1 that resolves build failure of 2.2.0 with CC.
* Mon Feb 25 2008 - damien.carbery@sun.com
- Bump to 2.2.0.
* Fri Feb 22 2008 - elaine.xiong@sun.com
- Include tests binaries into dev package.
* Tue Feb 12 2008 - ghee.teo@sun.com
- Clean up %files section
* Fri Feb 01 2008 - elaine.xiong@sun.com
- create. split from SFEsigcpp.spec
