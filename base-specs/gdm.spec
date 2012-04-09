#
# spec file for package gdm
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         gdm
License:      GPL v2, LGPL v2, MIT
Group:        System/GUI/GNOME
Version:      2.30.7
Release:      1
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      The GNOME 2.x Display Manager
Source:       http://download.gnome.org/sources/gdm/2.30/gdm-%{version}.tar.bz2
Source1:      box.png
Source2:      logo.png
Source3:      bottom-panel-image-gdm.png
Source4:      bkg.jpg
# Manage displays on the fly
# date:2008-06-03 owner:yippi type:feature bugzilla:536355
Patch1:       gdm-01-dynamic-display.diff
# date:2009-02-13 owner:yippi type:branding
# Branding changes (e.g. configuration differences from upstream) for Solaris.
Patch2:       gdm-02-branding.diff
# Adds SDTLOGIN interface, which drops the Xserver to user
# perms rather than running as root, for added security on Solaris.
# date:2008-05-06 owner:yippi type:feature
Patch3:       gdm-03-sdtlogin.diff
# date:2008-05-05 owner:yippi type:feature doo:14007
Patch4:       gdm-04-smf.diff
# Add support for /etc/default/login configuration.
# date:2009-03-31 owner:yippi type:feature
Patch5:       gdm-05-default.diff
# Solaris does not support system GConf settings.
# date:2009-04-28 owner:yippi type:branding
Patch6:       gdm-06-no-system-gconf.diff
# date:2009-08-20 owner:yippi type:bug bugzilla:583856
Patch7:       gdm-07-pam-problem-dialog.diff
# Add fbconsole integration.
# date:2009-08-20 owner:yippi type:feature doo:10640
Patch8:       gdm-08-fbconsole.diff
# date:2009-09-08 owner:yippi type:bug bugster:6989892
Patch9:       gdm-09-lang.diff
# date:2009-10-16 owner:yippi type:branding
Patch10:      gdm-10-sol-notty.diff
# date:2009-10-13 owner:niall type:bug doo:10981
Patch11:      gdm-11-trusted-extensions.diff
# GDM needs to provide the "gdm" user with access to the audio device for
# orca text-to-speech to work in the login GUI.
# date:2009-10-26 owner:yippi type:feature doo:12125,13570,15539 bugster:6915777
Patch12:      gdm-12-setfacl.diff
# Add "ShowLast" configuration option, needed for Sun Ray.
# date:2009-11-05 owner:yippi type:bug doo:11298 bugzilla:600914
Patch13:      gdm-13-last.diff
# date:2009-12-03 owner:yippi type:bug bugzilla:594818 doo:10915
Patch14:      gdm-14-gconf.diff
# Use pstack to get stack trace, not gdb.
# date:2009-12-07 owner:yippi type:branding
Patch15:      gdm-15-pstack.diff
# date:2010-01-18 owner:erwannc type:branding doo:13943
Patch16:      gdm-16-opensolaris-visual-branding.diff
# date:2009-12-18 owner:yippi type:branding bugster:6897155,6908857
Patch17:      gdm-17-trusted-extensions.diff
# date:2010-04-19 owner:yippi type:bug doo:15117 bugzilla:616258
Patch18:      gdm-18-xdmcp-seatid.diff
# date:2010-02-15 owner:yippi type:feature bugster:6606096
Patch19:      gdm-19-audio-default.diff
# date:2010-05-13 owner:yippi type:bug bugzilla:617017
# Since GConf-06-pkg-config.diff is patched for gconf, we can the requirement
# This patch should be removed after gconf is upgraded to 2.31.3
Patch20:      gdm-20-down-gconf.diff
# date:2010-02-19 owner:yippi type:feature bugster:6923733
Patch21:      gdm-21-xauth.diff
# date:2010-02-19 owner:yippi type:bug bugster:6951765 bugzilla:619129
Patch22:      gdm-22-custom.diff
# date:2010-06-22 owner:yippi type:feature bugzilla:602663 bugster:6874334
Patch23:      gdm-23-firsttime-helper.diff
# date:2010-07-20 owner:yippi type:branding
Patch24:      gdm-24-unnamed-union.diff
# date:2010-06-22 owner:yippi type:bug bugzilla:629713 bugster:6985185
Patch25:      gdm-25-expire-dialog.diff
# date:2010-09-24 owner:yippi type:bug bugzilla:630485 bugster:6973743
Patch26:      gdm-26-runtime-dir.diff
# date:2010-09-24 owner:yippi type:feature bugzilla:630848
Patch27:      gdm-27-pamservice.diff
# date:2010-12-14 owner:yippi type:feature bugster:6998997 bugzilla:621581
Patch28:      gdm-28-logindevperm.diff
# date:2011-03-29 owner:liyuan type:bug bugster:7013886
Patch29:      gdm-29-remove-gok.diff
# date:2011-03-29 owner:yippi type:bug bugster:7026714,7046515
Patch30:      gdm-30-no-warning.diff
# date:2011-05-19 owner:yippi type:bug bugster:7046505
Patch31:      gdm-31-audit.diff
#owner:yippi date:2011-06-24 type:bug bugster:6985971
Patch32:      gdm-32-disconnect.diff
#owner:yippi date:2011-07-25 type:branding
Patch33:      gdm-33-linc-cleanup.diff
#owner:yippi date:2011-08-29 type:bug bugster:7082840
Patch34:      gdm-34-vt.diff
#owner:yippi date:2011-11-07 type:bug bugster:7096672
Patch35:      gdm-35-restart.diff
#owner:ja208388 date:2012-02-01 type:bug bugster:7116350
Patch36:      gdm-36-no-remote-layout.diff
#owner:yippi date:2011-02-21 type:bug
Patch37:      gdm-37-strndup.diff
# date:2012-03-23 owner:pengwang type:bug bugster: 7060748
Patch38:      gdm-38-bindtextdomaincodeset.diff
URL:          http://projects.gnome.org/gdm/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%description
This version of GDM, the GNOME Display manager is based on
GTK2 and suited for the GNOME Desktop Environment. GDM is a
flexible X-Window Display Manager that allows to set many
options, usable for remote login, and provides a good looking
graphical interface.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1 
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1

cp %SOURCE1 gui/simple-greeter
cp %SOURCE2 gui/simple-greeter
cp %SOURCE3 gui/simple-greeter
cp %SOURCE4 gui/simple-greeter

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

# FIXME: create m4 dir as workaround for bugzilla #575218
test ! -d ./m4 && mkdir ./m4
glib-gettextize -f
intltoolize --force --copy --automake
libtoolize --force
aclocal $ACLOCAL_FLAGS -I . -I ./m4
autoheader
gnome-doc-prepare --force
automake -a -c -f
autoconf
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
	--mandir=%{_mandir} \
	--libexecdir=%{_libexecdir} \
	--with-pam-prefix=%{_sysconfdir} \
	--disable-scrollkeeper \
	--with-default-path=/usr/bin \
	--enable-rbac-shutdown=solaris.system.shutdown \
	--enable-ipv6 \
	--with-xauth-dir=/tmp \
	--with-incomplete-locales
make -j $CPUS


%install
make install DESTDIR=$RPM_BUILD_ROOT

# remove empty folder
rmdir $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d
rmdir $RPM_BUILD_ROOT/var/gdm

# The gdm-factory-slave and gdm-product-slave are non-functional and
# under development.  Likewise for gdm-restart and gdm-safe-restart.
# Do not ship these until they are ready.
#
rm $RPM_BUILD_ROOT/%{_libexecdir}/gdm-factory-slave
rm $RPM_BUILD_ROOT/%{_libexecdir}/gdm-product-slave
rm $RPM_BUILD_ROOT/%{_datadir}/gdm/autostart/LoginWindow/polkit-gnome-authentication-agent-1.desktop

# Remove gdm command.  We patch gdm to use pstack instead.
rm $RPM_BUILD_ROOT/%{_datadir}/gdm/gdb-cmd

