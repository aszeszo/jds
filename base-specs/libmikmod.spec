#
# spec file for package libmikmod
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wjs
#

%define OSR 8590:3.2.0

Name:         libmikmod
License:      LGPL
Group:        System/Libraries
Version:      3.2.0
Release:      1
Distribution: Java Desktop System
Vendor:       mikmod.raphnet.net
Summary:      libmikmod  - a portable sound library for Unix and other systems.
%define tarball_version 3.2.0-beta2
Source:       http://mikmod.raphnet.net/files/libmikmod-%{tarball_version}.tar.bz2
# date:2009-02-20 type:branding owner:mattman
Patch1:       libmikmod-01-manpage.diff
URL:          http://mikmod.raphnet.net/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on
Requires: SUNWlibms

%description
The MikMod sound library is an excellent way for a programmer to add music
and sound effects to an application. It is a powerful and flexible library,
with a simple and easy-to-learn API.

%package devel
Summary:      Headers for developing programs that will use libmikmod
Group:        Development/Libraries
Requires:     %name

%description   devel
This package contains the headers that programmers will need to develop
applications which will use libmikmod.

%prep
%setup -q -n libmikmod-%tarball_version
%patch1 -p1

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

./configure --prefix=%{_prefix}              \
            --mandir=%{_mandir}              \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --enable-shared                  \
            --disable-static

make -j$CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT

# delete libtool .la files
rm $RPM_BUILD_ROOT%{_libdir}/*la
# Remove the libmikmod.info file. No other modules install .info files.
rm -rf $RPM_BUILD_ROOT%{_prefix}/info

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr (-, root, root)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/*.so

%changelog
* Fri Feb 20 2009 - matt.keenan@sun.com
- Add manpage patch
* Tue Sep 2 2008 - william.schoofs@sun.com
- Create
