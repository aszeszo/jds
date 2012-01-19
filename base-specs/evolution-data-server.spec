# spec file for package evolution-data-server
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         evolution-data-server
License:      LGPL v2
Group:        System/Libraries/GNOME
Version:      2.30.3
Release:      2
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      Backend Library for Evolution
Source:       http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.30/%{name}-%{version}.tar.bz2
%if %build_l10n
Source1:      l10n-configure.sh
%if %build_l10n
Source2:                 l10n-configure.sh
%endif
%endif
%if %option_with_sun_branding
# date:2009-03-11 owner:jefftsai doo:6752 bugster:6791003 type:bug
Patch1:       evolution-data-server-01-open-address-book-sparc.diff
%endif
# date:2009-10-13 owner:jefftsai bugzilla:593998 bugster:6878377 type:bug
Patch2:       evolution-data-server-02-ldap-search.diff
# date:2009-12-03 owner:jefftsai type:branding bugzilla:410164
Patch3:       evolution-data-server-03-remove-bdb.diff
# date:2009-12-03 owner:jefftsai type:branding
Patch4:       evolution-data-server-04-not-build-test.diff
# date:2009-12-03 owner:jefftsai type:bug bugzilla:603773
Patch5:       evolution-data-server-05-comm-err.diff
# date:2010-01-16 owner:chrisk
Patch7:       evolution-data-server-07-fixxref-modules.diff
# date:2010-01-27 owner:jefftsai type:bug bugzilla:
Patch8:       evolution-data-server-08-groupwise-makefile.diff
# date:2010-01-27 owner:jefftsai type:bug bugzilla:
Patch9:       evolution-data-server-09-socket.diff
# date:2010-01-27 owner:jefftsai type:bug bugster:6910597 bugzilla:608457
Patch10:       evolution-data-server-10-vfolder-count.diff
# date:2010-07-20 owner:jefftsai type:bug doo:16467 bugzilla:624789
Patch11:       evolution-data-server-11-connect-ldap.diff
# date:2010-12-07 owner:jefftsai type:bug bugzilla:6366676 bugster:7003764
Patch12:       evolution-data-server-12-sqlite.diff
# date:2011-05-16 owner:jefftsai type:branding bugster:6639570
Patch13:       evolution-data-server-13-gpg.diff

Docdir:       %{_defaultdocdir}/evolution-data-server
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%define api_version 1.2
%define base_version 1.6

%define libbonobo_version 2.4.2
%define gnome_vfs_version 2.4
%define libgnome_version 2.4
%define GConf_version 2.4
%define libsoup_version 2.2.3
%define gtk_doc_version 1.1
%define openldap2_version 2.1.4

Requires:       libbonobo >= %{libbonobo_version}
Requires:       gnome-vfs >= %{gnome_vfs_version}
Requires:       libgnome >= %{libgnome_version}
Requires:       GConf >= %{GConf_version}
Requires:       libsoup >= %{libsoup_version}
Requires:       openldap2-client >= %{openldap2_version}
Requires:       SUNWtls
Requires:       SUNWpr

BuildRequires:  libbonobo-devel >= %{libbonobo_version}
BuildRequires:  gnome-vfs-devel >= %{gnome_vfs_version}
BuildRequires:  libgnome-devel >= %{libgnome_version}
BuildRequires:  GConf-devel >= %{GConf_version}
BuildRequires:  libsoup-devel >= %{libsoup_version}
BuildRequires:  openldap2-devel >= %{openldap2_version}
BuildRequires:  gtk-doc >= %{gtk_doc_version}
BuildRequires:  bison
BuildRequires:  heimdal-devel
BuildRequires:  SUNWtlsd
BuildRequires:  SUNWprd

%description
evolution-data-server is the backend library for Evolution, providing
support for calendar and addressbook.

%package devel
Summary:      Development Backend Library for Evolution
Group:        Development/Libraries/GNOME
Autoreqprov:  on
Requires:     %name = %version
BuildRequires:  libbonobo-devel >= %{libbonobo_version}
BuildRequires:  gnome-vfs-devel >= %{gnome_vfs_version}
BuildRequires:  libgnome-devel >= %{libgnome_version}
BuildRequires:  GConf-devel >= %{GConf_version}
BuildRequires:  openldap2-devel >= %{openldap2_version}
BuildRequires:  libsoup-devel >= %{libsoup_version}

