#
# spec file for package SUNWgnome-text-editor
#
# includes module(s): gedit gtksourceview
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%use gedit = gedit.spec

Name:                    SUNWgnome-text-editor
IPS_package_name:        editor/gedit
Meta(info.classification): %{classification_prefix}:Applications/Accessories,%{classification_prefix}:Development/Editors
Summary:                 GNOME text editor
Version:                 %{gedit.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gedit.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: library/desktop/gtk2
Requires: library/gnome/gnome-libs
Requires: gnome/config/gconf
Requires: library/gnome/gnome-vfs
Requires: library/gnome/gnome-component
Requires: system/library/math
Requires: library/libxml2
Requires: runtime/python-26
Requires: library/python-2/pygobject-26
Requires: library/python-2/pygtk2-26
Requires: library/python-2/pygtksourceview2-26
Requires: library/python-2/python-gnome-desktop-26
Requires: service/gnome/desktop-cache
Requires: library/desktop/gtksourceview
Requires: library/spell-checking/enchant
BuildRequires: library/desktop/gtk2
BuildRequires: library/libxml2
BuildRequires: gnome/config/gconf
BuildRequires: library/gnome/gnome-vfs
BuildRequires: library/gnome/gnome-libs
BuildRequires: library/gnome/gnome-component
BuildRequires: runtime/python-26
BuildRequires: library/python-2/pygobject-26
BuildRequires: library/python-2/pygtk2-26
BuildRequires: library/python-2/pygtksourceview2-26
BuildRequires: library/python-2/python-gnome-desktop-26
BuildRequires: library/desktop/gtksourceview
BuildRequires: library/spell-checking/enchant
BuildRequires: developer/gnome/gnome-doc-utils

%package l10n
Summary:                 %{summary} - l10n files

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}

