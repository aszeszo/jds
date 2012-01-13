#
# spec file for package o3read
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%define OSR 9318:0.x

Name:         o3read
License:      GPL v2
Group:        Development/Tools
Version:      0.0.4
Distribution: Java Desktop System
Vendor:       siag.nu/o3read
Summary:      A standalone converter for the OpenOffice.org swriter (*.sxw) and scalc (*.sxc) formats
Source:       http://siag.nu/pub/o3read/%{name}-%{version}.tar.gz
#date:2008-08-01 owner:jefftsai type:branding
Patch1:       o3read-01-man.diff
URL:          http://siag.nu/o3read/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:	      %{_datadir}/doc 

%description
This is a standalone converter for the OpenOffice.org swriter (.sxw)
and scalc (.sxc) formats.

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

make -j $CPUS INTLLIBS= GMSGFMT=msgfmt

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp o3read $RPM_BUILD_ROOT/usr/bin
cp o3totxt $RPM_BUILD_ROOT/usr/bin
cp o3tohtml $RPM_BUILD_ROOT/usr/bin
cp utf8tolatin1 $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
cp o3read.1 $RPM_BUILD_ROOT/usr/share/man/man1
cp o3totxt.1 $RPM_BUILD_ROOT/usr/share/man/man1
cp o3tohtml.1 $RPM_BUILD_ROOT/usr/share/man/man1
cp utf8tolatin1.1 $RPM_BUILD_ROOT/usr/share/man/man1

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%{_bindir}/o3read
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_bindir}/o3*

%changelog
* Fri Jul 4 2008 - jerry.tan@sun.com
- Created spec file for o3read
