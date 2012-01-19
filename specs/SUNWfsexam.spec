#
# spec file for package SUNWfsexam
#
# includes module(s): fsexam
#
# Copyright (c) 2008, 2010, Oracle and/or its affiliates. All rights reserved. 
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yongsun
#

%define OSR n/a:n/a

%include Solaris.inc

%define name    SUNWfsexam 
%define cmpt    fsexam

Summary:	Filesystem Examiner
Name:		SUNWfsexam 
IPS_package_name: storage/fsexam
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Version: 	0.8.3
Release:	1
License: 	cr_Oracle
SUNW_BaseDir: 	%{_basedir}
Source: 	%{cmpt}-%{version}.tar.bz2
Source1:	fsexam-l10n-po-1.11.tar.bz2
Source2:	l10n-configure.sh
Source3:        %{name}-manpages-0.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_Category:	G11NTOOLS,application,%{jds_version}
SUNW_Copyright:	%{name}.copyright

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlibglade
Requires: SUNWgnome-libs
Requires: SUNWgnome-config
Requires: SUNWgnome-panel
Requires: SUNWgnome-file-mgr
Requires: SUNWfsexam-root
Requires: SUNWgnome-vfs
Requires: SUNWpostrun
Requires: SUNWautoef
Requires: SUNWgnome-component
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWgnome-file-mgr-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWautoef

%package l10n
Summary:	Fsexam - l10n files
Requires: %{name}

%package root
Summary:	%{summary} - / filesystem
SUNW_BaseDir:	/
SUNW_Category:	G11NTOOLS,application,%{jds_version}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWpostrun-root
Requires: SUNWgnome-config

%description
File System Examiner is to help user migrate file name and file content from
legacy encoding to UTF8 encoding.

%prep
%setup -q -n %{cmpt}-%{version}
bzcat %SOURCE1 | tar xf -
gzcat %SOURCE3 | tar xf -

bash -x %SOURCE2 --enable-sun-linguas

%build
export LDFLAGS="%_ldflags -L%{_libdir} -R%{_libdir}"
export CFLAGS="-I%{_includedir} %optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export PKG_CONFIG_PATH=%{_pkg_config_path}

intltoolize --copy --force --automake

bash -x %SOURCE2 --enable-copyright

libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f
autoconf
./configure --prefix=%{_prefix}              \
            --sysconfdir=%{_sysconfdir}

make

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall

rm -rf $RPM_BUILD_ROOT/var

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

cd $RPM_BUILD_ROOT/%{_bindir}
ln -s fsexam fsexamc

# /usr/share/man
cd %{_builddir}/%cmpt-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%restart_fmri gconf-cache

