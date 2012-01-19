#
# spec file for package unique
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:           libunique
License:        LGPL v2.1
Group:          System/Libraries
Version:        1.1.6
Release:        1	
Distribution:   Java Desktop System
Vendor:         Gnome Community
Summary:        A library for writing single instance applications
Source:         http://download.gnome.org/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
URL:            http://live.gnome.org/LibUnique
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Docdir:         %{_defaultdocdir}/doc
Autoreqprov:on
Prereq:        /sbin/ldconfig

Patch1:         libunique-01-fixxref-modules.diff

%define gtk2_version 2.4.0
%define pkgconfig_version 0.15.0
%define gtk_doc_version 1.1

Requires: gtk2 >= %{gtk2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: gtk-doc >= %{gtk_doc_version}
BuildRequires: pkgconfig >= %{pkgconfig_version}

%description
LibUnique is a library for writing single instance applications, that is
applications that are run once and every further call to the same binary
either exits immediately or sends a command to the running instance.

LibUnique can be compiled against various backends, to allow the usage of
different IPC mechanisms depending on the platform.

%package devel
Summary:        unique development headers
Group:          Development/Libraries

%description devel
unique development headers

%prep
%setup -q
%patch1 -p1

#FIXME: remove uncompatible m4 files
rm -f build/autotools/lt~obsolete.m4
rm -f build/autotools/ltoptions.m4
rm -f build/autotools/libtool.m4
rm -f build/autotools/ltsugar.m4
rm -f build/autotools/ltversion.m4

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

libtoolize --force
aclocal $ACLOCAL_FLAGS  -I build/autotools
autoheader
automake -a -c -f
autoconf

./configure --prefix=%{_prefix}         \
            --bindir=%{_bindir}         \
            --libdir=%{_libdir}         \
            --includedir=%{_includedir} \
            --sysconfdir=%{_sysconfdir} \
            --mandir=%{_mandir}         \
            --enable-introspection=no   \
            %{gtk_doc_option}           \
%if %debug_build
            --enable-debug=yes          \
%else
            --enable-debug=no           \
%endif

# FIXME: hack: stop the build from looping
#touch po/stamp-it

make -j $CPU

%install
make install DESTDIR=$RPM_BUILD_ROOT
#Clean up unpackaged files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/unique/*

%changelog
* Tue Jan 12 2010 - christian.kelly@sun.com
- Add libunique-01-fixxref-modules to fix build issue.
* Fri Nov 13 2009 - halton.huo@sun.com
- Bump to 1.1.6
* Tue Aug 25 2009 - halton.huo@sun.com
- Bump to 1.1.2
- Disable gobject-introspection because 64bit build fail
* Sat Mar 28 2009 - halton.huo@sun.com
- Bump to 1.0.8
- Remove upstreamed patch gcc-warn-flags.diff
* Sat Jan 24 2009 - halton.huo@sun.com
- Initial package
