#
# spec file for package SUNWslocate
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%include Solaris.inc

%define OSR 9390:3.x

Name:			SUNWslocate
IPS_package_name: file/slocate
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:        	Finds files on a system via a central database
Version:		3.1
License:		GPL v2
Distribution:   	Java Desktop System
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:         %{name}.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
#Source:			http://slocate.trakker.ca/files/slocate-%{version}.tar.gz
Source:			http://fossies.org/unix/misc/old/slocate-%{version}.tar.gz
# date:2008-09-02 owner:wangke type:feature
Patch1:		slocate-01-makefile.diff
# date:2008-09-02 owner:wangke type:feature
Patch2:		slocate-02-string.diff
# date:2009-02-19 owner:wangke type:branding
Patch3:		slocate-03-manpages.diff
# date:2010-10-21 owner:wangke type:branding
Patch4:		slocate-04-strcasestr.diff
# date:2012-03-26 owner:gheet type:bug bugster:7152240
Patch5:		slocate-05-remove-libast.diff
Patch6:		slocate-06-compile-fix.diff
%include desktop-incorporation.inc
Requires:	system/library
Requires:	system/library/math
BuildRequires:	system/header

%description
Slocate is a security-enhanced version of locate. Just like locate,
slocate searches through a central database (updated regularly)
for files which match a given pattern. Slocate allows you to quickly
find files anywhere on your system.

%package root
Summary:		%{summary} - / filesystem
SUNW_BaseDir:		/
Requires:               system/library

%prep
%setup -q -n slocate-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
cd src
make
cd ..


%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install src/slocate $RPM_BUILD_ROOT%{_bindir}/
ln -s slocate $RPM_BUILD_ROOT%{_bindir}/updatedb
install doc/slocate.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install doc/updatedb.1 $RPM_BUILD_ROOT%{_mandir}/man1/
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man1/slocate.1
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man1/updatedb.1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/slocate/samples
install debian/updatedb.conf $RPM_BUILD_ROOT%{_datadir}/doc/slocate/samples/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/
install debian/updatedb.conf $RPM_BUILD_ROOT%{_sysconfdir}/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/slocate

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%actions
group gid=95 groupname=slocate

%files
%defattr(-,root,bin)
%attr(2755,root,slocate) %{_bindir}/slocate
%attr(-,root,slocate) %{_bindir}/updatedb
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr(0755, root, other) %{_datadir}/doc
%dir %attr(0755, root, bin) %{_datadir}/doc/slocate
%dir %attr(0755, root, bin) %{_datadir}/doc/slocate/samples
%attr (444, root, bin) %{_datadir}/doc/slocate/samples/updatedb.conf
%doc README
%doc(bzip2) LICENSE Changelog

%files root
%defattr (-, root, bin)
%attr (0755, root, sys) %dir %{_sysconfdir}
%attr (0644, root, root) %{_sysconfdir}/updatedb.conf
%defattr (-, root, sys)
%dir %{_localstatedir}
%dir %attr (0755, root, other) %{_localstatedir}/lib
%dir %attr (0750, root, slocate) %{_localstatedir}/lib/slocate

%changelog
* Mon Mar 26 2012 - Ghee.Teo@oracle.com
- Added patch -remove-libast.diff and modified -makefile.diff to fix 7152240.
* Thu Feb 19 2009 - Matt.Keenan@sun.com
- Add manpages patch for Attributes and ARC Comment
* Wed Sep 17 2008 - Jim.Li@sun.com
- Revised new copyright file
* Mon Jun 30 2008 - Jim.Li@sun.com
- initial release



