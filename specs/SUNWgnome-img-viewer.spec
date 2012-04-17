#
# spec file for package SUNWgnome-img-viewer
#
# includes module(s): eog
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%define eog_bindir /usr/bin
%define eog_libdir /usr/lib
%define eog_libexecdir /usr/lib

%use eog = eog.spec

%define _bindir %{eog_bindir}
%define _libexecdir %{eog_libexecdir}
%define _libdir %{eog_libdir}

Name:                    SUNWgnome-img-viewer
IPS_package_name:        image/viewer/eog
Meta(info.classification): %{classification_prefix}:Applications/Graphics and Imaging
Summary:                 GNOME image viewer
Version:                 %{eog.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GPLv2

BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: image/library/libart
Requires: library/desktop/gtk2
Requires: library/gnome/gnome-libs
Requires: gnome/file-manager/nautilus
Requires: gnome/gnome-camera
Requires: library/gnome/gnome-component
Requires: gnome/config/gconf
Requires: gnome/gnome-panel
Requires: library/gnome/gnome-vfs
Requires: image/library/libjpeg
Requires: image/library/libexif
Requires: system/library/math
Requires: library/popt
Requires: service/gnome/desktop-cache
Requires: library/lcms
BuildRequires: library/desktop/gtk2
BuildRequires: library/gnome/gnome-component
BuildRequires: gnome/config/gconf
BuildRequires: gnome/gnome-panel
BuildRequires: library/gnome/gnome-vfs
BuildRequires: image/library/libjpeg
BuildRequires: image/library/libexif
BuildRequires: library/popt
BuildRequires: gnome/file-manager/nautilus
BuildRequires: gnome/gnome-camera
BuildRequires: library/gnome/gnome-libs
BuildRequires: gnome/theme/gnome-icon-theme
BuildRequires: developer/documentation-tool/gtk-doc
BuildRequires: library/lcms
BuildRequires: developer/gnome/gnome-doc-utils

%package l10n
Summary:                 %{summary} - l10n files

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: library/gnome/gnome-libs
Requires: gnome/file-manager/nautilus
Requires: gnome/gnome-camera
Requires: library/desktop/gtk2
Requires: library/gnome/gnome-component
Requires: gnome/config/gconf
Requires: gnome/gnome-panel
Requires: library/gnome/gnome-vfs
Requires: image/library/libjpeg
Requires: image/library/libexif
Requires: system/library/math
Requires: library/popt

%prep
rm -rf %name-%version
mkdir %name-%version
%eog.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export PKG_CONFIG_PATH="%{_pkg_config_path}:/usr/sfw/lib/pkgconfig"
export CFLAGS="%optflags -I%{_includedir}"
export RPM_OPT_FLAGS="$CFLAGS"
export CPPFLAGS="-I/usr/sfw/include"
export LDFLAGS="%_ldflags -lm -L/usr/sfw/lib -R/usr/sfw/lib"

%eog.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%eog.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man1/eog.1

install -d $RPM_BUILD_ROOT%{eog_libdir}/bonobo/servers

# Remove *.a and *.la
# .a files are no longer installed (2.23.4.1 tarball)
#rm $RPM_BUILD_ROOT%{eog_libdir}/eog/plugins/*.a
rm $RPM_BUILD_ROOT%{eog_libdir}/eog/plugins/*.la

# Never install English locales because should support full functions
# on English locales as same as Solaris.
rm -r $RPM_BUILD_ROOT%{_datadir}/gnome/help/eog/en_GB
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/en_GB
rm $RPM_BUILD_ROOT%{_datadir}/omf/eog/eog-en_GB.omf

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}(eog):$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{eog_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{eog_libdir}/bonobo/servers
%{eog_libdir}/eog
# %{eog_libdir}/eog-collection-view
# %{eog_libdir}/eog-image-viewer
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/eog
%{_datadir}/gtk-doc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/C
# %{_datadir}/idl
%{_datadir}/omf/*/*-C.omf
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/eog.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/eog.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/eog.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/eog.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/eog.svg
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc -d eog-%{eog.version} AUTHORS ChangeLog MAINTAINERS NEWS README THANKS
%doc(bzip2) -d eog-%{eog.version} COPYING
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/eog/[a-z]*
%{_datadir}/omf/eog/eog-[a-z][a-z].omf
%{_datadir}/omf/eog/eog-[a-z][a-z]_[A-Z][A-Z].omf

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/eog.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Mon Jan 18 2009 - yuntong.jin@sun.com
- Bump to 2.29.5
* Mon Dec 21 2009 - ghee.teo@sun.com
- Remove SUNWgnome-print dependency.
* Tue Aug 27 2009 - yuntong.jin@sun.com
- Bump to 2.27.91 
* Mon Aug 03 2009 - yuntong.jin@sun.com
- Bump to 2.27.5
* Mon Jun 29 2009 - yuntong.jin@sun.com
- change the owner to jouby 
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Web Mar 04 2009 - chris.wang@sun.com
- Transfer the ownership to bewitche
* Tue Feb 17 2009 - dave.lin@sun.com
- Add BuildRequires: SUNWgnome-themes-devel because it requires gnome-icon-theme.
* Wed Jun 18 2008 - damien.carbery@sun.com
- *.a are no longer installed so comment out their deletion.
* Wed Jun 11 2008 - damien.carbery@sun.com
- Delete *.a/*.la during %install; add %{_datadir}/gtk-doc and
  %{eog_libdir}/eog to %files.
* Wed May 21 2008 - damien.carbery@sun.com
- Add Build/Requires: SUNWlcms after check-deps.pl run.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Fri Sep 28 2007 - laca@sun.com
- delete Nevada X dep
* Tue Aug 28 2007 - damien.carbery@sun.com
- Remove pixmaps from %files because they are not installed by new tarball.
* Sat Aug 18 2007 - damien.carbery@sun.com
- Comment out removal of /var and /usr/var dirs as they are no longer installed.
* Thu Aug 16 2007 - damien.carbery@sun.com
- Remove actions icons from %files after tarball bump.
* Wed Jul 11 2007 - damien.carbery@sun.com
- Add eog-image-collection.png and thumbnail-frame.png to %files.
* Wed May 16 2007 - damien.carbery@sun.com
- Add devel package; add icons to base package.
* Thu May 10 2007 - damien.carbery@sun.com
- Remove pixmaps dir from %files as it is no longer populated.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Wed Feb 14 2006 - damien.carbery@sun.com
- Delete en_GB files in %install.
* Thu Jan 11 2006 - damien.carbery@sun.com
- Add new icons to %files.
* Wed Dec 13 2006 - damien.carbery@sun.com
- Delete some l10n omf files in %install when not building l10n packages.
* Wed Dec 06 2006 - damien.carbery@sun.com
- Update packaging for new tarball - remove scrollkeeper files, add omf files
  to the l10n package.
* Wed Nov 29 2006 - damien.carbery@sun.com
- Fix packaging as some locales have been removed.
* Fri Oct 20 2006 - damien.carbery@sun.com
- Fix packaging for new locales.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Fri Jul 28 2006 - damien.carbery@sun.com
- Remove scrollkeeper files before packaging. Update l10n package as some 
  files are no longer installed.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri Jun  2 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue May 09 2006 - damien.carbery@sun.com
- Move gthumb to spec-files-extra/SUNWgnome-img-organizer as it has been EOL'd.
* Mon May 01 2006 - damien.carbery@sun.com
- Add %{_datadir}/icons to share package.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Wed Feb 15 2006 - damien.carbery@sun.com
- Set PKG_CONFIG_PATH to find libgphoto; Set LDFLAGS to link with libpng.
* Sat Jan 28 2006 - damien.carbery@sun.com
- Add BuildRequires for '-devel' equivalents of the Requires packages.
- Added BuildRequires SUNWgnome-camera-devel for gthumb.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Mon Oct 03 2005 - damien.carbery@sun.com
- Remove unpackaged files.
* Sat Dec 18 2004 - damien.carbery@sun.com
- Move gthumb to /usr/sfw per ARC decision.
* Sun Nov 14 2004 - laca@sun.com
- move gthumb to /usr/demo/jds
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Mon Jun 26 2004  shirley.woo@sun.com
- change eog.1 permissions to 0755 for Solaris integration error
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Tue May 18 2004 - laca@sun.com
- add sfw to LDFLAGS/CPPFLAGS (patch from Shirley)
* Tue May 11 2004 - brian.cameron@sun.com
- add %{_datadir}/eog to files share so glade files
  get installed.  This corrects core dumping problem
  when bringing up preferences dialog.
* Tue May 04 2004 - laca@sun.com
- add SUNWgnome-camera dependency
* Fri Mar 26 2004 - laca@sun.com
- add SUNWgnome-file-mgr dependency (for eel)
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Mon Mar 01 2004 - <laca@sun.com>
- fix dependencies
- define PERL5LIB
- file %files share
* Mon Feb 23 2004 - <niall.power@sun.com>
- install gconf schemas at the end of the install stage