%prep
rm -rf %name-%version
mkdir %name-%version
%gedit.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -
cd %{_builddir}/%name-%version/gedit-%gedit.version

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED
export LDFLAGS="%_ldflags -norunpath"
export CFLAGS="%optflags"
export LD_LIBRARY_PATH="/usr/sfw/lib:$LD_LIBRARY_PATH"
export LDFLAGS="%_ldflags -L/usr/X11/lib -R /usr/X11/lib -lX11"
%gedit.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gedit.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 0755 $RPM_BUILD_ROOT%{_datadir}/gnome/help/gedit/C/*.xml

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rf $RPM_BUILD_ROOT%{_localstatedir}

find $RPM_BUILD_ROOT -name "*.a" -exec rm {} \;

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
%{_libdir}/gedit-2/gedit-bugreport.sh
%{_libdir}/gedit-2/plugins/*.so*
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_libdir}/gedit-2/plugins/snippets
%{_libdir}/gedit-2/plugins/externaltools
%{_libdir}/gedit-2/plugins/pythonconsole
%{_libdir}/gedit-2/plugin-loaders
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/gedit-2
%{_datadir}/gtk-doc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/gedit/C
%{_datadir}/omf/gedit/*-C.omf
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%doc -d gedit-%{gedit.version} AUTHORS ChangeLog MAINTAINERS NEWS README
%doc(bzip2) -d gedit-%{gedit.version} COPYING
%dir %attr (0755, root, other) %{_datadir}/doc
%{_libdir}/gedit-2/plugins/quickopen/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z]*.omf

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/gedit.schemas
%{_sysconfdir}/gconf/schemas/gedit-file-browser.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Remove .a files.
* Mon Jan 18 2010 - yuntong.jin@sun.com
- Bump to 2.29.4
* Mon Dec 21 2009 - ghee.teo@sun.com
- Remove SUNWgnome-print dependency.
* Sun Jul 26 2009 - christian.kelly@sun.com
- Minor change to %files.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 30 2009 - yuntong.jin@sun.com
- change the owner to yuntong.jin
* Fri Dec 26 2008 - dave.lin@sun.com
- Add %{_libdir}/gedit-2/plugin-loaders in %file.
* Sun Oct 07 2007 - damien.carbery@sun.com
- Add BuildRequires SUNWwxinc for sm.pc and SUNWlxml-devel for libxml-2.0.pc
  (both referenced in configure.ac).
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Sun Oct 07 2007 - damien.carbery@sun.com
- Add python plugin dirs, now installed because pygtksourceview is part of
  SUNWgnome-python-libs.
* Fri Sep 28 2007 - laca@sun.com
- delete unneeded env variables that break the indiana build
- delete SUNWxwrtl dep -- already depend on SUNWgnome-base-libs
* Tue Jul 03 2007 - damien.carbery@sun.com
- Remove 3 plugins dirs from %files because they are no longer installed.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Mon Mar 12 2007 - damien.carbery@sun.com
- Add %{_libdir}/gedit-2/gedit-bugreport.sh, for 2.18.0 tarball.
* Thu Mar 08 2007 - jeff.cai@sun.com
- Remove the dependency on aspell.
* Thu Jan 25 2007 - damien.carbery@sun.com
- Remove plugins/*.py* from %files as none are installed.
* Tue Sep 05 2006 - damien.carbery@sun.com
- Fix root pkg (s/filebrowser.schemas/gedit-file-browser.schemas/).
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Wed Aug 16 2006 - damien.carbery@sun.com
- Add gtk-doc dir to %files.
* Fri Jul 28 2006 - damien.carbery@sun.com
- Update %files for new tarball.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Thu Jun 29 2006 - laca@sun.com
- update %post/%preun gconf scripts, add SUNWgnome-gtksourceview deps
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri Jun  2 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Sat May 13 2006 - laca@sun.com
- Remove /usr/lib/jds-private from LDFLAGS
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Mon May 08 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-python-desktop/-devel to build python plugins.
* Thu Mar 20 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-python-libs/-devel to build python plugins.
* Wed Mar 15 2006 - damien.carbery@sun.com
- Add to Build/Requires after running check-deps.pl.
* Wed Mar 15 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-component/-devel for ORBit2.
* Tue Mar 14 2006 - damien.carbery@sun.com
- Add plugins files to %files and remove unneeded rmdir of /usr/var.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Jan 31 2006 - damien.carbery@sun.com
- Remove application-registry and mime-info directories as no files installed 
  there now.
* Wed Jan 18 2006 - damien.carbery@sun.com
- Remove scrollkeeper files under /usr/var and /var.
* Sat Jan 07 2006 - damien.carbery@sun.com
- Update %files for new tarball.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Wed Sep 14 2005 - laca@sun.com
- remove unpackaged files
* Wed Aug 31 2005 - damien.carbery@sun.com
- Set LD_LIBRARY_PATH so that libfreetype.so.6 can be found when a built
  binary is run during the build step.
* Thu May 19 2005 - brian.cameron@sun.com
- Updte to 2.10, fix LDFLAGS and packaging for Solaris.
* Sat Jun 26 2004  shirley.woo@sun.com
- move sman3 manpages to devel pkg per Solaris pkg requirement
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Thu Sep 09 2004 - matt.keenan@sun.com
- Added gtksourceview manpage
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Wed Aug 18 2004 - damien.carbery@sun.com
- Change manpage perms for Solaris integration.
* Fri Jul 09 2004 - damien.carbery@sun.com
- Return -R to LDFLAGS. I had incorrectly implemented the ARC decision.
* Thu Jul 08 2004 - damien.carbery@sun.com
- Remove -R from LDFLAGS because ARC said to use -norunpath.
* Fri Jul 02 2004 - damien.carbery@sun.com
- Add /usr/lib/jds-private to LDFLAGS.
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Mon May 03 2004 - <vijaykumar.patwari@wipro.com>
- Added entry in spec for plugins files to get installed.
* Fri Mar 26 2004 - <laca@sun.com>
- add SUNWgnome-file-mgr dependency (for libeel)
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Thu Mar 04 2004 - <laca@sun.com>
- fix build
- fix files %share
* Mon Mar 01 2004 - <laca@sun.com>
- fix dependencies
* Thu Feb 26 2004 - <laca@sun.com>
- set PERL5LIB to make intltool happy
* Mon Feb 23 2004 - <niall.power@sun.com>
- install gconf schemas at end of install stage.



