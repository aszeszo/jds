#
# spec file for package SUNWtime-slider
#
# includes module(s): time-slider
#
# Copyright (c) 2010, 2012 Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner niall
#
%include Solaris.inc
%include l10n.inc
# NOTE: If the version is bumped the new tarball just submit the new tarball
#       to /sgnome.

%define OSR developed in the open, no OSR needed:0

Name:                    SUNWgnome-time-slider
IPS_package_name:        desktop/time-slider
Meta(info.classification): %{classification_prefix}:Applications/Configuration and Preferences
Summary:                 Time Slider ZFS snapshot management for GNOME
License:                 cr_Oracle
Version:                 0.2.101
Source:                  http://dlc.sun.com/osol/jds/downloads/extras/time-slider/time-slider-%{version}.tar.bz2
Source1:                 time-slider-po-sun-%{po_sun_version}.tar.bz2
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires:           library/python-2/pygtk2-26
BuildRequires:           desktop/gksu
Requires:                runtime/python-26
Requires:                library/python-2/python-dbus-26
Requires:                library/python-2/python-notify-26
Requires:                desktop/gksu
Requires:                gnome/zenity
Requires:                service/gnome/desktop-cache
Obsoletes:               SUNWzfs-auto-snapshot

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n time-slider-%{version}
bzcat %SOURCE1 | tar xf -
# replace the old translations
cd po-sun; cp *.po LINGUAS ../po; cd ..

%build
make

%install
export PYTHON="/usr/bin/python2.6"
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/security/auth_attr.d
mkdir -p $RPM_BUILD_ROOT/etc/user_attr.d
echo 'zfssnap::::auths=solaris.smf.manage.zfs-auto-snapshot;profiles=ZFS File System Management' > $RPM_BUILD_ROOT/etc/user_attr.d/desktop-time-slider
echo 'solaris.smf.manage.zfs-auto-snapshot:::Manage the ZFS Automatic Snapshot Service::' > $RPM_BUILD_ROOT/etc/security/auth_attr.d/desktop-time-slider

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%post
%restart_fmri icon-cache

%actions
user ftpuser=false gcos-field="ZFS Automatic Snapshots Reserved UID" group=daemon login-shell=/usr/bin/pfsh password=NP uid=51 username=zfssnap

