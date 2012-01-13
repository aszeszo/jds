#
# spec file for package ncurses
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
# bugdb :
#

%define OSR 12492:5.7

Name:		ncurses
Version:	5.7
Release:  1
License:	MIT
Group:    System/Libraries
Distribution:	Java Desktop System
Vendor:		Other
Summary:  A CRT screen handling and optimization package.
Source:   http://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
# date:2008-09-12 owner:jouby type:branding
Patch0:			ncurses-01-widec.diff
# date:2009-06-06 owner:jouby type:branding bugster:6754653
Patch1:                 ncurses-02-rpath.diff
URL:		  http://www.gnu.org/software/ncurses/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Docdir:		%{_defaultdocdir}/ncurses
Autoreqprov:	on

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.

%package devel
Summary: The development files for applications which use ncurses.
Group:   Development/Libraries
Requires:     %name = %version
Autoreqprov:  on

%description devel
The header files and libraries for developing applications that use
the ncurses CRT screen handling and optimization package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod +w ANNOUNCE AUTHORS MANIFEST NEWS README

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

%define _preincludedir  /usr/include/ncurses

CFLAGS="$RPM_OPT_FLAGS"			  \
./configure 				          \
	--prefix=%{_prefix} 		    \
	--sysconfdir=%{_sysconfdir} \
  --includedir=%{_preincludedir} \
  --datadir=%{_datadir}       \
  --bindir=%{_bindir}       \
  --mandir=%{_mandir}      \
  --libdir=%{_libdir}       \
  --with-normal   \
  --with-shared   \
  --enable-rpath  \
  --enable-widec  \
%if %debug_build
  --with-debug
%else
  --without-debug
%endif

make -j $CPUS
 
%install
make DESTDIR=$RPM_BUILD_ROOT install \
    SITEPREFIX=/dummy VENDORPREFIX=/dummy PERLPREFIX=/dummy

#rm -rf $RPM_BUILD_ROOT/%{_prefix}/man
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%files
%defattr(-, root, root)
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_datadir}/terminfo/*
%{_datadir}/tabset/*

%files devel
%defattr(-, root, root)
%{_preincludedir}/*.h

%clean
rm -r $RPM_BUILD_ROOT

%changelog
* Tue Jue 02 2009 - yuntong.jin@sun.com
- change the owner to yuntong.jin
- fix bug 6754653
- fix bug 9168
- fix bug 9267
* Fri Sep 12 2008 - rick.ju@sun.com
- Add widechar support
* Mon Aug 18 2008 - rick.ju@sun.com
- use /usr/gnu as prefix
* Tue Jul 18 2008 - rick.ju@sun.com
- Initial spec file created.