# The /var/run directory should not be included with the packages.
# GDM will create it at run-time.
#
rmdir $RPM_BUILD_ROOT/var/run/gdm/greeter
rmdir $RPM_BUILD_ROOT/var/run/gdm
rmdir $RPM_BUILD_ROOT/var/run

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libexecdir}/gdm-crash-logger
%attr(755,root,root) %{_libexecdir}/gdm-factory-slave
%attr(755,root,root) %{_libexecdir}/gdm-host-chooser
%attr(755,root,root) %{_libexecdir}/gdm-product-slave
%attr(755,root,root) %{_libexecdir}/gdm-session-worker
%attr(755,root,root) %{_libexecdir}/gdm-simple-chooser
%attr(755,root,root) %{_libexecdir}/gdm-simple-greeter
%attr(755,root,root) %{_libexecdir}/gdm-simple-slave
%attr(755,root,root) %{_libexecdir}/gdm-user-switch-applet
%attr(755,root,root) %{_libexecdir}/gdm-xdmcp-chooser-slave
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init/Default
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession
%dir %{_sysconfdir}/gdm/PostLogin
%config %{_sysconfdir}/gdm/PostLogin/Default.sample
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/custom.conf
%{_sysconfdir}/gdm/gdm.schemas
%{_sysconfdir}/gconf/schemas/gdm-simple-greeter.schemas
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.gdm
%attr(750,gdm,gdm) %{_localstatedir}/gdm
%attr(750,gdm,gdm) %{_localstatedir}/log/gdm
%{_datadir}/pixmaps/*
%{_datadir}/gdm
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/gnome-2.0/ui/GNOME_FastUserSwitchApplet.xml
%{_libdir}/bonobo/servers/*.server
%{_localstatedir}/lib/gdm

%changelog
* Fri Mar 23 2012 - peng.pe.wang@oracle.com
- Add gdm-38-bindtextdomaincodeset.diff to fix CR #7060748
* Tue Feb 21 2012 - brian.cameron@oracle.com
- Add gdm-37-strndup.diff to ensure PAM_MAX_RESP_SIZE is honored.
* Wed Feb 01 2012 - javier.acosta@oracle.com
- Add patch gdm-36-no-remote-layout.diff to fix #7116350 (Escalated).
  Do not display Keyboard Layout Selection in GDM when GDM is
  is launched remotely.
* Mon Nov 07 2011 - brian.cameron@oracle.com
- Add patch gdm-35-restart.diff to fix CR #7096672, so that GDM will stop
  trying to manage a display if it fails 5 times in less than 60 seconds.
* Mon Aug 29 2011 - brian.cameron@oracle.com
- Add patch gdm-34-vt.diff to fix CR #7082840, where GDM does not return to
  VT1 when the gdm service is disabled.  This was a regression caused by
  fixing ConsoleKit to start the Xserver with the -novtswitch option
  (refer to CR #7032861).
* Mon Jul 25 2011 - brian.cameron@oracle.com
- Add patch gdm-33-linc-cleanup.diff to fix CR #7067741.
* Fri Jun 24 2011 - brian.cameron@oracle.com
- Add patch gdm-32-disconnect.diff to fix CR #6985971.
* Thu Jun 02 2011 - brian.cameron@oracle.com
- Bump to 2.30.7.
* Mon May 23 2011 - brian.cameron@oracle.com
- Add patch gdm-34-double-free.diff to fix bug #650659.
* Thu May 19 2011 - brian.cameron@oracle.com
- Add patch gdm-33-audit.diff to fix CR #7046505.
* Fri Apr 08 2011 - brian.cameron@oracle.com
- Bump to 2.30.6.
* Tue Mar 29 2011 - brian.cameron@oracle.com
- Add patch gdm-34-no-warning.diff to fix CR #7026714.
* Tue Mar 29 2011 - lee.yuan@oracle.com
- Add patch gdm-33-remove-gok.diff to remove gok desktop file.
* Tue Dec 14 2010 - brian.cameorn@oracle.com
- Add patches gdm-31-fix-version.diff to fix upstream bug #636662 and
  gdm-32-logindevperm.diff to fix bugster CR #6998997.
* Fri Sep 29 2010 - brian.cameron@oracle.com
- Add patch gdm-27-runtime-dir.diff to fix bugster #6973743.
- Add patch gdm-28-sigpipe.diff to fix bugster #6985932.
- Add patch gdm-29-pamservice.diff to make it possible to configure the PAM
  stack per display.
- Add patch gdm-30-xdmcp.diff to backport some fixes for XDMCP from GDM head.
* Thu Sep 16 2010 - brian.cameron@oracle.com
- Add patch gdm-26-expire-dialog.diff to fix CR #6985185.
* Fri Sep 10 2010 - jeff.cai@sun.com
- Rework the patch -21-xauth, fix for bugster #6982773
* Wed Aug 11 2010 - brian.cameron@oracle.com
- Bump to 2.30.5.
* Mon Jul 19 2010 - brian.cameron@oracle.com
- Add patch gdm-24-restart-buttons.diff.
* Wed Jul 07 2010 - halton.huo@sun.com
- Remove upstreamed patch gdm-19-allusers.diff and reorder
* Wed Jun 30 2010 - brian.cameron@oracle.com
- Bump to 2.30.4.
* Tue Jun 22 2010 - brian.cameron@oracle.com
- Add patch gdm-26-firsttime-helper.diff to improve LiveCD GDM integration.
* Thu May 27 2010 - halton.huo@sun.com
- Remove gdm-19-set-console.diff and reorder since CR #6942816 and
  CR #6885612 are now integrated in b140. Fixes CR #6955561 and doo #16077
* Mon May 17 2010 - brian.cameron@oracle.com
- Add patch gdm-24-xauth.diff to fix CR #6923733.  GDM needs to save
  xauth files in /tmp, not in /var.
- Add patch gdm-25-custom.diff to fix CR #6951765.  This fixes GDm so that if
  the user has Session=custom or Session=default in their dmrc file it is
  honored even if there is no corresponding desktop file installed.
* Thu May 13 2010 - halton.huo@sun.com
- Add patch gdm-23-down-gconf.diff to allow gdm is built with gconf 2.31.1
* Wed Apr 28 2010 - brian.cameron@sun.com
- Bump to 2.30.2.
* Mon Apr 26 2010 - brian.cameron@sun.com
- Bump to 2.30.1.  Remove 6 upstream patches.
* Thu Apr 22 2010 - brian.cameron@sun.com
- Add patch gdm-28-audiodefault.diff to fix bugster CR #6606096.
* Wed Apr 21 2010 - halton.huo@sun.com
- Add patch gdm-27-allusers.diff to fix doo #13723, bugzilla #614531.
* Mon Apr 19 2010 - halton.huo@sun.com
- Add patch gdm-26-xdmcp-seatid.diff to fix doo #15157.
* Mon Mar 29 2010 - brian.cameron@sun.com
- Bump to 2.30.0.
* Mon Mar 29 2010 - halton.huo@sun.com
  Reorder gdm-24-set-console.diff to gdm-25-set-console.diff
* Fri Mar 26 2010 - brian.cameron@sun.com
- Add patch gdm-21-timedlogin.diff to fix upstream bug #614062.  Renumber
  patches since gdm-22-no-click-login.diff depends on gdm-21-timedlogin.diff.
  Also update patch gdm-22-no-click-login to fix doo bug #15217.
* Fri Mar 26 2010 - halton.huo@sun.com
- Rework patch gdm-11-sol-notty.diff to only assign "/dev/console"
  when device is "?".
- Rework patch gdm-19-trusted-extensions.diff to fix simple-slave core dump
- Add patch gdm-24-set-console.diff to change ownership "/dev/console"
  for display :0 runns on VT.
* Tue Mar 09 2010 - halton.huo@sun.com
- Bump to 2.29.92
- Remove upstreamed patch 22-no-killall.diff and reorder
* Mon Feb 15 2010 - brian.cameron@sun.com
- Add patches gdm-23-windowpath.diff and gdm-24-xauth.diff to fix GNOME
  bugzilla bugs #609272, #605350, and doo bug #13571.
* Wed Jan 27 2010 - brian.cameron@sun.com
- Bump to 2.29.6.  Update patches.
* Tue Jan 26 2010 - brian.cameron@sun.com
- Add patch gdm-27-conversation.diff to fix bugzilla #607861, doo #13208.
* Mon Jan 25 2010 - halton.huo@sun.com
- Add patch 26-no-killall.diff to fix GNOME buzilla #607738, doo #13982.
* Thu Jan 21 2010 - halton.huo@sun.com
- Remove unused --ctrun argument 
- Add patch 25-atspi-dir.diff to fix GNOME bugzilla #607643.
* Thu Jan 21 2010 - halton.huo@sun.com
- Remove branding patch 24-xpath.diff since we add better fix in 
  gdm-01-dynamic-display.diff and reorder rest
* Fri Jan 15 2010 - halton.huo@sun.com
- Add branding patch xpath.diff to allow run progmrams under /usr/X11/bin.
- Update -09-userswitch.diff to a bug on GNOME bugzilla #607051.
* Thu Jan 14 2010 - brian.cameron@sun.com
- Add patch gdm-23-pam.diff to fix a typo in the PAM code introduced by the
  previous gdm-21-pam.diff patch.
* Thu Jan 14 2010 - halton.huo@sun.com
- Bump to 2.29.5
- Remove upstreamed patches: xdmcp.diff, pam.diff and scripts.diff and reorder
- Add patch libxklavier.diff to fix bugzilla #606808.
* Wed Jan 13 2010 - halton.huo@sun.com
- Add branding patch no-click-login.diff to fix doo bug #13568.
* Tue Jan 12 2010 - halton.huo@sun.com
- Add patch xdmcp-fail-second.diff to fix GNOME bugzilla bug #606724.
* Mon Jan 11 2010 - brian.cameron@sun.com
- Add patch gdm-20-xdmcp.diff to fix doo bug #13623, GNOME bugzilla bug
  #494817.
  Add patch gdm-21-pam.diff to fix bugster CR #6914426, bugzilla #606703.
  Add patch gdm-22-scripts.diff to fix doo bug #13811, GNOME bugzilla bug
  #602403.
* Tue Dec 22 2009 - brian.cameron@sun.com
- Reworked the patch to fix CR #6897155 and #6908857, renaming patch from
  gdm-19-workstation-owner.diff to gdm-19-trusted.diff.
* Mon Dec 21 2009 - brian.cameron@sun.com
- Bump to 2.29.4.  Remove upstream patches.
* Fri Dec 18 2009 - brian.cameron@sun.com
- Add patch gdm-22-workstation-owner.diff to fix bugster CR #6897155.
* Fri Dec 18 2009 - brian.cameron@sun.com
- Add patch gdm-20-combox-mnemonic.diff to fix GNOME bugzilla bug #604151.
- Add patch gdm-21-a11y-enable.diff to enable a11y.
* Mon Dec 07 2009 - brian.cameron@sun.com
- Add patch gdm-19-pstack.diff to use pstack to get the stack trace instead of
  using gdb.
* Fri Dec 04 2009 - brian.cameron@sun.com
- Add patch gdm-18-timed.diff to fix bug #603697.
* Wed Dec 02 2009 - brian.cameron@sun.com
- Add patch gdm-16-gconf.diff to fix doo bug #10915, bugzilla bug #594818.  Add
  patch gdm-17-runtime.diff to fix bugzilla bug #603756.
* Mon Nov 30 2009 - brian.cameron@sun.com
- Bump to 2.29.1.
* Mon Nov 30 2009 - halton.huo@sun.com
- Remove gdm-17-get-actual-vt.diff
* Fri Nov 27 2009 - halton.huo@sun.com
- Move -04-dynamic-display.diff to -01 and reorder
* Thu Nov 26 2009 - halton.huo@sun.com
- Add gdm-17-get-actual-vt.diff to fix doo bug #12563.
* Fri Nov 20 2009 - halton.huo@sun.com
- Merge gdm-14-console-user.diff into gdm-12-sol-notty.diff and reorder rest.
* Tue Nov 17 2009 - brian.cameron@sun.com
- Bump to 2.29.0.
* Thu Nov 05 2009 - brian.cameron@sun.com
- Add patch gdm-22-authdir.diff to lock down the GDM auth directory more
  tightly.  This patch is upstream.
* Thu Nov 05 2009 - brian.cameron@sun.com
- Add patch gdm-20-debug.diff to fix bugzilla bug #596831.  Renumber the
  gdm-20-last.diff patch to gdm-21-last.diff.
* Thu Nov 05 2009 - brian.cameron@sun.com
- Add patch gdm-20-last.diff to fix doo bug #11298.
* Tue Oct 27 2009 - brian.cameron@sun.com
- Port fix for bugzilla bug #494817 to the new GDM.
* Mon Oct 26 2009 - brian.cameron@sun.com
- Add patch gdm-18-setfacl.diff so that audio device permissions are set
  when GDM is running on "/dev/console", so that screen readers like orca work.
  Fixes doo bug #12125.
* Mon Oct 19 2009 - brian.cameron@sun.com
- Bump to 2.28.1.
* Fri Oct 16 2009 - brian.cameron@sun.com
- Add patch gdm-18-fixfocus.diff to fix bugzilla bug #598235, doo #10611.
* Fri Oct 16 2009 - halton.huo@sun.com
- Add branding patch console-user.diff to set /dev/console when display :0
  running on VT.
* Tue Oct 13 2009 - niall.power@sun.com
- Fix opensolaris.org defect #10981 to enable trusted extensions support
* Fri Oct 02 2009 - brian.cameron@sun.com
- Fix bugzilla bug #596830 which causes the login GUI to briefly display when
  using automatic login, which it is not supposed to do.
* Fri Sep 25 2009 - halton.huo@sun.com
- Add branding patch sol-notty.diff
* Mon Sep 21 2009 - brian.cameron@sun.com
- Bump to 2.28.0.  Remove upstream patches.
* Fri Sep 11 2009 - niall.power@sun.com
- Add patch gdm-17-failsafe-session.diff for  bugzilla: 594833, doo: 11302
* Thu Sep 10 2009 - brian.cameron@sun.com
- Add patch gdm-16-gconf.diff to address doo bug #10915.
* Tue Sep 08 2009 - brian.cameron@sun.com
- Add patch gdm-15-lang.diff to address bugzilla bug #536387, doo bug #10643.
* Tue Sep 08 2009 - brian.cameron@sun.com
- Add patch gdm-14-dialog-focus.diff so that the login GUI does not lose 
  focus after a dialog is presented.
* Tue Sep 08 2009 - brian.cameron@sun.com
- Add patch gdm-13-fixguioption.diff so that the greeter GUI does not mess
  up your language/session settings on follow-up logins if you fail
  authenticate once.
* Thu Sep 03 2009 - brian.cameron@sun.com
- Add patch gdm-12-userswitch.diff to ensure the switch user feature is only
  available when vtdaemon service is enabled.
* Wed Sep 02 2009 - brian.cameron@sun.com
- Add patch gdm-11-autologin to address bugzilla bug #591383, doo #10914.
* Tue Sep 01 2009 - brian.cameron@sun.com
- Add patch gdm-10-cache.diff to address bugzilla bug #565151, doo #10912.
* Mon Aug 31 2009 - brian.cameron@sun.com
- Add patch gdm-09-include-exclude.diff to address bugzilla #557553, doo #10913.
* Mon Aug 24 2009 - brian.cameron@sun.com
- Bump to 2.27.90
* Thu Aug 20 2009 - brian.cameron@sun.com
- Add patch gdm-08-pam-problem-dialog.diff to address bugzilla bug #583856.
* Wed Aug 19 2009 - brian.cameron@sun.com
- Remove gdm-restart and gdm-safe-restart since they are non-functional.  Add
  them back when they work.
* Mon Jul 27 2009 - halton.huo@sun.com
- Bump to 2.27.4, this is a rewrite release compared gdm 2.20x version,
  rework totally.
* Mon Jun 08 2009 - brian.cameron@sun.com
- Fix crashing issue in gdmsetup by adding patch gdm-10-gdmsetup.diff.
* Wed May 13 2009 - brian.cameron@sun.com
- Add patch gdm-09-fixlabels.diff to fix the labels in dialog box.
* Fri Apr 17 2009 - harry.fu@sun.com
- Provide corrected translations in po-community to fix doo bug #1510,#4919.
* Thu Mar 19 2009 - brian.cameron@sun.com
- Bump to 2.20.10.  Remove upstream patches.
* Wed Mar 18 2009 - brian.cameron@sun.com
- Add patch gdm-14-gid.diff to fix bugster bug #6819281.
* Wed Mar 04 2009 - takao.fujiwara@sun.com
- Add gdm-13-g11n-add-ka-es.diff for new es_US.UTF-8 and ka_GE.UTF-8. #6809375
* Fri Feb 27 2009 - brian.cameron@sun.com
- Add patch gdm-12-display.diff so that the DISPLAY variable is available 
  after changing the language.  Some PAM modules need the DISPLAY variable.
  Fixes bug #6811555.
* Mon Feb 24 2009 - brian.cameron@sun.com
- Add patch gdm-10-gestures.diff to fix doo bug #6766.  Add patch
  gdm-11-gok.diff to fix bug #6789400.
* Mon Feb 09 2009 - takao.fujiwara@sun.com
- Add patch gdm-09-xinitrc-migration.diff. Scripts are moved into xinitrc.d
* Mon Jan 05 2008 - brian.cameron@sun.com
- Add patch gdm-07-audit.diff to fix bug #6734635.  Add patch
  gdm-08-createdt.diff to fix doo bug #5973.
* Tue Dec 19 2008 - brian.cameron@sun.com
- Add patch gdm-06-xfree-xinerama.diff so that GDM builds using the Xfree
  Xinerama interfaces and not the obsolete Solaris ones.  Fixes P1 bug
  #6768573.
* Wed Dec 10 2008 - brian.cameron@sun.com
- Bump to 2.20.9.  Remove upstream patches.
* Thu Dec 04 2008 - halton.huo@sun.com
- Add disable-vt.diff to disable VT, remove it after bugster #6480003 is fixed
* Fri Nov 21 2008 - brian.cameron@sun.com
- Remove patch gdm-06-dbus.spec, it is no longer needed since D-Bus autolaunch
  is working better.
* Wed Nov 12 2008 - brian.cameron@sun.com
- Add gdm-10-no-recreate-sockets.diff so that GDM avoids recreating the
  sockets directories in /tmp.  This fixes Trusted Extensions.  Refer to
  doo bug #4719.
* Thu Oct 23 2008 - brian.cameron@sun.com
- Add patch gdm-09-fbconsole-fix.diff to address doo bug #3316.
* Mon Oct 20 2008 - takao.fujiwara@sun.com
- Updated gdm-07-xsession.diff to apply CJK locale only.
* Mon Sep 22 2008 - william.walker@sun.com
- Add bug number and better comment for gdm-06-dbus.diff patch.
* Wed Sep 17 2008 - brian.cameron@sun.com
- Add patch gdm-06-dbus.diff and gdm-07-xsession.diff.
* Wed Sep 03 2008 - brian.cameron@sun.com
- Bump to 2.20.8.  Remove upstream patches.
* Wed Sep 03 2008 - takao.fujiwara@sun.com
- Updated gdm-02-showlocale.diff not to show broken locales.
* Mon Aug 25 2008 - brian.cameron@sun.com
- In discussion with the Xserver team, it was determined that the previous
  patch is inappropriate.  The fbconsole program itself will be modified
  so it does a null-operation when it shouldn't be called, so GDM shouldn't
  avoid calling it in various situations.  In this discussion it was 
  highlighted that fbconsole needs the "-n" argument when called from the
  login program to avoid a race condition with XDMCP remote sessions.  Now
  the patch adds this feature.
* Tue Aug 19 2008 - takao.fujiwara@sun.com
- Replce gdm-04-disable-im.diff with gdm-04-im-config.diff with 6733528
* Thu Aug 07 2008 - simon.zheng@sun.com
- Add 07-fbconsole.diff.
* Tue Aug 05 2008 - brian.cameron@sun.com
- Add patch to add Kazakh language, as requested by Jan Trejbal and Jan Lana
  from the Sun localization team.  This patch is upstream.  Fixes bugster bug
  #6724439.
* Tue Jul 01 2008 - brian.cameron@sun.com
- Bump to 2.20.7.  Remove upstream patches.
* Fri Jun 20 2008 - simon.zheng@sun.com
- Add patch gdm-07-suspend-auth.diff to check suspend auth before
  showing supend button on sysmenu.
- Add patch gdm-06-fixcrash.diff to avoid GDM crashing on exit.  Fixes
  bugzilla bug #517526. 
* Thu May 22 2008 - brian.cameron@sun.com
- Add patch gdm-05-atom.diff so that GDM does not create the XFree86_VT
  atom if it does not exist.
* Mon May 12 2008 - brian.cameron@sun.com
- Bump to 2.20.6.
* Thu May 01 2008 - brian.cameron@sun.com
- Add patch gdm-06-disable-cde.diff so that we mark the CDE.desktop 
  file as being hidden.  Users can re-enable it by simply removing
  the "Hidden=true" line in the /usr/share/xsessions/CDE.desktop
  file.  And fix a bug that causes desktop files marked as
  Hidden=true to show up.
* Wed Apr 30 2008 - brian.cameron@sun.com
- Add patch gdm-05-fixcrash.diff fixing bugzilla crashing bug #517526.
* Tue Apr 15 2008 - brian.cameron@sun.com
- The gdmflexiserver.desktop file moved to a different directory, so 
  remove it from the correct location.  Fixes bug #6689633.
* Thu Apr 10 2008 - takao.fujiwara@sun.com
- Add gdm-04-disable-im.diff for disable IM on greeter.
* Mon Apr 07 2008 - brian.cameron@sun.com
- Bump to 2.20.5.
* Mon Mar 10 2008 - brian.cameron@sun.com
- Bump to 2.20.4.
* Fri Feb 29 2008 - takao.fujiwara@sun.com
- Add gdm-03-locale-support.diff
* Mon Jan 07 2008 - brian.cameron@sun.com
- Bump to 2.20.3 and remove upstream patch.
* Tue Nov 27 2007 - brian.cameron@sun.com
- Remove upstream gdm-03-sockaddr-len.diff patch and added new
  gdm-03-xdmcp-close.diff patch needed for XDMCP to work properly.
* Tue Nov 27 2007 - damien.carbery@sun.com
- Bump to 2.20.2.
* Thu Nov 08 2007 - brian.cameron@sun.com
- Add patch gdm-03-sockaddr-len.diff to fix XDMCP so it works.
* Fri Oct 19 2007 - damien.carbery@sun.com
- Bump to 2.20.1.
* Fri Oct  5 2007 - laca@sun.com
- use separate branding patches for nevada and indiana
- delete CDE.desktop when --without-dt is used
* Tue Sep 18 2007 - damien.carbery@sun.com
- Bump to 2.20.0.
* Thu Sep 06 2007 - damien.carbery@sun.com
- Bump to 2.19.8.
* Tue Aug 28 2007 - damien.carbery@sun.com
- Bump to 2.19.7.
* Wed Aug 15 2007 - brian.cameron@sun.com
- Bump to 2.19.6.  Remove upstream patch.
* Thu Aug 02 2007 - brian.cameron@sun.com
- Add patch gdm-02-showlocale.diff to address bugzilla bug #457871.
* Tue Jul 31 2007 - damien.carbery@sun.com
- Bump to 2.19.5. Remove upstream patch, 02-g11n-memory-handle.
* Fri Jul 13 2007 - takao.fujiwara@sun.com
- Added gdm-02-g11n-memory-handle.diff for memory handling.
* Tue Jul 10 2007 - damien.carbery@sun.com
- Bump to 2.19.4. Remove upstream patch, 02-vtsupport.
* Thu Jun 21 2007 - brian.cameron@sun.com
- Add patch for better utmpx processing and for VT support when it goes
  into Nevada.
* Mon Jun 18 2007 - damien.carbery@sun.com
- Bump to 2.19.3. Remove upstream patch, 02-xnestperms.
* Mon Jun 11 2007 - brian.cameron@sun.com
- Add patch to fix GDM so it doesn't modify device permissions if logging
  into a xnest session.
* Mon Jun  4 2007 - brian.cameron@sun.com
- Bump to 2.19.2.  Remove upstream patch gdm-02-no-gdm-in-cde-menu.diff.
* Thu Jue  1 2007 - simon.zheng@sun.com
- Point download path to 2.19.
* Mon May 14 2007 - brian.cameron@sun.com
* Merge patch gdm-03-nossh-in-xsession.diff with gdm-01-branding.diff
  since this is really a branding change.
* Mon May 14 2007 - brian.cameron@sun.com
- Bump to 2.19.1.
* Fri May 11 2007 - brian.cameron@sun.com
- Add --with-ctrun flag since I udpated the patch to require this
  argument.  This way people who want to build GDM on Solaris without
  SVC can do so.  Also added new gdm-05-nossh-in-xsession.diff patch.
* Thu May 10 2007 - brian.cameron@sun.com
- Bump to 2.19.0
* Thu Apr 12 2007 - brian.cameron@sun.com
- Fix upstream bug where if you fail to enter the proper root password
  after asking to run "Configure GDM" from the login menu, it asks for
  the password again.  If you type it in properly, then it starts a
  session as the root user.  This patch fixes this problem.
* Tue Apr 10 2007 - brian.cameron@sun.com
- Backout patch gdm-06-languages.diff since the patch doesn't work 
  properly.  Code needs to be backported from gdm SVN head, and I'll add
  back the patch later if we decide we need this in GNOME 2.18.
* Mon Apr 09 2007 - brian.cameron@sun.com
- Bump to 2.18.1.
* Wed Mar 21 2007 - brian.cameron@sun.com
- Add gdm-10-desktop.diff to fix Catagory in gdmsetup and gdmphotosetup
  desktop file.
* Tue Mar 13 2007 - brian.cameron@sun.com
- Add gdm-07-xephyr.diff and gdm-08-nodbus.diff patches.  Both are 
  upstream.
* Mon Mar 12 2007 - damien.carbery@sun.com
- Bump to 2.18.0.
* Fri May 09 2007 - brian.cameron@sun.com
- Add patch gdm-07-fixdesktop.diff to move GDM desktop entries into
  control center.  Add patch gdm-08-fixxnest.diff to fix GDM to send
  the right fontpath to the Xsun Xnest program.  Add patch
  gdm-09-no-gdm-in-cdu-menu.diff to ensure that GDM desktop menu 
  choices only appear if using GDM.  If not using GDM these programs
  are non-functional.
* Fri Mar 02 2007 - brian.cameron@sun.com
- Bump to 2.17.8
* Wed Feb 28 2007 - brian.cameron@sun.com
- Add patch to fix bugster bug #4877721 and bugzilla bug #108820.
  This patch won't go into GDM until 2.19, but we want this patch
  to go into 2.18 for Solaris.
* Tue Feb 15 2007 - brian.cameron@sun.com
- Remove sessionexit patch due to patch review comments.
* Tue Feb 13 2007 - takao.fujiwara@sun.com
- Add l10n tarball.
* Tue Feb 13 2007 - brian.cameron@sun.com
- Bump to 2.17.7 and add sessionexit patch to fix bugster bug
  6228488.
* Mon Jan 22 2007 - damien.carbery@sun.com
- Bump to 2.17.6.
* Mon Jan 08 2007 - damien.carbery@sun.com
- Bump to 2.17.5. Remove upstream patch, 07-fixdialogs.
* Sun Dec 17 2006 - laca@sun.com
- delete upstream patch fixsecurity.diff
- renumber remaining patch
* Fri Dec 15 2006 - brian.cameron@sun.com
- Patch from CVS head to fix dialog boxes so that they display text.
* Thu Dec 14 2006 - damien.carbery@sun.com
- Bump to 2.17.4.
* Wed Dec 06 2006 - brian.cameron@sun.com
- Remove Linux specific gdm-01-branding-defaults-linux.diff and
  gdm-03-pam-security-setup.diff.  Add patch comments.
* Tue Dec 05 2006 - brian.cameron@sun.com
- Add patch gdm-08-fixsecurity.diff to fix a security vulnerability found
  in gdmchooser.
* Tue Dec 05 2006 - damien.carbery@sun.com
- Bump to 2.17.3. Remove upstream patches, 07-linguas, 10-fixsessionname,
  09-gdmsetup-launch-menu-tooltip and 11-defaultdesc: Renumber remainder.
* Thu Nov 27 2006 - brian.cameron@sun.com
- Patch to fix setting the sesison name for gnome.desktop.
  Define better name for default.desktop and turn off console kit support
  since it doesn't work on Solaris yet.
* Thu Nov 23 2006 - damien.carbery@sun.com
- Remove upstream patchs, 09-sun-branding-patch and 10-fixfocus. Renumber
  remainder.
* Mon Nov 20 2006 - damien.carbery@sun.com
- Bump to 2.17.2.
* Wed Nov 15 2006 - calum.benson@sun.com
- Modify tooltip to match latest UI spec.
* Tue Oct 31 2006 - brian.cameron@sun.com
- Add patch to fix focus problem, fixed in CVS head.
* Tue Oct 31 2006 - damien.carbery@sun.com
- Bump to 2.16.2.
* Tue Oct 03 2006 - damien.carbery@sun.com
- Bump to 2.16.1. Remove upstream patch, gdm-10-fixcrash.diff.
* Sat Sep 23 2006 - brian.cameron@sun.com
- Add patch to fix crashing.
* Tue Sep 05 2006 - damien.carbery@sun.com
- Bump to 2.16.0.
* Tue Aug 22 2006 - damien.carbery@sun.com
- Bump to 2.15.10.
* Tue Aug 08 2006 - damien.carbery@sun.com
- Bump to 2.15.9.
* Tue Aug 01 2006 - damien.carbery@sun.com
- Bump to 2.15.8.
* Fri Jul 28 2006 - dermot.mccluskey@sun.com
- Fix minor typo.
* Wed Jul 26 2006 - brian.cameron@sun.com
- No longer set --with-at-bindir when calling configure since gok and
  gnopernicus are now in the standard /usr/bin location, not /usr/sfw/bin.
* Wed Jul 26 2006 - brian.cameron@sun.com
- Remove patches 7 and 11, merged into CVS head.  Also remove 
  gdmflexiserver.desktop from Solaris builds since we do not support
  Virtual Terminals.  Running this menu choice causes the session to
  hang on Solaris, so we shouldn't put it in the menus.
* Mon Jul 24 2006 - damien.carbery@sun.com
- Bump to 2.15.7.
* Fri Jun 16 2006 - brian.cameron@sun.com
- Fix focus so it returns to entry field after session, language, restart,
  suspend, and shutdown dialogs are used from options button.
* Mon Jun 12 2006 - brian.cameron@sun.com
- Bumped to 2.14.9.  This fixes automatic login, which was broken, and 
  corrects a number of warnings that were causing core dumping issues.
* Wed Jun 07 2006 - brian.cameron@sun.com
- Bumped to 2.14.8.  Removed patches no longer needed.  This fixes a serious
  security issue where a user can access the gdmsetup GUI with their user 
  password if the face browser is enabled (off by default on Solaris).
* Tue Jun 06 2006 - brian.cameron@sun.com
- Added patch gdm-12-fixflexiserver.diff to fix a core dumping problem.
  Modified gdm-01-branding-defaults-solaris.diff to better integrate with
  ctrun and updated the gdm.xml SVC manifest so that core dumps do not
  cause GDM to restart.  Removed gdm-05-fix-a11y-crash.diff since it didn't
  work as a fix.
* Mon May 23 2006 - brian.cameron@sun.com
- Bump to 2.14.7.
* Fri May 19 2006 - glynn.foster@sun.com
- Don't show the login photo dialog in the menus - removed according to
  the UI spec, and the functionality should really be apart of the 
  'Personal Information' dialog.
* Fri May 12 2006 - brian.cameron@sun.com
- Added patch gdm-12-fixconfig.diff to fix a problem that prevents users
  from disabiling the failsafe session in the menu.
* Fri May 12 2006 - brian.cameron@sun.com
- Updated to 2.14.6 which has the new features included in the patch
  added in the previous comment.  Replace the patch with a much smaller
  patch that just adds the "startagain" feature.  This is much more
  maintainable.  Also added a patch to update the Lanugage display
  provided by Peter Nugent.
* Thu May 11 2006 - brian.cameron@sun.com
- Add patch to add per-display configuration needed by Sun Ray.
  This patch also adds the updated Cancel button, the pam-error-logo,
  and real GTK+ buttons needed by Coolstart branding.  These changes
  all copied from GDM CVS head.
* Tue May 09 2006 - brian.cameron@sun.com
- Remove two patches that have been integrated into GDM, and add the
  avoidchown patch so that building this package works if you are a
  running as non-root.
* Wed May 03 2006 - damien.carbery@sun.com
- Bump to 2.14.5.
* Wed Apr 26 2006 - damien.carbery@sun.com
- Bump to 2.14.4.
* Tue Apr 25 2006 - damien.carbery@sun.com
- Bump to 2.14.3.
* Tue Apr 18 2006 - damien.carbery@sun.com
- Bump to 2.14.2.
* Thu Apr 13 2006 - damien.carbery@sun.com
- Remove upstream patches, 10-libvicious-dir and 11-fixaudit.
* Tue Apr 11 2006 - damien.carbery@sun.com
- Bump to 2.14.1.
* Tue Mar 14 2006 - damien.carbery@sun.com
- Bump to 2.14.0.
* Mon Mar 13 2006 - brian.cameron@sun.com
- Add patch 11 to fix auditing logic.  This patch can go away when the
  GDM 2.14.1 comes out.
* Fri Mar  3 2006 - damien.carbery@sun.com
- Bump to 2.13.0.10.
* Tue Feb 28 2006 - damien.carbery@sun.com
- Bump to 2.13.0.9.
- Remove upstream patch, 11-fixcore.
* Thu Feb 16 2006 - brian.cameron@sun.com
- Add patch 11 to fix core dumping issue in gdmsetup.  This fix is in 
  CVS head so it can go away when we update to the next version of GDM.
* Tue Feb 14 2006 - damien.carbery@sun.com
- Bump to 2.13.0.8.
* Tue Jan 31 2006 - damien.carbery@sun.com
- Bump to 2.13.0.7.
* Thu Jan 19 2006 - brian.cameron@sun.com
- Bump to 2.13.0.6.
* Mon Jan 16 2006 - damien.carbery@sun.com
- Move sfw reference (a Solaris specific dir) to SUNWgnome-display-mgr.spec.
* Mon Jan 16 2006 - padraig.obriain@sun.com
- Bump to 2.13.0.5; dd --with-prefetch and add /usr/sfw/include to CFILES to
  find <tcpd.h>
* Sun Jan 15 2006 - damien.carbery@sun.com
- Bump to 2.13.0.4
* Tue Dec 20 2005 - dermot.mccluskey@sun.com
- Bump to 2.13.0.3
* Tue Nov 29 2005 - laca.com
- remove javahelp stuff
* Tue Nov 29 2005 - damien.carbery@sun.com
- Bump to 2.8.0.7.
* Thu Oct 13 2005 - damien.carbery@sun.com
- Added patch, 10-libvicious-dir, to remove dir in vicious-extensions 
  Makefile.am, as it caused build to fail.
* Tue Oct 11 2005 - damien.carbery@sun.com
- Bump to 2.0.8.5
* Wed Sep 21 2005 - brian.cameron@sun.com
- Bump to 2.8.0.4
* Wed Sep 07 2005 - damien.carbery@sun.com
- Remove capplets dir from %files. Contents moved in 2.8.0.3.
* Mon Sep 05 2005 - damien.carbery@sun.com
- Bump to 2.8.0.3.
* Mon Aug 15 2005 - damien.carbery@sun.com
- Bump to 2.8.0.1.
* Wed Aug 03 2005 - laca@sun.com
- remove upstream patch xnext-remote-session.diff
* Thu Jul 14 2005 - damien.carbery@sun.com
- Add unpackaged files to %files (pixmaps/faces and gnome/capplets).
* Wed Jul 13 2005 - brian.cameron@sun.com
- Upgraded to 2.8.0.1
* Fri Jun 10 2005 - matt.keenan@sun.com
- Re-applied patch 01 linux branding
- Added patch 04/05 to build
* Tue May 10 2005 - leena.gunda@wipro.com
- Added patch gdm-45-xnest-remote-session.diff to allow remote login
  using XDMCP chooser in nested window. Fixes bug #6245415.
* Tue Apr 19 2005 - bill.haneman@sun.com
- Reinstated xevie-enabling patch on Linux, via gdm-44-linux-xevie.diff.
* Fri Apr 1 2005 - brian.cameron@sun.com
- Add patch 43 so that we set the Xserver on Solaris to 
  /usr/X11/bin/Xserver instead of /usr/X11/bin/X as per ARQ
  request.  Also now put /usr/openwin/bin in the user default
  patch here instead of in SUNWdtlogin-integration.spec.
* Thu Mar 17 2005 - brian.cameron@sun.com
- Add patch 42 to allow configure to specify the full path to the
  a11y AT programs used in the gesture listener configuration files.
  Patch in gdm CVS head.
* Thu Mar 10 2005 - Chookij.Vanatham@Sun.COM
- Fix gdm to fork user's session with "system locale" if "Default" option
  at the language menu being selected. [CR Id: 5032088]
* Thu Mar 03 2005 - brian.cameron@sun.com
- Fix XDMCP logic so that it works when an IPv4 address requests a 
  connection and IPV6 is enabled in GDM.  Patch40 fixes this.
* Tue Mar 01 2005 - dermot.mccluskey@sun.com
- remove patch 40 (XEVIE) - break new X server
* Fri Feb 25 2005 - brian.cameron@sun.com
- Added patch 40 to turn on XEVIE on Linux by default for the
  standard server to meet a11y requirements.  Fixes bug 6226645.
* Thu Feb 24 2005 - brian.cameron@sun.com
- Added branding patch 39 to change the GNOME string to "Java Desktop
  System" in a number of places in the c-code.
* Tue Feb 22 2005 - brian.cameron@sun.com
- Backed out patch 39/40 since ARC determined that these flags should
  not be set by default after initially indicating it was okay.
* Mon Feb 14 2005 - brian.cameron@sun.com
- Added patch 39/40 to support setting the Xserver with needed 
  a11y Xserver flags.  Fixes CR 6226645. 
* Tue Feb 08 2005 - brian.cameron@sun.com
- Removed --with-post-path argument since /usr/dt/bin and
  /usr/openwin/bin are added also by the /usr/dt/config/Xinitrc.jds.
  No need to have them in the PATH twice.  Also we do not
  need to add /usr/demo/jds/bin since all the *.desktop files
  have full-paths defined.
* Mon Feb 07 2005 - brian.cameron@sun.com
- Added patch-38 to more cleanly set the default PATH.  This replaces
  patches gdm-15-default.path.diff and gdm-16-reboot-shutdown-option.diff.
  The new patch sets more sensible definitions for Halt, Reboot, Shutdown
  commands on Solaris.  Also updated gdm-18-help.diff so it forwards
  the user to the right subsection when running gdmsetup help.
* Fri Jan 21 2005 - brian.cameron@sun.com
- Now only apply patch 37 when building on Linux.  Modified patch 37 to
  include needed changes for Solaris.
* Tue Jan 18 2005 - brian.cameron@sun.com
- Added patch gdm-37-branding.diff to fix branding issue in gnome.desktop
  file.  Also updated gdm-21-fix-a11y-crash.diff patch so it works on
  JDS Linux.
* Fri Jan 14 2005 - kazuhiko.maekawa@sun.com
- Updated l10n help tarball for cinnabar-linux
* Thu Dec 30 2004 - Chookij.Vanatham@Sun.COM
- #6213083 - Add note that legacy locales are NOT SUPPORTED for linux platform.
* Wed Dec 22 2004 - leena.gunda@wipro.com
- Added gdm-35-flexi-xdmcp-option.diff to make XDMCP chooser work in 
  flexiserver. Fixes bug #4992853.
* Fri Nov 26 2004 - leena.gunda@wipro.com
- Added gdm-34-xsession-use-ksh.diff to execute Xsession script using
  ksh on Solaris. Fixes stopper bug #6199960.
* Wed Nov 24 2004 - Chookij.Vanatham@Sun.COM
- #6196675 - all single byte locales removed.
* Thu Nov 18 2004 - hidetoshi.tajima@sun.com
- #5081827 - run /usr/dt/config/Xsession.jds instead of gnome-session
  for gnome session vid gdm. Solaris only.
* Wed Nov 17 2004 - matt.keenan@sun.com
- #6195855 Install correct man page
* Wed Nov 10 2004 - Chookij.Vanatham@Sun.COM
- Added gdm-31-current-locale.diff to fix bug#5100351
* Wed Nov 10 2004 - leena.gunda@wipro.com
- Remove gdm-26-start-gnome-volcheck.diff as gnome-volcheck is now
  started by gnome-session.
* Mon Nov 09 2004 - alvaro.lopez@sun.com
- Added new patch 31. It fixes #6182860: IPv6 logic is broken for New
  Login in a Nested Window, so the enable-ipv6 parameter of configure
  is "yes" again.
* Mon Nov 01 2004 - hidetoshi.tajima@sun.com
- Modify gdm-07-set-lc-messages-to-lang.diff. set LANG from RC_LANG
  in /etc/sysconfig/language when it is NULL. (CR 6188663)
* Fri Oct 29 2004 - damien.carbery@sun.com
- Add gdm-30-xorg-conf.diff to fix 6185918. configure.in checks for Xorg
  binary before looking for X (Xsun) binary.
* Thu Oct 28 2004 - matt.keenan@sun.com
- Added gdm-binary.1.gz, gdm.1.gz, gdmXnest.1.gz, gdmXnestchooser.1.gz,
  gdmchooser.1.gz, gdmflexiserver.1.gz, gdmgreeter.1.gz, gdmlogin.1.gz,
  gdmphotosetup.1.gz, gdmsetup.1.gz, gdmthemetester.1.gz, gdm-restart.1m.gz,
  gdm-safe-restart.1m.gz, gdm-stop.1m.gz, gdmconfig.1m.gz man pages
* Thu Oct 28 2004 - kazuhiko.maekawa@sun.com
- Updated l10n help tarball and added pt_BR
* Fri Oct 22 2004 - alvaro.lopez@sun.com
- "Source" entry updated
* Thu Oct 21 2004 - brian.cameron@sun.com
- Removed ipv6 support (--enable-ipv6=no) since this is breaking 
  gdm's ability to "login in a nested window".  Created bug 6182860
  so that issue gets fixed.
* Wed Oct 20 2004 - leena.gunda@wipro.com
- Added patch gdm-27-alt-meta-mapping.diff to restore 'Alt' and 'Meta' 
  mappings on sparc Solaris. Fixes bug 6173594.
* Wed Oct 20 2004 - leena.gunda@wipro.com
- Added patch gdm-26-start-gnome-volcheck.diff to start gnome-volcheck
  if Xserver is local. Fixes bug #5107205.
* Fri Oct 15 2004 - brian.cameron@sun.com
- Correct GreenLine integration.  The problem with disabling core dumps
  in the GreenLine XML file is that this causes GreenLine to ignore 
  core dumps for all programs, including gdm.  Now using patch 25
  we use ctrun to specify that only programs launched from gdm's 
  Xsession script (the user's session) are run in a separate GreenLine
  contract that ignores core dumps.  This way if gdm itself core dumps,
  GreenLine will correctly default back to the console login.
* Thu Oct 14 2004 - brian.cameron@sun.com
- Added patch gdm-24-sanitize-conf.diff to clean up language in
  gdm.conf file.  Fixes bug 5097046.  
* Wed Oct 06 2004 - balamurali.viswanathan@wipro.com
- Add patch gdm-22-xserver-location.diff to set GDM_XSERVER_LOCATION 
  with the x server type. Fixes bug #6174802
* Wed Oct 06 2004 - padraig.obriain@sun.com
- Added patch gdm-21-fix-a11y-crash.diff to remove
  /var/tmp/orbit-gdm/bonobo-activation-server-ior.  Fixes bug #5103715.
* Tue Oct 05 2004 - balamurali.viswanathan@wipro.com
- Modified patch gdm-15-default-path.diff to add 
  /usr/openwin/bin to the path. Fixes bug #5106790
* Mon Oct 04 2004 - yuriy.kuznetsov@sun.com
- Added gdm-20-g11n-i18n-button.diff to fix bug#5109970
* Wed Sep 29 2004 - <hidetoshi.tajima@sun.com>
- updated gdm-03-locale-alias.diff to remove non-UTF-8
locale entries from Traditional Chinese (big5 and big5hkscs)
* Mon Sep 20 2004 - dermot.mccluskey@sun.com
- Added chmod xdm in post-install script
* Fri Sep 17 2004 - bill.haneman@sun.com
- Added patch gdm-20-gdmwm-struts.diff, to fix bugzilla
  #143634.
* Thu Sep 16 2004 - dermot.mccluskey@sun.com
- Added post install script to set gdm as displaymanager
* Wed Sep 15 2004 - archana.shah@wipro.com
- Patch added gdm-19-add-acroread-path.diff
  Fixes bug# 5087934
* Thu Aug 26 2004 - vinay.mandyakoppal@wipro.com
- Patch gdm-18-help.diff provide help link.
* Thu Aug 26 2004 - bill.haneman@sun.com
- Updated patch gdm-10-a11y-gestures.diff.
* Tue Aug 24 2004 - brian.cameron@sun.com
- Enabling ipv6.
* Tue Aug 24 2004 - glynn.foster@sun.com
- Add back icons
* Tue Aug 24 2004 - laszlo.kovacs@sun.com
- removed some icons
* Thu Aug 19 2004 - damien.carbery@sun.com
- Integrate updated docs tarball from eugene.oconnor@sun.com.
* Fri Aug 13 2004 - bill.haneman@sun.com
- Update patch gdm-10-a11y-gestures.diff.  Fixes bug #5067111.
* Thu Jul 29 2004 - bill.haneman@sun.com
- use version 2.6.0.3 (fix for bugzilla 144920 and related GOK problem)
- remove patches gdm-08-gdmtranslate.diff and gdm-09-fix-which.diff,
  since they are included in 2.6.0.3.
* Thu Jul 22 2004 - vinay.mandyakoppal@wipro.com
- add patch to remove reboot/shutdown option on Solaris box
* Thu Jul 22 2004 - leena.gunda@wipro.com
- add patch gdm-15-default-path.diff to add /usr/dt/bin and /usr/sfw/bin
  to PATH for Solaris. 
* Wed Jul 14 2004 - niall.power@sun.com
- add patch from Johan to invoke jds registration on first login
* Thu Jul 08 2004 - arvind.samptur@wipro.com
- add patch to pass X server options instead of hardcoding 
  it in the gdm.conf.in
* Wed Jul 07 2004 - niall.power@sun.com
- ported to rpm4
* Wed Jul 07 2004 - dermot.mccluskey@sun.com
- added "-j $CPUS" to make to speed up builds
* Wed Jun 23 2004 - damien.carbery@sun.com
- Update a11y-gestures patch to add HAVE_XINPUT to acconfig.h.
  Remove xdmcp-enable patch (10) for app security reasons and move 13 to 10.
* Thu Jun 10 2004 - damien.carbery@sun.com
- Add patch 12 to add 'docs/C/figures' directory to the build.
* Mon May 31 2004 - niall.power@sun.com
- bump to 2.6.0.2
* Wed May 12 2004 - damien.donlon@sun.com
- Updated l10n content to gdm-l10n-po-1.1.tar.bz2
* Sun Apr 18 2004 - laca@sun.com
- enable javahelp conversion on Solaris
* Thu Apr 08 2004 - <niall.power@sun.com>
- bumped to 2.6.0.0 and updated dependencies
* Sat Apr 03 2004 - Chookij.Vanatham@Sun.COM
- added gdm-11-g11n-truncated-username.diff to fix 4955151
* Thu Apr 01 2004 - matt.keenan@sun.com
- javahelp conversion
* Wed Mar 31 2004 - <hidetoshi.tajima@sun.com>
- updated gdm-03-locale-alias.diff to fix 4884887
* Mon Mar 29 2004 - damien.donlon@sun.com
- Updated l10n content to gdm-l10n-po-1.0.tar.bz2
* Tue Mar 23 2004 - <glynn.foster@sun.com>
- Remove photo setup from %files since we didn't want it part of the 
  menus by default [$datadir/gnome/capplets/..]
* Mon Mar 22 2004 - <laca@sun.com>
- simplify %build
* Fri Mar 19 2004 - <damien.carbery@sun.com>
- Move autoheader and autoconf out of the platform specific section because
  it is common to both platforms.
* Fri Mar 19 2004 - <damien.carbery@sun.com>
- Change '\' to ';' so autoheader and autoconf run separately.
* Thu Mar 18 2004 - <brian.cameron@sun.com>
- Add patch 8 that fixes gdmtranslate so it compiles with -g, add
  patch 9 to fix scripts so that they don't call which (since which
  doesn't work on Solaris without an associated TTY), and add patch
  10 to turn on XDMCP support by default.
* Tue Mar 09 2004 - <niall.power@sun.com>
- bump to 2.5.90.2
* Mon Mar 01 2004 - <laca@sun.com>
- s$/usr/share$%{_datadir}$
* Thu Feb 26 2004 - <damien.carbery@sun.com>
- Fix small typos in description and change tar commmand to bzcat/tar.
- Remove --enable-console-helper on Solaris.
* Fri Feb 06 2004 - <matt.keenan@sun.com>
- Bump to 2.5.90.0, add docs, and ported QS patches
* Wed Jan 07 2004 - <niall.power@sun.com>
- Update to 2.4.4.7 for gnome-2.5.x
- Regenerated gdm-07-enable-tcp-by-default.diff
* Fri Oct 31 2003 - <glynn.foster@sun.com>
- Remove the Sun Supported menu entry patch, and reorder.
* Tue Oct 14 2003 - <markmc@sun.com> 2.4.4.3-2
- Add patch from Toshi to normalize the locale environment
  variables to be the same as LANG if they are unset.
* Fri Oct 10 2003 - <niall.power@sun.com> 2.4.4.3
- Update to 2.4.4.3 for gnome-2.4
* Wed Oct 01 2003 - <michael.twomey@sun.com> 2.4.2.101-14
- Add patch from Chookij to fix bug 4901817 (ja_JP.eucJP name)
* Thu Sep 18 2003 - <markmc@sun.com> 2.4.2.101-12
- Add patch from Leena to set AlwaysRestartServer to true.
* Thu Aug 21 2003 - <markmc@sun.com> 2.4.2.101-1
- Upgrade to 2.4.2.101
* Mon Aug 18 2003 - <markmc@sun.com> 2.4.2.99-7
- Set DisallowTCP to false by default.
* Fri Aug 08 2003 - <michael.twomey@sun.com> 2.4.2.99-3
- Updated locale.alias patch with a fix for zh_HK and a tweak
  for ja_JP.sjis (now ja_JP.SJIS). Fixing bug 4899317.
- Added a dependancy on openssl-devel. My build failed because 
  it was missing. I've also added openssl for good measure.
* Thu Aug 07 2003 - <michael.twomey@sun.com> 2.4.2.99-2
- Patched /etc/X11/gdm/Xsession so ~/.xim or /etc/skel/.xim is sourced which
  ensures that XIM input methods are started.
* Fri Aug 01 2003 - <markmc@sun.com> 2.4.2.99-1
- Upgrade to 2.4.2.99.
* Fri Aug 01 2003 - <glynn.foster@sun.com>
- Add supported menu category.
* Sun Jul 27 2003 - <markmc@sun.com>
- Update to 2.4.2.98
- Remove POTFILES.in patch. Seems to be in new tarball.
* Tue Jul 22 2003 - <michael.twomey@sun.com>
- Added a patch to update the POTFILES.in.
* Mon Jul 21 2003 - <glynn.foster@sun.com>
- Changed category of gdmsetup.desktop, so it appears in 
  the system menu again.
* Mon Jul 21 2003 - <michael.twomey@sun.com>
- Added zh_HK (Hong Kong Chinese) to the available languages.
* Fri Jul 18 2003 - <michael.twomey@sun.com>
- Patched locale.alias to include more Asian locale codeset 
  variants as requested by the Asian teams.
* Thu Jul 17 2003 - <markmc@sun.com>
- Fixed up the PAM configuration files.
- Removed the sysconfig/displaymanager hack
* Thu Jul 17 2003 - <niall.power@sun.com>
- update to version 2.4.2.97, release 0
- removed patches gdm-04-setlocale.diff and
  gdm-05-potfiles_in.diff, which are integrated upstream
- Changed sysconfdir to /etc/X11 so that new common sessions
  configuration directory (/etc/X11/dm/Sessions) can be shared
  with kdm etc.
- New common sessions dir /etc/X11/dm added to %files
* Fri Jul 11 2003 - <niall.power@sun.com>
- added setlocal patch - No more Welsh :) (or Czech!)
* Tue Jul 08 2003 - <niall.power@sun.com>
- Remove .desktop capplets from %files since photo setup
  is gone.
* Mon Jul 07 2003 - <glynn.foster@sun.com>
- Remove the photo setup .desktop menu item from the
  Settings menu.
* Tue Jul 01 2003 - <glynn.foster@sun.com>
- Move the pam and branding stuff to patches, and not 
  dirty copy hacks ;)
* Tue Jul 01 2003 - <glynn.foster@sun.com>
- Make gdm now depend on sun-gdm-themes which is a new
  package, replacing the old one.
* Fri Jun 30 2003 - <glynn.foster@sun.com>
- Make gdm now depend on Sundt-gdm-theme. This may be
  crack that we shouldn't do, but until I figure out
  how things work, let's go with it. 
* Fri Jun 30 2003 - <glynn.foster@sun.com>
- New tarball, bump version and reset release. Remove
  the old greeter theme, since we probably don't want
  it installed anyway
* Fri May 02 2003 - <niall.power@sun.com>
- Initial Sun release.
