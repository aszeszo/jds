# spec file for package SUNWgnome-pdf-viewer
#
# includes module(s): poppler, poppler-data, evince
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#
%include Solaris.inc

%use popplerdata = poppler-data.spec
%use poppler = poppler.spec
%use libspectre = libspectre.spec
%use evince = evince.spec

Name:                    SUNWgnome-pdf-viewer
IPS_package_name:        desktop/pdf-viewer/evince
License:                 Adobe, GPLv2, LGPLv2.1, MIT, X/MIT
Meta(info.classification): %{classification_prefix}:Applications/Office
Summary:                 GNOME PDF document viewer
Version:                 %{evince.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: library/desktop/libglade
BuildRequires: library/popt
BuildRequires: library/gnome/gnome-libs
BuildRequires: gnome/file-manager/nautilus
BuildRequires: library/gnome/gnome-component
BuildRequires: runtime/python-26
BuildRequires: system/library/fontconfig
BuildRequires: image/library/libtiff
BuildRequires: system/library/dbus
BuildRequires: gnome/config/gconf
BuildRequires: library/gnome/gnome-vfs
BuildRequires: image/library/libjpeg
BuildRequires: print/filter/ghostscript
BuildRequires: developer/gnome/gnome-doc-utils
BuildRequires: gnome/theme/gnome-icon-theme
BuildRequires: library/gnome/gnome-keyring
Requires: library/desktop/libglade
Requires: library/popt
Requires: library/gnome/gnome-libs
Requires: gnome/file-manager/nautilus
Requires: library/gnome/gnome-component
Requires: system/library/fontconfig
Requires: image/library/libtiff
Requires: system/library/dbus
Requires: system/library/freetype-2
Requires: gnome/config/gconf
Requires: library/gnome/gnome-vfs
Requires: image/library/libjpeg
Requires: system/library/c++-runtime
Requires: system/library/math
Requires: library/libxml2
Requires: library/zlib
Requires: service/gnome/desktop-cache

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
BuildRequires: runtime/perl-512

%package l10n
Summary:                 %{summary} - l10n files

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%prep
rm -rf %name-%version
mkdir %name-%version
%libspectre.prep -d %name-%version
%popplerdata.prep -d %name-%version
%poppler.prep -d %name-%version
%evince.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
# There seems to be an issue with the version of libtool that GStreamer is
# now using.  The libtool script uses the echo and RM variables but does not
# define them, so setting them here addresses this.
export echo="/usr/bin/echo"
export RM="/usr/bin/rm"

export PKG_CONFIG_PATH=%{_pkg_config_path}
export LDFLAGS="%_ldflags -L/usr/X11/lib -R /usr/X11/lib -L/usr/sfw/lib -R/usr/sfw/lib -lX11 -lm"
export CFLAGS="%optflags -I/usr/sfw/include"
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"
export RPM_OPT_FLAGS="$CFLAGS"

%libspectre.build -d %name-%version
%popplerdata.build -d %name-%version
%poppler.build -d %name-%version

export PKG_CONFIG_PATH=../poppler-%{poppler.version}:../libspectre-%{libspectre.version}:%{_pkg_config_path}
%evince.build -d %name-%version

%install
# There seems to be an issue with the version of libtool that GStreamer is
# now using.  The libtool script uses the echo and RM variables but does not
# define them, so setting them here addresses this.
export echo="/usr/bin/echo"
export RM="/usr/bin/rm"

rm -rf $RPM_BUILD_ROOT
%libspectre.install -d %name-%version
%popplerdata.install -d %name-%version
%poppler.install -d %name-%version
%evince.install -d %name-%version
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

# Remove *.a and *.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/evince/*/backends/*.a || true
rm $RPM_BUILD_ROOT%{_libdir}/evince/*/backends/*.la || true

# Remove unneeded scrollkeeper dirs
rm -rf $RPM_BUILD_ROOT%{_localstatedir}

cd $RPM_BUILD_ROOT%{_bindir}
ln -s evince gpdf

# Never install English locales because should support full functions
# on English locales as same as Solaris.
rm -r $RPM_BUILD_ROOT%{_datadir}/gnome/help/evince/en_GB
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/en_GB
rm $RPM_BUILD_ROOT%{_datadir}/omf/evince/evince-en_GB.omf

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/evince
%{_libdir}/nautilus
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/evince
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/evince/C
%{_datadir}/omf/evince/*-C.omf
%attr (-, root, other) %{_datadir}/icons
%dir %attr (0755, root, bin) %{_datadir}/poppler
%{_datadir}/poppler/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc libspectre-%{libspectre.version}/AUTHORS
%doc libspectre-%{libspectre.version}/README
%doc libspectre-%{libspectre.version}/NEWS
%doc libspectre-%{libspectre.version}/COPYING
%doc libspectre-%{libspectre.version}/ChangeLog
%doc poppler-data-%{popplerdata.version}/README
%doc poppler-data-%{popplerdata.version}/COPYING
%doc poppler-data-%{popplerdata.version}/COPYING.adobe
%doc poppler-data-%{popplerdata.version}/COPYING.gpl2
%doc poppler-%{poppler.version}/AUTHORS
%doc poppler-%{poppler.version}/README
%doc poppler-%{poppler.version}/README-XPDF
%doc(bzip2) poppler-%{poppler.version}/COPYING
%doc(bzip2) poppler-%{poppler.version}/cmake/modules/COPYING-CMAKE-SCRIPTS
%doc(bzip2) poppler-%{poppler.version}/ChangeLog
%doc(bzip2) poppler-%{poppler.version}/NEWS
%doc evince-%{evince.version}/AUTHORS
%doc evince-%{evince.version}/README
%doc(bzip2) evince-%{evince.version}/COPYING
%doc(bzip2) evince-%{evince.version}/ChangeLog
%doc(bzip2) evince-%{evince.version}/po/ChangeLog
%doc(bzip2) evince-%{evince.version}/help/ChangeLog
%doc(bzip2) evince-%{evince.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/dbus-1/services/org.gnome.evince.Daemon.service
%{_libdir}/evinced
%{_libdir}/evince-convert-metadata

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z]*.omf

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc/html

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/evince.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer.schemas
%{_sysconfdir}/gconf/schemas/evince-thumbnailer-ps.schemas

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Mon Dec 21 2009 - ghee.teo@sun.com
- Remove SUNWgnome-print dependency.
* Fri Oct 02 2009 - darren.kenny@sun.com
- Update to include new licence files in poppler-data 0.3.0
* Mon Aug 31 2009 - dave.lin@sun.com
- Redirect echo/rm to /usr/bin/* to fix improper libtool version issue.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Sep 15 2008 - matt.keenan@sun.com
- Update copyright
* Fri Aug 15 2008 - darren.kenny@sun.com
- Reverting back to evince 2.22 due to no libspectre or libgs.so on Solaris
  yet. When these appear I will bump evince again, so adding back in the PS
  backend file references.
* Fri Jun 20 2008 - darren.kenny@sun.com
- PS backend is disabled until libspectre is delivered - see defect 2288 for
  more information.
* Wed Jan 30 2008 - damien.carbery@sun.com
- Delete *.a and *.la. Add %{_libdir}/evince to %files.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Tue Nov 13 2007 - brian.cameron@sun.com
- Add evince manpage.
* Fri Sep 28 2007 - laca@sun.com
- delete SUNWxwrtl dep, not needed since this pkg depends on SUNWgnome-base-libs
* Thu Sep 27 2007 - laca@sun.com
- delete some unnecessary env variables
* Mon Sep 17 2007 - darren.kenny@sun.com
- Remove the now obsolete xpdf fonts since this is not supported in poppler
  any more since 0.6. Add the poppler-data datafiles which are replacing the
  xpdf fonts.
* Wed Jul 04 2007 - darren.kenny@sun.com
- Add evince-thumbnailer.schemas from %files and %preun root back, they were
  net being generated because evince was building without PDF support.
* Fri Jun 22 2007 - damien.carbery@sun.com
- Remove evince-thumbnailer.schemas from %files and %preun root as it is no
  longer in the module.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Thu Apr 12 2007 - damien.carbery@sun.com
- Add evince-thumbnailer-ps.schemas to %files and %preun root.
* Wed Feb 14 2007 - damien.carbery@sun.com
- Delete en_GB files in %install.
* Tue Nov 28 2006 - damien.carbery@sun.com
- Change attr of xpdfrc file in root package to fix 6497737.
* Mon Nov 06 2006 - darren.kenny@sun.com
- Add XPDF Language Support Packages that are used by poppler to correctly
  view localised PDF files. Fixes Bug#2143558. (forward port from Stable)
- Also fix FIXME comments (same as stable)
* Fri Nov  3 2006 - laca@sun.com
- add -lm to LDFLAGS so that libpoppler links against it, fixes 6470804
* Fri Sep 08 2006 - Matt.Keenan@sun.com
- Remove "rm" of _mandir during %install, Deliver community pages, pdf*.1
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
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
* Wed Mar 15 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-component/-devel for ORBit2.
* Tue Mar 14 2006 - damien.carbery@sun.com
- Remove unneeded scrollkeeper files before packaging.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Jan 24 2006 - damien.carbery@sun.com
- Set perms for %{_datadir} in devel package.
* Sun Jan 22 2006 - damien.carbery@sun.com
- Add gtk-doc dir to devel package.
* Wed Dec  7 2005 - brian.cameron@sun.com
- add /usr/sfw/lib to LDFLAGS because without this running evince complains
  it cannot find libfreetype.so.6
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Thu Dec 01 2005 - damien.carbery@sun.com
- Add include dir to CFLAGS to find ft2build.h, a dir missing from freetype2.pc
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Fri Oct 01 2004 - takao.fujiwara@sun.com
- Added xpdfrc
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Fri Aug 20 2004 - damien.carbery@sun.com
- Fix 5089628: mark two %gconf.xml files as volatile in root package.
* Mon Jul 26 2004 - damien.carbery@sun.com
- Return mime-info %files line to match Glynn's change to gpdf.spec.
* Fri Jul 23 2004 - damien.carbery@sun.com
- Remove mime-info %files line to match Glynn's change to gpdf.spec.
* Wed Jul 14 2004 - takao.fujiwara@sun.com
- add xpdf language support packs. #4921809
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Tue Jun 22 2004 - niall.power@sun.com
- add xpdf language support packs. #4921809
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Mon Apr 05 2004 - laca@sun.com
- Added %_libdir to %files
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Wed Mar 03 2004 - <laca@sun.com>
- fix %files share
- fix gconf files in root subpkg
* Mon Mar 01 2004 - <laca@sun.com>
- fix dependencies
* Mon Feb 23 2004 - <niall.power@sun.com>
- install gconf schemas at end of install stage.



