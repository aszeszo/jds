#
# spec file for package libmusicbrainz
#
# Copyright (c) 2005, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# Bugdb: http://bugs.musicbrainz.org/ticket/
#

%define OSR 13113:3.0.2

Name:         libmusicbrainz
License:      LGPL v2.1
Group:        System Environment/Libraries
Version:      3.0.3
Release:      1
Distribution: Java Desktop System
Vendor:       musicbrainz.org
Summary:      Software library for accessing MusicBrainz servers
Source:       http://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz 
# date:2010-10-05 owner:yippi type:bug bugid:5801
Patch1:       libmusicbrainz-01-compile.diff
URL:          http://musicbrainz.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD-ROMs.

%package devel
Summary: Headers for developing programs that will use libmusicbrainz
Group:      Development/Libraries
Requires:   %{name}

%description   devel
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.

%prep
%setup -q
%patch1 -p1

mv AUTHORS.txt AUTHORS
mv COPYING.txt COPYING
mv README.txt README

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

%if %debug_build
%define build_type Debug
%else
%define build_type Release
%endif

export LDFLAGS="%_ldflags -i -lCstd -lCrun"

cmake   -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}                          \
        -DCMAKE_BUILD_TYPE=%{build_type}                                \
        -DCMAKE_C_COMPILER:FILEPATH=$(CC)                               \
        -DCMAKE_C_FLAGS:STRING="%optflags"                              \
        -DCMAKE_CXX_COMPILER:FILEPATH=$(CXX)                            \
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="%cxx_optflags -O4"            \
        -DCMAKE_VERBOSE_MAKEFILE=1
make

%install
make install DESTDIR=$RPM_BUILD_ROOT CMAKE_INSTALL_PREFIX=/usr

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Oct 04 2010 - brian.cameron@oracle.com
- Bump to 3.0.3.
* Wed Dec 23 2009 - ke.wang@sun.com
- Add cxx_optflags to fix bugster #6911844 - Invalid RUNPATH and RPATH in
  SUNWmusicbrainz.
* Mon Nov 30 2009 - ke.wang@sun.com
- Use SunStudio as C++ compiler instead of g++.
* Wed Nov 18 2009 - ke.wang@sun.com
- Bump to 3.0.2
* Mon May 14 2006 - damien.carbery@sun.com
- Bump to 2.1.5. Remove upstream patch, 01-fixduration.
* Mon Jan 22 2006 - brian.cameron@sun.com
- Add patch comments.
* Thu Nov 30 2006 - brian.cameron@sun.com
- Bump to 2.1.4.
* Fri Jul 21 2006 - brian.cameron@sun.com
- Add patch to fix calculation of track durations on Solaris.
* Tue Jul 11 2006 - brian.cameron@sun.com
- Bump to 2.1.3.
* Wed Jan 04 2006 - damien.carbery@sun.com
- Specify include dir in CFLAGS so configure finds expat files. And lists the
  dir in Makefiles.
* Tue Jan 03 2006 - damien.carbery@sun.com
- Bump to 2.1.2.
* Mon Jul 25 2005 - balamurali.viswanathan@wipro.com
- Change the name of the spec file to libmusicbrainz.spec
* Wed Jun 15 2005 - balamurali.viswanathan@wipro.com
- Initial spec file checkin
