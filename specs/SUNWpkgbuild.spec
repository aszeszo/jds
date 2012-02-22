#
# spec file for package SUNWpkgbuild
#
# includes module(s): pkgbuild
#
# Copyright (c) 2010,2012 Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc

Name:         pkgbuild
IPS_Package_Name: package/pkgbuild
License:      GPLv2
URL:	      http://pkgbuild.sourceforge.net/
Version:      1.3.104
Release:      1
Summary:      pkgbuild - rpmbuild-like tool for building Solaris packages
Source:       http://prdownloads.sourceforge.net/pkgbuild/pkgbuild-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir: %{_basedir}
SUNW_Pkg:                  SUNWpkgbuild
SUNW_Copyright:            SUNW%{name}.copyright
Meta(info.classification):	%{classification_prefix}:System/Packaging
Requires:     /usr/bin/bash
BuildRequires: runtime/perl-512
Requires:     text/gnu-patch
%include desktop-incorporation.inc

%description
A tool for building Solaris packages based on RPM-like spec files.
Most features and some extensions of the spec format are implemented.
More details at http://pkgbuild.sf.net/

%prep
%setup -q -n pkgbuild-%version

%build
./configure --prefix=%{_prefix}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc COPYING AUTHORS NEWS
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%attr (0755, root, bin) %{_bindir}
%attr (0755, root, bin) %{_libdir}
%{_datadir}/%{name}
%{_mandir}

%changelog
* Tue Feb 21 2012 - laszlo.peter@oracle.com
- bump to 1.3.104, minor updates
* Mon Jul 26 2010 - laszlo.peter@oracle.com
- bump to 1.3.103
* Sun Jun  6 2010 - laszlo.peter@oracle.com
- update for the JDS
* Fri Apr 17 2009 - laca@sun.com
- add IPS Meta tags
* Fri Aug 11 2006 - <laca@sun.com>
- delete topdir stuff, we have per-user topdirs now
* Mon Aug 08 2005 - <laca@sun.com>
- add GNU Patch dependency
* Thu Dec 09 2004 - <laca@sun.com>
- Remove %topdir/* from the pkgmap and create these directories in %post
* Fri Mar 05 2004 - <laca@sun.com>
- fix %files
* Wed Jan 07 2004 - <laszlo.peter@sun.com>
- initial version of the spec file


