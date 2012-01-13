#
# spec file for package SUNWgnome-display-mgr
#
# includes module(s): gdm
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%use gdm = gdm.spec

Name:                    SUNWgnome-display-mgr
Summary:                 GNOME display manager
Version:                 %{gdm.version}
Source:                  %{name}-manpages-0.1.tar.gz
Source1:                 gdm.xml
Source2:                 svc-gdm
# gdmdynamic is wrapper script for ck-seat-tool and ck-list-sessions.
# This script is for back compatible for SRSS.
# Should be removed when SRSS using ck-seat-tool and ck-list-sessions instead.
Source3:                 gdmdynamic
Source4:                 xterm.desktop
Source5:                 gdm.auth_attr
Source6:                 gdm.prof_attr
Source7:                 ManageDtHeader.html
Source8:                 ManageDtLogin.html
SUNW_Pkg:                SUNWgnome-display-mgr
IPS_package_name:        system/display-manager/gdm
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Sessions
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gdm.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

Requires: gnome/config/gconf
Requires: gnome/gnome-panel
Requires: gnome/gnome-power-manager
Requires: gnome/gnome-session
Requires: gnome/preferences/control-center
Requires: gnome/theme/gnome-themes
Requires: gnome/theme/hicolor-icon-theme
Requires: gnome/theme/tango-icon-theme
Requires: gnome/window-manager/metacity
Requires: library/glib2
Requires: library/gnome/gnome-component
Requires: library/gnome/gnome-libs
Requires: library/desktop/cairo
Requires: library/desktop/gtk2
Requires: library/desktop/libxklavier
Requires: library/desktop/pango
Requires: library/desktop/xdg/libcanberra
Requires: library/xdg/consolekit
Requires: system/library/libdbus-glib
Requires: system/library/dbus
Requires: system/library/fontconfig
Requires: system/library/libdbus
Requires: system/library/math
Requires: system/display-manager/desktop-startup
Requires: system/display-manager/xdm
# xmodmap, xrdb
Requires: x11/x11-server-utilities
# setxkbmap
Requires: x11/keyboard/xkb-utilities
# Xserver
Requires: x11/server/xserver-common

BuildRequires: SUNWxwplt
BuildRequires: SUNWcairo-devel
BuildRequires: SUNWconsolekit-devel
BuildRequires: SUNWdbus-glib-devel
BuildRequires: SUNWdbus-devel
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWlibcanberra-devel
BuildRequires: SUNWpango-devel
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWlibgnome-keyring
BuildRequires: SUNWuiu8

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%gdm.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export XGETTEXT=/usr/gnu/bin/xgettext

%gdm.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gdm.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/lib/svc/manifest/application/graphical-login
install --mode=0444 %SOURCE1 $RPM_BUILD_ROOT/lib/svc/manifest/application/graphical-login
install -d $RPM_BUILD_ROOT/lib/svc/method
cp %SOURCE2 $RPM_BUILD_ROOT/lib/svc/method/

install --mode=0744 %SOURCE3 $RPM_BUILD_ROOT/%{_bindir}/

# Install fail safe desktop
install -d $RPM_BUILD_ROOT/%{_datadir}/xsessions
install --mode=0644 %SOURCE4 $RPM_BUILD_ROOT/%{_datadir}/xsessions/

# RBAC files for gdm service
install -d $RPM_BUILD_ROOT%{_sysconfdir}/security/auth_attr.d
install --mode=0444 %SOURCE5 $RPM_BUILD_ROOT%{_sysconfdir}/security/auth_attr.d/desktop-login
install -d $RPM_BUILD_ROOT%{_sysconfdir}/security/prof_attr.d
install --mode=0444 %SOURCE6 $RPM_BUILD_ROOT%{_sysconfdir}/security/prof_attr.d/desktop-login
install -d $RPM_BUILD_ROOT%{_libdir}/help/auths/locale/C/
install --mode=0444 %SOURCE7 $RPM_BUILD_ROOT%{_libdir}/help/auths/locale/C/
install --mode=0444 %SOURCE8 $RPM_BUILD_ROOT%{_libdir}/help/auths/locale/C/

# Create the 'interface' directory so that user's session scripts can be
# run by gdm and which are populated by other applications.
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/X11/xinit/xinitrc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache icon-cache gconf-cache

%post root
cat >> $BASEDIR/var/svc/profile/upgrade <<\EOF

