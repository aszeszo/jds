#
# spec file for package poppler
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
# bugdb: bugzilla.freedesktop.org
#

%define OSR 12956:0.3

Name:         poppler-data
License:      MIT,Adobe,GPLv2
Group:        System/Libraries
Version:      0.4.3
Release:      1 
Distribution: Java Desktop System
Vendor:       freedesktop.org
Summary:      PDF Rendering Library
Source:       http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
URL:          http://poppler.freedesktop.org/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_docdir}/%{name}
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%description
poppler-data consists of encoding files for use with poppler.  These
files allow poppler to correctly render CJK and Cyrrilic properly.

%prep
%setup -q

%build

# Nothing to make

%install
make DESTDIR=$RPM_BUILD_ROOT install datadir=%{_datadir} 

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%{_datadir}/poppler/*

%changelog
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Bump to 0.4.3.
* Thu May 13 2010 - brian.cameron@oracle.com
- Bump to 0.4.2.
* Wed Sep 30 2009 - darren.kenny@sun.com
- Bump to 0.3.0.
* Wed Dec 19 2007 - brian.cameron@sun.com
- Bump to 0.2.0.
* Fri Oct 19 2007 - damien.carbery@sun.com
- Bump to 0.1.1. Remove upstream patch 01-fixmake.
* Mon Sep 03 2007 - brian.cameron@sun.com
- Created.
