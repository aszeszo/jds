#
# spec file for package SUNWgnome-desktop-prefs
#
# includes module(s): desktop-file-utils, gnome-settings-daemon, control-center
#
# Copyright (c) 2004, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#temporarily taken from dkenny
%define owner stephen
#

# NOTE: You must set up the OpenGL symlinks before building SUNWcompiz:
#   #  /lib/svc/method/ogl-select start

%include Solaris.inc

%define with_hal %(pkginfo -q SUNWhal && echo 1 || echo 0)

%use dfu = desktop-file-utils.spec
%use gsd = gnome-settings-daemon.spec
%use cc = control-center.spec

Name:                    SUNWgnome-desktop-prefs
IPS_package_name:        gnome/preferences/control-center
Meta(info.classification): %{classification_prefix}:Applications/Configuration and Preferences
Summary:                 GNOME desktop wide preference configuration tools
Version:                 %{default_pkg_version}
License:		 GPL
Source:                  %{name}-manpages-0.1.tar.gz
# date:2007-11-07 bugster:6531454 owner:dkenny type:bug
Patch1:                  control-center-01-passwd-in-terminal.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: library/desktop/libglade
Requires: system/library/libdbus-glib
Requires: library/desktop/evolution-data-server
Requires: system/library/fontconfig
Requires: system/library/freetype-2
Requires: gnome/gnome-audio
Requires: gnome/config/gconf
Requires: library/gnome/gnome-component
Requires: gnome/gnome-panel
Requires: gnome/file-manager/nautilus
Requires: library/gnome/gnome-libs
Requires: library/audio/gstreamer
Requires: library/gnome/gnome-vfs
Requires: gnome/window-manager/metacity
Requires: library/desktop/xdg/libcanberra
Requires: system/library/math
Requires: library/popt
Requires: library/libxml2
Requires: service/gnome/desktop-cache
Requires: shell/bash
Requires: library/desktop/libxklavier
Requires: library/gnome/libgnomekbd
%if %with_hal
Requires: service/hal
%endif
Requires: library/audio/pulseaudio
Requires: x11/library/mesa
BuildRequires: x11/library/libxft
BuildRequires: library/desktop/libglade
BuildRequires: x11/library/libxscrnsaver
BuildRequires: x11/library/mesa
BuildRequires: library/audio/gstreamer
BuildRequires: library/gnome/gnome-vfs
BuildRequires: library/desktop/xdg/libcanberra
BuildRequires: library/popt
BuildRequires: gnome/window-manager/metacity
%if %option_without_fox
BuildRequires: x11/server/xorg
%endif
%if %option_with_dt
BuildRequires: library/tooltalk
%endif
BuildRequires: library/audio/pulseaudio
BuildRequires: library/desktop/evolution-data-server
BuildRequires: gnome/config/gconf
BuildRequires: library/gnome/gnome-component
BuildRequires: gnome/file-manager/nautilus
BuildRequires: gnome/gnome-panel
BuildRequires: library/gnome/gnome-libs
BuildRequires: system/library/libdbus-glib
BuildRequires: developer/gnome/gnome-doc-utils

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package  devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: library/file-monitor/gamin
                                                                                
%if %build_l10n
%package l10n
IPS_package_name:        gnome/preferences/control-center/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
%endif

%prep
rm -rf %name-%version
mkdir %name-%version
%dfu.prep -d %name-%version
%gsd.prep -d %name-%version
%cc.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -
#cd %{_builddir}/%name-%version/%{cc.name}-%{cc.version}
#%patch1 -p1
#cd ..
# Hack to make the uninstalled pc file work.
cd %{_builddir}/%name-%version/%{gsd.name}-%{gsd.version}/gnome-settings-daemon
ln -s ../data/gsd-enums.h
cd ../..

%build
export CFLAGS="%optflags -I/usr/sfw/include -I/usr/X11/include -DGNOME_DESKTOP_USE_UNSTABLE_API"
export RPM_OPT_FLAGS="$CFLAGS"
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED
export PKG_CONFIG_PATH="../gnome-settings-daemon-%{gsd.version}/data:%{_pkg_config_path}"
#FIXME: This stuff should be fixed in the component or the configure script
export LDFLAGS="%_ldflags -L/usr/X11/lib -R/usr/X11/lib -L/usr/sfw/lib -R/usr/sfw/lib -lfreetype -lresolv -lgthread-2.0"
export EMACS=no