# We changed gdm's FMRI.  If the old service exists and is enabled,
# disable it and enable the new one.
gdm=svc:/application/gdm2-login:default
if svcprop -q $gdm; then
	set -- `svcprop -C -t -p general/enabled $gdm`
	if [ $? -ne 0 ]; then
		echo "Could not read whether $gdm was enabled."
	elif [ $2 != boolean ]; then
		echo "general/enabled property of $gdm has bad type."
	elif [ $# -ne 3 ]; then
		echo "general/enabled property of $gdm has the wrong number\c"
		echo " of values."
	elif [ $3 = true ]; then
		svcadm disable $gdm
		svcadm enable svc:/application/graphical-login/gdm:default
	fi
fi

EOF

%postun
%restart_fmri desktop-mime-cache icon-cache

%actions
group groupname="gdm" gid="50"
user gcos-field="GDM Reserved UID" group=gdm home-dir=/var/lib/gdm uid=50 username=gdm

%files
%doc -d gdm-%{gdm.version} AUTHORS README
%doc(bzip2) -d gdm-%{gdm.version} COPYING NEWS
%doc(bzip2) -d gdm-%{gdm.version} ChangeLog po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_sbindir}
%{_sbindir}/gdm
%{_sbindir}/gdm-binary
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/bonobo
%{_libexecdir}/gdm*
%dir %{_libdir}/help
%dir %{_libdir}/help/auths
%dir %{_libdir}/help/auths/locale
%dir %{_libdir}/help/auths/locale/C
%doc %{_libdir}/help/auths/locale/C/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/gdm
%{_datadir}/gdm/autostart/LoginWindow/*.desktop
%{_datadir}/gdm/gdm-greeter-login-window.ui
%{_datadir}/gdm/locale.alias
%{_datadir}/gdm/box.png
%{_datadir}/gdm/logo.png
%{_datadir}/gdm/bkg.jpg
%{_datadir}/gdm/bottom-panel-image-gdm.png
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/gdm/C
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/omf/gdm/*-C.omf
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/gnome-2.0/*
%{_datadir}/pixmaps/*
%{_datadir}/xsessions/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man1m
%{_mandir}/man1/*
%{_mandir}/man1m/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1/system.d
%{_sysconfdir}/dbus-1/system.d/*
%{_sysconfdir}/gconf
%dir %{_sysconfdir}/gdm
%{_sysconfdir}/gdm/gdm.schemas
%{_sysconfdir}/gdm/Init
%{_sysconfdir}/gdm/Post*
%{_sysconfdir}/gdm/Pre*
%{_sysconfdir}/gdm/X*
%config %ips_tag(original_name=SUNWgnome-display-mgr:etc/X11/gdm/custom.conf) %{_sysconfdir}/gdm/custom.conf
%dir %{_sysconfdir}/security
%dir %{_sysconfdir}/security/auth_attr.d
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %{_sysconfdir}/security/auth_attr.d/*
%dir %{_sysconfdir}/security/prof_attr.d
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %{_sysconfdir}/security/prof_attr.d/*
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinitrc.d
# don't use %_localstatedir for the /var/log and /var/svc directory,
# because these are an absolute path defined by another package, so
# it has to be /var/svc even if this package has its %_localstatedir
# redefined.
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/log
%dir %attr (1770, root, gdm) /var/log/gdm
# SVC method file
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%dir %attr (0755, root, sys) /lib/svc/manifest
%dir %attr (0755, root, sys) /lib/svc/manifest/application
%dir %attr (0755, root, sys) /lib/svc/manifest/application/graphical-login
%attr (0555, root, bin) /lib/svc/method/svc-gdm
%ips_tag(restart_fmri="svc:/system/manifest-import:default") %attr (0444, root, sys) /lib/svc/manifest/application/graphical-login/gdm.xml
%dir %attr (0755, root, bin) %{_localstatedir}/cache
%dir %attr (0755, root, gdm) %{_localstatedir}/cache/gdm
%dir %attr (0755, root, other) %{_localstatedir}/lib
%dir %attr (1770, root, gdm) %{_localstatedir}/lib/gdm
%dir %attr (0770, root, gdm) %{_localstatedir}/lib/gdm/.gconf.mandatory
%attr (1640, root, gdm) %{_localstatedir}/lib/gdm/.gconf.path
%attr (1640, root, gdm) %{_localstatedir}/lib/gdm/.gconf.mandatory/*
%dir %attr (0770, root, gdm) %{_localstatedir}/lib/gdm/.local
%dir %attr (0770, root, gdm) %{_localstatedir}/lib/gdm/.local/share
%dir %attr (0770, root, gdm) %{_localstatedir}/lib/gdm/.local/share/applications
%attr (1640, root, gdm) %{_localstatedir}/lib/gdm/.local/share/applications/* 

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/gnome/*help/*/[a-z]*
%{_datadir}/omf/gdm/*-[a-z]*.omf

%changelog
* Tue Nov 29 2011 - brian.cameron@oracle.com
- Fix packaging CR #7110596.
* Mon Dec 27 2010 - alan.coopersmith@oracle.com
- Move RBAC files shared by application/graphical-login/* SMF services here
  from the no-longer delivered dtlogin package.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Apr 23 2010 - halton.huo@sun.com
- Move manifest from /var/svc to /lib/svc
* Thu Jan 14 2010 - halton.huo@sun.com
- Update %files caused by glade to GtkBuild
- Remove dependency on libglade.
* Thu Dec 17 2009 - brian.cameron@sun.com
- Add SUNWtango-icon-theme as a dependency.
* Mon Dex 14 2009 - christian.kelly@sun.com
- Fix %files.
* Mon Dec 14 2009 - halton.huo@sun.com
- Add Requires:%{name}-root to base pkg to fix doo #13254.
* Mon Dec 07 2009 - brian.cameron@sun.com
- No longer deliver /usr/share/gdm/gdb-cmd since we patch GDM to use pstack
  instead.
* Tue Dec 01 2009 - halton.huo@sun.com
- Add Requires/BuildRequires for SUNWlibcanberra
* Thu Nov 26 2009 - christian.kelly@sun.com
- Fix directory perms.
* Mon Oct 19 2009 - brian.cameron@sun.com
- Change /var/log/gdm so that it has root:root ownership and 750 permissions,
  better matching what GDM actually installs to the system.
* Tue Sep 01 2009 - brian.cameron@sun.com
- Update packaging after adding patch gdm-10-cache.diff since this adds
  /var/cache/gdm to the package.
* Wed Aug 19 2009 - brian.cameron@sun.com
- Do not package /usr/sbin/gdm-restart and /usr/sbin/gdm-safe-restart since
  they are non-functional.  Add them back when they work.
* Wed Aug 12 2009 - halton.huo@sun.com
- Add xterm.desktop for fail safe.
* Tue Aug 11 2009 - halton.huo@sun.com
- Add gdmdynamic as Source3
* Mon Jul 27 2009 - halton.huo@sun.com
- We bump gdm to 2.27.4, this is a rewrite release compared gdm 2.20x version,
  rework totally.
* Tue May 12 2009 - dave.lin@sun.com
- Remove 'Requires: SUNWgnome-display-mgr' from root pkg to fix the circular dependency issue.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Wed Apr 01 2009 - jeff.cai@sun.com
- Add the dependency of SUNWswmt for the root package since the customer.conf
  uses i.preserve.
* Tue Mar 24 2009 - jeff.cai@sun.com
- Add the dependency of SUNWgnome-display-mgr for the root package.
* Web Feb 25 2009 - dave.lin@sun.com
- Changed to Requires: SUNWdesktop-startup due to SUNWgnome-dtstart was renamed.
* Fri Dec 05 2008 - halton.huo@sun.com
- Add workaround to fix CR #6781266 - gdmsetup fails to startup
* Wed Nov 21 2008 - brian.cameron@sun.com
- Add /lib/svc/method/svc-gdm SMF method file so that the "stop" method
  doesn't cause errors on shutdown/restart.  Fix packaging permissions.
  Fix for doo bug #4887.
* Thu Oct 02 2008 - ghee.teo@sun.com
- Added directory /etc/X11/xinit/xinitrc.d as part of the fix to 6755007 and
  also d.o.o #4097.
* Sun Sep 14 2008 - brian.cameron@sun.com
- Add new copyright files.
* Tue Jun 24 2008 - damien.carbery@sun.com
- Remove "-lgailutil" from LDFLAGS. Root cause found in gtk+: bugzilla 536430.
* Thu Jun 05 2008 - damien.carbery@sun.com
- Add "-lgailutil" to LDFLAGS so that libgailutil is linked in when
  libgnomecanvas is linked. libgnomecanvas.so includes some gail functions.
* Wed May 07 2008 - damien.carbery@sun.com
- Remove PERL5LIB setting as it is not necessary.
* Thu May 01 2008 - brian.cameron@sun.com
- Fix packaging.  Ship the CDE desktop file if building with
  "with_dt".
* Thu Mar 27 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Sat Jan 26 2008 - brian.cameron@sun.com
- Minor cleanup
* Thu Jan 17 2008 - damien.carbery@sun.com
- Delete %{_datadir}/xsessions/gnome.desktop file as it is now delivered by
  gnome-session module.
* Fri Oct 12 1007 - laca@sun.com
- add x11 compile flags to CFLAGS if x11.pc exists (FOX fix)
* Fri Sep 28 2007 - laca@sun.com
- add support for building with FOX and using dtstart instead of
  dtlogin-integration
* Fri May 11 2007 - brian.cameron@sun.com
- Fix packaging and add needed -R/usr/sfw/lib to link flags.
* Thu May 10 2007 - brian.cameron@sun.com
- Fix packaging for bumping to 2.19.0.
* Thu Apr 12 2007 - brian.cameron@sun.com
- Add SUNWxorg-server as a dependency, since GDM depends on Xephyr
* Fri Mar 09 2007 - brian.cameron@sun.com
- Change file permissions for gdmsetup to 700 so that the gdmsetup
  menu choice only appears for the root user.  Also no longer install
  the %{datadir}/applications directory since we now install to 
  /usr/share/gdm/applications.
* Sun Jan 28 2007 - laca@sun.com
- update %files root so that dir attributes work on both s10 and nevada
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Mon Aug 28 2006 - brian.cameron@sun.com
- Add gdmdynamic manpage.
* Fri Aug 25 2006 - laca@sun.com
- move the smf profile rename postinstall stuff into the -root subpkg,
  because the base package doesn't have access to the / files in the
  case of a diskless installation, part of CR6448317
* Wed Aug 23 2006 - brian.cameron@sun.com
- Move some GDM manpages to sman1m to reflect that the binaries have
  moved to /usr/sbin.
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Fri Jun 23 2006 - christopher.hanna@sun.com
- Removed manpages which arent needed: gdmchooser, gdmgreeter and gdmlogin
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri May 12 2006 - brian.cameron@sun.com
- Add SUNWgnome-dialog as a dependency since GDM does use zenity in places.
* Thu May 11 2006 - brian.cameron@sun.com
- Added %post scripting to migrate users from the old SMF service name
  to the new one.  
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue May 09 2006 - brian.cameron@sun.com
- No longer install the /var/gdm directories here since they get installed via
  make install.
* Tue Apr 18 2006 - brian.cameron@sun.com
- Mark custom.conf as in the preserve class so it doesn't get deleted on pkgrm.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Mark custom.conf as volatile (%config).
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Feb 14 2006 - damien.carbery@sun.com
- Update %files for new tarball (conf files renamed).
* Sat Jan 21 2006 - damien.carbery@sun.com
- Remove locale.alias.orig file from %files. Mistake in build.
* Thu Jan 19 2006 - brian.cameron@sun.com
- Fixed packaging after updating to 2.13.0.6
* Thu Jan 19 2006 - damien.carbery@sun.com
- Add new %files from bumped tarball.
* Tue Jan 17 2006 - damien.carbery@sun.com
- Add SUNWlibcroco to Build/Requires list.
* Mon Jan 16 2006 - damien.carbery@sun.com
- Move /usr/sfw/include reference from gdm.spec to here as it is Solaris only.
- Update Build/Requires lines.
* Mon Jan 16 2006 - padraig.obriain@sun.com
- add reference to %{_libexecdir}/X11/gdm/gdmprefetchlist
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Thu Sep 15 2005 - laca@sun.com
- Remove unpackaged empty directories
* Thu Jul 28 2005 - damien.carbery@suncom
- Add SUNWlibrsvg-devel build dependency. Add SUNWlibrsvg runtime dependency.
- Wed Jul 13 2005 - brian.cameron@sun.com
- Updated to 2.8.0.5.  Updated SVC (GreenLine) integration.
+ Mon Feb 07 2004 - brian.cameron@sun.com
- Fixed permissions on /var/lib/gdm so it doesn't complain on
  reinstall.  The gdm binary program changes the ownership and
  permissions of this file on runtime if they aren't set 
  properly.  This change makes the original permissions set
  by the package correct so gdm won't change them.
* Thu Nov 18 2004 - hidetoshi.tajima@sun.com
- #5081827 - required SUNWgnome-dtlogin-integration to run
/usr/dt/config/Xsession.jds in gnome session
* Wed Nov 17 2004 - matt.keenan@sun.com
- #6195852 - Fix manpage directory installed (stopper)
* Sat Nov 13 2004 - laca@sun.com
- include gdm.conf in the "preserve" class, fixes 5101934
  Note: requires pkgbuild-0.8.2 (CBE 0.18)
* Fri Nov 12 2004 - kazuhiko.maekawa@sun.com
- Revised files section
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Thu Sep 02 2004  <damien.carbery@sun.com>
- Add %dir %attr for mandir and mandir/man1. Attribute change install error.
* Thu Sep 02 2004  <matt.keenan@sun.com>
- Added gdm manpages for solaris
* Tue Jul 27 2004  <glynn.foster@sun.com>
- Put back the New Login in New Window as it's supported.
* Tue Jul 27 2004  <glynn.foster@sun.com>
- Remove the flexiserver .desktop items. Need to have a 
  look to see if the flexiserver binary stuff should be
  include as well or not. Part fix for #5043894.
* Fri Jul 23 2004  <brian.cameron@sun.com>
- Now include /var/lib/gdm and /var/lib/log/gdm in the
  package so that gdm can run out-of-the-box.
* Sun Jun 27 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Mon Mar 01 2004 - <laca@sun.com>
- define PERL5LIB.
- add share and root subpkgs

