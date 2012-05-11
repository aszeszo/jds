#
# spec file for package SUNWgnome-applets
#
# includes module(s): gnome-applets, gnome-netstatus, deskbar-applet
#
# Copyright (c) 2005, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner migi
#
%include Solaris.inc
%use gapplets = gnome-applets.spec
#%use gnetstatus = gnome-netstatus.spec
#%use deskbar_applet = deskbar-applet.spec

Name:                    SUNWgnome-applets
IPS_package_name:        gnome/applet/gnome-applets
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:                 GNOME panel applets
Version:                 %{default_pkg_version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{deskbar_applet.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk3-devel
BuildRequires: SUNWlibart-devel
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWgnome-media
BuildRequires: SUNWgnome-media-devel
BuildRequires: SUNWgnome-character-map-devel
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWgnome-python26-desktop-devel
BuildRequires: library/python-2/setuptools-26
BuildRequires: release/name
BuildRequires: SUNWarc
BuildRequires: SUNWevolution-data-server-devel
BuildRequires: SUNWlibgtop
BuildRequires: SUNWgnome-icon-theme
BuildRequires: SUNWgnome-xml-share
Requires: SUNWgtk3
Requires: SUNWgnome-python26-desktop
Requires: SUNWgnome-character-map
Requires: SUNWgnome-panel
Requires: SUNWgnome-libs
Requires: SUNWgnome-media
Requires: SUNWgnome-config
Requires: SUNWgnome-vfs
Requires: SUNWgnome-component
Requires: SUNWlibpopt
Requires: SUNWlibgtop
Requires: SUNWlibgweather
Requires: SUNWdesktop-cache
Requires: SUNWevolution-data-server
Requires: SUNWhal

%if %option_without_fox
%ifarch i386
Requires: SUNWxorg-xkb
BuildRequires: SUNWxorg-xkb
%endif
%endif

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package -n SUNWgnome-internet-applets
IPS_package_name:        gnome/applet/gnome-internet-applets
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:                 %{summary} - internet
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-applets
Requires: SUNWgtk2
Requires: SUNWlibart
Requires: SUNWgnome-panel
Requires: SUNWgnome-libs
Requires: SUNWgnome-config
Requires: SUNWgnome-vfs

%package -n SUNWgnome-intranet-applets
IPS_package_name:        gnome/applet/gnome-intranet-applets
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:                 %{summary} - intranet
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-intranet-applets-root
Requires: SUNWlibglade
Requires: SUNWgnome-applets
Requires: SUNWgnome-panel
Requires: SUNWgnome-libs
Requires: SUNWgnome-config
Requires: SUNWlibms
Requires: SUNWdesktop-cache

%package -n SUNWgnome-intranet-applets-root
Summary:                 %{summary} - intranet - / filesystem
IPS_package_name:        gnome/applet/gnome-intranet-applets
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package -n SUNWgnome-mm-applets
IPS_package_name:        gnome/applet/gnome-mm-applets
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:                 %{summary} - multimedia
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-mm-applets-root
Requires: SUNWgtk2
Requires: SUNWgnome-applets
Requires: SUNWgnome-panel
Requires: SUNWgnome-media
Requires: SUNWgnome-libs
Requires: SUNWgnome-config
Requires: SUNWdesktop-cache

%package -n SUNWgnome-mm-applets-root
Summary:                 %{summary} - multimedia - / filesystem
IPS_package_name:        gnome/applet/gnome-mm-applets
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package -n SUNWgnome-utility-applets
IPS_package_name:        gnome/applet/gnome-utility-applets
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:                 %{summary} - utility
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-utility-applets-root
Requires: SUNWgtk2
Requires: SUNWgnome-python26-desktop
Requires: SUNWgnome-applets
Requires: SUNWgnome-panel
Requires: SUNWgnome-libs
Requires: SUNWgnome-config
Requires: SUNWgnome-character-map
Requires: SUNWgnome-component
Requires: SUNWgnome-vfs
Requires: SUNWevolution-data-server
Requires: SUNWdesktop-cache
Requires: SUNWhal

%package -n SUNWgnome-utility-applets-root
Summary:                 %{summary} - utility - / filesystem
IPS_package_name:        gnome/applet/gnome-utility-applets
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package -n SUNWgnome-utility-applets-devel
Summary:                 %{summary} - utility - development files
IPS_package_name:        gnome/applet/gnome-utility-applets
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%gapplets.prep -d %name-%version
#%gnetstatus.prep -d %name-%version
#%deskbar_applet.prep -d %name-%version
chmod -R u+w %{_builddir}/%name-%version

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED
export CPPFLAGS="-I/usr/sfw/include"
export CFLAGS="%optflags -I/usr/sfw/include -DANSICPP"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib -L/usr/X11/lib -R/usr/X11/lib -lX11"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

%gapplets.build -d %name-%version

export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib"

#%gnetstatus.build -d %name-%version
#%deskbar_applet.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gapplets.install -d %name-%version
#%gnetstatus.install -d %name-%version
#%deskbar_applet.install -d %name-%version

chmod 0644 $RPM_BUILD_ROOT%{_datadir}/gnome/help/*/C/*.xml

#rm -r $RPM_BUILD_ROOT%{_prefix}/var

# Never install English locales because should support full functions
# on English locales as same as Solaris. See SUNWzz-gnome-l10n.spec.
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/en_GB
rm -r $RPM_BUILD_ROOT%{_datadir}/gnome/help/*/en_GB
rm -r $RPM_BUILD_ROOT%{_datadir}/omf/*/*-en_GB.omf
rm -r $RPM_BUILD_ROOT%{_datadir}/omf/*/*-ast.omf

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%restart_fmri icon-cache gconf-cache

%files
%doc -d gnome-applets-%{gapplets.version} README stickynotes/README cpufreq/README geyes/README mini-commander/README trashapplet/README null_applet/README AUTHORS gweather/AUTHORS cpufreq/AUTHORS geyes/AUTHORS multiload/AUTHORS mini-commander/AUTHORS drivemount/AUTHORS accessx-status/AUTHORS mixer/AUTHORS modemlights/AUTHORS COPYING-DOCS accessx-status/COPYING COPYING MAINTAINERS
%doc(bzip2) -d gnome-applets-%{gapplets.version} ChangeLog NEWS geyes/NEWS mini-commander/NEWS
#%doc gnome-netstatus-%{gnetstatus.version}/README
#%doc gnome-netstatus-%{gnetstatus.version}/NEWS
#%doc gnome-netstatus-%{gnetstatus.version}/AUTHORS
#%doc gnome-netstatus-%{gnetstatus.version}/MAINTAINERS
#%doc gnome-netstatus-%{gnetstatus.version}/COPYING
#%doc(bzip2) gnome-netstatus-%{gnetstatus.version}/ChangeLog
#%doc(bzip2) gnome-netstatus-%{gnetstatus.version}/po/ChangeLog
#%doc(bzip2) gnome-netstatus-%{gnetstatus.version}/help/ChangeLog
#%doc deskbar-applet-%{deskbar_applet.version}/README
#%doc deskbar-applet-%{deskbar_applet.version}/NEWS
#%doc deskbar-applet-%{deskbar_applet.version}/AUTHORS
#%doc deskbar-applet-%{deskbar_applet.version}/MAINTAINERS
#%doc deskbar-applet-%{deskbar_applet.version}/COPYING
#%doc(bzip2) deskbar-applet-%{deskbar_applet.version}/ChangeLog
#%doc(bzip2) deskbar-applet-%{deskbar_applet.version}/po/ChangeLog
#%doc(bzip2) deskbar-applet-%{deskbar_applet.version}/help/ChangeLog

%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, sys) %{_datadir}

%defattr (-, root, bin)

%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/null_applet
%{_libdir}/trashapplet
%{_libdir}/bonobo/servers/GNOME_MiniCommanderApplet.server
%{_libdir}/gweather-applet-2

%{_libexecdir}/geyes_applet2
%{_libexecdir}/charpick_applet2
%{_libexecdir}/stickynotes_applet
%{_libexecdir}/accessx-status-applet
%{_libexecdir}/multiload-applet-2
%{_libexecdir}/battstat-applet-2

%{_datadir}/dbus-1/services/*
%{_datadir}/gnome-applets

%{_datadir}/omf/geyes/*-C.omf
%{_datadir}/omf/gweather/gweather*-C.omf
%{_datadir}/omf/char-palette/char-palette-C.omf
%{_datadir}/omf/stickynotes_applet/stickynotes_applet-C.omf
%{_datadir}/omf/accessx-status/accessx-status-C.omf
%{_datadir}/omf/trashapplet/trashapplet-C.omf
%{_datadir}/omf/multiload/multiload-C.omf
%{_datadir}/omf/battstat/battstat-C.omf
%{_datadir}/gnome-panel

%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps

%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg

%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*

%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/geyes/C
%{_datadir}/gnome/help/gweather/C
%{_datadir}/gnome/help/char-palette/C
%{_datadir}/gnome/help/stickynotes_applet/C
%{_datadir}/gnome/help/accessx-status/C
%{_datadir}/gnome/help/multiload/C
%{_datadir}/gnome/help/trashapplet/C
%{_datadir}/gnome/help/battstat/C

%files root
%defattr(-, root, sys)
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/geyes.schemas
%{_sysconfdir}/gconf/schemas/charpick.schemas
%{_sysconfdir}/gconf/schemas/stickynotes.schemas
%{_sysconfdir}/gconf/schemas/multiload.schemas
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/battstat_applet.soundlist

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/[a-c]*/[a-z]*
#%{_datadir}/gnome/help/deskbar/[a-z]*
%{_datadir}/gnome/help/[e-z]*/[a-z]*
%{_datadir}/omf/*/*-[a-z][a-z].omf
#%{_datadir}/omf/*/*-[a-z][a-z][a-z].omf
%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z][A-Z].omf

