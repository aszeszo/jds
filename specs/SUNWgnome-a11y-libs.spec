#
# spec file for package SUNWgnome-a11y-libs
#
# includes module(s): at-spi java-atk-wrapper libgail-gnome freetts gnome-mag
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan 
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use at_spi_64 = at-spi.spec
%if %option_with_java
%define build_java 0
%use java_atk_wrapper_64 = java-atk-wrapper.spec
%endif
%endif

%include base.inc
%use at_spi = at-spi.spec
%use libgail_gnome = libgail-gnome.spec
%if %option_with_java
%define build_java 1
%use java_atk_wrapper = java-atk-wrapper.spec
%endif
%use freetts = freetts.spec
%use gnome_mag = gnome-mag.spec

Name:                    SUNWgnome-a11y-libs
License:		 LGPL v2 MIT
IPS_package_name:        gnome/accessibility/gnome-a11y-libs
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
Summary:                 Accessibility implementation for GNOME
Version:                 %{default_pkg_version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: library/desktop/gtk2
Requires: library/gnome/gnome-libs
Requires: gnome/gnome-panel
Requires: library/gnome/gnome-component
Requires: gnome/config/gconf
Requires: system/library/math
Requires: library/popt
Requires: runtime/java/jre-6
Requires: system/zones
Requires: package/svr4
Requires: service/gnome/desktop-cache
Requires: library/python-2/pygtk2-26
Requires: library/python-2/pygobject-26
Requires: library/python-2/python-gnome-26
# xprop
Requires: x11/x11-server-utilities
BuildRequires: library/python-2/pygtk2-26
BuildRequires: library/python-2/pygobject-26
BuildRequires: library/python-2/python-gnome-26
BuildRequires: library/desktop/gtk2
BuildRequires: gnome/config/gconf
BuildRequires: gnome/gnome-panel
BuildRequires: library/gnome/gnome-libs
BuildRequires: library/gnome/gnome-component
BuildRequires: compress/unzip
BuildRequires: library/gnome/gnome-keyring
BuildRequires: developer/java/jdk-6
BuildRequires: runtime/perl-512
Requires:      runtime/python-26
BuildRequires: runtime/python-26
BuildRequires: library/python-2/setuptools-26

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}

%package python26
IPS_package_name: library/python-2/pyatspi-26
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
Summary:       %{summary} - Python 2.6 binding files
SUNW_BaseDir:  %{_basedir}

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%at_spi_64.prep -d %name-%version/%_arch64
%if %option_with_java
%java_atk_wrapper_64.prep -d %name-%version/%_arch64
%endif
%endif

mkdir %name-%version/%base_arch
%at_spi.prep -d %name-%version/%base_arch
%libgail_gnome.prep -d %name-%version/%base_arch
%if %option_with_java
%java_atk_wrapper.prep -d %name-%version/%base_arch
%endif
%freetts.prep -d %name-%version/%base_arch
%gnome_mag.prep -d %name-%version/%base_arch
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED
export PKG_CONFIG_PATH="%{_pkg_config_path}:../at-spi-%{at_spi.version}"
export CFLAGS="%optflags -I/usr/X11/include"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

%ifarch amd64 sparcv9
%at_spi_64.build -d %name-%version/%_arch64
%if %option_with_java
%java_atk_wrapper_64.build -d %name-%version/%_arch64
%endif
%endif

%at_spi.build -d %name-%version/%base_arch
%libgail_gnome.build -d %name-%version/%base_arch
%if %option_with_java
%java_atk_wrapper.build -d %name-%version/%base_arch
%endif
%freetts.build -d %name-%version/%base_arch
%gnome_mag.build -d %name-%version/%base_arch

%install

%ifarch amd64 sparcv9
%at_spi_64.install -d %name-%version/%_arch64
%endif

%at_spi.install -d %name-%version/%base_arch
%libgail_gnome.install -d %name-%version/%base_arch

%if %option_with_java
%java_atk_wrapper.install -d %name-%version/%base_arch

%ifarch amd64 sparcv9
%java_atk_wrapper_64.install -d %name-%version/%_arch64
%endif
%endif

