#
# spec file for package SUNWevolution-bdb-devel
#
# Copyright (c) 2004 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc

Name:                    SUNWevolution-bdb-devel
License:                 Sleepycat License
IPS_package_name:        %name
Summary:                 BerkeleyDB development
Version:                 4.7.25
Source:                  evolution-bdb47-devel-files.tar.bz2
SUNW_BaseDir:            %{_basedir}
SUNW_Category:           DontShipMe
SUNW_Copyright:%{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}
cd $RPM_BUILD_ROOT%{_includedir}/
bzcat %SOURCE | tar xf -
install -d $RPM_BUILD_ROOT%{_libdir}
cd $RPM_BUILD_ROOT%{_libdir}
ln -s libdb.so.5 libdb.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Wed Nov 19 2008 - jeff.cai@sun.com
- Bump to 4.7.25
* Wed Apr 02 2008 - jeff.cai@sun.com
- Add copyright file.
* Sat Nov 11 2006 - damien.carbery@sun.com
- Change pkg category to DontShipMe, removing underscores, as the category must
  be alphanumeric.
* Fri Nov 10 2006 - laca@sun.com
- set the pkg category to dont_ship_me; this will result in an error
  if we accidentally try to integrate it into Solaris
* Wed Jul 26 2006 - halton.huo@sun.com.
- Initial version created.