%changelog
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Fix packaging for gnome-applets 3.1.3 release.  No longer build
  gnome-netstatus or deskbar-applet since they have not been ported yet to
  GTK3.  No longer deliver multiple applet packages.
* Fri Dec 03 2010 - brian.cameron@oracle.com
- Remove the quick-lounge-applet.
* Fri Oct 22 2010 - Michal.Pryc@Oracle.Com
- Removed etc/security/* files, fixes 6932829
* Mon Nov 02 2009 - dave.lin@sun.com
- Updated the python binding dependencies to version 2.6. 
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Thu Apr 02 2009 - brian.cameron@sun.com
- Add SUNWhal as a dependency since the Battery Status applet uses it.
* Mon Mar 23 2009 - jeff.cai@sun.com
- Since /usr/lib/invest-applet (SUNWgnome-internet-applets) requires
  /usr/bin/i86/isapython2.4 which is found in SUNWPython, add the
  dependency.
- Since /usr/lib/deskbar-applet/deskbar-applet (SUNWgnome-utility-applets)
  requires /usr/bin/i86/isapython2.4 which is found in SUNWPython, add the
  dependency.
* Tue Feb 24 2009 - dave.lin@sun.com
- Fixed %{_datadir}, %{_datadir}/doc attribute issue.
* Wed Feb 18 2009 - Michal.Pryc@Sun.Com
- Fixed %files section for new quick-lounge-applet
* Tue Feb 17 2009 - Matt.Keenan@sun.com
- Bump tarball to 2.25.90, and add back mixer applet files
* Fri Jan 30 2009 - Michal.Pryc@Sun.Com
- Removed lines to remove all drivemount files, this is now done
  through reworked patch: gnome-applets-01-disable-drivemount.diff
- Temporary commented lines for mixer applet. The mixer applet will be available
  in the new tarball of gnome-applets.
* Mon Sep 15 2008 - darren.kenny@sun.com
- Removed icon dirs not being used any more.
- Added line to remove empty drivemount directory that was causing build
  error.
* Mon Sep 08 2008 - dave.lin@sun.com
- Fixed /usr/share/icons/... attribute issue for SUNWgnome-internet-applets
* Fri Aug 22 2008 - darren.kenny@sun.com
- Update for additional netstatus wireless files (icons and helper).
* Fri May 30 2008 - damien.carbery@sun.com
- Update %files for new tarballs.
* Fri May 16 2008 - jedy.wang@sun.com
- Remove panel-default-setup-laptop.entries and corresponding post and preun
  script to fix 6703518.
* Thu Feb 28 2008 - damien.carbery@sun.com
- Update %files for new tarballs.
* Tue Jan 22 2008 - damien.carbery@sun.com
- Remove Requires: SUNWgnome-internet-applets-root from
  SUNWgnome-internet-applets list.
* Thu Jan 17 2008 - damien.carbery@sun.com
- Remove SUNWgnome-internet-applets-root and SUNWgnome-internet-applets-devel
  packages as the libgweather module is in SUNWgnome-panel now.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Thu Jan  3 2008 - laca@sun.com
- use includes instead of inline scripts
* Thu Oct 11 2007 - brian.cameron@sun.com
- Fix packaging so that invest applet's python code gets installed.
  Fixes bug #6502277.
* Fri Sep 28 2007 - laca@sun.com
- delete Nevada X deps; make xorg-xkb dep dependent upon nevada X build
* Thu Sep 27 2007 - laca@sun.com
- add postrun script that rebuilds the icon cache for each package that
  installs icons
* Sat Aug 18 2007 - damien.carbery@sun.com
- Comment out removal of %{_prefix}/var dir as it's no longer created.
* Tue Aug 07 2007 - damien.carbery@sun.com
- Update l10n %files for new deskbar-applet tarball.
* Wed Aug 01 2007 - damien.carbery@sun.com
- Update %files for new tarball.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Sun Apr 15 2007 - jedy.wang@sun.com
- Ship battstat applet on sparc.
* Wed Mar 07 2007 - damien.carbery@sun.com
- Delete en_GB locale files in %install as it breaks SUNWzz-gnome-l10n build. 
* Mon Feb 19 2007 - damien.carbery@sun.com
- Add now applet back to %files.
* Sun Feb 18 2007 - glynn.foster@sun.com
- Update the install location for the python files into vendor-packages.
* Tue Jan 23 2007 - damien.carbery@sun.com
- Rename %{_datadir}/quick-lounge to quick-lounge-applet.
* Wed Jan 10 2007 - damien.carbery@sun.com
- Add deskbar help files to %files.
* Wed Jan 03 2007 - damien.carbery@sun.com
- Changes in %files for 2.17.1 update. Remove GNOME_KeyboardApplet.server as the
  base patch that creates it has been removed. Added %{_datadir}/xmodmap dir.
* Fri Nov 03 2006 - damien.carbery@sun.com
- Remove the 'rm' of invest-big.png as it is referenced in %files.
* Thu Nov 02 2006 - damien.carbery@sun.com
- Remove the invest-chart files as it is not in the UI spec (#6488895).
* Thu Oct 19 2006 - damien.carbery@sun.com
- Remove obsolete 'rm -r' calls from %install.
* Tue Oct 17 2006 - glynn.foster@sun.com
- Remove webeyes from the build. deskbar-applet is the natural
  (and better) replacement. Compatibility is preserved through 
  user migration to the new applet.
* Mon Sep 04 2006 - brian.cameron@sun.com
- Remove libical since we no longer ship the now applet.  Also
  remove -g from CFLAGS.  Not good to have on by default for
  performance.
* Fri Aug 25 2006 - damien.carbery@sun.com
- More updates to %files for new deskbar-applet tarball.
* Thu Aug 24 2006 - damien.carbery@sun.com
- Minor update to %files.
* Wed Aug 23 2006 - damien.carbery@sun.com
- Update %files for new icons.
* Wed Aug 16 2006 - damien.carbery@sun.com
- Add invest-applet to internet-applets package.
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
* Thu Aug 03 2006 - damien.carbery@sun.com
- Add 'multiload' files back to %files.
* Tue Aug 01 2006 - darren.kenny@sun.com
- Add SUNWlibgtop build dependency for multiload
* Sat Jul 29 2006 - damien.carbery@sun.com
- Remove 'multiload' files from %files.
* Fri Jul 28 2006 - damien.carbery@sun.com
- Remove 'gtik' stuff and add deskbar stuff to %files. Fix dir perms.
* Fri Jul 28 2006 - darren.kenny@sun.com
- Add multiload applet.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Sat Jul 15 2006 - glynn.foster@sun.com
- Remove gswitchit and friends.
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Tue May 09 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Wed Mar 15 2006 - damien.carbery@sun.com
- Add to Build/Requires after running check-deps.pl.
* Wed Mar 15 2006 - glynn.foster@sun.com
- Add deskbar-applet to the utility package.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Mon Feb 13 2006 - damien.carbery@sun.com
- Remove mini-commander stuff that is gone.
* Fri Jan 06 2006 - damien.carbery@sun.com
- Add internet-applets-devel for gweather files.
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Wed Oct 19 2005 - damien.carbery@sun.com
- Add SUNWgnome-doc-utils build dependency for /usr/bin/xml2po.
* Tue Sep 13 2005 - laca@sun.com
- remove unpackaged files or add to %files
* Wed Jul 13 2005 - brian.cameron@sun.com
- Split from SUNWgnome-panel.spec.