%files 
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/bonobo/servers/*.server
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/fsexam.desktop
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*.png
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/fsexam/C
%{_datadir}/omf/fsexam/*-C.omf
%dir %attr (0755, root, other) %{_datadir}/fsexam
%{_datadir}/fsexam/glade/*.glade2
%dir %attr (0755, root, bin) %{_datadir}/idl
%{_datadir}/idl/*.idl
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc AUTHORS ChangeLog COPYING NEWS README
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/fsexam/[a-z]*
%{_datadir}/omf/fsexam/*-[a-z]*.omf

%files root
%defattr (0755, root, sys)
%attr (-, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/fsexam.schemas

%changelog
* Fri Jul 01 2011 - y.yong.sun@oracle.com
- bumped to 0.8.3
* Tue Jun 14 2011 - y.yong.sun@oracle.com
- bumped to 0.8.2
- fixed bug 7020599
* Fri Apr 23 2010 - ghee.teo@oracle.com
- Added patch to remove reference to libeel.so.2
* Wed Jun 17 2009 - yong.sun@sun.com
- replace the postrun script with a restart_fmri
* Fri Sep 19 2008 - dave.lin@sun.com
- Set attribute of the dir /usr/share/doc in base pkg.
* Wed Aug 13 2008 - takao.fujiwara@sun.com
- commit messages translation as fsexam-l10n-po-1.11.tar.bz2 for cs.po
* Mon Jul 21 2008 - jedy.wang@sun.com
- Set the owner to yongsun.
* Mon Mar 31 2008 - yandong.yao@sun.com
- use SUNWfsexam.copyright instead of default copyright.
* Fri Mar 21 2008 - yandong.yao@sun.com
- bump to 0.8.1
- commit messages translation as fsexam-l10n-po-1.10.tar.bz2
- merge patch fsexam-01-obsolete-eel-func to trunk
* Thu Jan 03 2008 - damien.carbery@sun.com
- Add patch fsexam-01-obsolete-eel-func to eliminate the use of an obsoleted
  eel function (eel_str_get_after_prefix).
* Thu Nov 15 2007 - damien.carbery@sun.com
- Correct dir ownership for %{_datadir}/idl.
* Tue Nov 13 2007 - Yandong.Yao@Sun.COM
- Bump to version 0.8.0 as 0.6.* is reserved for jds3.1
* Mon Sep 10 2007 - Yandong.Yao@Sun.COM
- Bump to version 0.6.0
* Fri Aug 17 2007 - yandong.yao@sun.com
- Bump to version 0.4.6
* Mon Jul 30 2007 - yandong.yao@sun.com
- Bump to version 0.4.4
* Thu Jun 28 2007 - yandong.yao@sun.com
- Bump to version 0.4.3
* Wed May 30 2007 - yandong.yao@sun.com
- Fix bug 6561612 fsexam crash when config a log file at the first time
- Fix bug 6561617 fsexam search with incorrect result 
* Tue May 29 2007 - yandong.yao@sun.com
- Add man page fsexam.1 and fsexam.4
* Thu May 10 2007 - yandong.yao@sun.com
- Bump to version 0.4.2
- Symlink fsexamc to fsexam
* Mon Apr 02 2007 - damien.carbery@sun.com
- Remove upstream patch, 01-check-auto_ef.
* Tue March 27 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWautoef for auto_ef.h header file.
* Sat Mar 24 2007 - yandong.yao@sun.com
- Bump to version 0.4.0
- Add fsexam.glade2, idl into SUNWfsexam pkg
* Mon Mar 7 2007 - yandong.yao@sun.com
- Fix bug 6444322: provide custermized sorting function for GtkTreeModel
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Fri Jun 23 2006 - yandong.yao@sun.com
- Fix bug 6441381
* Thu Jun 15 2006 - yandong.yao@sun.com
- add libtool,automake before autoconf
  Fix bug 6432608
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri Jun  2 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Mon Sep 12 2005 - laca@sun.com
- remove unpackaged files
* Wed Nov 24 2004 - kieran.colfer@sun.com
- updating l10n tarballs to fix 5094817, 6197170, 6197173, 6197203
(tarball revisions have to be kept consistent)
* Fri Oct 29 2004 - kieran.colfer@sun.com
- Uprevved l10n po tarball version from 1.6 to 1.7
* Thu Oct 28 2004
- Merged fsexam-g11n-desktopfix.diff to source tree, so remove it from spec file
- Update l10n po tarball from 1.5 to 1.6
* Thu Oct 14 2004
- Adding fsexam-g11n-desktopfix.diff to fix bug#6179139 
* Fri Oct 08 2004 - kieran.colfer@sun.com
- Adding latest l10n po tarball to the build
* Sun Oct 3  2004  Yong.Sun@Sun.COM
- Move OLH files of C locale from SUNWfsexam-l10n to SUNWfsexam
* Sun Sep 19 2004  laca@sun.com
- fix defattr tags
- add chmod to %install to fix gconf permissions
* Thu Sep 16 2004  laca@sun.com
- set category to g11ntools
- remove dependency on SUNWfsexam-l10n pkg, since it's nodist
- minor clean-ups, polishing...
* Thu Sep 16 2004 Yong Sun <Yong.Sun@Sun.COM>
- Add dependency of SUNWgnome-panel, SUNWgnome-file-mgr
* Wed Aug 11 2004 Federic Zhang <federic.zhang@sun.com>
- Bump to 0.3
* Tue Aug 10 2004 Federic Zhang <federic.zhang@sun.com>
- For Cinnabar build 16, implement Undo and UI polish 
* Fri Jul 23 2004 Federic Zhang <federic.zhang@sun.com>
- For Cinnbar Beta build 15
* Mon May 31 2004 Gain  Tu <gavin.tu@sun.com>
- For Cinnabar build 11, add l10en menu, context-sensitive menu, help, reverse
* Mon May 24 2004 Gavin Tu <gavin.tu@sun.com>
- menu can be l10ned, alloc memory for name dynamiclly 
* Thu May 13 2004 Federic Zhang <federic.zhang@sun.com>
- For Cinnabar build 10, added fsexam.desktop and fsexam-icon.png
* Tue Apr 20 2004 Federic Zhang <federic.zhang@sun.com>
- For Cinnabar build8, added CFLAGS env and prefix option
* Mon Apr 11 2004 Federic Zhang <federic.zhang@sun.com>
- version 0.1



