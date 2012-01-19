#
# spec file for package SUNWfirefox-bookmark
#
# includes module(s): firefox-bookmark
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner hawklu
#
# DO NOT REMOVE NEXT LINE
# PACKAGE NOT INCLUDED IN GNOME UMBRELLA ARC
#
%include Solaris.inc
%use firefox = firefox.spec

Name:                    SUNWfirefox-bookmark
IPS_package_name:        web/data/firefox-bookmarks
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:                 Firefox's default bookmark
Version:                 %{firefox.version}
# default bookmarks for OpenSolaris
Source:                  opensolaris-default-bookmarks.html
# default bookmarks for development Solaris builds
Source1:                 firefox-default-bookmarks.html
SUNW_Copyright:          SUNWfirefox.copyright
License:                 MOZILLA PUBLIC LICENSE V1.1

SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: consolidation/desktop/gnome-incorporation
Requires: SUNWfirefox

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/
%if %option_with_indiana_branding
cp %{SOURCE} $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/bookmarks.html
%else
cp %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/bookmarks.html
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*

%changelog
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add 'License' tag
* Fri Feb 20 2009 - jeff.cai@sun.com
- Add comment to remove the output in modulediffs
* Sat Dec 20 2008 - alfred.peng@sun.com
- Change the mod bits of the bookmark file to 0644.
* Fri Nov 28 2008 - alfred.peng@sun.com
- Initial version


