#
# spec file for package SUNWgnome-media-player
#
# includes module(s): totem
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%define makeinstall make install DESTDIR=$RPM_BUILD_ROOT
%use totem = totem.spec
%use rhythmbox = rhythmbox.spec

Name:                    SUNWgnome-media-player
IPS_package_name:        gnome/media/gnome-media-player
Meta(info.classification): %{classification_prefix}:Applications/Sound and Video
Summary:                 GNOME media player 
Version:                 %{default_pkg_version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_prefix}
SUNW_Copyright:          %{name}.copyright
License:                 GPL v2, LGPL v2, BSD, MIT
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: library/desktop/libglade
BuildRequires: library/audio/gstreamer
BuildRequires: x11/server/xorg
BuildRequires: gnome/gnome-panel
BuildRequires: data/iso-codes
BuildRequires: library/media-player/totem-pl-parser
BuildRequires: gnome/file-manager/nautilus
BuildRequires: system/library/dbus
BuildRequires: gnome/config/gconf
BuildRequires: library/gnome/gnome-vfs
BuildRequires: library/gnome/gnome-component
BuildRequires: runtime/python-26
BuildRequires: library/python-2/pygtk2-26
BuildRequires: library/python-2/pygobject-26
BuildRequires: library/desktop/gtkhtml
BuildRequires: library/popt
BuildRequires: library/musicbrainz/libmusicbrainz
BuildRequires: gnome/media/gnome-media
BuildRequires: web/browser/firefox
BuildRequires: gnome/theme/gnome-icon-theme
BuildRequires: library/libsoup
BuildRequires: library/python-2/python-gst-26
BuildRequires: library/desktop/libsexy
BuildRequires: library/desktop/libgdata
BuildRequires: crypto/gnupg
BuildRequires: developer/documentation-tool/gtk-doc
BuildRequires: developer/gnome/gnome-doc-utils
BuildRequires: data/xml-common
BuildRequires: data/docbook/docbook-style-dsssl
BuildRequires: data/docbook/docbook-style-xsl
BuildRequires: data/docbook/docbook-dtds
BuildRequires: data/sgml-common
BuildRequires: text/gnu-sed
BuildRequires: developer/vala
Requires: library/desktop/libglade
Requires: library/gnome/gnome-libs
Requires: gnome/file-manager/nautilus
Requires: gnome/gnome-panel
Requires: library/media-player/totem-pl-parser
Requires: data/iso-codes
Requires: system/library/dbus
Requires: gnome/config/gconf
Requires: gnome/media/gnome-media
Requires: library/gnome/gnome-vfs
Requires: system/library/math
Requires: library/libxml2
Requires: library/gnome/gnome-component
Requires: service/gnome/desktop-cache
Requires: runtime/python-26
Requires: library/python-2/pygtk2-26
Requires: library/python-2/pygobject-26
Requires: library/desktop/gtkhtml
Requires: library/popt
Requires: library/musicbrainz/libmusicbrainz
Requires: gnome/media/gnome-media
Requires: web/browser/firefox
Requires: gnome/theme/gnome-icon-theme
Requires: system/hal
Requires: library/libsoup
Requires: library/python-2/python-gst-26
Requires: library/desktop/libsexy
Requires: library/desktop/libgdata
Requires: library/desktop/gtk2
Requires: gnome/file-manager/nautilus
Requires: library/audio/gstreamer
Requires: system/library/dbus

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
%totem.prep -d %name-%version
%rhythmbox.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export CFLAGS="%optflags -D__EXTENSIONS__ -I%{_includedir} -I/usr/X11/include"
export CXXFLAGS="%cxx_optflags -features=extensions -I/usr/X11/include"
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%{?arch_ldadd} -z ignore -Bdirect -z combreloc -L/usr/X11/lib -R/usr/X11/lib -L/usr/sfw/lib -R/usr/sfw/lib -lX11"

%ifarch sparc
export x_includes="/usr/openwin/include"
export x_libraries="/usr/openwin/lib"
%endif

%totem.build -d %name-%version
%rhythmbox.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%totem.install -d %name-%version
%rhythmbox.install -d %name-%version
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'


