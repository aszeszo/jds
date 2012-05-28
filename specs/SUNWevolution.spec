# spec file for package SUNWevolution
#
# includes module(s): evolution
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc

%define with_hal %(pkginfo -q SUNWhal && echo 1 || echo 0)

%use evolution = evolution.spec
%define with_pilot_link 1

Name:          SUNWevolution
License: GPL v2, LGPL v2.1, FDL v1.1
IPS_package_name: mail/evolution
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       Evolution Email and Calendar
Version:       %{evolution.version}
SUNW_Category: EVO25,%{default_category}
SUNW_BaseDir:  %{_basedir}
SUNW_Copyright:%{name}.copyright
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Source1:       idnkit.pc
Source2:       %{name}-manpages-0.1.tar.gz
Requires:       library/desktop/libgnomecanvas
Requires:       library/desktop/gtkhtml
Requires:       library/security/nss
Requires:       library/idnkit
Requires:       library/desktop/evolution-data-server
Requires:       library/gnome/gnome-component
Requires:       gnome/config/gconf
Requires:       library/gnome/gnome-libs
Requires:       library/gnome/gnome-vfs
Requires:       library/popt
Requires:       library/libxml2
Requires:       system/library/math
Requires:       system/library/security/libgcrypt
Requires:       service/security/kerberos-5
Requires:       system/library/security/gss
Requires:       library/gnome/gnome-keyring
Requires:       system/library/dbus
Requires:       library/desktop/evolution-data-server
Requires:       library/gnutls
Requires:       system/library/security/libgcrypt
Requires:       library/security/libgpg-error
Requires:       library/zlib
Requires:       service/gnome/desktop-cache
Requires:       library/nspr
Requires:       library/audio/gstreamer
%{?with_pilot_link:Requires:      communication/pda/pilot-link }
%{?with_pilot_link:Requires:      communication/pda/gnome-pilot }
BuildRequires:       runtime/perl-512
BuildRequires:       library/desktop/libgnomecanvas
BuildRequires:       library/idnkit/header-idnkit
BuildRequires:       library/desktop/evolution-data-server
BuildRequires:       library/gnome/gnome-component
BuildRequires:       gnome/config/gconf
BuildRequires:       library/gnome/gnome-libs
BuildRequires:       library/gnome/gnome-vfs
BuildRequires:       library/popt
BuildRequires:       library/libxml2
BuildRequires:       system/library/math
BuildRequires:       system/library/security/libgcrypt
BuildRequires:       library/audio/gstreamer  
BuildRequires:       library/gnome/gnome-keyring
BuildRequires:       system/library/iconv/unicode
BuildRequires:       developer/gnome/gnome-doc-utils
BuildRequires:       library/libunique
BuildRequires:       gnome/theme/gnome-icon-theme
BuildRequires:       system/library/iconv/utf-8
BuildRequires:       library/desktop/libgweather
BuildRequires:       library/desktop/evolution-data-server

%if %with_hal
BuildRequires:       system/hal
%endif
%{?with_pilot_link:BuildRequires:     communication/pda/pilot-link}
%{?with_pilot_link:BuildRequires:     communication/pda/pilot-link}
%{?with_pilot_link:BuildRequires:     communication/pda/gnome-pilot}

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package root
Summary:       %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:       %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:       mail/evolution

%prep
rm -rf %name-%version
mkdir -p %name-%version
%evolution.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE2 | tar xf -
cd %{_builddir}/%name-%version/evolution-%{evolution.version}

cd ..
cp %SOURCE1 %{_builddir}/%name-%version/evolution-%{evolution.version}

%build
export LDFLAGS="%_ldflags -L%{_libdir} -R%{_libdir} -R`pkg-config --variable=libdir nss` -R`pkg-config --variable=libdir nspr`"
export CFLAGS="%optflags"
%if %option_with_gnu_iconv
export CFLAGS="$CFLAGS -I/usr/gnu/include -L/usr/gnu/lib -R/usr/gnu/lib"
%endif
export RPM_OPT_FLAGS="$CFLAGS"
export PERL=/usr/perl5/bin/perl
export PKG_CONFIG_PATH=%{_pkg_config_path}:%{_builddir}/%name-%version/evolution-%{evolution.version}
%evolution.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%evolution.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