%dfu.build -d %name-%version
%gsd.build -d %name-%version
%cc.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%dfu.install -d %name-%version
export PATH=%{_builddir}/%name-%version/desktop-file-utils-%{dfu.version}/src:$PATH
%gsd.install -d %name-%version
%cc.install -d %name-%version

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove %{_datadir}/mime until clash with SUNWgnome-vfs resolved.
#rm -r $RPM_BUILD_ROOT%{_datadir}/mime

# put real version number in gnome-control-center.1
perl -pi -e 's/%%{cc_version}/%{cc.version}/g' $RPM_BUILD_ROOT%{_mandir}/man1/gnome-control-center.1

# Remove unused PolKit files.
rm -rf $RPM_BUILD_ROOT%{_datadir}/polkit-1

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
rm -rf $RPM_BUILD_ROOT%{_datadir}/omf/*/*-[a-z][a-z].omf
rm -rf $RPM_BUILD_ROOT%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z][A-Z].omf
rm -rf $RPM_BUILD_ROOT%{_datadir}/omf/control-center/control-center-ca@valencia.omf
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/help/*/[a-z]*
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/gnome-settings-daemon-3.0
%{_libexecdir}/control-center-1
%{_libexecdir}/gnome-settings-daemon
%{_libexecdir}/gnome-fallback-mount-helper
%{_libexecdir}/gsd-locate-pointer
%{_libexecdir}/gsd-printer

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories
%{_datadir}/dbus-1
%{_datadir}/GConf
%{_datadir}/glib-2.0
%{_datadir}/gnome-control-center
%{_datadir}/gnome-settings-daemon
%{_datadir}/gnome-settings-daemon-3.0
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%{_datadir}/pkgconfig
# PulseAudio
%{_datadir}/sounds

