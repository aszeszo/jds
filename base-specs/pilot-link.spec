#
# spec file for package pilot-link
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
# bugdb: http://bugs.pilot-link.org/
#

%define OSR 3221:0.12

Name:     	pilot-link
License:        GPL v2 LGPL v2
Group:		Applications/Communications
Version: 	0.12.5
Release:	1
Distribution:   Java Desktop System
Vendor:		Other
Summary:	PalmOS link utilities
Source:		http://downloads.pilot-link.org/%{name}-%{version}.tar.bz2
#date:2007-11-23 owner:wangke type:bug bugid:6632092
Patch1:		pilot-link-01-man.diff
#date:2008-08-07 owner:wangke type:branding
Patch2:		pilot-link-02-manpages.diff
#date:2010-08-02 owner:kewang type:bug
Patch3:		pilot-link-03-libpng.diff
URL:		http://www.pilot-link.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Autoreqprov:    on

%description
pilot-link is a suite of tools used to connect your Palm or PalmOS[tm]
compatible handheld with Unix, Linux, and any other POSIX-compatible
machine.

%package devel
Summary:	pilot-link development files.
Group:		Development/Libraries

%description devel
pilot-link is a suite of tools used to connect your Palm or PalmOS[tm]
compatible handheld with Unix, Linux, and any other POSIX-compatible
machine.
This package contains the files required for developing or building
programs that use pilot-link.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p0
%patch2 -p1
%patch3 -p1

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

#libtoolize --force
aclocal $ACLOCAL_FLAGS -I m4
autoheader
automake -a -c -f
autoconf
CFLAGS="$RPM_OPT_FLAGS"					\
./configure  --prefix=%{_prefix}			\
	     --sysconfdir=%{_sysconfdir}		\
	     --mandir=%{_mandir}			\
	     --libexecdir=%{_libexecdir}		\
	     --libdir=%{_libdir}			\
	     --includedir=%{_includedir}/libpisock	\
	     --enable-libusb				\
	     --enable-conduits

make -j $CPUS

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_datadir}/pilot-link
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/libpisock/*
%{_libdir}/pkgconfig
%{_datadir}/aclocal

%changelog
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 0.12.5.
* Fri Sep 18 2009 - ke.wang@sun.com
- Rework patch 02
* Mon Jun 22 2009 - halton.huo@sun.com
- Use ./configure instead of ./autogen.sh
* Thu Aug 07 2008 - jijun.yu@sun.com
- Add a  manpage patch.
* Fri Nov 23 2007 - jijun.yu@sun.com
- Add a patch.
* Tue Nov 13 2007 - jijun.yu@sun.com
- Bump to 0.12.3
* Wed Feb 14 2007 - jijun.yu@sun.com
- Bump to 0.12.2
* Wed Dec 13 2006 - halton.huo@sun.com
- Bump to 0.12.1
* Wed Mar  8 2006 - <laszlo.peter@sun.com>
- Initial version
