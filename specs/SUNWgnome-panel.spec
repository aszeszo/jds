#
# spec file for package SUNWgnome-panel
#
# includes module(s): libwnck, notification-daemon, 
#                     gnome-desktop, gnome-menus, gnome-panel
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby
#
%include Solaris.inc
%use lwnck = libwnck.spec
%use gdesktop = gnome-desktop.spec
%use gnome_menus = gnome-menus.spec
%use gpanel = gnome-panel.spec
%use notificationdaemon = notification-daemon.spec

Name:                    SUNWgnome-panel
IPS_package_name:        gnome/gnome-panel
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:                 GNOME panel and support libraries
Version:                 %{gpanel.version}  
Source:                  %{name}-manpages-0.1.tar.gz
Source1:                 %{name}-gnome-about.ksh
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GPLv2, LGPLv2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: x11/trusted/libxtsol
BuildRequires: library/desktop/libglade
BuildRequires: library/gnome/gnome-libs
BuildRequires: gnome/config/gconf
BuildRequires: library/gnome/gnome-vfs
BuildRequires: library/gnome/gnome-component
BuildRequires: developer/gnome/gnome-doc-utils
BuildRequires: library/popt
BuildRequires: image/library/libpng
BuildRequires: release/name
BuildRequires: developer/library/lint
BuildRequires: library/desktop/evolution-data-server
BuildRequires: data/iso-codes
BuildRequires: system/library/libdbus
BuildRequires: library/libxml2
BuildRequires: library/python-2/libxml2-26
BuildRequires: image/library/librsvg
BuildRequires: library/desktop/libsexy
BuildRequires: library/python-2/setuptools-26
BuildRequires: developer/documentation-tool/gtk-doc
BuildRequires: library/libnotify
BuildRequires: library/desktop/gobject/gobject-introspection
BuildRequires: system/library/iconv/utf-8
BuildRequires: library/gnome/gnome-keyring
BuildRequires: library/desktop/libgweather
Requires: library/desktop/libglade
Requires: library/desktop/libsexy
Requires: library/gnome/gnome-libs
Requires: gnome/config/gconf
Requires: library/gnome/gnome-vfs
Requires: library/libxml2
Requires: library/gnome/gnome-component
Requires: library/popt
Requires: system/library/math
Requires: image/library/librsvg
Requires: image/library/libpng
Requires: service/gnome/desktop-cache
Requires: library/desktop/evolution-data-server
Requires: data/iso-codes
Requires: system/library/libdbus
Requires: runtime/python-26
Requires: library/libnotify
Requires: library/desktop/xdg/libcanberra
Requires: library/desktop/libxklavier
# FIXME: circular dep
# BuildRequires: SUNWgnome-python26
BuildRequires: gnome/trusted/libgnometsol
%ifarch i386
Requires: x11/keyboard/data-xkb
BuildRequires: x11/keyboard/data-xkb
%endif

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir %name-%version
%lwnck.prep -d %name-%version
%notificationdaemon.prep -d %name-%version
%gdesktop.prep -d %name-%version
%gnome_menus.prep -d %name-%version
%gpanel.prep -d %name-%version
chmod -R u+w %{_builddir}/%name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED
export PYTHON=/usr/bin/python%{default_python_version}
export PKG_CONFIG_PATH="../gnome-desktop-%{gdesktop.version}/libgnome-desktop:../libwnck-%{lwnck.version}:../gnome-menus-%{gnome_menus.version}/libmenu:../gnome-panel-%{gpanel.version}/libpanel-applet"
export CFLAGS="%optflags -I/usr/sfw/include -I/usr/openwin/share/include -DANSICPP"
export RPM_OPT_FLAGS="$CFLAGS"
export CPPFLAGS="-I/usr/sfw/include"
export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib -L/usr/openwin/sfw/lib -R/usr/openwin/sfw/lib -L/usr/openwin/lib -R/usr/openwin/lib"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

%lwnck.build -d %name-%version

