#
# spec file for package iso-codes
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#

%define OSR 9420:3.0

Name:         iso-codes
License:      LGPLv2.1
Group:        System/Base
Version:      3.21
Release:      1
BuildArch:    noarch
Distribution: Java Desktop System
Vendor:       Other
Summary:      ISO code lists and translations
Source:       ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/iso-codes-%{version}.tar.bz2
URL:          http://alioth.debian.org/projects/pkg-isocodes/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on

%description
This package provides the ISO-639 Language code list,
the ISO-3166 Territory code list,
and ISO-3166-2 sub-territory lists,
and all their translations in gettext .po form.

%prep
%setup -q -n iso-codes-%{version}

%build

aclocal $ACLOCAL_FLAGS
automake
autoconf
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_datadir}/*

%changelog
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Bump to 3.21.
* Thu Jul 15 2010 - brian.cameron@oracle.com
- Bump to 3.18.
* Mon May 03 2010 - brian.cameron@oracle.com
- Bump to 3.16.
* Tue Apr 20 2010 - brian.cameron@sun.com
- Bump to 3.15.
* Thu Jan 28 2010 - brian.cameron@sun.com
- Bump to 3.12.1.
* Sat Aug 15 2009 - christian.kelly@sun.com
- Bump to 3.10.2.
* Tue Jul 28 2009 - christian.kelly@sun.com
- Bump to 3.10.1.
* Mon Jun 08 2009 - brian.cameron@sun.com
- Bump to 3.10.
* Thu Mar 26 2009 - brian.cameron@sun.com
- Bump to 3.7.
* Fri Jun 06 2008 - brian.cameron@sun.com
- Bump to 3.0.
* Fri Dec 07 2007 - brian.cameron@sun.com
- Bump to 1.6.  Remove upstream patch iso-codes-01-msgfmt.diff.
* Sun Apr  1 2007 - laca@sun.com
- add missing aclocal call
* Sun Feb  7 2007 - laca@sun.com
- remove MSGFMT_FLAGS hack, no longer needed with the new patch
* Sun Jan 21 2007 - laca@sun.com
- bump to 1.0
* Mon Jan 16 2006 - damien.carbery@sun.com
- Update source URL to working server.
* Thu Sep 15 2005 - laca@sun.com
- Initial version