%description devel
evolution-data-server is the backend library for Evolution, providing
support for calendar and addressbook.

%prep
%setup -q
%if %build_l10n
# bugster 6558756
sh -x %SOURCE1 --disable-gnu-extensions
%endif
%if %option_with_sun_branding
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build

%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%define ldap_option --with-openldap=%{_prefix}
%define krb5_option --with-krb5=%{_prefix}
%else
%define ldap_option --with-sunldap=%{_prefix}
%if %is_s10
%define krb5_option --without-krb5
%else
%define krb5_option --with-krb5=%{_prefix}
%endif
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif

if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

%if %option_with_gnu_iconv
%define iconv_option --with-libiconv=/usr/gnu
%else
%define iconv_option
%endif

aclocal $ACLOCAL_FLAGS -I m4
glib-gettextize --force --copy
intltoolize --force --automake

%if %build_l10n
bash -x %SOURCE2 --enable-copyright
%endif

autoheader
automake -a -f -c --gnu
autoconf
./configure --prefix=%{_prefix}						\
	    --libexecdir=%{_libexecdir}					\
	    --sysconfdir=%{_sysconfdir}					\
	    --enable-nss=yes						\
	    --enable-smime=yes						\
	    --enable-nntp=yes						\
            --enable-largefile                                          \
	    --with-krb4=%{_prefix}					\
            --disable-gnome-keyring					\
	    %ldap_option						\
	    %krb5_option						\
            %gtk_doc_option                                             \
	    %bdb_option                                                 \
            %iconv_option

