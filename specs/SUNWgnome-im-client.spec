#
# # spec file for package SUNWgnome-im-client
#
# includes module(s): pidgin, pidgin-otr, libotr
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%use pidgin = pidgin.spec
%use libotr = libotr.spec
%use pidginotr = pidgin-otr.spec

Name:                    SUNWgnome-im-client
IPS_package_name:        communication/im/pidgin
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:                 GNOME multi-protocol instant messaging client
Version:                 %{pidgin.version}
Source:                  %{name}-manpages-0.1.tar.gz
#Patch1:                  pidgin-12-libpurple-py26.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GNU General Public License v2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: library/desktop/gtk2
Requires: library/gnome/gnome-libs
Requires: runtime/python-26
Requires: shell/bash
Requires: system/library/dbus
Requires: library/desktop/evolution-data-server
Requires: library/gnome/gnome-component
Requires: library/gnutls
Requires: system/library/math
Requires: runtime/perl-512
Requires: service/gnome/desktop-cache
Requires: library/audio/gstreamer
Requires: system/network/avahi
Requires: database/sqlite-3
Requires: library/nspr
Requires: library/security/nss
Requires: library/desktop/gtkspell
Requires: library/libidn
Requires: library/gnome/gnome-keyring
BuildRequires: library/desktop/gtk2
BuildRequires: runtime/python-26
BuildRequires: system/library/dbus
BuildRequires: library/desktop/evolution-data-server
BuildRequires: library/gnome/gnome-component
BuildRequires: library/gnome/gnome-libs
BuildRequires: library/gnutls
BuildRequires: library/audio/gstreamer
BuildRequires: system/network/avahi
BuildRequires: database/sqlite-3
BuildRequires: library/desktop/gtkspell
BuildRequires: library/gnome/gnome-keyring
BuildRequires: x11/library/libxscrnsaver

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
%pidgin.prep -d %name-%version
%libotr.prep -d %name-%version
%pidginotr.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

#date:2009-12-4 owner:elaine type:bug :explicitly use python2.6 in purple-remote and pruple-url-handler
#%patch1 -p0
%build
%{!?perl_installarchlib: %define perl_installarchlib %(eval "`%{__perl} -V:installarchlib`"; echo $installarchlib)}
%{!?perl_installvendorlib: %define perl_installvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}
export PKG_CONFIG_PATH=../pidgin-%{pidgin.version}/libpurple:../pidgin-%{pidgin.version}:%{_pkg_config_path}
export CFLAGS="%optflags -DHAVE_ALLOCA_H"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
%pidgin.build -d %name-%version
%libotr.build -d %name-%version
export ACLOCAL_FLAGS="-I %{_builddir}/%name-%version/libotr-%{libotr.version}"
export CFLAGS="$CFLAGS -I %{_builddir}/%name-%version/libotr-%{libotr.version}/my_build_tmp"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="$LDFLAGS -L%{_builddir}/%name-%version/libotr-%{libotr.version}/src/.libs -lotr"
export LIBOTR_BLD_DIR=%{_builddir}/%name-%version/libotr-%{libotr.version}
%pidginotr.build -d %name-%version

%install
%pidgin.install -d %name-%version
%libotr.install -d %name-%version
%pidginotr.install -d %name-%version

