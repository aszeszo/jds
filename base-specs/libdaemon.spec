#
# spec file for package libdaemon
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner padraig
#

%define OSR 6984:0.12

Name:         libdaemon
License:      LGPLv2.1
Group:        System/Libraries
Version:      0.14
Release:      1
Distribution: Java Desktop System
Vendor:       0pointer.de
Summary:      Lightweight C library for writing Unix daemons
Source:       http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
Patch1:       libdaemon-01-configure.diff
URL:          http://0pointer.de/lennart/projects/libdaemon/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:	      %{_defaultdocdir}/doc
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%description
libdaemon is a lightweight C library which eases the writing of UNIX daemons.
It consists of the following parts:

- A wrapper around fork() which does the correct daemonization procedure of 
  a process
- A wrappeer around syslog() for simpler and compatible log output to Syslog
  or STDERR
- An API for writing PID files
- An API for serializing UNIX signals into a pipe for usage with select()
  or poll()
- an API for running subprocesses with STDOUT and STDERR redirected to syslog

%package devel
Summary:      A lightweight C library for writing UNXI daemons.
Group:        Development/Libraries
Requires:     %{name} = %{version}

%description devel
libdaemon is a lightweight C library which eases the writing of UNIX daemons.
It consists of the following parts:

- A wrapper around fork() which does the correct daemonization procedure of 
  a process
- A wrappeer around syslog() for simpler and compatible log output to Syslog
  or STDERR
- An API for writing PID files
- An API for serializing UNIX signals into a pipe for usage with select()
  or poll()
- an API for running subprocesses with STDOUT and STDERR redirected to syslog

%prep
%setup -q
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

CONFLAGS="--prefix=%{_prefix} --disable-lynx"
aclocal $ACLOCAL_FLAGS -I ./m4
autoconf
automake -a -c -f
CFLAGS="$RPM_OPT_FLAGS"
./configure $CONFLAGS

make -j $CPUS

%install

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/libdaemon*a

%clean 
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files 
%defattr(-, root, root)
%{_libdir}/libdaemon*.so*

%files devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/libdaemon/*
%{_libdir}/pkgconfig/*

%changelog
* Thu Jan 28 2010 - brian.cameron@sun.com
- Bump to 0.14.
* Tue Jul 28 2009 - christian.kelly@sun.com
- Bump to 0.13.
- Add patch to fix build issue.
* Wed Aug 22 2006 - damien.carbery@sun.com
- Bump to 0.12.
* Mon May 29 2006 - padraig.obriain@sun.com
- Initial spec file for libdaemon.
