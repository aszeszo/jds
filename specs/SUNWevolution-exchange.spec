#
# spec file for package SUNWevolution-exchange
#
# includes module(s): exchange-connector
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jedy
#
%include Solaris.inc
%use evolution = evolution.spec
%use evoexchange = evolution-exchange.spec
%define evo_prefix /usr/lib/evolution

Name:          SUNWevolution-exchange
License: GPL v2, LGPL v2.1, FDL v1.1
IPS_package_name: mail/evolution/connector/evolution-exchange
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       Exchange connector for Evolution
Version:       %{evoexchange.version}
SUNW_Category: EVO25,%{default_category}
SUNW_Copyright: %{name}.copyright
SUNW_BaseDir:  %{_basedir}
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Source1:       %{name}-manpages-0.1.tar.gz
Requires:       library/desktop/libgnomecanvas
Requires:       mail/evolution
Requires:       gnome/config/gconf
Requires:       library/gnome/gnome-libs
Requires:       library/desktop/evolution-data-server
Requires:       library/desktop/gtkhtml
Requires:       library/libsoup
Requires:       library/gnome/gnome-component
Requires:       library/gnome/gnome-vfs
Requires:       gnome/gnome-panel
Requires:       library/gnutls
Requires:       system/library/security/libgcrypt
Requires:       library/security/libgpg-error
Requires:       system/library/math
Requires:       library/popt
Requires:       library/libxml2
Requires:       library/zlib
Requires:       service/gnome/desktop-cache
Requires:       library/libunique
#BuildRequires:       library/security/nss
BuildRequires: system/library/mozilla-nss/header-nss
BuildRequires:       library/desktop/libgnomecanvas
BuildRequires:       library/desktop/evolution-data-server
BuildRequires:       library/desktop/gtkhtml
BuildRequires:       library/libsoup
BuildRequires:       library/gnome/gnome-component
BuildRequires:       library/gnome/gnome-vfs
BuildRequires:       library/gnutls
BuildRequires:       system/library/security/libgcrypt
BuildRequires:       library/security/libgpg-error
BuildRequires:       library/popt
BuildRequires:       gnome/config/gconf
BuildRequires:       library/gnome/gnome-libs
BuildRequires:       mail/evolution
BuildRequires:       library/libunique

%package root
Summary:       %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc
Requires:       gnome/config/gconf