# Remove bogofilter junk plugin since bogofilter is not available on Solaris.
rm -rf $RPM_BUILD_ROOT%{_libdir}/evolution/%{evolution.major_version}/plugins/*bogo*
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/bogo-junk-plugin.schemas

# Delete scrollkeeper files
rm -rf $RPM_BUILD_ROOT/var

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_ROOT}DISABLE

# replace the old scripts with script files
%post
%restart_fmri gconf-cache desktop-mime-cache icon-cache

%postun
%restart_fmri desktop-mime-cache

%files

%doc -d evolution-%{evolution.version} AUTHORS README
%doc(bzip2) -d evolution-%{evolution.version} ChangeLog ChangeLog.pre-1-4
%doc(bzip2) -d evolution-%{evolution.version} COPYING COPYING.LGPL2 COPYING-DOCS
%doc(bzip2) -d evolution-%{evolution.version} NEWS NEWS-1.0
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/evolution/%{evolution.major_version}/*.so*
%{_libdir}/evolution/%{evolution.major_version}/modules/*
%{?with_pilot_link:%{_libdir}/evolution/%{evolution.major_version}/conduits/*.so}
%{_libdir}/evolution/%{evolution.major_version}/plugins/*
%{_libexecdir}/evolution/%{evolution.major_version}/csv2vcard
%{_libexecdir}/evolution/%{evolution.major_version}/evolution-addressbook-clean
%{_libexecdir}/evolution/%{evolution.major_version}/evolution-addressbook-export
%{_libexecdir}/evolution/%{evolution.major_version}/evolution-alarm-notify
%{_libexecdir}/evolution/%{evolution.major_version}/evolution-backup
%{_libexecdir}/evolution/%{evolution.major_version}/killev
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/evolution
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/mime-info
%{_datadir}/mime-info/*
%{?with_pilot_link:%attr (0755, root, bin) %{_datadir}/gnome-pilot}
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/evolution*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/evolution*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/evolution*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/evolution*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/evolution.svg

%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/evolution*/C
%{_datadir}/omf/evolution/evolution*C.omf
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%dir %attr (0755, root, bin) %{_datadir}/gtk-doc
%{_datadir}/gtk-doc/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/omf/evolution/evolution-[a-z][a-z].omf
%{_datadir}/omf/evolution/evolution-[a-z][a-z]_[A-Z][A-Z].omf
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/evolution/[a-z][a-z]
%{_datadir}/gnome/help/evolution/[a-z][a-z]_[A-Z][A-Z]

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/apps_evolution_email_custom_header.schemas
%{_sysconfdir}/gconf/schemas/apps-evolution-mail-prompts-checkdefault.schemas
%{_sysconfdir}/gconf/schemas/apps_evolution_addressbook.schemas
%{_sysconfdir}/gconf/schemas/apps-evolution-attachment-reminder.schemas
%{_sysconfdir}/gconf/schemas/apps-evolution-mail-notification.schemas
%{_sysconfdir}/gconf/schemas/apps_evolution_calendar.schemas
%{_sysconfdir}/gconf/schemas/apps_evolution_shell.schemas
%{_sysconfdir}/gconf/schemas/evolution-mail.schemas
%{_sysconfdir}/gconf/schemas/apps-evolution-template-placeholders.schemas
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg/autostart
%{_sysconfdir}/xdg/autostart/*

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu May 27 - jeff.cai@sun.com
- Comment the dependency on SUNWgtkimageview
* Tue Apr 20 - christian.kelly@oracle.com
- Correct typo from previous commit!
* Tue Mar 19 - jeff.cai@sun.com
- Add dependency on SUNWiconv-unicode
* Wed Feb 10 - jedy.wang@sun.com
- Add dependency on SUNWgtkimageview.
* Tue Jan 26 - jeff.cai@sun.com
- Add dependency on SUNWlibgnome-keyring
* Wed Dec 23 - jedy.wang@sun.com
- Use default ld.
* Wed Dec 23 2009 - jedy.wang@sun.com
- Moves ldfalgs from evolution.spec.
* Mon Dec 21 2009 - ghee.teo@sun.com
- Remove SUNWgnome-print dependency.
* Fri Sep 11 2009 - jedy.wang@sun.com
- Remove SUNWmlib dependency.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Thu Oct 16 2008 - jeff.cai@sun.com
- Update copyright, add file COPYING.LGPL2.
* Tue Sep 16 2008 - jeff.cai@sun.com
- Add copyright.
* Fri Aug 29 2008 - jeff.cai@sun.com
- Remove bogofilter plugin.
* Wed Jul 23 2008 - jeff.cai@sun.com
- Add apps-evolution-template-placeholders.schemas to %files root and %preun root.
* Fri Jun 05 2008 - damien.carbery@sun.com
- Add apps_evolution_email_custom_header.schemas to %files root and %preun root.
* Wed Apr 02 2008 - jeff.cai@sun.com
- Add copyright file.
* Fri Jan 18 2008 - damien.carbery@sun.com
- Add evolution-backup to %files.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Mon Nov  5 2007 - jeff.cai@sun.com
- Use system ldflag to enable -Bdirect
* Wed Oct 31 2006 - damien.carbery@sun.com
- Put the /usr/gnu references inside '%if %option_with_gnu_iconv' test.
* Wed Oct 31 2006 - damien.carbery@sun.com
- Remove %{_libexecdir}/evolution/%{evolution.major_version}/evolution-backup
  as it is not in the 2.21.1 tarball.
* Mon Oct 22 2006 - damien.carbery@sun.com
- Add %{_libexecdir}/evolution/%{evolution.major_version}/evolution-backup to
  %files for evolution 2.12.1 tarball.
* Wed Oct 10 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Thu Oct  4 2007 - laca@sun.com
- add %arch_ldadd to LDFLAGS so that the GNU libiconv flags are used
- delete -I %{_includedir} from CFLAGS -- breaks the indiana build because
  the wrong iconv.h is picked up; otherwise it's useless; add /usr/gnu stuff
  instead
* Tue Aug 28 2007 - damien.carbery@sun.com
- Add a new schemas files to %files and remove version number from another.
* Wed Jul 11 2007 - damien.carbery@sun.com
- Add a new schemas file to %files.
* Wed Jun 06 2007 - damien.carbery@sun.com
- Add new schema file and remove Evolution version number from muliple files.
* Tue May 15 2007 - damien.carbery@sun.com
- Add %{_datadir}/icons/hicolor/48x48 dir to %files for new tarball.
* Thu May 10 2007 - damien.carbery@sun.com
- Add bogo-junk-plugin-2.12.schemas to %files.
* Thu Apr 26 2007 - laca@sun.com
- set PERL to /usr/perl5/bin/perl
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Fri Mar 16 2007 - damien.carbery@sun.com
- Correct code that removes l10n files.
* Wed Mar 14 2007 - damien.carbery@sun.com
- Add en_GB files to l10n package.
* Tue Feb 27 2007 - simon.zheng@sun.com
- Move evolution icons from /usr/share/pixmaps to /usr/share/icons/hicolor 
* Thu Jan 04 2007 - jijun.yu@sun.com
- Its dependencies-gnome-pilot and pilot-link are upgraded to new version
* Tue Dec 12 2006 - damien.carbery@sun.com
- Fix %build_l10n section in %install to remove the files when necessary.
* Wed Dec 06 2006 - damien.carbery@sun.com
- Remove scrollkeeper files during %install. Add l10n files to l10n pkg.
* Wed Nov 29 2006 - damien.carbery@sun.com
- Revert version to %{default_pkg_version} as this module has been integrated
  to Nevada with this version. Using the base module's version number (2.8.x)
  is lower than 2.16.x and will cause an integration error.
* Mon Nov 27 2006 - jeff.cai@sun.com
- Use evolution's version information to replace default one. 
* Mon Oct 23 2006 - irene.huang@sun.com
- Moved all patches to ../patches/
* Fri Oct 20 2006 - damien.carbery@sun.com
- Remove SUNWhalh BuildRequires because header files are in SUNWhea in snv_51.
* Wed Oct 18 2006 - damien.carbery@sun.com
- Use %{evolution.major_version} instead of hard coded version number.
* Tue Oct 17 2006 - Jeff.Cai@sun.com
- Remove patch patches/evolution-03-mail-rlimit.diff
* Mon Sep 18 2006 - Brian.Cameron@sun.com
- Add SUNWhalh BuildRequires.
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Mon Aug 14 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWhal after check-deps.pl run.
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Tue Aug 07 2006 - jeff.cai@sun.com
- add patch evolution-03-mail-rlimit.diff to resolve stoping updating review
  page.
* Tue Jul 25 2006 - jeff.cai@sun.com
- Reorder patches
* Fri Jul 21 2006 - jeff.cai@sun.com
- Bump to 2.7.4
  Remove patch evolution-01-solaris-ldap.diff.
* Thu Jul 20 2006 - irene.huang@sun.com
- remove manpage evolution-addressbook-export.1
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Fri Jun 23 2006 - Christopher.Hanna@sun.com
- Added manpange for evolution-addressbook-export because it
  is still in /usr/bin and so should still have a manpage.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Sun May 28 2006 - irene.huang@sun.com
- Add patch evolution-03-kerberos.diff, add package requirement of
  SUNWkrbu and SUNWgss.
* Fri May 26 2006 - irene.huang@sun.com
- Remove manpanges for evolution-addressbook-export and
  evolution-addressbook-import.
* Thu May 25 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Fri May 12 2006 - damien.carbery@sun.com
- Update dir perms for omf/evolution to correct WOS integration error.
* Fri May 12 2006 - damien.carbery@sun.com
- Small update to dependency list after check-deps.pl run.
* Thu May 11 2006 - halton.huo@sun.com
- Merge -share pkg(s) into the base pkg(s).
* Wed Apr 26 2006 - halton.huo@sun.com
- Use JES's NSS/NSPR(/usr/lib/mps) instead of that provided by
  mozilla or firefox, to fix bug #6418049.
* Tue Apr 04 2006 - halton.huo@sun.com
- Alter remove .a/.la filepkginfo s part into linux spec. 
* Thu Mar 30 2006 - halton.huo@sun.com
- Remove all *.a/*.la files.
* Thu Feb 23 2006 - damien.carbery@sun.com
- Use default pkg version to match other pkgs; add EVO25 to default category.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Mon Jan 23 2006 - Irene.Huang@sun.com
- Move patch evolution-caldav-startup-fail.diff 
  to ../../patches.
* Mon Jan 23 2006 - Irene.Huang@sun.com
- Add patch evolution-caldav-startup-fail.diff.
* Tue Jan 10 2006 - halton.huo@sun.com
- Enable pilot-conduits option.
* Wed Jan 04 2006 - halton.huo@sun.com
- Add all files under plugins.
* Wed Dec 21 2005 - halton.huo@sun.com
- Change major_verion from 2.4 to 2.6.
* Tue Dec  6 2005 - laca@sun.com
- disable -Bdirect as due to symbol clashes
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Fri Oct 21 2005 - halton.huo@sun.com
- Disable gnome_pilot_link.
* Mon Oct 10 2005 - halton.huo@sun.com
- Change build require from mozilla to firefox.
- Move upstreamed patch evolution-02-solaris-kerberos.diff.
- Add patch evolution-02-solaris-sed.diff.
* Thu Sep 15 2005 - halton.huo@sun.com
- Remove define krb5_prefix and related.
- Add patch evolution-02-solaris-kerberos.diff to disable krb5.
- Change changelog more readable.
* Thu Sep  8 2005 - halton.huo@sun.com
- Add krb5_prefix define.
- Add "-L%{krb5_prefix}/lib -R%{krb5_prefix}/lib" to LDFLAGS.
- Add "-I%{krb5_prefix}/include" to CFLAGS.
* Tue Sep  7 2005 - halton.huo@sun.com
- Remove "-L/usr/sfw/lib -R/usr/sfw/lib" from LDFLAGS, remove
  "-I/usr/sfw/include" from CFLAGS and remove LD_LIBRARY_PATH=/usr/sfw/lib,
  because current gnome-pilot-link packages are deployed on /usr not /usr/sfw.
* Tue Sep  6 2005 - halton.huo@sun.com
- Change SUNWevolution package files defination.
- Add patch evolution-01-solaris-ldap.diff
* Wed Aug 31 2005 - halton.huo@sun.com
- Change SUNW_Category for open solaris.
- Remove DB3 since now is included in evolution-data-server.
- Remove obsoleted patch evolution-01-solaris-compile.diff
- Added "-L/usr/sfw/lib -R /usr/sfw/lib" to LDFLAGS to use pilot-link
- Added "-I/usr/sfw/include" to CFLAGS to use pilot-link
- Added "LD_LIBRARY_PATH=/usr/sfw/lib" to pass use pilot-link check
* Tue Jul 19 2005 - damien.carbery@sun.com
- Enable gnome-pilot-link.
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Fri Oct  1 2004 - damien.carbery@sun.com
- Add option to enable/disable gnome-pilot-link.
* Fri Jul 23 2004  laca@sun.com
- use evolution-copyright.txt as copyright notice
* Tue Jul 20 2004 - brian.cameron@sun.com
- Added man pages.
* Tue Jun 29 2004 - shirley.woo@sun.com
- Added "-L%{moz_prefix}/lib/mozilla -R%{moz_prefix}/lib/mozilla" to LDFLAGS
 so mozilla libraries can be found
* Mon Jun 28 2004 - shirley.woo@sun.com
- Changed install location to /usr/... so need to use moz-prefix for nss/nspr
  since install location of mozilla is different for Linux and Solaris
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Tue May 25 2004 - <laca@sun.com>
- add SUNWdtbas dep
* Fri May 14 2004 - <laca@sun.com>
- add idnkit dependencies
* Sun May 02 2004 - <laca@sun.com>
- add the source directory to the end of PKG_CONFIG_PATH so that idnkit.pc
  is picked up from here on Solaris (bad, bad hack...)
* Tue Apr 20 2004 - <laca@sun.com>
- add SUNWgnome-pilot-link dependency
- fix libexec stuff
* Fri Apr 16 2004 - <laca@sun.com>
- remove static libs
* Thu Mar 11 2004 - <laca@sun.com>
- initial version created



