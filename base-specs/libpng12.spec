#
# spec file for package libpng12
#
# Copyright (c) 2007, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#

%define OSR delivered in s10:0

Name:         libpng10
License:      libpng
Group:        System/Libraries
Version:      1.2.49
Release:      1
Distribution: Java Desktop System
Vendor:       Sun Microsystems, Inc.
Summary:      Portable Network Graphics library
Source:       ftp://ftp.simplesystems.org/pub/png/src/libpng-%{version}.tar.bz2
URL:          http://www.libpng.org/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on

%description
libpng is a C library for working with PNG (Portable Network Graphics) format
images.

%package devel
Summary: Headers for developing programs that will use libpng
Group:      Development/Libraries
Requires:   %{name}

%description   devel
This package contains the headers that programmers will need to develop
applications which will use libpng

%prep
%setup -q -n libpng-%{version}

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
./configure \
	--prefix=%{_prefix} \
        --libdir=%{_libdir} \
        --bindir=%{_bindir} \
	--sysconfdir=%{_sysconfdir} \
        --with-esd-prefix=%{_prefix} \
	--mandir=%{_mandir}
make -j $CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT

# delete libtool .la files and static libs
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/*la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr (-, root, root)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/pkgconfig
%{_bindir}/*-config
%{_mandir}/*

%changelog
* Mon Apr 30 2012 - padraig.obriain@oracle.com
- bump to 1.2.49
* Wed Aug 17 2011 - laszlo.peter@oracle.com
- bump to 1.2.46
* Wed Jul 21 2010 - laszlo.peter@oracle.com
- bump to 1.2.44
* Tue Jul 28 2009 - christian.kelly@sun.com
- Bump to 1.2.38.
* Sun Mar 22 2009 - laca@sun.com
- bump to 1.2.35
* Thu May 17 2007 - laca@sun.com
- Create
