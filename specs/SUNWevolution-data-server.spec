#
# spec file for package SUNWevolution-data-server
#
# includes module(s): evolution-data-server
#
# Copyright 2007 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc
%use eds = evolution-data-server.spec

Name:          SUNWevolution-data-server
License: LGPL v2
IPS_package_name: library/desktop/evolution-data-server
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       Backend library for Evolution
Version:       %{eds.version}
SUNW_Category: EVO25,%{default_category}
SUNW_BaseDir:  %{_basedir}
SUNW_Copyright:%{name}.copyright
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Source2:       %{name}-manpages-0.1.tar.gz
Requires:      library/desktop/libglade
Requires:      library/gnome/gnome-libs
Requires:      library/gnome/gnome-component
Requires:      library/desktop/gtkhtml
Requires:      library/libsoup
Requires:      library/popt
Requires:      library/zlib
Requires:      library/security/libgpg-error
Requires:      gnome/config/gconf
Requires:      library/gnome/gnome-vfs
Requires:      library/gnutls
Requires:      system/library/security/libgcrypt
Requires:      system/library/math
Requires:      library/libxml2
Requires:      service/security/kerberos-5
Requires:      system/library/security/gss
Requires:      database/sqlite-3
Requires:      library/libical
BuildRequires: database/berkeleydb-5
BuildRequires: library/desktop/libglade
BuildRequires: library/gnutls
BuildRequires: system/library/security/libgcrypt
BuildRequires: library/security/libgpg-error
BuildRequires: library/gnome/gnome-libs
BuildRequires: library/gnome/gnome-component
BuildRequires: gnome/config/gconf
BUildRequires: library/gnome/gnome-vfs
BuildRequires: library/desktop/gtkhtml
BuildRequires: library/libsoup
BuildRequires: library/popt
BuildRequires: system/header
BuildRequires: database/sqlite-3
BuildRequires: library/libical
BuildRequires: library/desktop/libgweather
BuildRequires: developer/gperf
BuildRequires: system/library/iconv/utf-8
BuildRequires: system/library/iconv/unicode
BuildRequires: library/gnome/gnome-component
BuildRequires: library/gnome/gnome-keyring
BuildRequires: data/sgml-common
#XXX BuildRequires: library/security/nss
BuildRequires: system/library/mozilla-nss/header-nss
BuildRequires: library/nspr

%package devel
Summary:       %{summary} - development files
SUNW_BaseDir:  %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%eds.prep -d %name-%version
# Apply patch for SUN LDAP
cd %{_builddir}/%name-%version/evolution-data-server-%{eds.version}
cd ..
# Expand manpages tarball
cd %{_builddir}/%name-%version
gzcat %SOURCE2 | tar xf -

%build
export LDFLAGS="%_ldflags -L%{_libdir} -R%{_libdir} -R`pkg-config --variable=libdir nss` -R`pkg-config --variable=libdir nspr`"
export CFLAGS="%optflags -D__EXTENSIONS__"
export RPM_OPT_FLAGS="$CFLAGS"
export PKG_CONFIG_PATH="%{_pkg_config_path}"

%if %option_with_sun_branding
%define bdb_option --with-libdb=%{_basedir}
%else
%define bdb_option
%endif

%eds.build -d %name-%version