%notificationdaemon.build -d %name-%version

export CFLAGS="%optflags -I/usr/sfw/include -DANSICPP"
export RPM_OPT_FLAGS="$CFLAGS"
%gdesktop.build -d %name-%version
%gnome_menus.build -d %name-%version
%gpanel.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%lwnck.install -d %name-%version

%notificationdaemon.install -d %name-%version
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%gdesktop.install -d %name-%version
%gnome_menus.install -d %name-%version

%gpanel.install -d %name-%version

rm -r $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 0644 $RPM_BUILD_ROOT%{_datadir}/gnome/help/*/C/*.xml

# Remove empty directories
rm -r $RPM_BUILD_ROOT%{_sysconfdir}/dbus-1
rm -r $RPM_BUILD_ROOT%{_datadir}/dbus-1/system-services

%if %option_with_sun_branding
# Change to allow for addition of a gnome-about wrapper script to allow
# one-time processing.
# Move binary to /usr/lib
mv $RPM_BUILD_ROOT/%{_bindir}/gnome-about $RPM_BUILD_ROOT/%{_libdir}/gnome-about
# Now place script in to bin dir.
install --mode=0755 %SOURCE1 $RPM_BUILD_ROOT/%{_bindir}/gnome-about
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gnome-about
%{_bindir}/gnome-panel
%{_bindir}/gnome-desktop-item-edit
%{_bindir}/gnome-cleanup
%{_bindir}/gmenu-simple-editor
%{_bindir}/wnckprop
%{_bindir}/notification-properties
%{_bindir}/wnck-urgency-monitor
%dir %attr (0755, root, bin) %{_libdir}
%if %option_with_sun_branding
%{_libdir}/gnome-about
%endif
%{_libdir}/lib*.so*
%{_libdir}/python*
%{_libdir}/bonobo/servers/*.server
%{_libdir}/notification-daemon
%dir %attr (0755, root, bin) %{_libdir}/notification-daemon-1.0
%dir %attr (0755, root, bin) %{_libdir}/notification-daemon-1.0/engines
%{_libdir}/notification-daemon-1.0/engines/*.so*
%{_libexecdir}/*-applet
%dir %attr(0755, root, sys) %{_datadir}
%{_datadir}/gnome-about
%{_datadir}/gnome-menus
%{_datadir}/desktop-directories
%{_datadir}/omf/*/*-C.omf
%{_libdir}/gnome-panel-add
%{_datadir}/gnome-panel/ui/*.ui
%{_datadir}/polkit-1/actions
%{_datadir}/gnome-panel/pixmaps
%{_datadir}/gnome-panelrc
%{_datadir}/notification-daemon
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/C
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%attr (-, root, other) %{_datadir}/icons
%{_datadir}/gnome-2.0/ui/*.xml
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/libgnome-desktop/pnp.ids
%dir %attr (0755, root, bin) %{_datadir}/dbus-1
%dir %attr (0755, root, bin) %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*
%dir %attr(0755, root, bin) %{_mandir}/man5
%{_mandir}/man5/*

%{_libdir}/girepository-1.0/GMenu-2.0.typelib
%{_datadir}/gir-1.0/GMenu-2.0.gir
%{_libdir}/girepository-1.0/Wnck-1.0.typelib
%{_datadir}/gir-1.0/Wnck-1.0.gir


%doc gnome-desktop-%{gdesktop.version}/AUTHORS
%doc gnome-desktop-%{gdesktop.version}/README
%doc(bzip2) gnome-desktop-%{gdesktop.version}/COPYING
%doc(bzip2) gnome-desktop-%{gdesktop.version}/COPYING.LIB
%doc(bzip2) gnome-desktop-%{gdesktop.version}/COPYING-DOCS
%doc(bzip2) gnome-desktop-%{gdesktop.version}/ChangeLog
%doc(bzip2) gnome-desktop-%{gdesktop.version}/NEWS
%doc gnome-menus-%{gnome_menus.version}/AUTHORS
%doc gnome-menus-%{gnome_menus.version}/README
%doc(bzip2) gnome-menus-%{gnome_menus.version}/COPYING
%doc(bzip2) gnome-menus-%{gnome_menus.version}/COPYING.LIB
%doc(bzip2) gnome-menus-%{gnome_menus.version}/ChangeLog
%doc(bzip2) gnome-menus-%{gnome_menus.version}/NEWS
%doc gnome-panel-%{gpanel.version}/AUTHORS
%doc gnome-panel-%{gpanel.version}/README
%doc(bzip2) gnome-panel-%{gpanel.version}/COPYING
%doc(bzip2) gnome-panel-%{gpanel.version}/COPYING.LIB
%doc(bzip2) gnome-panel-%{gpanel.version}/COPYING-DOCS
%doc(bzip2) gnome-panel-%{gpanel.version}/ChangeLog
%doc(bzip2) gnome-panel-%{gpanel.version}/NEWS
%doc libwnck-%{lwnck.version}/AUTHORS
%doc libwnck-%{lwnck.version}/README
%doc(bzip2) libwnck-%{lwnck.version}/COPYING
%doc(bzip2) libwnck-%{lwnck.version}/ChangeLog
%doc(bzip2) libwnck-%{lwnck.version}/NEWS
%doc notification-daemon-%{notificationdaemon.version}/AUTHORS
%doc notification-daemon-%{notificationdaemon.version}/NEWS
%doc(bzip2) notification-daemon-%{notificationdaemon.version}/COPYING
%doc(bzip2) notification-daemon-%{notificationdaemon.version}/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/clock.schemas
%{_sysconfdir}/gconf/schemas/panel-compatibility.schemas
%{_sysconfdir}/gconf/schemas/panel-general.schemas
%{_sysconfdir}/gconf/schemas/panel-global.schemas
%{_sysconfdir}/gconf/schemas/panel-object.schemas
%{_sysconfdir}/gconf/schemas/panel-toplevel.schemas
%{_sysconfdir}/gconf/schemas/window-list.schemas
%{_sysconfdir}/gconf/schemas/workspace-switcher.schemas
%{_sysconfdir}/gconf/schemas/notification-daemon.schemas
%{_sysconfdir}/gconf/schemas/panel-default-setup.entries
%{_sysconfdir}/xdg

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/panel-test-applets
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr(0755, root, sys) %{_datadir}
%{_datadir}/idl
%{_datadir}/gtk-doc
%dir %attr (0755, root, other) %{_datadir}/gnome

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/gnome/help/[a-c]*/[a-z]*
%{_datadir}/gnome/help/[e-z]*/[a-z]*
%{_datadir}/omf/*/*-[a-z][a-z].omf
%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z][A-Z].omf
%{_datadir}/omf/gpl/gpl-nds.omf

%changelog
* Mon Aug 02 2010 - javier.acosta@sun.com
- Adding requires SUNWlibxklavier, needed for Keyboard Switcher
* Mon Jun 20 2010 - yuntong.jin@sun.com
- Change own to jouby
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Tue Apr  6 2010 - christian.kelly@oracle.com
- Fix %files.
* Mon Feb 08 2010 - jedy.wang@sun.com
- Uses default python to build.
* Fri Jan 29 2010 - christian.kelly@sun.com
- Fix dependency, should be SUNWlibcanberra.
* Fri Jan 22 2010 - christian.kelly@sun.com
- Add dependecy on SUNWlibcanberra-gtk.
* Thu Dec 10 2009 - christian.kelly@sun.com
- Separate out libgweather into it's own spec.
* Fri Dec  4 2009 - jedy.wang@sun.com
- Add SUNWlibnotify to denpendency.
* Thu Dec  3 2009 - christian.kelly@sun.com
- Separate libnotify out into it's own spec.
* Fri Oct 23 2009 - jedy.wang@sun.com
- Change owner to jedy.
* Thu Jul 30 2009 - christian.kelly@sun.com
- Fix %files.
* Tue Jun 09 2009 - brian.cameron@sun.com
- Remove files from %docs that are no longer in the tarball.
* Fri Apr 03 2009 - laca@sun.com
- Use desktop-cache instead of postrun.
* Mon Mar 23 2009 - jeff.cai@sun.com
- Since /usr/bin/gmenu-simple-editor (SUNWgnome-panel) requires
  /usr/bin/i86/isapython2.4 which is found in SUNWPython, and 
* Wed Mar 11 2009 - jedy.wang@sun.com
- Bring back gweather.pc because evolution needs it.
* Tue Jan 20 2009 - brian.cameron@sun.com
- Update PKG_CONFIG_PATH so it finds libnotify uninstalled pc file.
* Tue Jan 20 2009 - jedy.wang@sun.com
- Ship new files from notification-daemon.
* Wed Dec 10 2008 - dave.lin@sun.com
- Removed non-exist libgweather/ChangeLog.
* Thu Sep 11 2008 - matt.keenn@sun.com
- Update copyright.
* Fri Jun 20 2008 - damien.carbery@sun.com
- Change libsexy dependency to apply to sparc too as SUNWlibsexy builds and
  works on sparc now.
* Mon Jun 16 2008 - damien.carbery@sun.com
- Make libsexy dependency x86-only.
* Mon Jun 16 2008 - jedy.wang@sun.com
- Add new dependency to libsexy.
* Wed Apr 9 2008 - brian.cameron@sun.com
- Fix packaging.
* Tue Apr 8 2008 - matt.keenan@sun.com
- Add libgweather include back in as required by SUNWgnome-applets.
* Mon Apr 7 2008 - matt.keenan@sun.com
- Remove libgweather include and pc file in %install section.
* Wed Feb 13 2008 - damien.carbery@sun.com
- Update %files, removing %{_bindir}/gnome-menu-spec-test.
* Thu Jan 17 2008 - damien.carbery@sun.com
- Add BuildRequires SUNWlibrsvg-devel because librsvg is required by
  gnome-panel 2.21.5. Remove some empty dirs.
* Thu Nov 15 2007 - damien.carbery@sun.com
- Add BuildRequires SUNWlxml-python for building documentation.
* Fri Oct 19 2007 - laca@sun.com
- only install the gnome-about wrapper script if sun branding is requested.
* Thu Oct 11 2007 - damien.carbery@sun.com
- Remove install dependency on SUNWgnome-doc-utils and change the build
  dependency from SUNWgnome-doc-utils-devel to SUNWgnome-doc-utils.
* Fri Sep 28 2007 - laca@sun.com
- delete Nevada X deps; make xorg-xkb dep dependent upon nevada X build.
- delete some unneeded env vars.
* Tue Jul 10 2007 - damien.carbery@sun.com
- Add %{_bindir}/wnckprop and update dir for timezone.glade in %files.
* Tue Jun 26 2007 - michal.pryc@sun.com
- gnome-panel-07-restrict-app-launching.diff changed. Fixes 6565785.
* Tue Jun 12 2007 - matt.keenan@sun.com
- re-include timezone glade file.
* Tue May 15 2007 - damien.carbery@sun.com
- Some files now installed to %{_datadir}/gnome-panel instead of
  %{_datadir}/gnome/panel.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable.
* Wed Feb 14 2006 - damien.carbery@sun.com
- Delete en_GB files in %install.
* Sun Jan 28 2007 - laca@sun.com
- Add /usr/openwin/lib to library search path, needed for libXau on s10.
* Fri Jan 12 2006 - brian.cameron@sun.com
- No longer remove %{datadir}/omf/gnome-feedback since this was removed
  from gnome-desktop.
* Thu Dec 07 2006 - darren.kenny@sun.com
- Create a wrapper script around gnome-about to handle Solaris Developer Guide
  launching.
* Tue Nov 21 2006 - damien.carbery@sun.com
- Remove man3 dir from -devel package. Fixes 6495907.
* Sat Nov 04 2006 - damien.carbery@sun.com
- Undo removal of man5 dir. A manpage is installed there.
* Fri Nov 03 2006 - damien.carbery@sun.com
- Remove man5 dir as nothing is installed there now. Add man3 dir as updated 
  manpage tarball installs 2 files there.
* Tue Sep 05 2006 - brian.cameron@sun.com
- Remove libxklavier from the build.
* Mon Sep 04 2006 - brian.cameron@sun.com
- Fix comments.  Also remove -g from CFLAGS.  Not good to have on by default
  for performance.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball.
* Mon Aug 21 2006 - damien.carbery@sun.com
- Fix l10n package - C locale omf file was in base and l10n package.
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317.
* Mon Jun 26 2006 - dave.lin@sun.com
- remove the dependency from thunderbird since this dependency doesn't 
  exist any more.
* Fri Jun 23 2006 - Christopher.Hanna@sun.com
- Removed gkb_xmmap.1 and gnome-panel-preferences.1 manpages.
* Sun Jun 11 2006 - laca.com
* Thu Jun 22 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWevolution-data-server/-devel after check-deps.pl run.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys.
* Thu May 25 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files.
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s).
* Mon May 01 2006 - damien.carbery@sun.com
- Change build dependency from SUNWthunderbird-devel to SUNWthunderbird as the
  devel package has been removed. 
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Thu Feb 14 2006 - damien.carbery@sun.com
- Remove scrollkeeper files before packaging.
* Tue Nov 29 2005 - laca.com
- remove javahelp stuff.
* Wed Nov 09 2005 - damien.carbery@sun.com
- Add Build/Requires SUNWthunderbird, for libnss3.so dependency.
* Thu Oct 27 2005 - damien.carbery@sun.com
- Remove some empty dirs when not building l10n packages.
* Mon Sep 12 2005 - laca@sun.com
- Remove unpackaged files or add to %files.
* Tue Aug 30 2005 - damien.carbery@sun.com
- Add BuildRequires SUNWgnome-doc-utils-devel as gnome-desktop uses
  gnome-doc-prepare.
  Correct packaging list (gif->png) and remove some docs lines.
* Wed Jul 13 2005 - brian.cameron@sun.com
- Split SUNWgnome-panel to two spec files, SUNWgnome-panel and
  SUNWgnome-applets.spec.
* Wed May 25 2005 - brian.cameron@sun.com
- Finally finished packaging this for Solaris.
* Tue May 24 2005 - brian.cameron@sun.com
- More packaging fixes.  Not yet completely right.
* Thu May 20 2005 - brian.cameron@sun.com
- Packaging fixes.  Not yet completely right, but better.
* Fri May 13 2005 - brian.cameron@sun.com
- Removed now from panel since it doesn't build right.  It has
  AC_CONFIG_AUX_DIR set to config, which causes intltoolize to fail.
* Fri May 13 2005 - brian.cameron@sun.com
- Fix PKG_CONFIG_PATH for 2.10 and add new gnome-menus.
* Fri Apr 08 2005 - glynn.foster@sun.com
- Add hicolor locations.
* Fri Jan 28 2005 - Matt.keenan@sun.com
- #6222336 : Remove gweather from yelp toc.
* Wed Nov 24 2004 - kazuhiko.maekawa@sun.com
- Add English help files under l10n dir to fix 6197769(P1 STP).
* Tue Nov 16 2004 - laca@sun.com
- move section 5 man page to share from devel-share.
* Tue Nov 02 2004 - balamurali.viswanathan@sun.com
- Added BuildConflicts: SUNWgnome-media.
* Fri Oct 29 2004 - arvind.samptur@wipro.com
- pick the desktop files from datadir/applications.
* Tue Oct 19 2004 - laca@sun.com
- remove xorg-xkb dependency on sparc as it's only available on x86.
* Fri Oct  8 2004 - damien.carbery@sun.com
- Comment out %{_bindir}/now to match now.spec.
* Mon Oct 04 2004 - matt.keenan@sun.com
- Remove drivemount help files #5108690.
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess.
* Fri Oct  1 2004 - damien.carbery@sun.com
- Remove references to fish applet to match gnome-panel.spec change.
* Thu Sep 30 2004 - vinay.mandyakoppal@wipro.com
- Added code to install "gswitchit" help documents.
  Fixes bug #5076490.
* Tue Sep 21 2004 - vinay.mandyakoppal@wipro.com
- Added code to install "now" help documents.
  Fixes bug #5101703.
* Sun Sep 13 2004 - damien.carbery@sun.com
- Move manpages from SUNWgnome-utility-applets to 
  SUNWgnome-utility-applets-share.
* Thu Sep 09 2004 - matt.keenan@sun.com
- Added gkb_xmmap.1, gnome-keyboard-layout.1, gswitchit-plugins-capplet.1
  manpages.
* Mon Sep 06 2004 - matt.keenan@sun.com
- Bug 5083735 : Uncommented javahelp/gnome-netstatus from %files section.
* Mon Aug 30 2004 - shirley.woo@sun.com
- Bug 5091588 : sman3/4/5 files should be in a separate devel package.
* Mon Aug 23 2004 - shirley.woo@sun.com
- Bug 5090965 : Removed duplicate entries.
* Wed Aug 18 2004 - damien.carbery@sun.com
- Changed xml perms to 0644 for Solaris integration.
- Changed manpage perms for Solaris integration.
* Mon Aug 16 2004 - damien.carbery@sun.com
- Changed SOURCE7 mode to 0755 for Solaris integration.
* Tue Aug 10 2004 - kaushal.kumar@wipro.com
- Remove GNOME_DriveMountApplet.server to remove applet's panel menu entry.
* Tue Jul 27 2004 - glynn.foster@sun.com
- Remove drivemount on Solaris. Part fix for #5043894.
* Fri Jul 23 2004 - damien.carbery@sun.com
- Remove GNOME_WirelessApplet.xml because a gnome-panel.spec patch remove it.
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Fri Jun 25 2004 - vijaykumar.patwari@wipro.com
- Updated for mini commander applet.
* Thu Jun 24 2004 - vijaykumar.patwari@wipro.com
- Associate default macros for mini commander applet.
* Thu May 27 2004 - laca@sun.com
- added gnome-cleanup man page.  Also made SUNWgnome-media a dependency
  since it is needed for the mixer applet.
* Thu May 27 2004 - laca@sun.com
- added l10n subpkg.
* Fri May 28 2004 - <laca@sun.com>
- added gnome-cleanup to %files.
* Mon May 24 2004 - <danek.duvall@sun.com>
- Only Sun banner should show up in gnome-about.
* Fri May 21 2004 - <glynn.foster@sun.com>
- Remove wireless applet from the Solaris builds.
* Sun May 02 2004 - <laca@sun.com>
- don't redefine __STDC_VERSION__ on S9, as it breaks the build.
* Fri Apr 30 2004 - <arvind.samptur@wipro.com>
- get the panel-default-setup.entries to be installed in
  $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.defaults.
* Wed Apr 07 2004 - <laca@sun.com>
- update quick-lounge-applet files.
* Fri Mar 26 2004 - <laca@sun.com>
- fixed libexecdir in %files.
- update gnome-netstatus icon locations.
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration.
* Wed Mar 10 2004 - <laca@sun.com>
- remove duplicate entries from %files.
* Wed Mar 03 2004 - <niall.power@sun.com>
- merge in gnome-netstatus applet.
* Tue Mar 02 2004 - <laca@sun.com>
- add %libical.install.
- add libical*.so*.
* Mon Feb 23 2004 - <niall.power@sun.com>
- install gconf schemas at end of install stage.
- define mappings for all the installed schemas.