# Delete .a and .la files.
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/pidgin/*.la
rm -r $RPM_BUILD_ROOT%{_libdir}/perl5

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

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
%{_libdir}/*.so*
%{_libdir}/pidgin/*.so*
%{_libdir}/purple-2/*.so*
%attr(0755, root, bin) %{_libdir}/pidgin/perl/Pidgin.pm
%attr(0755, root, bin) %{_libdir}/purple-2/perl/Purple.pm
%attr(0755, root, bin) %{_libdir}/pidgin/perl/auto/Pidgin
%attr(0755, root, bin) %{_libdir}/purple-2/perl/auto/Purple
#%attr(0755, root, bin) %{perl_installarchlib}/perllocal.pod
#%dir %attr (0755, root, bin) %{perl_installvendorlib}
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/purple/
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%{_datadir}/sounds
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/pidgin.*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/pidgin.*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/pidgin.*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/pidgin.*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/pidgin.*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/pidgin.*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/*
%{_mandir}/man3/*
%doc pidgin-%{pidgin.version}/COPYRIGHT
%doc(bzip2) pidgin-%{pidgin.version}/COPYING
%doc pidgin-%{pidgin.version}/ChangeLog
%doc pidgin-%{pidgin.version}/README
%doc(bzip2) pidgin-otr-%{pidginotr.version}/COPYING
%doc pidgin-otr-%{pidginotr.version}/ChangeLog
%doc pidgin-otr-%{pidginotr.version}/README
%doc pidgin-otr-%{pidginotr.version}/NEWS
%doc pidgin-otr-%{pidginotr.version}/AUTHORS
%doc(bzip2) libotr-%{libotr.version}/COPYING
%doc(bzip2) libotr-%{libotr.version}/COPYING.LIB
%doc libotr-%{libotr.version}/ChangeLog
%doc libotr-%{libotr.version}/README
%doc libotr-%{libotr.version}/NEWS
%doc libotr-%{libotr.version}/AUTHORS
%dir %attr (0755, root, other) %{_datadir}/doc

%files root
%defattr(-, root, sys)
%attr(0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/purple.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/pidgin
%{_includedir}/libpurple
%{_includedir}/libotr
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Mon Feb 13 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Mon Aug 29 2011 - yanjing.guo@oracle.com
- remove the perl empty directory
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add 'License' tag
* Fri Mar 05 2010 - brian.lu@sun.com
- Fix bug d.o.o 14897
* Tue Jan 26 2009 - jeff.cai@sun.com
- Add dependency on SUNWlibgnome-keyring
* Tue Dec 17 2009 - brian.lu@sun.com
- Fix bug CR6908695
* Fri Dec 04 2009 - yuntong.jin@sun.com
- explicitly use python2.6 in purple-url-handler&purple-remote
* Wed Oct 14 2009 - brian.lu@sun.com
- Add dependency SUNWgnome-idn (CR6886486)
* Tue Sep 01 2009 - dave.lin@sun.com
- Removed "../pidgin-%{pidgin.version}/pidgin" in PKG_CONFIG_PATH. 
* Mon Aug 31 2009 - dave.lin@sun.com
- Add "../pidgin-%{pidgin.version}/pidgin" in PKG_CONFIG_PATH
* Fri Apr 10 2009 - elaine.xiong@sun.com
- correct gtkspell-devel build dependency.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Wed Mar 11 2009 - elaine.xiong@sun.com
- Change ownership to elaine.
* Fri Aug 01 2008 - christian.kelly@sun.com
- Correct %files: add in man3 entries 
* Thu Jul 23 2008 - damien.carbery@sun.com
- Move libotr from pidgin-otr.spec to libotr.spec. This makes is easier to
  track for ARC and Legal reviews.
* Wed May 21 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWsqlite3, SUNWpr and SUNWtls to fix #6703993.
* Fri Mar 07 2008  - rick.ju@sun.com
- add SUNWavahi-bridge-dsd dependency
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Thu Dec 06 2007  - rick.ju@sun.com
- %files changed to bump to pidgin 2.3.0
* Tue Nov 16 2007  - rick.ju@sun.com
- Use SGML man page instead of the one from community
* Tue Nov 06 2007  - rick.ju@sun.com
- Add ../pidgin-%{pidgin.version}/libpurple to PKG_CONFIG_PATH so that
  pidgin-otr can find the libpurple libraries during build.
* Fri Nov 02 2007  - rick.ju@sun.com
  remove SUNWavahi-bridge-dsd dependency
* Wed Oct 10 2007 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Sep 28 2007 - laca@sun.com
- delete some unnecessary env variables
* Wed Aug 22 2007 - damien.carbery@sun.com
- Update %files for new pidgin tarball.
* Fri Jun 01 2007 - damien.carbery@sun.com
- Set %attr for %{datadir}/icons dirs.
* Tue May 30 2007 - rick.ju@sun.com
- bump to pidgin 2.0.1
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Fri Feb  9 2007 - damien.carbery@sun.com
- After a review, remove code that made unnecessary copy of $RPM_BUILD_ROOT
  before installing second module in this spec file.
* Wed Feb  7 2007 - rick.ju@sun.com
- Fixed an install issue (copy $RPM_BUILD_ROOT before %gaimotr.install.
* Mon Feb  5 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-media/-devel after check-deps.pl run.
* Wed Jan 17 2007 - rick.ju@sun.com
- Add gaim-otr.spec.
* Fri May 12 2006 - damien.carbery@sun.com
- Updates for new tarball. Add 'root' package for the gaim.schemas file (and 
  %post/%preun scripts too). Remove %{_datadir}/doc from %files as nothing is 
  installed there now.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri May 12 2006 - damien.carbery@sun.com
- Small update to dependency list after check-deps.pl run.
* Thu May 11 2006 - brian.cameron@sun.com
- Move gaim-client-example to demo directory.
* Thu May 11 2006 - halton.huo@sun.com
- Merge -share pkg(s) into the base pkg(s).
* Wed May 10 2006 - brian.cameron@sun.com
- Now package gaim-notifications-example demo program.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Wed Jan 18 2006 - damien.carbery@sun.com
- Add devel files from 2.0.0beta1 tarball.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Thu Sep 15 2005 - laca@sun.com
- Define devel subpkg
* Fri Nov 12 2004 - kazuhiko.maekawa@sun.com
- Added workaround fix for 6193354
* Wed Nov  3 2004 - damien.carbery@sun.com
- Add BuildRequires of SUNWgnome-javahelp-convert to get 
  javahelp-convert-install.
* Tue Oct 05 2004 - matt.keenan@sun.com
- Added localized help files to l10n %files section
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Thu Sep 23 2004 - damien.carbery@sun.com
- Add BuildRequires of SUNWgnome-libs to get scrollkeeper-preinstall.
* Mon Sep 06 2004 - matt.keenan@sun.com
- Added javahelp to %files share
* Fri Sep 03 2004 - damien.carbery@sun.com
- Changes to support docs tarball added to gaim.spec.
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Mon Jul 12 2004 - damien.carbery@sun.com
- Unset perms for /usr/share/pixmaps and /usr/share/applications.
* Sat Jul 10 2004 - damien.carbery@sun.com
- Set perms for /usr/share/pixmaps and /usr/share/applications.
* Tue Jun 22 2004 - shirley.woo@sun.com
- changed install location to /usr/lib and /usr/bin
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Tue Mar 23 2004 - <laca@sun.com>
- add -DHAVE_ALLOCA_H to CFLAGS
* Fri Mar 05 2004 - <laca@sun.com>
- define PERL5LIB
* Wed Mar 03 2004 - <laca@sun.com>
- remove unnecessary env vars
- fix %files share
* Mon Mar 01 2004 - <laca@sun.com>
- set CFLAGS, LDFLAGS