%install
%eds.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc(bzip2) -d evolution-data-server-%{eds.version} ChangeLog
%doc(bzip2) -d evolution-data-server-%{eds.version} COPYING
%doc(bzip2) -d evolution-data-server-%{eds.version} NEWS 
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/camel-index-control-*
%{_libdir}/camel-lock-helper-*
%{_libdir}/e-addressbook-factory
%{_libdir}/e-calendar-factory
%{_libdir}/evolution-data-server-*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr (0755, root, bin) %{_datadir}/dbus-1
%dir %attr (0755, root, bin) %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/*
%{_datadir}/evolution-data-server-*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Mar 20 2012 - jeff.cai@oracle.com
- Change to ips package names
* Thu Dec 02 2010 - jeff.cai@oracle.com
- Add BuildRequires data/docbook
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Mon Mar 08 2010 - jeff.cai@sun.com
- Add build dependency on SUNWgnu-gperf since IMAPx uses it
* Fri Jan 15 2009 - jeff.cai@sun.com
- Add dependency on SUNWprod which contains nspr
* Wed Dec 23 - jedy.wang@sun.com
- Use default ld.
* Thu Dec 10 2009 - christian.kelly@sun.com
- Add dependency on SUNWlibgweather.
* Fri Sep 11 2009 - jedy.wang@sun.com
- Remove SUNWmlib dependency.
* Web Jul 22 2009 - jeff.cai@sun.com
- Replace with-bdb with option_with_sun_branding
  Fix #10176
* Wed Feb 04 2009 - jeff.cai@sun.com
- Add the dependency on SUNWlibical
* Tue Sep 16 2008 - jeff.cai@sun.com
- Add copyright.
* Wed Jul 23 2008 - jeff.cai@sun.com
- Add dependency of SUNWsqlite3
* Wed Apr 02 2008 - jeff.cai@sun.com
- Add copyright file.
* Thu Dec 20 2007 - halton.huo@sun.com
- Fix build problem when %support_level is not supported. Only set
  bdb_option and depend on SUNWbdb and SUNWevolution-bdb-devel when 
  %support_level is supported.
* Mon Nov 05 2007 - jeff.cai@sun.com
- Use system ldflag to enable -BDirect 
* Fri Sep 28 2007 - laca@sun.com
- delete -I%{_includedir} from CFLAGS -- it's redundant but breaks the
  indiana build; add %{?arch_ldadd} to LDFLAGS for iconv LDFLAGS
* Wed Nov 29 2006 - damien.carbery@sun.com
- Revert version to %{default_pkg_version} as this module has been integrated
  to Nevada with this version. Using the base module's version number (2.8.x)
  is lower than 2.16.x and will cause an integration error.
* Tue Nov 28 2006 - jeff.cai@sun.com
- Use eds to refer to the spec file.
- Use evolution-data-server's version information to replace 
* Mon Nov 27 2006 - jeff.cai@sun.com
- Use evolution-data-server's version information to replace 
  default one. 
* Mon Oct 23 2006 - irene.huang@sun.com
- Moved all patches to ../patches
* Fri Oct 20 2006 - damien.carbery@sun.com
- Add code to expand manpage tarball, otherwise build breaks.
* Thu Oct 19 2006 - irene.huang@sun.com
- add manpages
* Tue Oct 17 2006 - jeff.cai@sun.com
- add patch evolution-data-server-03-mail-rlimit.diff to fix bug 348888
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Thu Jul 27 2006 - halton.huo@sun.com
- Correct with_bdb_devel depend on SUNWbdb, not SUNWevolution-bdb-devel
* Wed Jul 26 2006 - halton.huo@sun.com
- Add SUNWbdb Requires and SUNWevolution-bdb-devel BuildRequires to use
  system BerkeleyDB.
* Tue Jul 25 2006 - jeff.cai@sun.com
- Reorder patches.
* Fri Jul 20 2006 - jeff.cai@sun.com
- Bump to 1.7.4
  Remove patch evolution-data-server-01-ldap-ssl.diff.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Tue May 30 2006 - Irene.Huang@sun.com
- Remove '-I%{_includedir}/kerberosv5' from CFLAGS as this has been
  defined in evolution-data-server/configure.in
* Mon May 29 2006 - damien.carbery@sun.com
- Add '-I%{_includedir}/kerberosv5' to CFLAGS to find headers.
* Sun May 28 2006 - irene.huang@sun.com
- Add patch evolution-data-server-02-kerberos.diff, add package requirement of
  SUNWkrbu and SUNWgss.
* Fri May 12 2006 - damien.carbery@sun.com
- Small update to dependency list after check-deps.pl run.
* Thu May 11 2006 - halton.huo@sun.com
- Change %defattr to (-, root, other).
* Thu May 04 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Wed Apr 26 2006 - halton.huo@sun.com
- Use JES's NSS/NSPR(/usr/lib/mps) instead of that provided by
  mozilla or firefox, to fix bug #6418049.
* Thu Apr 13 2006 - halton.huo@sun.com
- Use firefox_prefix defination in linux spec.
* Tue Apr 04 2006 - halton.huo@sun.com
- Alter remove .a/.la files part into linux spec.
* Thu Mar 30 2006 - halton.huo@sun.com
- Remove all *.a/*.la files.
* Thu Feb 23 2006 - damien.carbery@sun.com
- Use default pkg version to match other pkgs; add EVO25 to default category.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Further update of Build/Requires after running check-deps.pl script.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Jan 6 2006 - simon.zheng@sun.com
- Update patch evolution-data-server-01-ldap-ssl.diff
- Remove patch evolution-data-server-02-ldap-ssl-addfiles.diff
* Tue Dec  6 2005 - laca@sun.com
- disable -Bdirect as due to symbol clashes
* Fri Oct 21 2005 - halton.huo@sun.com
- evolution-data-server-03-libexec.diff: Fix bug #6334159.
- Add firefox dependence, add firefox lib to LDFLAGS, add firefox include to CFLAGS.
* Mon Oct 10 2005 - halton.huo@sun.com
- Move upstreamed patch evolution-data-server-03-solaris-kerberos.diff.
* Thu Sep 15 2005 - halton.huo@sun.com
- Change Source1 evolution-data-server-ldap-ssl-patch.tar 
  to Patch2 evolution-data-server-02-ldap-ssl-addfiles.diff,
  and re-order patch.
- Remove define krb5_prefix and related.
- Add patch evolution-data-server-03-solaris-kerberos.diff
  to disable krb5.
* Thu Sep  8 2005 - halton.huo@sun.com
- Add krb5_prefix define.
- Add "-L%{krb5_prefix}/lib -R%{krb5_prefix}/lib" to LDFLAGS.
- Add "-I%{krb5_prefix}/include" to CFLAGS.
- Use /bin/tar to extract Source1.
- Replace version number to * in %files section to avoid
  version update error.
* Tue Sep 6 2006 - halton.huo@sun.com
- Add patch evolution-data-server-01-ldap-ssl.diff and Source1
  evolution-data-server-ldap-ssl-patch.tar to support SUN LDAP.
* Wed Aug 31 2005 - halton.huo@sun.com
- Change SUNW_Category for open solaris.
* Mon Jul 18 2005 - damien.carbery@sun.com
- Add SUNWevolution-libs-devel (libsoup) dependency.
- Fix %files sections.
* Thu Jul 14 2005 - laca@sun.com
- add missing dependencies
* Thu Jul 14 2005 - damien.carbery@sun.com
- Initial version created