%package l10n
Summary:	%{summary} - l10n files
Requires:	%{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%evoexchange.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
export LDFLAGS="%_ldflags -L%{_libdir} -R%{_libdir} -L%{evo_prefix}/%{evolution.major_version} -R%{evo_prefix}/%{evolution.major_version}"
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export PKG_CONFIG_PATH="%_pkg_config_path"
%evoexchange.build -d %name-%version

%install
%evoexchange.install -d %name-%version
mv $RPM_BUILD_ROOT%{_bindir}/exchange-connector-setup-%{evolution.major_version} $RPM_BUILD_ROOT%{_bindir}/exchange-connector-setup

# Delete gtk-doc files before packagine.
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc

cd %{_builddir}/%name-%version/sun-manpages
rm -rf $RPM_BUILD_ROOT%{_mandir}
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%files
%doc -d evolution-exchange-%{evoexchange.version} AUTHORS
%doc(bzip2) -d evolution-exchange-%{evoexchange.version} ChangeLog
%doc(bzip2) -d evolution-exchange-%{evoexchange.version} COPYING
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/evolution
%{_libdir}/evolution-data-server-*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/evolution-exchange
%{_datadir}/evolution/%{evolution.major_version}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/apps_exchange_addressbook-*.schemas

%changelog
* Mon Dec 21 2009 - ghee.teo@sun.com
- Remove SUNWgnome-print dependency.
* Wed Dec 09 2009 - jedy.wang@sun.com
- Update to fix build problem.
* Fri Sep 11 2009 - jedy.wang@sun.com
- Remove SUNWmlib dependency.
* Wed Sep 09 2009 - dave.lin@sun.com
- Add dependency 'Requires: SUNWgnome-panel'.
* Thu Jun 18 2009 - jedy.wang@sun.com
- Update 2.26 to 2.28.
_ Fix build problem.
* Tue Jun 16 2009 - christian.kelly@sun.com
- Minor build/pkg'ing issue.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Fri Sep 19 2008 - christian.kelly@sun.com
- Set permissions on /usr/share/doc.
* Wed Sep 16 2008 - jedy.wang@sun.com
- Add new copyright files.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Fri Oct  5 2007 - laca@sun.com
- add %{arch_ldadd} to LDFLAGS for GNU libiconv/libintl
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Wed Dec 13 2006 - jedy.wang@sun.com
- Replace evo_major_version with major_version in evolution.spec.
- Ship schema.
* Wed Nov 29 2006 - damien.carbery@sun.com
- Revert version to %{default_pkg_version} as this module has been integrated
  to Nevada with this version. Using the base module's version number (2.8.x)
  is lower than 2.16.x and will cause an integration error.
- Bump evo_major_version to 2.10 to match SUNWevolution.
- Remove unnecessary 'cd' calls in %prep.
* Tue Nov 28 2006 - jeff.cai@sun.com
- use evoexchange to refer to the spec file.
* Mon Nov 27 2006 - jeff.cai@sun.com
- Use evolution-exchange's version information to replace default one. 
* Mon Oct 23 2006 - irene.huang@sun.com
- Moved all patches to ../patches/
* Fri Sep 01 2006 - matt.keenan@sun.com
- Add new man page tarball
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Tue Jul 25 2006 - Jeff.Cai@sun.com
- Reorder patches.
* Mon Jun 24 2006 - Jeff.Cai@sun.com
- Bump to trunk 2.7.4
  Remove patch evolution-exchange-01-ldap.diff.
- Updated patch evolution-exchange-01-ldap.diff.
* Sun Jun 22 2006 - Simon.zheng@sun.com
- Updated patch evolution-exchange-01-ldap.diff.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu Jun 8 2006 - Jeff.Cai@sun.com
- Add man page exchange-connector-setup.1
* Thu Jun 1 2006 - Irene.Huang@sun.com
- Change renaming of ximian-connector-setup to renaming
  of exchange-connector-setup in %install section. 
* Wed May 31 2006 - damien.carbery@sun.com
- When moving ximian-connector-setup-2.6 use %{tarball} instead of '*'.
- Revmove references to gtk-doc dir from %files as files no longer installed.
* Thu May 11 2006 - halton.huo@sun.com
- Change %defattr to (-, root, other).
* Thu Apr 27 2006 - halton.huo@sun.com
- Move ximian-connector-setup-2.6 to ximian-connector-setup, 
  ARC request: no version binnaries under /usr/bin
* Thu Apr 06 2006 - brian.cameron@sun.com
- Now use tarball_version.
* Tue Apr 04 2006 - halton.huo@sun.com
- Alter remove .a/.la files part into linux spec. 
* Thu Mar 30 2006 - halton.huo@sun.com
- Remove all *.a/*.la files.
* Thu Feb 23 2006 - damien.carbery@sun.com
- Use default pkg version to match other pkgs; add EVO25 to default category.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Jan 06 2006 - simon.zheng@sun.com
- Remove Solaris/patches/evolution-exchange-02-ldap-addfiles.diff
* Wed Dec 21 2005 - halton.huo@sun.com
- Change evo_major_version from 2.4 to 2.6.
- Remove evolution-exchange-03-solaris-kerberos.diff and reorder.
* Wed Dec  7 2005 - laca@sun.com
- disable -Bdirect as due to symbol clashes
* Wed Nov 09 2005 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-print as required by evolution-exchange.
* Tue Nov 08 2005 - halton.huo@sun.com
- Add /usr/lib/evolution/2.4 to LDFLAGS, fix bug #6347334.
* Mon Oct 10 2005 - halton.huo@sun.com
- Moved define moz_prefix.
- Moved "-L%{moz_prefix}/lib/mozilla -R%{moz_prefix}/lib/mozilla" from LDFLAGS.
* Thu Sep 15 2005 - halton.huo@sun.com
- Added define moz_prefix.
- Added "-L%{moz_prefix}/lib/mozilla -R%{moz_prefix}/lib/mozilla" to LDFLAGS
  so mozilla libraries can be found.
- Added patch evolution-exchange-01-ldap.diff, evolution-exchange-02-ldap-addfiles.diff
  for SUN LDAP.
- Added patch evolution-exchange-03-solaris-kerberos.diff to disable krb5.
- Added patch evolution-exchange-04-solaris-eutil.diff to fix -leutil not found problem.
- Change %files section.
- Change changelog more readable.
* Wed Aug 31 2005 - halton.huo@sun.com
- Change SUNW_Category for open solaris
* Wed Aug 31 2005 - damien.carbery@sun.com
- Use evolution-exchange instead of ximian-connector.
* Thu Jul 14 2005 - damien.carbery@sun.com
- Use ximian-connector instead of oxygen2. %files changes will be needed.
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Sep 13 2004 - dave.lin@sun.com
- change the component name from SUNWevolution-xchg-connect to SUNWevolution-exchange per Michelle Lei
* Tue Sep 07 2004 - laca@sun.com
- change copyright to ximian
* Sun Jun 27 2004  shirley.woo@sun.com
- Changed install location to /usr/...
- Added -root package for /etc files
* Wed Jun 16 2004 - laca@sun.com
- rename back to SUNWevolution-xchg-connect
* Fri Jun 11 2004 - damien.carbery@sun.com
- Set perms on _sysconfdir to correct a conflict.