make -j$CPUS

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make -i install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*
%{_libdir}/evolution-data-server-%{api_version}/extensions/*.so
%{_libdir}/evolution-data-server-%{api_version}/camel-providers/*.so
%{_libdir}/evolution-data-server-%{api_version}/camel-providers/*urls
%{_libdir}/bonobo/servers/*
%{_libexecdir}/*
%{_datadir}/evolution-data-server-%{base_version}/*
%{_datadir}/pixmaps/evolution-data-server-%{base_version}/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%files devel
%defattr (-, root, root)
%{_libdir}/*.so
%{_includedir}/evolution-data-server-%{base_version}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/*
%{_datadir}/idl/*

%changelog
* Mon May 16 2011 - jeff.cai@oracle.com
- Add patch -13-gpg.diff to fix bug 6639570
* Tue Dec 07 2010 - jeff.cai@oracle.com
- Add patch -12-sqlite to fix bugster #7003764, bugzilla #636676.
  This may be a bug of sqlite3 2.7.3, but no test case for it.
  should be removed if sqlite3 could fix this issue.
* Fri Oct 22 2010 - jeff.cai@oracle.com
- Bump to 2.30.3
* Mon Sep 06 2010 - jeff.cai@sun.com
- Add patch -11-connect-ldap to fix doo #16147 and bugzilla #624789
  Use ldapssl_init to replace ldap_set_opt (LDAP_OPT_SSL) since the
  option LDAP_OPT_SSL is not supported in sun ldap.

* Mon Jun 21 2010 - jeff.cai@sun.com
- Bump to 2.30.2
* Mon Apr 26 2010 - christian.kelly@oracle.com
- Bump to 2.30.1.
* Mon Mar 30 2010 - christian.kelly@sun.com
- Bump to 2.30.0.
* Mar 08 2010  - jeff.cai@sun.com
- Bump to 3.29.92
* Feb 23 2010  - jeff.cai@sun.com
- Bump to 2.29.91
- disable the use of gnome keyring temporarily since keyring does not 
  work correctly.
* Feb 08 2010  - jeff.cai@sun.com
- Bump to 2.29.90
* Fri Jan 28 2010 - jeff.cai@sun.com
- Add patch -10-vfolder-count to fix #6910597
  On solaris, because junk plugin is not shipped, the message flags
  is not updated.
* Tue Jan 26 2010 - jeff.cai@sun.com
- Bump to 2.29.6
- Upstream -06-marshal-list
* Sat Jan 16 2010 - christian.kelly@sun.com
- Add evolution-data-server-07-fixxref-modules.diff.
* Thu Jan 14 2010 - jedy.wang@sun.com
- Bump to 2.29.5
* Wed Dec 23 2009 - jedy.wang@sun.com
- Fix bug comments.
- Patch 1 should be protected by option_with_sun_branding.
* Tue Dec 22 2009 - jeff.cai@sun.com
- Bump to 2.29.4.
- Remove patch -04-a11y-crash.diff.
- Remove patch -09-func-macro.diff.
- Remove patch -10-union.diff.
- Reorder the other patches.
* Wed Dec 09 2009 - jeff.cai@sun.com
- Remove patch -01-libexec, since evolution-data-server does not exist
* Tue Dec 08 2009 - jedy.wang@sun.com
- Use new way to figure out cflags and ldflags for nss and nspr.
- Enable gweather and large file support.
- Add SUNWtlsd and SUNWprd dependency.
* Fri Dec 04 2009 - jeff.cai@sun.com
- Bump to 2.29.3
- Add patch -05-remove-bdb
- Add patch -06-not-build-test
- Add patch -07-comm-err
- Add patch -08-marshal-list
- Add patch -09-func-macro
- Add patch -10-union
* Wed Dec 02 2009 - jedy.wang@sun.com
- Add patch 04-a11y-crash.diff.
* Mon Oct 20 2009 - jeff.cai@sun.com
- Bump to 2.28.1
* Wed Oct 13 2009 - jeff.cai@sun.com
- Add patch -03-ldap-search to fix bugster 6878377, bugzilla 593998
* Tue Sep 22 2009 - jeff.cai@sun.com
- Bump to 2.28.0
* Wed Sep 09 2009 - jeff.cai@sun.com
- Bump to 2.27.92
* Mon Aug 24 2009 - jeff.cai@sun.com
- Bump to 2.27.91
* Mon Aug 10 2009 - jeff.cai@sun.com
- Bump to 2.27.90
* Wed Jul 29 2009 - jeff.cai@sun.com
- Bump to 2.27.5
- Upstream path -03-local-start-hang.diff
* Tue Jul 14 2009 - jeff.cai@sun.com
- Bump to 2.27.4
* Fri Jul 10 2009 - jeff.cai@sun.com
- Add patch -03-local-start-hang, fix doo #9913, bugzill #588220
- Add the old patch -02-open-address-book-sparc back removed by christian
* Thu Jul 02 2009 - christian.kelly@sun.com
- Remove references to evolution-data-server-02-open-address-book-sparc.
* Tue Jun 16 2009 - jeff.cai@sun.com
- Bump to 2.27.3
- Remove -03-http-proxy, upstreamed
- Remove -04-nss, upstreamed
* Fir Jun 12 2009 - jeff.cai@sun.com
- Add patch -04-nss to fix #585523
  Since nss/nspr has a private copy of sqlite3, it says a symbol
  is not found if link to libsoftoken3.
* Tue May 26 2009 - jeff.cai@sun.com
- Bump to 2.27.2
- Remove patch -04-http-service, upstreamed
* Wed May 13 2009 - jeff.cai@sun.com
- Change patch comment.
* Tue May 05 2009 - jeff.cai@sun.com
- Add patch -03-http-proxy, fix #579199
  Use http->url->path if no proxy is used.
- Add patch -04-http-service, fix gbo #581420, bugster #6836920
  If service name is 'http' or 'https', use port '80' or '443'
  as the name.
* Thu Apr 16 2009 - jedy.wang@sun.com
- Bump to 2.26.1.1
* Tue Apr 14 2009 - jedy.wang@sun.com
- Bump to 2.26.1
* Tue Mar 16 2009 - jeff.cai@sun.com
- Bump to 2.26.0
- Remove -02-conditional-if and -03-imap-mail, upstreamed.
- Rename -04-open-address-book-sparc to -02-open-address-book-sparc
* Wed Mar 11 2009 - jeff.cai@sun.com
- Not apply the patch -04-open-address-book-sparc on OpenSolaris.
* Wed Mar 11 2009 - zhichao.wang@sun.com
- Add patch -04-open-address-book-sparc to fix d.o.o bug #6752 
  To resolve the address book can not be open on sparc matchine.
  This patch can be removed after BDB is upgraded to 4.8.
* Mon Mar 09 2009 - jeff.cai@sun.com
- Add -03-imap-mail, Fix #574236
* Tue Mar 03 2009 - jeff.cai@sun.com
- Bump to 2.25.92
- Remove -02-view-local-mail, upstreamed
- Add -02-conditional-if, Fix #573870. Use the
  standard conditional if sentence.
* Tue Feb 17 2009 - jeff.cai@sun.com
- Bump to 2.25.91
- Remove patch -03-libical, upstreamed.
* Thu Feb 05 2009 - jedy.wang@sun.com
- Add patch 02-libical.diff to fix bugzilla 569459.
* Wed Feb 04 2009 - jeff.cai@sun.com
- Add patch -02-view-local-mail, This is a tempoary fix.
  Maybe the community can give a better solution.
  Fix bugster 6791021, bugzilla 567008.
* Wed Feb 04 2009 - jeff.cai@sun.com
- Bump to 2.25.90
* Wed Jan 20 2009 - jeff.cai@sun.com
- Bump to 2.25.5
* Wed Jan 07 2009 - jeff.cai@sun.com
- Bump to 2.25.4
* Tue Dec 15 2008 - dave.lin@sun.com
- Bump to 2.25.3
- Remove -02-func, upstreamed.
- Add --without-weather since GWeather is not shipped.
* Wed Dec 03 2008 - dave.lin@sun.com
- Bump to 2.25.2
* Wed Nov 04 2008 - jeff.cai@sun.com
- Bump to 2.25.1
* Fri Oct 31 2008 - jeff.cai@sun.com
- Change the license tag.
* Wed Oct 29 2008 - jeff.cai@sun.com
- Bump to 2.24.1
* Wed Sep 22 2008 - jeff.cai@sun.com
- Bump to 2.24.0
* Wed Sep 09 2008 - jeff.cai@sun.com
- Bump to 2.23.92
- Add patch -02-func.diff
* Wed Sep 02 2008 - jeff.cai@sun.com
- Bump to 2.23.91
- Remove upstream patch -02-local.
* Wed Aug 27 2008 - jeff.cai@sun.com
- Add patch -02-local to fix 213072
* Mon Aug 20 2008 - jeff.cai@sun.com
- Bump to 2.23.90.1
- Remove patch -02-errno and -03-mbox-spool
* Tue Aug 05 2008 - jeff.cai@sun.com
- Roll back to 2.23.6
- Add patch -03-mbox-spool to fix 
  #6732079, #6732076
- Bump to 2.23.6.2
* Tue Aug 05 2008 - jeff.cai@sun.com
- Bump to 2.23.6.2
* Tue Aug 04 2008 - jeff.cai@sun.com
- Bump to 2.23.6
* Tue Jul 29 2008 - jedy.wang@sun.com
- Add patch -05-summary.
* Wed Jul 23 2008 - jeff.cai@sun.com
- Add patch -04-google-backend. Fix 544264
- Remove -04-no-google-backend.
- Remove -02-google-calendar.
- Add -02-gtk-doc. Fix 543855
* Tue Jul 22 2008 - damien.carbery@sun.com
- Bump to 2.23.5. Remove upstream patches 04-attachment and 05-ldap. Add patch
  to work around build failure in google backend (04-no-google-backend).
* Wed Jul 04 2008 - jeff.cai@sun.com
- Add patch -04-attachment.diff. Fix #534080.
* Wed Jul 03 2008 - jeff.cai@sun.com
- Add patch -03-errno.diff. Fix #538074.
* Tue Jun 17 2008 - jeff.cai@sun.com
- Bump to 2.23.4.
* Tue Jun 03 2008 - damien.carbery@sun.com
- Bump to 2.23.3. Remove upstream patch 03-build.
* Thu Jun 02 2008 - jeff.cai@sun.com
- Bump 2.23.2, add patch -03-build.diff. 
* Thu May 29 2008 - damien.carbery@sun.com
- Revert to 2.22.2 because of build error. Module owner notified.
* Wed May 28 2008 - damien.carbery@sun.com
- Bump to 2.23.2.
* Tue May 27 2008 - jeff.cai@sun.com
- Bump to 2.22.2
* Fri May 01 2008 - damien.carbery@sun.com
- Bump to 2.22.1.1.
* Mon Apr 23 2008 - jedy.wang@sun.com
- Bump to 2.22.1. Remove upstream patch 02-libical.diff.
  Add 02-google-calendar.diff. Fix 527544.
* Mon Mar 10 2008 - damien.carbery@sun.com
- Bump to 2.22.0.
* Tue Feb 26 2008 - damien.carbery@sun.com
- Bump to 2.21.92. Remove upstream patch 03-decode.
* Wed Feb 20 2008 - jeff.cai@sun.com
- Remove -02-camel-message.diff. Community has fixed
  in 513389.
* Mon Feb 18 2008 - jeff.cai@sun.com
- Add -03-decode.diff, Fix 517190
* Fri Feb 15 2008 - jeff.cai@sun.com
- Add -02-camel-message.diff, Fix 516598
* Wed Feb 13 2008 - damien.carbery@sun.com
- Bump to 2.21.91.
* Tue Jan 29 2008 - damien.carbery@sun.com
- Bump to 2.21.90.
* Fri Jan 18 2008 - damien.carbery@sun.com
- Bump to 2.21.5.1.
* Thu Jan 17 2008 - damien.carbery@sun.com
- Bump to 2.21.5.
* Tue Dec 18 2007 - damien.carbery@sun.com
- Bump to 2.21.4.
* Tue Dec 04 2007 - damien.carbery@sun.com
- Bump to 2.21.3.
* Tue Nov 13 2007 - damien.carbery@sun.com
- Bump to 2.21.2.
* Tue Oct 30 2007 - damien.carbery@sun.com
- Bump to 2.21.1. Remove upstream patch, 02-function.
* Fri Oct 19 2007 - damien.carbery@sun.com
- Bump to 1.12.1. Add patch 02-function to fix bugzilla 488173.
* Wed Oct  3 2007 - laca@sun.com
- use the --with-libiconv=/usr/gnu option when building with GNU libiconv
* Tue Sep 18 2007 - damien.carbery@sun.com
- Bump to 1.12.0.
* Mon Sep 03 2007 - damien.carbery@sun.com
- Bump to 1.11.92.
* Mon Aug 27 2007 - damien.carbery@sun.com
- Bump to 1.11.91. Remove upstream patches 02-endian and 03-timezone.
* Fri Aug 17 2007 - jedy.wang@sun.com
- Fix 'patch* -p0' - change to -p1 and change patch file too.
* Thu Aug 16 2007 - jedy.wang@sun.com
- Remove the commands to autotoolize libical.
* Wed Aug 15 2007 - damien.carbery@sun.com
- Bump to 1.11.90.
* Tue Aug 15 2007 - jedy.wang@sun.com
- Update patch 02-endian.diff and 03-timezone.diff
* Tue Aug 07 2007 - jeff.cai@sun.com
- Add patch 03-timezone.diff to use zone_sun.tab instead 
  of zone.tab. Fix #464252
* Wed Aug 01 2007 - damien.carbery@sun.com
- Bump to 1.11.6.1. Add patch 02-endian to fix build errors, #462499.
* Tue Jul 31 2007 - damien.carbery@sun.com
- Bump to 1.11.6.
* Tue Jul 10 2007 - damien.carbery@sun.com
- Bump to 1.11.5.
* Mon Jun 18 2007 - damien.carbery@sun.com
- Bump to 1.11.4. Remove upstream patch, 01-kerberos.
* Wed Jun 13 2007 - takao.fujiwara@sun.com
- Add l10n-configure.sh to remove GNU extension from de.po, et.po, hu.po,
  it.po and ja.po
* Wed Jun 06 2007 - damien.carbery@sun.com
- Bump to 1.11.3.
* Tue May 15 2007 - damien.carbery@sun.com
- Bump to 1.11.2.
* Thu May 10 2007 - damien.carbery@sun.com
- Bump to 1.11.1.
* Thu Apr 12 2007 - damien.carbery@sun.com
- Bump to 1.10.1. Remove upstream patch 03-libbdb.
* Wed Apr 04 2007 - simon.zheng@sun.com
- Add patch evolution-data-server-03-libbdb.diff, 
  to fix bugster bug #6538754.
* Tue Mar 13 2007 - simon.zheng@sun.com
- Bump to 1.10.0.
* Tue Feb 28 2007 - simon.zheng@sun.com
- Bump to 1.9.92.
* Mon Feb 12 2007 - damien.carbery@sun.com
- Bump to 1.9.91. Remove upstream patch, 03-mail-header.
* Fri Feb 09 2007 - jeff.cai@sun.com
- Add patch, 03-mail-header, to fix #400841.
* Sun Jan 28 2007 - laca@sun.com
- disable krb5 support on s10
* Wed Jan 24 2007 - damien.carbery@sun.com
- Bump to 1.9.6.1. Remove upstream patch, 03-gnome-keyring.
* Tue Jan 23 2007 - damien.carbery@sun.com
- Add patch, 03-gnome-keyring, to fix build error, #399706.
* Mon Jan 22 2007 - damien.carbery@sun.com
- Bump to 1.9.6.
* Tue Jan 09 2007 - jeff.cai@sun.com
- Bump to 1.9.5.
- Remove build patch for bug 387397.
* Wed Dec 20 2006 - jeff.cai@sun.com
- Add bugzilla bug number for patch 3.
* Tue Dec 19 2006 - jeff.cai@sun.com
- Add patch evolution-data-server-03-exchange-account.diff
  to resolve building broken on Solaris.
* Tue Dec 19 2006 - jeff.cai@sun.com
- Bump to 1.9.4.
* Wed Dec 13 2006 - jeff.cai@sun.com
- Change patch comments.
* Tue Dec 05 2006 - damien.carbery@sun.com
- Bump to 1.9.3.
* Tue Nov 28 2006 - jeff.cai@sun.com
- Bump to 1.9.2 and remove patch:
  evolution-data-server-03-mail-rlimit.diff
* Mon Nov 27 2006 - damien.carbery@sun.com
- Bump to 1.8.2.
* Fri Nov  3 2006 - laca@sun.com
- use %gtk_doc_option in configure so that it can be disabled using
  --without-gtk-doc
* Mon Nov 04 2006 - irene.huang@sun.com
- Change owner to be opensolaris account.
* Mon Oct 23 2006 - irene.huang@sun.com
- moved evolution-data-server-01-kerberos.diff
  and evolution-data-server-02-libexec.diff and 
  evolution-data-server-03-mail-rlimit.diff from
  Solaris/patches
* Mon Oct 02 2006 - damien.carbery@sun.com
- Bump to 1.8.1.
* Mon Sep 04 2006 - damien.carbery@sun.com
- Bump to 1.8.0.
- Remove upstream patch, 01-attachment.
* Tue Aug 21 2006 - jedy.wang@sun.com
- Add one patch, 01-attachment.diff, for 6461581.
* Tue Aug 08 2006 - damien.carbery@sun.com
- Bump to 1.7.91.
* Wed Jul 26 2006 - halton.huo@sun.com
- Use system BerkeleyDB.
* Wed Jul 26 2006 - jeff.cai@sun.com
- Bump to 1.7.90.1
  Remove patches/evolution-data-server-01-libebook-files.diff.
* Tue Jul 25 2006 - damien.carbery@sun.com
- Add patch to include files missing from tarball (but in cvs).
* Mon Jul 24 2006 - damien.carbery@sun.com
- Bump to 1.7.90
* Fri Jul 21 2006 - jeff.cai@sun.com
- Bump to 1.7.4
* Tue May 30 2006 - halton.huo@sun.com
- Bump to 1.6.2.
* Wed Apr 26 2006 - halton.huo@sun.com
- Use JES's NSS/NSPR(/usr/lib/mps) instead of that provided by
  mozilla or firefox, to fix bug #6418049.
* Thu Apr 13 2006 - halton.huo@sun.com
- Firefox move from /usr/sfw to /usr.
* Mon Apr 10 2006 - damien.carbery@sun.com
- Bump to 1.6.1.
* Tue Apr 04 2006 - halton.huo@sun.com
- Remove .a/.la files in linux spec.
* Thu Mar 30 2006 - halton.huo@sun.com
- Alter "remove *.a/*.la files part" to SUNWevolution-data-server.spec
* Mon Mar 13 2006 - damien.carbery@sun.com
- Bump to 1.6.0.
* Tue Feb 28 2006 - halton.huo@sun.com
- Bump to 1.5.92.
* Tue Feb 14 2006 - damien.carbery@sun.com
- Bump to 1.5.91.
* Mon Jan 30 2006 - damien.carbery@sun.com
- Bump to 1.5.90.
* Thu Jan 19 2006 - halton.huo@sun.com
- Bump to 1.5.5.
* Wed Jan 04 2006 - halton.huo@sun.com
- Bump to 1.5.4.
* Wed Dec 21 2005 - halton.huo@sun.com
- Correct Source filed.
- Remove upstreamed patch evolution-data-server-6341837.diff.
- Remove upstreamed patch evolution-data-server-6359639.diff.
* Fri Dec 19 2005 - damien.carbery@sun.com
- Bump to 1.5.3.
- Bump to 1.4.2.1.
* Fri Dec 09 2005 - dave.lin@sun.com
- Add the patch evolution-data-server-6359639.diff
* Fri Dec 02 2005 - dave.lin@sun.com
- Bump to 1.4.2.1.
- Add the patch evolution-data-server-6341837.diff
* Thu Dec 01 2005 - damien.carbery@sun.com
- Remove upstream patch, patches/evolution-data-server-01-6340601.diff.
* Tue Nov 29 2005 - damien.carbery@sun.com
- Bump to 1.4.2.
* Wed Nov 23 2005 - halton.huo@sun.com
- Add patch evolution-data-server-01-6340601.diff.
* Fri Oct 21 2005 - halton.huo@sun.com
- Use firefox nss/nspr lib instead of mozilla's.
* Wed Oct 12 2005 - halton.huo@sun.com
- change --with-ldap to --with-sunldap.
* Tue Oct 11 2005 - damien.carbery@sun.com
- Bump to 1.4.1.1.
* Mon Oct 10 2005 - halton.huo@sun.com
- Bump to 1.4.1.
- Move obsolete patches:
  evolution-data-server-01-libgobject.diff,
  evolution-data-server-02-pretty_function.diff.
- Move upstreamed patches:
  evolution-data-server-03-lock-helper.diff.
* Thu Sep 15 2005 - halton.huo@sun.com
- Add define krb5_option, disable Kerberos 5 on Solaris.
* Thu Sep 8 2005 - halton.huo@sun.com
- Add krb5_prefix define and enable Kerberos 5.
- Fix CFLAGS problem.
* Wed Sep 7 2005 - halton.huo@sun.com
- Bump to 1.4.0.
* Tue Sep 6 2005 - damien.carbery@sun.com
- Call configure instead of autogen.sh because autogen.sh not in 1.3.8 tarball.
  Remove some ver nums from %files because there is no consistency.
  Remove patch3 and reorder.
* Tue Sep  6 2005 - halton.huo@sun.com
- Move patch evolution-data-server-04-ldap-ssl.diff and Source1 
  evolution-data-server-ldap-ssl-patch.tar to SUNWgnutls.spec.
* Fri Sep 2 2005 - halton.huo@sun.com
- Add option --enable-nntp=yes to support news groups.
- Use SUN LDAP on solaris with %ldap_option.
- Add Source1 Patch4 to support SUN LDAP
- Use ./autogen.sh to replace libtoolize aclocal automake autoconf ./configure 
  steps, because we need build code that checked out from community HEAD.
- Temporarily disable Kerberos for header files are not installed on Nevada.
* Tue Aug 30 2005 - damien.carbery@sun.com
- Redefine major_version to 1.2 so that %files section can use while patch 03 
  redefines it to 1.2.
* Tue Aug 30 2005 - glynn.foster@sun.com
- Bump to 1.3.8
* Mon Aug 15 2005 - damien.carbery@sun.com
- Bump to 1.3.7.
* Thu Jul 28 2005 - damien.carbery@sun.com
- Rename --with-openldap configure option to --with-ldap as a result of Jerry's
  patch from Jul 27. Also remove '%ifos' code around this option.
* Wed Jul 27 2005 - damien.carbery@sun.com
- Add patch from Jerry Pu (Shi.Pu@sun.com) to support LDAP on Solaris.
* Thu Jul 14 2005 - damien.carbery@sun.com
- Add 5 patches to build on Solaris.
* Wed Jun 15 2005 - matt.keenan@sun.com
- Bump to 1.2.3
* Tue May 10 2005 - glynn.foster@sun.com
- Bump to 1.2.2
* Tue Nov 23 2004 - glynn.foster@sun.com
- Bump to 1.0.2
* Thu Jun 17 2004 - niall.power@sun.com
- rpm4´ified
* Thu Jun 17 2004 - glynn.foster@sun.com
- Bump to 0.0.94.1
* Tue Jun 08 2004 - glynn.foster@sun.com
- Bump to 0.0.94
* Fri May 21 2004 - glynn.foster@sun.com
- Bump to 0.0.93
* Tue Apr 20 2004 - glynn.foster@sun.com
- Bump to 0.0.92
* Mon Apr 19 2004 - glynn.foster@sun.com
- Initial spec file for evolution-data-server 0.0.91