%files
%defattr (-, root, bin)
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/time-slider-*
%{_libdir}/time-sliderd
%dir %attr (0755, root, bin) %{_libdir}/time-slider
%dir %attr (0755, root, bin) %{_libdir}/time-slider/plugins/
%dir %attr (0755, root, bin) %{_libdir}/time-slider/plugins/rsync
%{_libdir}/time-slider/plugins/rsync/*
%dir %attr (0755, root, bin) %{_libdir}/time-slider/plugins/zfssend
%{_libdir}/time-slider/plugins/zfssend/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*.desktop
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/time-slider-setup.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/time-slider-setup.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/time-slider-setup.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/36x36
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/36x36/apps
%{_datadir}/icons/hicolor/36x36/apps/time-slider-setup.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/time-slider-setup.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/72x72
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/72x72/apps
%{_datadir}/icons/hicolor/72x72/apps/time-slider-setup.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/96x96
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/96x96/apps
%{_datadir}/icons/hicolor/96x96/apps/time-slider-setup.png
%{_datadir}/time-slider/*

%files root
%defattr (-, root, bin)
%attr (0755, root, sys) %dir %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1/system.d
%{_sysconfdir}/dbus-1/system.d/*
%dir %attr (-, root, sys) %{_sysconfdir}/xdg
%dir %attr (-, root, sys) %{_sysconfdir}/xdg/autostart
%attr (-, root, sys) %{_sysconfdir}/xdg/autostart/*
# '/etc' directory already declared above as "%{_sysconfdir}"
%dir %attr (0755, root, sys) /etc/security
%dir %attr (0755, root, sys) /etc/security/auth_attr.d
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %attr (0444, root, sys) /etc/security/auth_attr.d/*
%dir %attr (0755, root, sys) /etc/user_attr.d
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %attr (0444, root, sys) /etc/user_attr.d/*
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, sys) /lib/svc/manifest
%dir %attr (0755, root, sys) /lib/svc/manifest/application
%class(manifest) %attr (0444, root, sys) /lib/svc/manifest/application/time-slider.xml
%class(manifest) %attr (0444, root, sys) /lib/svc/manifest/application/time-slider-plugin.xml
%dir %attr (0755, root, sys) /lib/svc/manifest/system
%dir %attr (0755, root, sys) /lib/svc/manifest/system/filesystem
%class(manifest) %attr (0444, root, sys) /lib/svc/manifest/system/filesystem/auto-snapshot.xml
%attr (0555, root, bin) /lib/svc/method/time-slider
%attr (0555, root, bin) /lib/svc/method/time-slider-plugin
%attr (0555, root, bin) /lib/svc/method/time-slider-rsync

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale/*

%changelog
* Mon Feb 06 2012 - padraig.obriain@oracle.com
- Bump to version 0.2.101 to fix CR 7065464.
* Tue Jan 24 2012 - padraig.obriain@oracle.com
- Bump to version 0.2.100 to fix CR 7064327.
* Fri Jul 29 2011 - erwann.chenede@oracle.com
- moved smf files from var to lib
* Tue Aug 17 2010 - niall.power@oracle.com
- Adjust License tag to cr_Oracle for build 146a
* Thu Jul 29 2010 - niall.power@oracle.com
- Drop upstreamed patch "-rsync-expire.diff"
- Bump to version 0.2.97
* Wed June 16 2010 - niall.power@oracle.com
- Add missing RBAC fragments for user_attr and auth_attr.
- Add patch "01-rsync-expire.diff" to fix defect 16280
* Fri June 04 2010 - niall.power@oracle.com
- Bump to version 0.2.96. Updated with new dependencies
* Fri Feb 05 2010 - harry.fu@sun.com
- Copy LINGUAS and po files from po-sun only, not Makefile.
* Thu Feb 04 2010 - harry.fu@sun.com
- Replace the old translations with the latest ones from po-sun.
* Wed Dec 09 2009 - niall.power@sun.com
- Add patch time-slider-01-python26.diff and update
  BuildRequires and Requires python deps to python26 variants.
* Mon Nov 23 2009 - niall.power@sun.com
- Revert to previous version (0.2.10) until removed features
  reimplemented or ARC review approved. Backs out prev. commit
* Thu Nov 05 2009 - niall.power@sun.com
- Bumped version to 0.2.95
- Bumped python requirements to 2.6
- Obsoletes SUNWzfs-auto-snapshot from 0.2.95+
* Fri Jul 10 2009 - niall.power@sun.com
- Bump version to 0.2.10. D.O.O# 8667, 8454 & 8685
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Fri Feb 20 2009 - niall.power@sun.com
- Bump to 0.2.6 tarball to incorporate updated l10n
  from Takao Fujiwara. bugster 6807414
- Dropped upstreamed -01-python-env.diff
* Thu Feb 12 2009 - niall.power@sun.com
- Add patch 01-python-env.diff to fully fix 6754650.
  Upstreamed patch. Remainder of fix already in 0.2.5 tarball
* Thu Feb 05 2009 - niall.power@sun.com
- Bump to 0.2.5
- Add patch potfiles.diff to get GTK translations.
- Add patch g11n-i18n-ui.diff to show localized date.
* Fri Jan 09 2009 - niall.power@sun.com
- Bump to 0.2.3
* Mon Dec 17 2008 - niall.power@sun.com
- Bump to 0.2.2
* Mon Oct 20 2008 - takao.fujiwara@sun.com
- Bump to 0.1.2 with .po files. Add l10n packages.
* Fri Oct 10 2008 - niall.power@sun.com
- disable auto SMF enabelment in post install
* Wed Oct 08 2008 - niall.power@sun.com
- Bump to 0.1.1 Drop upstreamed g11n-i18n.diff
* Thu Oct 02 2008 - takao.fujiwara@su.com
- Add time-slider-01-g11n-i18n.diff
* Wed Sep 18 2008 - niall.power@sun.com
- Initial spec file created.



