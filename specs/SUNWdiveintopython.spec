#
# spec file for package SUNWdiveintopython
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner dermot
#

%include Solaris.inc 

%define OSR 10597:5.4

Name:                    SUNWdiveintopython
IPS_package_name:        documentation/diveintopython
Meta(info.classification): %{classification_prefix}:Development/Python
License:  		 GNU Free Documentation License, v1.1
Summary:                 A book on Python programming
Version:                 5.4
#Source:                  http://www.diveintopython.org/download/diveintopython-html-%{version}.zip
Source:                  http://ftp.freebsd.org/pub/FreeBSD/ports/distfiles/diveintopython/diveintopython-html-%{version}.zip
Source1:                 diveintopython.desktop
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

Patch1:                  diveintopython-01-py26.diff
%include                 default-depend.inc
# SUNWgnome-libs needed for gnome-open command
Requires:                SUNWgnome-libs
# SUNWgnome-themes needed for gnome-devel icon
Requires:                SUNWgnome-themes-only
BuildRequires:           compress/unzip
BuildRequires:           SUNWzip

%include desktop-incorporation.inc

%prep
# source only needed in build area for %doc files
%setup -q -n diveintopython-%{version}
%patch1 -p1


%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/diveintopython
cp -r ./* $RPM_BUILD_ROOT/usr/share/doc/diveintopython
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cd $RPM_BUILD_ROOT/usr/share/applications
cp %SOURCE1 .


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/diveintopython
%{_datadir}/doc/diveintopython/*
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/diveintopython.desktop
%doc -d html/appendix fdl.html
%doc -d html/appendix fdl_aggregation.html
%doc -d html/appendix fdl_applicability.html
%doc -d html/appendix fdl_collections.html
%doc -d html/appendix fdl_combining.html
%doc -d html/appendix fdl_copying.html
%doc -d html/appendix fdl_copyinginquantity.html
%doc -d html/appendix fdl_future.html
%doc -d html/appendix fdl_howto.html
%doc -d html/appendix fdl_modifications.html
%doc -d html/appendix fdl_termination.html
%doc -d html/appendix fdl_translation.html
%doc -d py LICENSE.txt


%changelog
* Fri Nov 26 2010 - yun-tong.jin@oracle.com
- Fix D.o.o Bug 17437 - [gnome2.30] Dive Into Python Book launcher does not open file  
* Wen Feb 10 2010 - yuntong.jin@sun.com
- Refix Bug 13805  SUNWdiveintopython python interpreters path issue with osol_130
* Tue Jan 12 2009 - yuntong.jin@sun.com
- Use python2.6 explicity in py/kgp/kgp.py
* Mon Nov 24 2008 - dermot.mccluskey@sun.com
- Initial version.


