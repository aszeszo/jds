#
# spec file for package SUNWgnome-img-editor
#
# includes module(s): gimp
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner leon.sha
#
%include Solaris.inc
%define pythonver 2.6

%use gimp = gimp.spec
%use gimphdr = gimp-hdr.spec
Name:                    SUNWgnome-img-editor
License:                 GPL v3, LGPL v2.1
IPS_package_name:        image/editor/gimp
Meta(info.classification): %{classification_prefix}:Applications/Graphics and Imaging
Summary:                 The Gimp image editor
Version:                 %{gimp.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlibart
Requires: SUNWgtk2
Requires: SUNWgnome-libs
Requires: SUNWpygtk2-26
Requires: SUNWgnome-pdf-viewer
Requires: SUNWlibms
Requires: SUNWTiff
Requires: SUNWfontconfig
Requires: SUNWfreetype2
Requires: SUNWgnome-vfs
Requires: SUNWjpg
Requires: SUNWlibexif
Requires: SUNWlibrsvg
Requires: SUNWpng
Requires: SUNWzlib
Requires: SUNWdesktop-cache
Requires: SUNWlcms
Requires: SUNWPython26
Requires: SUNWgegl
Requires: SUNWbabl
Requires: SUNWaalib
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWTiff-devel
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWjpg-devel
BuildRequires: SUNWlibexif-devel
BuildRequires: SUNWlibrsvg-devel
BuildRequires: SUNWpng-devel
BuildRequires: SUNWpygtk2-26-devel
BuildRequires: SUNWpython26-setuptools
BuildRequires: SUNWgnome-pdf-viewer-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWlcms
BuildRequires: SUNWgegl-devel
BuildRequires: SUNWbabl-devel
BuildRequires: SUNWaalib

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

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

%prep
rm -rf %name-%version
mkdir %name-%version
%gimp.prep -d %name-%version
%gimphdr.prep -d %name-%version

%build
export CFLAGS="%optflags -I%{_includedir} -KPIC"
export RPM_OPT_FLAGS="$CFLAGS"
export CPPFLAGS="-I/usr/sfw/include"
export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib"
export PATH=$PATH:%{_builddir}/%name-%version/gimp-%{gimp.version}/tools
export PKG_CONFIG_PATH=%{_builddir}/%name-%version/gimp-%{gimp.version}:/usr/lib/python%{pythonver}/pkgconfig
export EXTRA_CFLAGS="-I%{_builddir}/%name-%version/gimp-%{gimp.version}/ -I%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpcolor -I%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpmath -I%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimp -I%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpconfig -I%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpwidgets"
export EXTRA_LDFLAGS="-L%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpbase/.libs -L%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpcolor/.libs -L%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpmath/.libs -L%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimp/.libs -L%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpconfig/.libs -L%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpwidgets/.libs -L%{_builddir}/%name-%version/gimp-%{gimp.version}/libgimpmodule/.libs"
export PYTHON=/usr/bin/python%{pythonver}

%gimp.build -d %name-%version
%gimphdr.build -d %name-%version

%install
export PATH=$PATH:%{_builddir}/%name-%version/gimp-%{gimp.version}/tools
export PKG_CONFIG_PATH=%{_builddir}/%name-%version/gimp-%{gimp.version}:/usr/lib/python%{pythonver}/pkgconfig
%gimp.install -d %name-%version
%gimphdr.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):unsupported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, bin) %{_libdir}/gimp
%dir %attr (0755, root, bin) %{_libdir}/gimp/%gimp.subver_install
%dir %attr (0755, root, bin) %{_libdir}/gimp/%gimp.subver_install/environ
%dir %attr (0755, root, bin) %{_libdir}/gimp/%gimp.subver_install/modules
%dir %attr (0755, root, bin) %{_libdir}/gimp/%gimp.subver_install/plug-ins
%{_libdir}/gimp/%gimp.subver_install/environ/*
%{_libdir}/gimp/%gimp.subver_install/modules/lib*.so*
%{_libdir}/gimp/%gimp.subver_install/plug-ins/*
%{_libdir}/gimp/%gimp.subver_install/interpreters
%{_libdir}/gimp/%gimp.subver_install/python
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/gimp
%attr (-, root, other) %{_datadir}/icons
%doc gimp-%{gimp.version}/plug-ins/script-fu/tinyscheme/COPYING
%doc gimp-%{gimp.version}/LICENSE
%doc gimp-%{gimp.version}/plug-ins/script-fu/ftx/LICENSE
%doc gimp-%{gimp.version}/devel-docs/README
%doc gimp-%{gimp.version}/devel-docs/tools/README.shooter
%doc gimp-%{gimp.version}/docs/Wilber.xcf.gz.README
%doc gimp-%{gimp.version}/app/pdb/README
%doc gimp-%{gimp.version}/plug-ins/script-fu/ftx/README
%doc gimp-%{gimp.version}/plug-ins/script-fu/tinyscheme/README
%doc gimp-%{gimp.version}/plug-ins/flame/README
%doc gimp-%{gimp.version}/plug-ins/gradient-flare/README
%doc gimp-%{gimp.version}/plug-ins/ifs-compose/README.ifscompose
%doc gimp-%{gimp.version}/plug-ins/lighting/README
%doc gimp-%{gimp.version}/plug-ins/map-object/README
%doc gimp-%{gimp.version}/plug-ins/metadata/README
%doc gimp-%{gimp.version}/plug-ins/selection-to-path/README
%doc gimp-%{gimp.version}/plug-ins/selection-to-path/README.limn
%doc gimp-%{gimp.version}/plug-ins/twain/README
%doc(bzip2) gimp-%{gimp.version}/AUTHORS
%doc(bzip2) gimp-%{gimp.version}/COPYING
%doc(bzip2) gimp-%{gimp.version}/libgimp/COPYING
%doc(bzip2) gimp-%{gimp.version}/plug-ins/pygimp/COPYING
%doc(bzip2) gimp-%{gimp.version}/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/ChangeLog.pre-1-0
%doc(bzip2) gimp-%{gimp.version}/ChangeLog.pre-1-2
%doc(bzip2) gimp-%{gimp.version}/ChangeLog.pre-2-0
%doc(bzip2) gimp-%{gimp.version}/ChangeLog.pre-2-2
%doc(bzip2) gimp-%{gimp.version}/ChangeLog.pre-2-4
%doc(bzip2) gimp-%{gimp.version}/devel-docs/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/po/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/po-libgimp/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/po-plug-ins/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/po-python/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/po-script-fu/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/po-tips/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/plug-ins/script-fu/tinyscheme/CHANGES
%doc(bzip2) gimp-%{gimp.version}/plug-ins/gimpressionist/ChangeLog
%doc(bzip2) gimp-%{gimp.version}/NEWS
%doc(bzip2) gimp-%{gimp.version}/NEWS.pre-2-0
%doc(bzip2) gimp-%{gimp.version}/NEWS.pre-2-2
%doc(bzip2) gimp-%{gimp.version}/NEWS.pre-2-4
%doc(bzip2) gimp-%{gimp.version}/README
%doc(bzip2) gimp-%{gimp.version}/devel-docs/README.gtkdoc
%doc(bzip2) gimp-%{gimp.version}/README.i18n
%doc(bzip2) gimp-%{gimp.version}/tools/pdbgen/README
%doc(bzip2) gimp-%{gimp.version}/plug-ins/gfig/README
%doc(bzip2) gimp-%{gimp.version}/plug-ins/gimpressionist/README
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%changelog
* Mon Dec 21 2009 - ghee.teo@sun.com
- Remove SUNWgnome-print dependency.
* Fri Oct 16 2009 - leon.sha@sun.com
- Bug 6890513 SUNWgnome-img-editor package dependency on dynamically
  linked libs not captured.
* Mon Sep 07 2009 - dave.lin@sun.com
- Change the dependency to python 2.6.
* Fri Jul 3  2009 - chris.wang@sun.com
- Change PATH to gimp2.66/tools as gimptool-2.0 is installed in
  this location since 2.6.6
* Fri Jun 26 2009 - chris.wang@sun.com
- Change owner to leon.sha
* Mon Jun  1 2009 - chris.wang@sun.com
- Change owner to bewitche
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 23 2009 - jeff.cai@sun.com
- Since /usr/lib/gimp/2.0/plug-ins/colorxhtml.py (SUNWgnome-img-editor)
  requires /usr/bin/i86/isapython2.4 which is found in SUNWPython, add
  the dependency.
* Tue Feb 24 2009 - laca@sun.com
- set PYTHON and PKG_CONFIG_PATH so the correct python version and
  dependencies are picked up
* Tue Sep 16 2008 - matt.keenan@sun.com
- Update copyright
* Wed May 21 2008 - damien.carbery@sun.com
- Add Build/Requires: SUNWlcms after check-deps.pl run.
* Fri Jan 11 2008 - laca@sun.com
- delete PKG_CONFIG_PATH setting since help was removed
* Fri Sep 28 2007 - laca@sun.com
- delete Nevada X dep
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
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
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Fri Apr 28 2006 - damien.carbery@sun.com
- Fix %files after move to /usr/bin.
* Fri Apr 28 2006 - glynn.foster@sun.com
- Move into /usr/bin as standard
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Fri Dec 02 2005 - damien.carbery@sun.com
- Change SUNWpoppler dependency to SUNWgnome-pdf-viewer as poppler has moved.
* Fri Sep 30 2005 - brian.cameron@sun.com
- add SUNWpoppler as build requirement.
* Tue Sep 20 2005 - laca@sun.com
- add unpackaged files to %files
* Tue Aug 30 2005 - damien.carbery@sun.com
- Add Build/Requires for SUNWgnome-pygtk2.
* Fri Jan 21 2005 - damien.carbery@sun.com
- Change PKG_CONFIG_PATH to build gimp-help module.
* Mon Dec 13 2004 - damien.carbery@sun.com
- Move to /usr/sfw to implement ARC decision.
* Sun Nov 14 2004 - laca@sun.com
- add -KPIC to CFLAGS, because the Makefiles hardcode -fPIC :/
* Fri Nov 12 2004 - laca@sun.com
- move to /usr/demo/jds
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Wed Sep 01 2004 - shirley.woo@sun.com
- Bug 5091588 : man5 files should be in devel-share package
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Fri Aug 20 2004 - damien.carbery@sun.com
- Change file paths for new version of Gimp. Use variable from gimp.spec so
  future version updates will not need a change here.
* Tue Jun 22 2004 - shirley.woo@sun.com
- changed install location to /usr/lib and /usr/bin
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Tue May 18 2004 - laca@sun.com
- add sfw to LDFLAGS/CPPFLAGS (patch from Shirley)
* Fri Mar 26 2004 - brian.cameron@sun.com
- Created,