%freetts.install -d %name-%version/%base_arch
%gnome_mag.install -d %name-%version/%base_arch

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files.
rm -f $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/GNOME_Magnifier_module.la
# Remove .pyo files
find $RPM_BUILD_ROOT -name '*.pyo' -exec rm {} \;

# Remove empty dir
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnome-mag-*/reference/html
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnome-mag-*/reference
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnome-mag-*

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%files
%defattr (-, root, bin)
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%{_libdir}/%{_arch64}/bonobo
%{_libdir}/%{_arch64}/gtk-2.0/modules/*.so
%{_libexecdir}/%{_arch64}/at-spi-registryd
%{_libdir}/%{_arch64}/orbit-2.0/*.so
%endif

%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/bonobo
%{_libdir}/gtk-2.0/modules/*.so
%{_libdir}/orbit-2.0/*.so
%{_libexecdir}/at-spi-registryd
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, sys) %{_datadir}/lib
%doc -d %{base_arch} at-spi-%{at_spi.version}/README 
%doc -d %{base_arch} at-spi-%{at_spi.version}/AUTHORS
%doc(bzip2) -d %{base_arch} at-spi-%{at_spi.version}/COPYING 
%doc(bzip2) -d %{base_arch} at-spi-%{at_spi.version}/NEWS 
%doc(bzip2) -d %{base_arch} at-spi-%{at_spi.version}/ChangeLog
%doc -d %{base_arch} freetts/freetts-%{freetts.version}/license.terms 
%doc -d %{base_arch} freetts/freetts-%{freetts.version}/acknowledgments.txt 
%doc -d %{base_arch} freetts/freetts-%{freetts.version}/ANNOUNCE.txt 
%doc -d %{base_arch} freetts/freetts-%{freetts.version}/RELEASE_NOTES 
%doc -d %{base_arch} freetts/freetts-%{freetts.version}/README.txt
%doc -d %{base_arch} gnome-mag-%{gnome_mag.version}/README 
%doc -d %{base_arch} gnome-mag-%{gnome_mag.version}/AUTHORS 
%doc(bzip2) -d %{base_arch} gnome-mag-%{gnome_mag.version}/COPYING 
%doc(bzip2) -d %{base_arch} gnome-mag-%{gnome_mag.version}/NEWS 
%doc(bzip2) -d %{base_arch} gnome-mag-%{gnome_mag.version}/ChangeLog
%if %option_with_java
%doc -d %{base_arch} java-atk-wrapper-%{java_atk_wrapper.version}/README 
%doc -d %{base_arch} java-atk-wrapper-%{java_atk_wrapper.version}/AUTHORS
%doc(bzip2) -d %{base_arch} java-atk-wrapper-%{java_atk_wrapper.version}/COPYING.LESSER 
%doc(bzip2) -d %{base_arch} java-atk-wrapper-%{java_atk_wrapper.version}/NEWS
%endif
%doc -d %{base_arch} libgail-gnome-%{libgail_gnome.version}/README 
%doc -d %{base_arch} libgail-gnome-%{libgail_gnome.version}/AUTHORS
%doc(bzip2) -d %{base_arch} libgail-gnome-%{libgail_gnome.version}/COPYING 
%doc(bzip2) -d %{base_arch} libgail-gnome-%{libgail_gnome.version}/NEWS 
%doc(bzip2) -d %{base_arch} libgail-gnome-%{libgail_gnome.version}/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/at-spi-%{at_spi.version}/*
%{_datadir}/gnome-mag
%{_datadir}/dbus-1/services/org.freedesktop.gnome.Magnifier.service

%if %option_with_java
%{_basedir}/jdk/instances/*/jre/lib/accessibility.properties
%{_basedir}/jdk/instances/*/jre/lib/ext/java-atk-wrapper.jar
%endif
%{_datadir}/lib/freetts

%files devel
%ifarch amd64 sparcv9
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/idl
%{_datadir}/gtk-doc
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/at-spi.schemas
%{_sysconfdir}/gconf/schemas/libgail-gnome.schemas
%{_sysconfdir}/xdg/autostart/at-spi-registryd.desktop

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files python26
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.6
%dir %attr (0755, root, bin) %{_libdir}/python2.6/vendor-packages
%{_libdir}/python2.6/vendor-packages/*

%changelog
* Mon Feb 13 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Mon Feb 08 2009 - li.yuan@sun.com
- Remove colorblind-applet.py from copyright files.
* Sat Dec 19 2009 - dave.lin@sun.com
- Change dependency SUNWj5rt to SUNWj6rt as no SUNWj5rt any more on OpenSolaris.
* Tue Nov 17 2009 - li.yuan@sun.com
- Bump at-spi to 1.29.2.
* Thu Nov 05 2009 - li.yuan@sun.com
- Remove pyatspi for python 2.4. Remove pyspi.
* Wed Aug 26 2009 - li.yuan@sun.com
- Add .desktop file.
* Thu Jul 23 2009 - christian.kelly@sun.com
- Comment out --with-java blocks temporarily. 
* Sun Jul 19 2009 - christian.kelly@sun.com
- Started overwriting /usr/java, rm this for now.
* Thu Jul 16 2009 - ke.wang@sun.com
- Bump java-atk-wrapper to 0.27.4
* Mon Jul 06 2009 - ke.wang@sun.com
- Use java-atk-wrapper to take the place of java-access-bridge
* Tue Jun 09 2009 - ke.wang@sun.com
- Add 64-bit support for java-access-bridge
* Tue Jun 02 2009 - dave.lin@sun.com
- fixed dependency issue(CR6845023).
* Tue Apr 14 2009 - dave.lin@sun.com
- set PKG_CONFIG_TOP_BUILD_DIR to fix top_builddir issue when using at-spi uninstalled pc file
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Wed Mar 25 2009 - li.yuan@sun.com
- Move pyspi from SUNWgnome-python-libs to SUNWgnome-a11y-libs.
* Tue Mar 24 2009 - jeff.cai@sun.com
- Since /usr/lib/amd64/pkgconfig/libloginhelper-1.0.pc
  (SUNWgnome-a11y-libs-devel) requires
  /usr/lib/amd64/pkgconfig/libbonobo-2.0.pc which is found in
  SUNWgnome-component-devel, add the dependency.
* Fri Feb 27 2009 - li.yuan@sun.com
- Add support to multi versions of python.
* Fri Jan 09 2009 - jeff.cai@sun.com
- Ship a JNI library for java-access-bridge
* Fri Oct 12 2008 - jeff.cai@sun.com
- Create symbol links for accessibility.properties and gnome-java-bridge.jar
  as parts of the package.
  In the previous versions,  the symbol links are created in post scripts which
  will not be executed in OpenSolaris.
  Fix d.o.o bug #5253
* Fri Oct 12 2008 - jeff.cai@sun.com
- Change rmdir to rm -rf since the doc pathes of gnome-mag are not
  empty after the integration of SUNWdoxygen.
  We still don't ship references of gnome-mag for now.
* Wed Oct 08 2008 - li.yuan@sun.com
- Do postrun for root package.
* Mon Sep 29 2008 - christian.kelly@sun.com
- Added -root pkg for /etc/gconf/schemas/at-spi-schmeas.
* Mon Sep 22 2008 - dave.lin@sun.com
- Removed the empty dir /usr/share/doc/gnome-mag*
* Thu Sep 18 2008 - li.yuan@sun.com
- Added %doc to %files for copyright.
* Wed Sep 03 2008 - dave.lin@sun.com
- Add %defattr (-, root, bin) for "/usr/lib/amd/pkgconfig" dir, otherwise
  the pc files have "gbuild" ownership
* Tue Aug 05 2008 - li-yan.zhang@sun.com
- Add manpages.
* Wed Jul 09 2008 - damien.carbery@sun.com
- Remove EXTRA_LDFLAGS after adding patch to at-spi.
* Wed Jul 09 2008 - li.yuan@sun.com
- Put %defattr prior to new files.
* Wed Jul 09 2008 - li.yuan@sun.com
- Move login-helper to EXTRA_LDFLAGS and add arch infomation so libraries depend
  on it can find it in the right place. Also add 
  %{_libdir}/%{_arch64}/bonobo/servers/*.server to the file section.
* Tue Jul 08 2008 - damien.carbery@sun.com
- Set ACLOCAL_FLAGS for use in gnome-mag.spec.
* Mon Jul 07 2008 - li.yuan@sun.com
- Fix 6697334. Add 64 bit libraries support for at-spi.
* Mon Mar 31 2008 - li.yuan@sun.com
- Add copyright file
* Wed Mar 19 2008 - dermot.mccluskey@sun.com
- Add dep on SUNWj6rt so that gnome-java-bridge.jar and accessibility.properties
  get installed in correct /usr/java link location. Fixes 6641866.
* Thu Jan 10 2008 - li.yuan@sun.com
- change owner to liyuan.
* Sun Oct  7 2007 - laca@sun.com
- add /usr/X11/include to CFLAGS
- delete Nevada X deps
* Fri Sep 28 2007 - laca@sun.com
- disable java access bridge if build without java support
* Wed Sep 05 2007 - damien.carbery@sun.com
- Remove references to SUNWgnome-a11y-base-libs as its contents have been
  moved to SUNWgnome-base-libs.
* Thu Jun 07 2007 - damien.carbery@sun.com
- Add %{_libdir}/python?.? to %files and remove .pyo files in %install.
* Tue Mar 13 2007 - damien.carbery@sun.com
- Incorporate %post changes from Mary Ding. Fixes 6531193.
* Mon Mar 05 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-config/-devel as gconf-2.0.pc is needed.
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Fri Jul 14 2006 - damien.carbery@sun.com
- Remove .la files before packaging.
* Thu Jun 22 2006 - damien.carbery@sun.com
- Change 'return 0' to 'exit 0' in main function in %post share. Fixes 6437617.
* Tue Jun 13 2006 - damien.carbery@sun.com
- Add dependencies on SUNWzoner/u and SUNWpkgcmdsu for zonename and pkgcond
  binaries that are used in the postinstall script. As suggested in 6377106.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Tue May 30 2006 - damien.carbery@sun.com
- Merge postinstall script from JDS3.1 branch. Include fix for 6431039.
* Tue May 09 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Fri May 05 2006 - damien.carbery@sun.com
- Copy postinstall script from JDS3.1 branch. Incorporate dynamic code.
* Tue Mar 14 2006 - damien.carbery@sun.com
- Add doc dir to share package.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
- Move Requires SUNWj5rt to share package as postinstall that installs the 
  symlink under a SUNWj5rt directory is in share package. Make base package
  require share package.
* Fri Dec 02 2005 - damien.carbery@sun.com
- Add Requires SUNWj5rt so that symlink can be created.
* Mon Nov 21 2005 - damien.carbery@sun.com
- Add %post share code to accomodate zones. Bug 6347858. Copied from 
  cinnabar-solaris branch.
* Mon Sep 12 2005 - laca@sun.com
- define l10n subpkg
* Tue Jun 14 2005 - brian.cameron@sun.com
- Fix packaging.
* Fri Jun 10 2005 - damien.carbery@sun.com
- Call %freetts.build, and add lib/freetts dir to share package.
* Mon Nov 22 2004 - damien.carbery@sun.com
- Fix for 6197816: gnopernicus moved to /usr/demo/jds so gnome-mag moved to
  SUNWgnome-a11y-libs package to remain in /usr/bin.
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Aug 30 2004 - shirley.woo@sun.com
- Bug 5091588 : sman3/4  files should be in a devel package
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Wed Aug 18 2004 - brian.cameron@sun.com
- Added back gtk-docs to packaging.  Needed because the at-cspi docs
  are referred to from the libcspi.3 man page.
* Wed Aug 18 2004 - damien.carbery@sun.com
- Change manpage perms for Solaris integration.
* Fri Jul 23 2004 - damien.carbery@sun.com
- Move freetts from SUNWgnome-a11y-speech.
* Tue Jun 22 2004 - shirley.woo@sun.com
- changed install location to /usr/lib and /usr/bin
* Wed Apr 14 2004 - padraig.obriain@sun.com
- Add entry to %files for accessibility.properties and gnome-java-bridge.jar
* Fri Mar 26 2004 - laca@sun.com
- add panel dependency
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Tue Mar 23 2004 - laca@sun.com
- Remove gtk-doc and _datadir/lib from %files
* Thu Feb 26 2004 - laca@sun.com
- Add devel-share subpkg for idl files and api docs



