#
# spec file for package cairomm 
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#

%define OSR 8314:1.4.6

Name:                    cairomm
License:		 LGPL
Group:			 System/Libraries
Version:                 1.8.2
Release:		 1
Distribution:		 Java Desktop System
Vendor:			 cairographics.org/cairomm
Summary:                 cairomm - C++ API for the Cairo Graphics Library
URL:                     http://cairographics.org/cairomm/
Source:                  http://cairographics.org/releases/cairomm-%{version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires: cairo

%package devel
Summary:                 %{summary} - development files

%prep
%setup -q -n cairomm-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir} 	\
	    --disable-python 		\
	    --disable-docs
make -j$CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Copied the example programs and binaries for testing
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/pdf-surface
cp examples/surfaces/pdf-surface.cc $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/pdf-surface
cp examples/surfaces/.libs/pdf-surface $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/pdf-surface

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/png-file
cp examples/surfaces/image-surface.cc $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/png-file
cp examples/surfaces/.libs/image-surface $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/png-file

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/ps-surface
cp examples/surfaces/ps-surface.cc $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/ps-surface
cp examples/surfaces/.libs/ps-surface $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/ps-surface

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/svg-surface
cp examples/surfaces/svg-surface.cc $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/svg-surface
cp examples/surfaces/.libs/svg-surface $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/svg-surface

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/text-rotate
cp examples/text/text-rotate.cc $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/text-rotate
cp examples/text/.libs/text-rotate $RPM_BUILD_ROOT/%{_datadir}/doc/cairomm/examples/text-rotate

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Mar 12 2008 - damien.carbery@sun.com
- Bump to 1.4.8.
* Tue Feb 19 2008 - ghee.teo@sun.com
- Modified according to review comments.
* Fri Feb 08 2008 - ghee.teo@sun.com
- Modified SFEcairomm.spec to make SUNWcairomm.spec and cairomm.spec
