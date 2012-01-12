#
# spec file for packages SUNWgnome-media
#
# includes module(s): libgnome-media-profiles
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%use gmedia = libgnome-media-profiles.spec

Name:                    SUNWlibgnome-media
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
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWgtk3-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-media-devel
BuildRequires: SUNWgnome-doc-utils
Requires: SUNWglib2
Requires: SUNWgtk3
Requires: SUNWlibglade
Requires: SUNWlibms
Requires: SUNWdesktop-cache
Requires: SUNWgnome-config
Requires: SUNWgnome-media
Requires: SUNWlibgnome-media-root
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

# Remove .la and .a file as we do not ship them.
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec rm {} \;

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache icon-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gnome-audio-profiles-properties
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libgnome-media*.so*
#%{_libdir}/libglade/2.0/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%doc libgnome-media-profiles-%{gmedia.version}/README
%doc(bzip2) libgnome-media-profiles-%{gmedia.version}/COPYING
%doc(bzip2) libgnome-media-profiles-%{gmedia.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/libgnome-media-profiles
%{_datadir}/omf/gnome-audio-profiles/gnome-audio-profiles-C.omf
%{_datadir}/gnome/help/gnome-audio-profiles/C/legal.xml
%{_datadir}/gnome/help/gnome-audio-profiles/C/figures/gnome-audio-profiles-profiles-window.png
%{_datadir}/gnome/help/gnome-audio-profiles/C/figures/gnome-audio-profiles-profile-window.png
%{_datadir}/gnome/help/gnome-audio-profiles/C/gnome-audio-profiles.xml
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/gnome-audio-profiles-properties.1
%{_mandir}/man3/*

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
%{_sysconfdir}/gconf/schemas/gnome-media-profiles.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/libgnome-media-profiles-3.0
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



