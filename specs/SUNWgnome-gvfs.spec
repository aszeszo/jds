#
# spec file for package SUNWgnome-gvfs
#
# includes module(s): gvfs
#
# Copyright (c) 2007, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#
%include Solaris.inc

%use gvfs = gvfs.spec

Name:                    SUNWgnome-gvfs
IPS_package_name:        library/gnome/gvfs
License:                 LGPLv2
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GNOME virtual file system framework
Version:                 %{gvfs.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: library/libxml2
Requires: library/glib2
Requires: system/library/dbus
Requires: system/library/math
Requires: library/libsoup
Requires: gnome/config/gconf
Requires: library/gnome/gnome-libs
Requires: system/network/avahi
Requires: library/gnome/gnome-keyring
BuildRequires: service/network/samba
#BuildRequires: system/hal
BuildRequires: library/glib2
BuildRequires: system/library/dbus
BuildRequires: library/libsoup
BuildRequires: gnome/config/gconf
BuildRequires: library/gnome/gnome-libs
BuildRequires: system/network/avahi
BuildRequires: library/gnome/gnome-keyring
Requires: system/library/iconv/utf-8

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%gvfs.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
# -D_XPG4_2 is to get CMSG_SPACE declaration in <sys/socket.h>.
# /usr/sfw/include needed for libsmbclient.h
export CFLAGS="%optflags -D_XPG4_2 -D__EXTENSIONS__ -I/usr/sfw/include"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags -lxml2 -L/usr/sfw/lib -R/usr/sfw/lib"
%gvfs.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gvfs.install -d %name-%version
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la
# Remove gvfs-bash-completion.sh, a bash autocompletion script in the
# %{_sysconfdir}/profile.d dir. We don't ship such files. It is the only file
# under %{_sysconfdir} so remove the entire structure.
# rm/rmdir used instead of 'rm -r' so that files added under %{_sysconfdir} are
# found, via build failure.
rm $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/gvfs-bash-completion.sh
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
rmdir $RPM_BUILD_ROOT%{_sysconfdir}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d gvfs-%{gvfs.version} README AUTHORS
%doc(bzip2) -d gvfs-%{gvfs.version} COPYING NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/gvfsd*
%{_libdir}/gvfs-hal-volume-monitor
%{_libdir}/libgvfscommon.so*
%{_libdir}/gio/modules/*.so*
%{_libdir}/libgvfscommon-dnssd.so*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/dbus-1/services/gvfs-daemon.service
%{_datadir}/dbus-1/services/gvfs-metadata.service
%{_datadir}/dbus-1/services/org.gtk.Private.HalVolumeMonitor.service
%{_datadir}/gvfs
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Dec 14 2011 - padraig.obriain@oracle.com
- Change system/hal to service/hal so that it builds with jucr.
* Wed Nov 30 2011 - padraig.obriain@oracle.com
- Update package names and remove gnu_iconv option.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu Feb 05 2009 - christian.kelly@sun.com
- Add lib to %files.
* Wed Jul 23 2008 - damien.carbery@sun.com
- Update %files for new tarball. Two new files delivered.
* Thu Jul 10 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWavahi-bridge-dsd/-devel to ensure avahi support built.
* Wed Jun 18 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-config/-devel, SUNWgnome-libs/-devel and SUNWhal
  after check-deps.pl run.
* Fri May 23 2008 - damien.carbery@sun.com
- Add code to incorporate manpages tarball.
* Wed Apr 16 2008 - damien.carbery@sun.com
- Change how %{_sysconfdir}/profile.d is removed to be correct and future proof.
* Tue Apr 15 2008 - alvaro@sun.com
- SUNWgnome-gvfs-root removed.
* Tue Apr 07 2008 - jedy.wang@sun.com
- Add manpages.
* Tue Mar 04 2008 - damien.carbery@sun.com
- Change SUNWevolution-libs to SUNWlibsoup as libsoup is the real dependency.
* Mon Mar 03 2008 - alvaro.lopez@sun.com
- Added new dependencies: SUNWevolution-libs{,-devel}
* Thu Feb 28 2008 - damien.carbery@sun.com
- Move from spec-files-extra, rename to SUNWgnome-gvfs and remove SFEgio
  dependency. Update %files and add l10n pkg for 0.1.8 tarball
* Sun Nov 18 2007 - daymobrew@users.sourceforge.net
- Add support for building on Indiana systems. Add changes for gvfs 0.0.2.
* Fri Nov 09 2007 - nonsea@users.sourceforge.net
- Add SFEgio to Requires, add SFEgio-devel to BuildRequires.
* Thu Nov 07 2007 - damien.carbery@sun.com
- Initial version.



