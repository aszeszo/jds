#
# spec file for package desktop-file-utils
#
# Copyright (c) 2003, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#temporarily taken from dkenny
%define owner stephen
#

%define OSR 4093:0.10

Name:			desktop-file-utils
License:		GPLv2
Group:			Development/Tools/Other 
Version:		0.20
Release:		1
Distribution:		Java Desktop System
Vendor:			freedesktop.org
Summary:		Desktop file utilities
Source:			http://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
URL:			http://www.gnome.org
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
Docdir: 		%{_defaultdocdir}/doc
Autoreqprov:		on
#owner:gheet date:2011-02-24 type:bug bugster:7021463
Patch1:                 desktop-file-utils-01-preserve-file-perm.diff

%define popt_version 1.6.4
%define glib2_version 2.2.1

Requires:      glib2 >= %{glib2_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: popt-devel >= %{popt_version}

%description
desktop-file-utils is a collection of command line tools for working with 
desktop files.

%prep
%setup -q
%patch1 -p1

%build
./configure --prefix=%{_prefix}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_prefix}/bin
%{_datadir}

%changelog
* Wed May 09 2012 - brian.cameron@oracle.com
- Bump to 0.20. 
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 0.17.
* Thu Apr 15 2010 - brian.cameron@sun.com
- Bump to 0.16.
* Thu Mar 06 2008 - brian.cameron@sun.com
- Bump to 0.15.
* Mon Dec 10 2007 - brian.cameron@sun.com
- Bump to 0.14.
* Wed Nov 29 2006 - damien.carbery@sun.com
- Bump to 0.12.
* Wed Jul 21 2006 - dermot.mccluskey@sun.com
- Bump to 0.11.
* Tue May 17 2005 - Laszlo Kovacs <laszlo.kovacs@sun.com>
- add %{_datadir} to %files.
* Fri May 06 2005 - Glynn Foster <glynn.foster@sun.com>
- Bump to 0.10.
* Tue Aug 12 2003 - Glynn Foster <glynn.foster@sun.com>
- Initial release.

