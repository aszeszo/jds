#
# spec file for packages SUNWgnome-media, SUNWgnome-sound-recorder
#
# includes module(s): gnome-media
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%use gmedia = gnome-media.spec

Name:                    SUNWgnome-media-apps
IPS_package_name:        gnome/media/gnome-media
Meta(info.classification): %{classification_prefix}:Applications/Sound and Video
Summary:                 GNOME media components
Version:                 %{gmedia.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gmedia.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWbison 
BuildRequires: runtime/python-26
BuildRequires: SUNWlibcanberra-devel
BuildRequires: SUNWgnome-audio-devel
BuildRequires: SUNWgnome-cd-burner-devel
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWgnome-media-devel
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWgnome-doc-utils
Requires: SUNWlibglade
Requires: SUNWlibcanberra
Requires: SUNWlibms
Requires: SUNWdesktop-cache
Requires: SUNWgnome-cd-burner
Requires: SUNWgnome-config
Requires: SUNWgnome-libs
Requires: SUNWgnome-media
Requires: SUNWgnome-media-apps-root
Requires: SUNWgnome-vfs
Requires: SUNWgnome-ui-designer

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

%package -n SUNWgnome-sound-recorder
IPS_package_name:        gnome/media/sound-recorder
Meta(info.classification): %{classification_prefix}:Applications/Sound and Video
Summary:                 GNOME sound recording utilities
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWgnome-sound-recorder-root
Requires: SUNWgtk2
Requires: SUNWgnome-libs
Requires: SUNWgnome-audio
Requires: SUNWgnome-config
Requires: SUNWgnome-media
Requires: SUNWgnome-media-apps
Requires: SUNWgnome-vfs
Requires: SUNWdesktop-cache

%package -n SUNWgnome-sound-recorder-root
Summary:                 GNOME sound recording utilities - / filesystem
IPS_package_name:        gnome/media/sound-recorder
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version
%gmedia.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
# Note that including  __STDC_VERSION n CFLAGS for gnome-media breaks the S9
# build for gstreamer,  gst-plugins, and gnome-media, so not including for them.
#
export CFLAGS="%optflags -I/usr/sfw/include -DANSICPP"
export RPM_OPT_FLAGS="$CFLAGS"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export LDFLAGS="%_ldflags"

%gmedia.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gmedia.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_mandir}/man1/*.1

# Remove .la and .a file as we don't ship them.
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec rm {} \;

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

# process doc files
cd %{_builddir}/%name-%version/gnome-media-%{gmedia.version}
# Use bzip2 -k option since the original files are needed when packaging
# the main SUNWgnome-media package.
bzip2 -k COPYING COPYING-DOCS COPYING.grecord ChangeLog.pre-2-26 grecord/ChangeLog.pre-2-26 grecord/doc/ChangeLog po/ChangeLog NEWS grecord/NEWS

mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/SUNWgnome-sound-recorder
tar cf - AUTHORS grecord/AUTHORS grecord/icons/AUTHORS README grecord/README COPYING.bz2 COPYING-DOCS.bz2 COPYING.grecord.bz2 ChangeLog-pre-2-26.bz2 po/ChangeLog.bz2 grecord/ChangeLog.bz2 grecord/doc/ChangeLog.bz2 NEWS.bz2 grecord/NEWS.bz2 | ( cd $RPM_BUILD_ROOT%{_datadir}/doc/SUNWgnome-sound-recorder; tar xf - )

%clean
rm -rf $RPM_BUILD_ROOT

%post -n SUNWgnome-sound-recorder
%restart_fmri desktop-mime-cache icon-cache gconf-cache

%postun -n SUNWgnome-sound-recorder
%restart_fmri desktop-mime-cache

%post
%restart_fmri desktop-mime-cache icon-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gnome-audio-profiles-properties
%{_bindir}/gnome-volume-control
%{_bindir}/gstreamer-properties
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libgnome-media*.so*
#%{_libdir}/libglade/2.0/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/gstreamer-properties.desktop
%{_datadir}/applications/gnome-volume-control.desktop
%doc gnome-media-%{gmedia.version}/AUTHORS
%doc gnome-media-%{gmedia.version}/README
%doc gnome-media-%{gmedia.version}/profiles/README
%doc(bzip2) gnome-media-%{gmedia.version}/COPYING
%doc(bzip2) gnome-media-%{gmedia.version}/COPYING-DOCS
%doc(bzip2) gnome-media-%{gmedia.version}/COPYING.gst-mixer
%doc(bzip2) gnome-media-%{gmedia.version}/COPYING.profiles
%doc(bzip2) gnome-media-%{gmedia.version}/NEWS
%doc(bzip2) gnome-media-%{gmedia.version}/ChangeLog.pre-2-26
%doc(bzip2) gnome-media-%{gmedia.version}/gst-mixer/doc/ChangeLog
%doc(bzip2) gnome-media-%{gmedia.version}/gstreamer-properties/help/ChangeLog
%doc(bzip2) gnome-media-%{gmedia.version}/profiles/help/ChangeLog
%doc(bzip2) gnome-media-%{gmedia.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/gnome-volume-control/C
%{_datadir}/gnome/help/gstreamer-properties/C
%{_datadir}/gnome-media
%{_datadir}/gstreamer-properties
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/devices
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/status
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/16x16/devices/gvc-3d-sound.png
%{_datadir}/icons/hicolor/16x16/devices/gvc-headphones.png
%{_datadir}/icons/hicolor/16x16/devices/gvc-line-in.png
%{_datadir}/icons/hicolor/16x16/devices/gvc-tone.png
%{_datadir}/icons/hicolor/16x16/status/audio-input-microphone-muted.png
%{_datadir}/icons/hicolor/48x48/apps/gstreamer-properties.png
%dir %attr (0755, root, bin) %{_datadir}/sounds
%{_datadir}/sounds/*
%{_datadir}/omf/gstreamer-properties/gstreamer-properties-C.omf
%{_datadir}/omf/gnome-volume-control/gnome-volume-control-C.omf
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/gnome-audio-profiles-properties.1
%{_mandir}/man1/gnome-volume-control.1
%{_mandir}/man1/gst*
%{_mandir}/man3/*
%{_datadir}/omf/gnome-audio-profiles/gnome-audio-profiles-C.omf
%{_datadir}/gnome/help/gnome-audio-profiles/C/legal.xml
%{_datadir}/gnome/help/gnome-audio-profiles/C/figures/gnome-audio-profiles-profiles-window.png
%{_datadir}/gnome/help/gnome-audio-profiles/C/figures/gnome-audio-profiles-profile-window.png
%{_datadir}/gnome/help/gnome-audio-profiles/C/gnome-audio-profiles.xml
%{_datadir}/glade3/catalogs/gnome-media-profiles.xml
%{_libdir}/glade3/modules/libgnome-media-profiles.so

%files -n SUNWgnome-sound-recorder
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gnome-sound-recorder
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/gnome-sound-recorder.desktop
%doc %{_datadir}/doc/SUNWgnome-sound-recorder
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/gnome-sound-recorder/C
%{_datadir}/gnome-sound-recorder
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
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/16x16/apps/gnome-sound-recorder.png
%{_datadir}/icons/hicolor/22x22/apps/gnome-sound-recorder.png
%{_datadir}/icons/hicolor/24x24/apps/gnome-sound-recorder.png
%{_datadir}/icons/hicolor/32x32/apps/gnome-sound-recorder.png
%{_datadir}/icons/hicolor/48x48/apps/gnome-sound-recorder.png
%{_datadir}/icons/hicolor/scalable/apps/gnome-sound-recorder.svg
%{_datadir}/omf/gnome-sound-recorder/gnome-sound-recorder-C.omf
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/gnome-sound-recorder.1

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z][a-z].omf
%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z][A-Z].omf

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/gnome-audio-profiles.schemas
%{_sysconfdir}/gconf/schemas/gnome-volume-control.schemas

%files -n SUNWgnome-sound-recorder-root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/gnome-sound-recorder.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/gnome-media/profiles
%dir %attr (0755, root, sys) %{_datadir}

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Sun Mar 21 2010 - christian.kelly@sun.com
- Add Requires SUNWgnome-ui-designer.
* Tue Jan 05 2010 - dave.lin@sun.com
- Changed the dependency from CBEbison to SUNWbison.
* Thu Jul 30 2009 - brian.cameron@sun.com
- Fix up packaging after bumping to 2.27.5.
* Fri Jul 24 2009 - christian.kelly@sun.com
- Fix up pkg'ing.
* Fri Apr 17 2009 - brian.cameron@sun.com
- Add SUNWlibcanberra as a dependency.  It is needed for the "Sound Theme" tab
  to be built into gnome-volume-control.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* ???
- Uncomment the line "%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z][A-Z].omf"
  in %file l10n as the file is available in 2.26.0.
* Fri Sep 26 2008 - brian.cameron@sun.com
- Now that the GPLv3 mixup is fixed, add new copyright files.
* Tue Jun 03 2008 - brian.cameron@sun.com
- Packaging changes related to bumping to 2.23.  No longer ship
  cddb code or vumeter since these are no longer supported upstream.
  Remove support for building with gnome-cd since this is also
  no longer supported upstream. Removes SUNWgnome-freedb-libs/-root.
* Wed May 07 2008 - damien.carbery@sun.com
- Remove PERL5LIB setting as it is not necessary.
* Wed Apr 02 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Wed Mar 12 2008 - damien.carbery@sun.com
- Update %files for new tarball.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Mon Oct  8 2007 - damien.carbery@sun.com
- Remove some icons from base package because they are already in
  SUNWgnome-sound-recorder. Fixes 6613798.
* Wed Sep 19 2007 - damien.carbery@sun.com
- Update %files for 2.20.0 tarball - remove omf files and move png files.
* Wed Sep 05 2007 - damien.carbery@sun.com
- Remove references to SUNWgnome-a11y-base-libs as its contents have been
  moved to SUNWgnome-base-libs.
* Wed Jan 24 2007 - brian.cameron@sun.com
- Change %with_cd to %build_with_gnome_cd with suggestions from Laca.
* Tue Jan 23 2007 - brian.cameron@sun.com
- Add %with_cd logic so it is easier to build with gnome-cd if desired.
* Mon Oct 16 2006 - damien.carbery@sun.com
- Remove the '-rf' from the 'rm *.la *.a' lines so that any changes to the
  module source will be seen as a build error and action can be taken.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Mon Aug 21 2006 - damien.carbery@sun.com
- Fix l10n package - C locale omf file was in base and l10n package.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri Jun  2 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Thu May 04 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue Mar 28 2006 - brian.cameron@sun.com
- Removed SUNWgnome-cd, since now using sound-juicer.
* Tue Feb 21 2006 - damien.carbery@sun.com
- Just a few more dependencies for SUNWgnome-cd.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Jan 20 2006 - brian.cameron@sun.com
- Do not package gstreamer gconf files since GStreamer already installs
  its own.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Fri Sep 30 2005 - brian.cameron@sun.com
- Fix l10n packaging.
* Thu Sep 22 2005 - brian.cameron@sun.com
- Build gnome-cd again since sound-juicer doesn't build on Solaris.
* Wed Sep 21 2005 - brian.cameron@sun.com
- Fix packaging.
* Tue Jul 12 2005 - balamurali.viswanathan@wipro.com
- Don't build gnome-cd and remove nautilus-cd-burner dependency
* Tue Jul 12 2005 - balamurali.viswanathan@wipro.com
- Add nautilus-cd-burner dependency
* Thu Jul 07 2005 - balamurali.viswanathan@wipro.com
- Initial spec-file created



