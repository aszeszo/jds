#
# spec file for package libdiscid
#
# Copyright (c) 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
# Bugdb: http://bugs.musicbrainz.org/ticket/
#

%define OSR 13114:0.2.2

Name:         libdiscid
License:      LGPL v2.1, Public Domain
Group:        System Environment/Libraries
Version:      0.2.2
Release:      1
Distribution: Java Desktop System
Vendor:       musicbrainz.org/doc/libdiscid
Summary:      Library for creating MusicBrainz DiscIDs
Source:       http://users.musicbrainz.org/~matt/%{name}-%{version}.tar.gz
#owner:wangke date:2009-11-16 type:branding
Patch1:       libdiscid-01-solaris.diff
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on

%description
libdiscid is a C library for creating MusicBrainz DiscIDs from audio
CDs. It reads a CD's table of contents (TOC) and generates an
identifier which can be used to lookup the CD at MusicBrainz.
Additionally, it provides a submission URL for adding the DiscID to
the database.

%package devel
Summary:  %{summary} - development files
Group:    Development/Libraries
Requires: %{name}

%prep
%setup -q
cp src/disc_linux.c src/disc_solaris.c
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

libtoolize --copy --force
aclocal
autoconf -f
autoheader
automake -a -f
./configure --prefix=%{_prefix}                 \
            --bindir=%{_bindir}                 \
            --libdir=%{_libdir}                 \
            --includedir=%{_includedir}         \
            --mandir=%{_mandir}                 \
            --infodir=%{_infodir}               \
            --disable-static                    \
            --enable-shared                     \
            --disable-debug

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Nov 16 2009 - ke.wang@sun.com
- Initial spec file
