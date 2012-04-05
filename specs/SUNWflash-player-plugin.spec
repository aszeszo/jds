#
# spec file for package SUNWflash-player-plugin
#
# includes module(s): Flash Player Plugin
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner leon.sha

%define OSR LFI 138605, 138638, 150241:n/a

#
# DO NOT REMOVE NEXT LINE
# PACKAGE NOT ARC REVIEWED BY SUN JDS TEAM
#
#####################################
##     Package Defines Section     ##
#####################################

%define minname flashplayer

#####################################
##   Package Information Section   ##
#####################################

%include Solaris.inc
%define _plugindir %{_libdir}/firefox/plugins

Name:		SUNWflash-player-plugin
IPS_package_name: web/browser/firefox/plugin/firefox-flashplayer
Meta(info.classification): %{classification_prefix}:Applications/Plug-ins and Run-times
Summary:	Adobe Flash Player plugin
Version:	11.2.202.223
Release:	4
Copyright:	Commercial
License:        Commercial
Vendor:         Adobe
Packager:	SCERI/Desktop 
Source:		%{minname}-%{version}-bin-solaris.tar.gz
URL:		http://www.adobe.com
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include desktop-incorporation.inc
SUNW_Category:  FLASH,FIREFOX,application,%{jds_version}
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
Requires:       library/desktop/gtk2
Requires:       system/library
Requires:       web/browser/firefox
Requires:       system/library/math
BuildRequires:  compatibility/packages/SUNWxwplt
BuildRequires:  library/desktop/gtk2

#####################################
##   Package Description Section   ##
#####################################

%description
Adobe Flash Player Plug-in for Solaris

%prep
#####################################
##   Package Preparation Section   ##
#####################################

%setup -q -n %{minname}

%build
# we just get the bits tarball from developer

%install
%ifarch sparc
cd sparc
%else
cd x86
%endif
install -d $RPM_BUILD_ROOT%{_plugindir}
install --mode=0755 libflashplayer.so $RPM_BUILD_ROOT%{_plugindir}/

%clean
rm -rf $RPM_BUILD_ROOT

#####################################
##      Package Files Section      ##
#####################################

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%ips_tag(com.oracle.elfsign=false) %{_plugindir}/*

%actions
depend fmri=pkg:/web/firefox/plugin/flash@10.1.82.76-1 type=optional

%changelog
* Wed Mar 28 2012 leon.sha@oracle.com
- Bump to 11.2.202.223 (CR 7157311).
* Mon Feb 20 2012 leon.sha@oracle.com
- Bump to 11.1.102.62 (CR 7146508).
- Change Requires and BuildRequires lines to IPS package names.
* Tue Nov 15 2011 leon.sha@oracle.com
- bump to 11.1.102.56 (CR 7111023).
* Thur Oct 27 2011 leon.sha@oracle.com
- bump to 11.0.1.152 (CR 7104985).
* Mon Sep 26 2011 leon.sha@oracle.com
- bump to 10.3.183.10 (CR 7093649).
* Thu Aug 11 2011 leon.sha@oracle.com
- bump to 10.3.183.5 (CR7069157).
* Fri May 13 2011 leon.sha@oracle.com
- bump to 10.3.181.26 (CR7051877).
* Fri May 13 2011 leon.sha@oracle.com
- bump to 10.3.181.14 (CR7036536).
* Tue Apr 19 2011 leon.sha@oracle.com
- bump to 10.2.159.1 (CR7035896).
* Fri Mar 25 2011 leon.sha@oracle.com
- bump to 10.2.153.1 (CR7028036).
* Fri Nov 12 2010 leon.sha@oracle.com
- bump to 10.1.102.64 (CR6995987).
* Fri Oct 29 2010 leon.sha@sun.com
- bump to 10.1.85.3 (CR6995843).
* Mon Feb 22 2010 leon.sha@sun.com
- bump to 10.0.45.2 (CR6928327).
* Wed Dec 9 2009 - leon.sha@sun.com
- bump to 10.0.42.34 (CR6908614).
* Fri Oct 16 2009 - leon.sha@sun.com
- Bug 6890475. SUNWflash-player-plugin package dependency on dynamically
  linked lib not captured.
* Fri Jul 31 2009 - leon.sha@sun.com
- bump to 10.0.32.18 (CR6866245).
* Mon Mar 30 2009 - ginn.chen@sun.com
- Correction for description and dependencies.
* Fri Feb 27 2009 - leon.sha@sun.com
- bump to 10.0.22.87 (CR6764865).
* Thu Nov 11 2008 - leon.sha@sun.com
- bump to 9.0.1510 to get security fixes(CR6766784).
* Thu Aug 07 2008 - dave.lin@sun.com
- Hack the version number from 9.0.125 9.0.1250 to fix the integration issue,
  that was caused by the incorrect version number(9.0.1124 should be 9.0.124)
  in the previous version bump.
* Thu Jul 14 2008 - leon.sha@sun.com
- bump to 9.0.125 to fix firefox3 crash bug(CR6693672).
* Thu Apr 24 2008 - dave.lin@sun.com
- bump to 9.0.1124 to get security fixes(CR6686059).
* Sun Feb 03 2008 - dave.lin@sun.com
- bump to 9.0.115 which is approved in cteam meeting
* Fri Jun 29 2007 - dave.lin@sun.com
- bump to 9.0 r47
* Mon Jan 29 2007 - dave.lin@sun.com
- bump version to 7.0.67.0(CR#6491186)
* Thu Sep 14 2006 - dave.lin@sun.com
- bump version to 7.0.66.0
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Wed Apr 19 2006 - dave.lin@sun.com
- changed spec file to fit for Vermillion,
  1, changed the installation location to firefox plugin directory
  2, changed wording to "firefox" 
  3, changed pkg category
* Mon Apr 10 2006 - damien.carbery@sun.com
- Add MOZ17 to category in order for scripts to package this module.
* Mon Mar 20 2006 - Dave Lin <dave.lin@sun.com>
- Update version to 7.0.63.0
* Wed Nov 02 2005 - Dave Lin <dave.lin@sun.com>
- Update version to 7.0.61
- Change SUNW_Category to FLASH7,application,JDS3
- Make other necessary changes to fit for S10U1
* Mon Jul 12 2004 - <shirley.woo@sun.com>
- Move install location from /usr to /usr/sfw to be consistent with Mozilla
* Thu Jun 17 2004 - <shirley.woo@sun.com>
- changed SUNW_Category to FLASH6,application,JDS2
* Thu Jun 17 2004 - <shirley.woo@sun.com>
- initial creation