# We remove the below totem plugins including Gromit since its
# respective dependecy gromit is missing on Solaris:
#
# - Gromit: presentation helper to make annotations on screen
#
rm -r $RPM_BUILD_ROOT%{_libdir}/totem/plugins/gromit

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):unsupported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%attr (0755, root, bin)%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/nautilus/extensions-2.0/lib*.so*
%{_libdir}/firefox/plugins
%{_libdir}/rhythmbox
%{_libdir}/rhythmbox-metadata
%{_libdir}/totem-plugin-viewer
%{_libdir}/totem
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, bin) %{_datadir}/dbus-1
%dir %attr (0755, root, bin) %{_datadir}/dbus-1/services
%doc rhythmbox-%{rhythmbox.version}/AUTHORS
%doc rhythmbox-%{rhythmbox.version}/README
%doc(bzip2) rhythmbox-%{rhythmbox.version}/COPYING
%doc(bzip2) rhythmbox-%{rhythmbox.version}/NEWS
%doc(bzip2) rhythmbox-%{rhythmbox.version}/ChangeLog
%doc(bzip2) rhythmbox-%{rhythmbox.version}/po/ChangeLog
%doc(bzip2) rhythmbox-%{rhythmbox.version}/help/ChangeLog
%doc totem-%{totem.version}/AUTHORS
%doc totem-%{totem.version}/README
%doc(bzip2) totem-%{totem.version}/COPYING
%doc(bzip2) totem-%{totem.version}/NEWS
%doc(bzip2) totem-%{totem.version}/license_change
%doc(bzip2) totem-%{totem.version}/ChangeLog
%doc(bzip2) totem-%{totem.version}/po/ChangeLog
%doc(bzip2) totem-%{totem.version}/help/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/dbus-1/services/org.gnome.Rhythmbox.service
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/rhythmbox/C
%{_datadir}/gnome/help/totem/C
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16/devices
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/22x22/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/22x22/devices
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/devices
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/places
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/devices
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/devices
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/256x256
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/256x256/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable/devices
%attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/16x16/devices/*
%attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/22x22/devices/*
%attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/24x24/devices/*
%attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/32x32/devices/*
%attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/48x48/devices/*
%attr (-, root, other) %{_datadir}/icons/hicolor/256x256/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/scalable/devices/*
%{_datadir}/omf/rhythmbox/*-C.omf
%{_datadir}/omf/totem/*-C.omf
%{_datadir}/rhythmbox
%{_datadir}/totem
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%{_datadir}/gtk-doc
%{_datadir}/icons/hicolor/*/places/*.png

%files root
%defattr(-, root, sys)
%attr(0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/rhythmbox.schemas
%{_sysconfdir}/gconf/schemas/totem-handlers.schemas
%{_sysconfdir}/gconf/schemas/totem-video-thumbnail.schemas
%{_sysconfdir}/gconf/schemas/totem.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/rhythmbox
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z]*.omf

%changelog
* Mon Feb 13 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Add devel package for include files.
* Thu Mar 06 2010 - yuntong.jin@sun.com
- Add BuildRequires: SUNWlibgdata to enable youtube plugin to fix d.o.o:15887
* Wed Jul 29 2009 - brian.cameron@sun.com
- Fix packaging after updating to 2.27.1.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Thu Mar 26 2009 - jerry.tan@sun.com
- move totem-pl-parser out to SUNWtotem-pl-parser 
* Fri Feb 27 2009 - jedy.wang@sun.com
- Use find command to remove static libraries.
* Tue Jan 20 2009 - brian.cameron@sun.com
- Fix packaging after bumping totem-pl-parser to 2.25.1 and totem to 2.25.3.
* Fri Dec 05 2008 - brian.cameron@sun.com
- Add attributes for icons in packaging.
* Thu Sep 18 2008 - brian.cameron@sun.com
- Fix packaging.
* Fri Sep 12 2008 - brian.cameron@sun.com
- Add new copyright files.
* Mon Jul 21 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWlibsexy/-devel to fix 6725226.
* Thu May 15 2008 - jijun.yu@sun.com
- Remove the rm commands which won't useful any more.
* Thu May 15 2008 - jijun.yu@sun.com
- Remove rhthmbox upnp_coherence plugin.
* Thu May 08 2008 - jijun.yu@sun.com
- Remove 2 plugins including youtube and gromit. 
* Mon Apr 28 2008 - jijun.yu@sun.com
- Remove the 4 rm commands added on Apr.25, since the same functions will be 
  done at configuring. 
* Fri Apr 25 2008 - jijun.yu@sun.com
- Remove some plugins including libtotem-gmp, libtotem-narrowspace,
  libtotem-mully and libtotem-cone, because they are not supported on Solaris.
* Mon Mar 31 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Thu Mar 13 2008 - brian.cameron@sun.com
- Remove .la/.a files from totem plugin library directories.
* Fri Jan 11 2008 - damien.carbery@sun.com
- nautilus extensions go to extensions-2.0 dir. Change %files and %install.
* Wed Jan 09 2008 - damien.carbery@sun.com
- Uncomment plugins code as firefox 2 is back in the build.
* Thu Jan 03 2008 - damien.carbery@sun.com
- Comment out plugins code as firefox is not found by totem or rhythmbox and
  browser plugins not built. This is a workaround while firefox build corrected.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Mon Dec 03 2007 - brian.cameron@sun.com
- Add totem-pl-parser.
* Thu Nov 08 2007 - brian.cameron@sun.com
- Added proper totem/totem-video-thumbnailer manpages in the manpage
  tarball, so now remove the NROF ones included by totem module in the
  %install step.
* Fri Oct 12 2007 - laca@sun.com
- add /usr/X11/include to CXXFLAGS
* Thu Oct  4 2007 - laca@sun.com
- add %arch_ldadd to LDFLAGS for the libintl libs
* Tue Jul 03 2007 - damien.carbery@sun.com
- Browser plugins now installed to firefox/plugins dir.
* Wed Jun 13 2007 - damien.carbery@sun.com
- Comment out removal of 2 la/a files as they are not being installed.
* Wed May 23 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-themes/-devel for gnome-icon-theme, required by
  totem.
* Tue May 15 2007 - damien.carbery@sun.com
- Add %{_libdir}/totem to %files; remove .a and .la files from there.
* Thu Apr 26 2007 - laca@sun.com
- delete some unnecessary env variables; set CXX to $CXX -norunpath because
  libtool swallows this option sometimes and leaves compiler paths in the
  binaries, fixes 6497719
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Mon Mar 12 2007 - laca@sun.com
- delete rhythmbox .la files in rhythmbox.spec
* Thu Mar 01 2007 - halton.huo@sun.com
- Remove -I%{_includedir}/mps from CXXFLAGS because it is 
  in /usr/lib/pkgconfig/firefox-xpcom.pc
* Wed Feb 28 2007 - halton.huo@sun.com
- Add -I%{_includedir}/mps into CXXFLAGS to fix build error.
* Thu Feb 22 2007 - damien.carbery@sun.com
- Add '-features=extensions' to CXXFLAGS because __func__ is used in new totem
  tarball.
* Mon Feb 12 2007 - damien.carbery@sun.com
- Remove '-I/usr/include/mps' from CFLAGS/CXXFLAGS. Make change to
  firefox-xpcom.pc file instead.
* Thu Nov 30 2006 - damien.carbery@sun.com
- Remove duplicate 'BuildRequires: SUNWfirefox-devel' line.
* Mon Nov 20 2006 - laca@sun.com
- s/Requires: SUNWfirefox-devel/Requires: SUNWfirefox/, fixes 6495619
* Fri Oct 20 2006 - damien.carbery@sun.com
- Remove SUNWhalh BuildRequires because header files are in SUNWhea in snv_51.
* Fri Oct 13 2006 - damien.carbery@sun.com
- Delete .a and .la files.
* Mon Oct 02 2006 - damien.carbery@sun.com
- Remove application-registry and mime-info dirs from %files as they are no 
  longer installed.
* Mon Sep 18 2006 - Brian.Cameron@sun.com
- Add SUNWhalh BuildRequires.
* Fri Sep 08 2006 - Matt.Keenan@sun.com
- Remove "rm" of _mandir during %install, add man page tarball for rhythmbox.1
  Deliver totem.1, totem-video-thumbnailer.1 from community, and manp
* Thu Aug 17 2006 - damien.carbery@sun.com
- Add the mozilla/plugins dir and totem-mozilla-viewer.
- Add Build/Requires SUNWfirefox/-devel for the xpidl compiler.
* Wed Aug 16 2006 - damien.carbery@sun.com
- Remove empty mozilla/plugins dir in %install.
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
* Fri Aug 11 2006 - damien.carbery@sun.com
- Change SUNWhal-devel ref to SUNWhal as the former does not exist.
* Tue Aug 08 2006 - damien.carbery@sun.com
- Update Build/Requires after check-deps.pl run.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Wed Jun 21 2006 - brian.cameron@sun.com
- Fix packaging.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu May 25 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Fri May 12 2006 - damien.carbery@sun.com
- Small update to dependency list after check-deps.pl run.
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Thu Mar  2 2006 - damien.carbery@sun.com
- Remove locale dir from l10n package - no files installed there.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Fri Sep 30 2005 - brian.cameron@sun.com
- Fix l10n packaging.
* Tue Sep 27 2005 - brian.cameron@sun.com
- Move back to default prefix instead of /usr/demo/jds, since we have
  decided to support this application.
* Wed Jan 19 2005 - matt.keenan@sun.com
- Deliver javahelp files for totem #6197736
* Mon Dec 13 2004 - damien.carbery@sun.com
- Move to /usr/sfw to implement ARC decision.
* Sun Nov 14 2004 - laca@sun.com
- move to /usr/demo/jds
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Fri Oct 01 2004 - takao.fujiwara@sun.com
- Added l10n package
- Added '--x-libraries' option in configure to fix bug 5081938
* Sat Sep 11 2004 - laca@sun.com
- Set LDFLAGS so Xrandr and Xrender can be found.
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Fri Jul 23 2004 - damien.carbery@sun.com
- Add SUNWgnome-media-devel as build requirement.
* Thu Jul 15 2004 - brian.cameron@sun.com
- Created.



