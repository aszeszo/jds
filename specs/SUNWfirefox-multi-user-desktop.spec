#
# spec file for package SUNWfirefox-multi-user-desktop
#
# includes module(s): None
#
# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner migi
#
# DO NOT REMOVE NEXT LINE
# PACKAGE NOT INCLUDED IN GNOME UMBRELLA ARC
#
%include Solaris.inc
%use firefox = firefox.spec

Name:                      SUNWfirefox-multi-user-desktop
SourcePackage:             SUNWfirefox-multi-user-src
IPS_package_name:          web/browser/firefox/multi-user-desktop
Meta(info.classification): %{classification_prefix}:System/Administration and Configuration
Summary:                   Multi User Desktop optimization for Mozilla Firefox Web browser
License:                   cr_Oracle
Version:                   %{firefox.version}
Source:                    all-multi-user-desktop.js
SUNW_BaseDir:              %{_basedir}
SUNW_Copyright:            %{name}.copyright
BuildRoot:                 %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: consolidation/desktop/gnome-incorporation
Requires: SUNWfirefox

%prep
rm -rf %name-%version
mkdir %name-%version

%build

%install
rm -rf $RPM_BUILD_ROOT

# Sun Ray Optimization files
install -m 755 -d $RPM_BUILD_ROOT/usr/lib/firefox/greprefs
install -m 755 -d $RPM_BUILD_ROOT/usr/lib/firefox/defaults/pref
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/firefox/greprefs/all-multi-user-desktop.js
cd $RPM_BUILD_ROOT/usr/lib/firefox/defaults/pref/
ln -s ../../greprefs/all-multi-user-desktop.js ./all-multi-user-desktop.js 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/firefox/greprefs/all-multi-user-desktop.js
%{_libdir}/firefox/defaults/pref/all-multi-user-desktop.js

%changelog
* Thu Apr 14 2011 - Michal.Pryc@Oracle.Com
- Added symbolic link to the all-multi-user-desktop.js inside the firefox
  preference directory as the default gecko one was overriden by the firefox
  pref. Fixes CR 7035883
- Reduce number of suggestions to 3.
* Thu Jan 13 2011 - Michal.Pryc@Oracle.Com
- Created.