%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/categories
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/emblems
#PulseAudio
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/status
%{_datadir}/icons/hicolor/*/apps/*.svg

%{_datadir}/icons/hicolor/*/*/slideshow-emblem.svg
%{_datadir}/icons/hicolor/*/*/slideshow-symbolic.svg
#PulseAudio
%{_datadir}/icons/hicolor/*/status/*.svg
%{_datadir}/icons/hicolor/48x48/apps/preferences-system-time.png
%{_datadir}/icons/hicolor/256x256/apps/preferences-system-time.png

#PulseAudio
%{_datadir}/icons/hicolor/48x48/apps/multimedia-volume-control.png
#PulseAudio
%{_datadir}/icons/hicolor/48x48/devices/audio-headset.svg

%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%doc desktop-file-utils-%{dfu.version}/AUTHORS
%doc desktop-file-utils-%{dfu.version}/README
%doc(bzip2) desktop-file-utils-%{dfu.version}/COPYING
%doc(bzip2) desktop-file-utils-%{dfu.version}/ChangeLog
%doc(bzip2) desktop-file-utils-%{dfu.version}/NEWS
%doc gnome-control-center-%{cc.version}/AUTHORS
%doc gnome-control-center-%{cc.version}/README
%doc(bzip2) gnome-control-center-%{cc.version}/COPYING
%doc(bzip2) gnome-control-center-%{cc.version}/ChangeLog
%doc(bzip2) gnome-control-center-%{cc.version}/NEWS
%doc gnome-settings-daemon-%{gsd.version}/AUTHORS
%doc(bzip2) gnome-settings-daemon-%{gsd.version}/COPYING
%doc(bzip2) gnome-settings-daemon-%{gsd.version}/ChangeLog
%doc(bzip2) gnome-settings-daemon-%{gsd.version}/po/ChangeLog
%doc(bzip2) gnome-settings-daemon-%{gsd.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/xdg
%{_sysconfdir}/gnome-settings-daemon

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z]*.omf
%endif

%changelog
* Fri May 11 2012 - brian.cameron@oracle.com
- Update packaging after updating to 3.4.1.
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Fix packaging for gnome-settings-daemon 3.1.3 and gnome-control-center 3.1.3
  release.
* Mon Aug 02 2010 - javier.acosta@sun.com
- Adding requires SUNWlibxklavier and SUNWgnome-keyboard-libs for Kb. Switcher
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Tue Jan 12 2010 - dave.lin@sun.com
- Remove OpenGL check, use 'Requires: SUNWxorg-mesa' instead.
* Fri May 22 2009 - dave.lin@sun.com
- set /usr/share/applications/mimeinfo.cache as type 'v' ie. %ghost to fix bug CR6842756.
* Wed Apr 29 2009 - laca@sun.com
- delete desktop-mime-cache postun script since it won't do any good
  after uninstalling update-desktop-database
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Thu Mar 05 2009 - brian.cameron@sun.com
- Change SUNWdbus-bindings to SUNWdbus-glib.
* Tue Jan 13 2009 - matt.keenan@sun.com
- Remove sound capplet reference as removed from 2.25.3 tarball
* Tue Jan 06 2009 - takao.fujiwara@sun.com
- Modify pkgmap for omf.
* Thu Sep 25 2008 - matt.keenan@sun.com
- Update copyright
* Wed Sep 17 2008 - halton.huo@sun.com
- Add script to replace real control-center version number in
  gnome-control-center.1
- Add %attr (-, root, other) for subfolders under %{_datadir}/icons
* Tue Aug 05 2008 - damien.carbery@sun.com
- Add apps_gnome_settings_daemon_xrandr.schemas to %post and %files. Remove
  hack that created mimeinfo.cache - it is not needed because gnome-vfs is
  obsolete now.
* Mon Aug 04 2008 - ghee.teo@sun.com
- Removed control-center-01-solaris-printmgr.diff now that the Presto's
  print manager is integrated into vermillion.
* Sat Jul 26 2008 - damien.carbery@sun.com
- Create mimeinfo.cache because build breaking with /dev/null in proto. Remove
  fontilus.schemas from %post and %files as it is not installed. Also remove
  %{_sysconfdir}/gnome-vfs-2.0 from %files as it is not installed either.
* Fri Jul 25 2008 - damien.carbery@sun.com
- Update %files, removing %{_libdir}/gnome-vfs-2.0/modules/*.so and
  %{_libdir}/nautilus.
* Thu Jun 05 2008 - damien.carbery@sun.com
- Remove themus.schemas as it is no longer installed.
* Wed May 21 2008 - damien.carbery@sun.com
- Add 'Requires: SUNWxorg-mesa' to base package to fix #6705123.
* Wed Apr 16 - damien.carbery@sun.com
- Add Requires SUNWgamin to devel package. Mentioned in #6688818.
* Mon Apr 07 - damien.carbery@sun.com
- Change OpenGL check to only happen on x86.
* Wed Apr 02 - damien.carbery@sun.com
- Copy in changes from gnome-2-20 branch: break the build if the openGL headers
  and libraries are not present on the machine.
* Wed Mar 12 2008 - damien.carbery@sun.com
- Update %files for new tarball.
* Tue Feb 26 2008 - brian.cameron@sun.com
- Now gnome-settings-daemon depends on gnome-desktop in the SUNWgnome-panel
  package.  So add this dependency.
* Fri Feb 15 2008 - damien.carbery@sun.com
- Remove obsolete sparc patches, 02-sun-volume-keys and 03-sun-help-key.
  Renumber rest.
* Fri Feb 15 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWdbus-bindings/-devel; Update %files for new location
  of plugins.
* Tue Jan 29 2008 - damien.carbery@sun.com
- Add -DGNOME_DESKTOP_USE_UNSTABLE_API to CFLAGS to get it to build.
* Wed Jan 23 2008 - damien.carbery@sun.com
- Set PKG_CONFIG_PATH to find the gnome-settings-daemon uninstalled.pc file.
* Wed Jan 23 2008 - darren.kenny@sun.com
- Move gnome-settings-daemon into it's own spec file to match project
  structures.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Wed Nov 07 2007 - darren.kenny@sun.com
- Add new patch control-center-04-passwd-in-terminal.diff
- This is a tempoary fix for Bug#6531454 - using gnome-terminal & passwd - the
  correct fix depends on ON RFE 6627014 being implemented.
* Tue Oct 30 2007 - laca@sun.com
- s/without_java/with_java
* Mon Oct  1 2007 - laca@sun.com
- move export EMACS=no to %build from %prep and delete emacs dir from %files
* Mon Oct  1 2007 - damien.carbery@sun.com
- Add %{_datadir}/emacs to %files.
* Fri Sep 28 2007 - laca@sun.com
- add support to build on FOX instead of Nevada X
- disable emacs support
* Wed Sep 05 2007 - darren.kenny@sun.com
- Bump to 2.19.92
- Update files sections for new version.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Thu Mar 15 2007 - damien.carbery@sun.com
- Add Requires SUNWbash after check-deps.pl run.
* Wed Feb 14 2007 - damien.carbery@sun.com
- Update %files for new tarball.
* Thu Feb  8 2007 - takao.fujiwara@sun.com
- Update control-center-01-solaris-printmgr.diff for SUN_BRANDING
* Sun Jan 28 2007 - laca@sun.com
- update dir attributes so they work on both s10 and nevada
* Wed Jan 24 2007 - damien.carbery@sun.com
- Add %{_datadir}/icons to %files.
* Tue Dec 19 2006 - ghee.teo@sun.com
- Replace the script, solaris-printmgr-wrappper to use gksu instead of sticking
  with the old CDE action script.
* Thu Dec 07 2006 - damien.carbery@sun.com
- Remove schema file from %preun root and %files as it is no longer in the 
  control-center module. Remove icons dir from %files as they are not installed.
* Fri Oct 20 2006 - damien.carbery@sun.com
- Remove SUNWhalh BuildRequires because header files are in SUNWhea in snv_51.
* Mon Sep 18 2006 - brian.cameron@sun.com
- Add SUNWhalh BuildRequires
* Tue Sep 05 2006 - brian.cameron@sun.com
- Now check for HAL so we can use --enable/disable-hal as appropriate in 
  the control-center.spec file.  Remove panel dependency now that we no
  longer link against libxklavier.
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Wed Jul 12 2006 - laca@sun.com
- set correct attributes for mimeinfo.cache, fixes #6431057
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Fri Jun 23 2006 - christopher.hanna@sun.com
- removed manpages not needed: gnome-file-types-properties and gnome-settings-daemon
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu May 25 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue Apr 18 2006 - damien.carbery@sun.com
- Add desktop-directories directory.
* Wed Apr 05 2006 - glynn.foster@sun.com
- Remove screensaver hack since xscreensaver installs into the
  right location.
* Tue Feb 21 2006 - damien.carbery@sun.com
- Add X packages to Requires after running check-deps.pl script.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Thu Jan 19 2006 - brian.cameron@sun.com
- Added %{_datadir}/gnome-default-applications to share package.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Thu Dec 01 2005 - damien.carbery@sun.com
- Add Build/Requires SUNWevolution-data-server/-devel for libebook dependency.
* Tue Jul 19 2005 - damien.carbery@sun.com
- Add BuildRequires SUNWtltk because build was breaking without that package.
* Wed Jul 13 2005 - brian.cameron@sun.com
- Added SUNWgnome-panel dependency
* Thu Jun 02 2005 - brian.cameron@sun.com
- Bumped to 2.10, fixed packaging.
* Tue Oct 26 2004 - srirama.sharma@wipro.com
- Added patch control-center-03-sun-help-key.diff (to sparc only) to bind the 
  Sun help key to launch default help with Sun tpe Keyboards. Fixes the bugtraq
  bug#6182405.
* Tue Oct 19 2004 - srirama.sharma@wipro.com
- Added patch control-center-02-sun-volume-keys.diff (to sparc only) to bind 
  Sun keys Volume up, Volume Down and Volume Mute to control volume with Sun type
  keyboards. Fixes bugtraq bug#6173921.
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Sat Sep 11 2004 - laca@sun.com
- Set LDFLAGS so Xrandr and Xrender can be found.
* Thu Sep 09 2004 - matt.keenan@sun.com
- Added gnome-at-properties.1, gnome-font-viewer.1 manpages
* Wed Aug 18 2004 - damien.carbery@sun.com
- Change manpage perms for Solaris integration.
* Fri Aug  6 2004 - danek.duvall@sun.com
- Add support for running the Solaris Print Manager (as root)
* Tue Jul 13 2004 - damien.carbery@sun.com
- Create symlink to screensaver-properties.desktop in capplets dir to fix
  bug 5070633.
* Tue Jun 22 2004 - shirley.woo@sun.com
- changed install location to /usr/lib and /usr/bin
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Tue Mar 02 2004 - niall.power@sun.com
- add {_libdir}/window-manager-settings
* Mon Mar 01 2004 - laca@sun.com
- remove libxklavier
- add dependency on SUNWgnome-wm
* Mon Feb 23 2004 - Niall.Power@sun.com
- install gconf schemas at the end of the install
  stage.
* Thu Feb 19 2004 - Niall.Power@sun.com
- initial Solaris spec file

