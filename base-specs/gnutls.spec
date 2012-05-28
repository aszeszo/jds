#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
# bugdb: savannah.gnu.org
#

%define OSR 11108:2.0

Name:     	gnutls
License:	LGPL v2.1
Version: 	2.8.6
Release:        1
Vendor:		gnu.org
Distribution:	Java Desktop System
Copyright:	LGPL/GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Docdir:         %{_datadir}/doc
Autoreqprov:    on
URL:		http://www.gnutls.org
#Source: 	ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.bz2
Source: 	http://ftp.heanet.ie/mirrors/ftp.gnupg.org/gcrypt/gnutls/%{name}-%{version}.tar.bz2
%if %build_l10n
Source1: 	l10n-configure.sh
%endif

# date:2009-05-31 owner:jefftsai type:branding 
Patch1:       gnutls-01-not-build-example.diff
# date:2012-04-06 owner:jefftsai type:bug bugster:7159444
Patch2:       gnutls-02-cve-2012-1573.diff
# date:2012-04-06 owner:jefftsai type:bug bugster:7159416
Patch3:       gnutls-03-cve-2011-4128.diff

%define glib2_version 2.0
%define libgcrypt_version 1.1.12
BuildRequires:	glibc-devel
BuildRequires:	libtool
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	libgcrypt >= %{libgcrypt_version}
Summary:	The GnuTLS implements the proposed standards by the IETF's TLS working group (RFC2246, TLS 1.0).
Group:		System Environment/Libraries
Requires:	libgcrypt >= %{libgcrypt_version}
Requires:	glib2 >= %{glib2_version}

%description
    GnuTLS is a project that aims to develop a library which provides a
    secure layer, over a reliable transport layer. Currently the GnuTLS
    library implements the proposed standards by the IETF's TLS working
    group (RFC2246, TLS 1.0).

%package -n gnutls-devel
Summary:	The GnuTLS implements the proposed standards by the IETF's TLS working group (RFC2246, TLS 1.0).
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= %{glib2_version}
Requires:       libgcrypt >= %{libgcrypt_version}

%description -n gnutls-devel
    GnuTLS is a project that aims to develop a library which provides a
    secure layer, over a reliable transport layer. Currently the GnuTLS
    library implements the proposed standards by the IETF's TLS working
    group (RFC2246, TLS 1.0).

%prep
%setup  -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags"

%if %build_l10n
sh %SOURCE1 --enable-copyright
%endif

./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --bindir=%{_bindir} \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --infodir=%{_datadir}/info \
    --localstatedir=%{_localstatedir} \
    --enable-guile=no \
	--disable-camellia

make -j $CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%files
%defattr(-, root, root)
%doc lib/COPYING ChangeLog AUTHORS INSTALL NEWS README
%{_libdir}/lib*.so.*

%files -n gnutls-devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_includedir}/*

%changelog
* Fri Apr 06 2012 - jeff.cai@oracle.com
- Add patch -02-cve-2012-1573 and -03-cve-2011-4128
* Tue Mar 17 2010 - jeff.cai@sun.com
- Bump to 2.8.6
* Thu Nov 05 2009 - jeff.cai@sun.com
- Bump to 2.8.5
* Tue Oct 13 2009 - jeff.cai@sun.com
- Change osr to 11108 since currently we don't use 9490
* Fri Sep 18 2009 - jeff.cai@sun.com
- Bump to 2.8.4
* Web Aug 14 2009 - jeff.cai@sun.com
- Bump to 2.8.3
* Web Aug 11 2009 - jeff.cai@sun.com
- Bump to 2.8.2
* Fri Jun 12 2009 - jeff.cai@sun.com
- Bump to 2.8.1
* Mon Jun 01 2009 - jeff.cai@sun.com
- Ship lib/COPYING
* Mon May 31 2009 - jeff.cai@sun.com
- Bump to 2.8.0
- Add path -01-not-build-example to disable building of example 
* Mon May 04 2009 - jeff.cai@sun.com
- Bump to 2.6.6
* Fri Apr 17 2009 - halton.huo@sun.com
- Bump to 2.6.5
* Thu Feb 12 2008 - jeff.cai@sun.com
- Bump to 2.6.4
- Remove patch -01-return-void, upstreamed
* Mon Feb 02 2008 - jeff.cai@sun.com
- Bump to 2.6.3
* Fri Dec 26 2008 - jeff.cai@sun.com
- Change the bug db.
* Thu Nov 13 2008 - jeff.cai@sun.com
- Bump to 2.6.2
- Add patch -01-return-void to fix
  #106549
* Fri Oct 31 2008 - jeff.cai@sun.com
- Change the license tag.
* Mon Jul 31 2008 - jeff.cai@sun.com
- Use the libtasn1 in the system
* Mon Jun 16 2008 - jeff.cai@sun.com
- Bump to 2.2.5.
* Thu Jun 12 2008 - jeff.cai@sun.com
- Add an option to disable guile
* Thu Jun 06 2008 - jeff.cai@sun.com
- Bump to 2.2.4.
* Thu Jan 31 2008 - jeff.cai@sun.com
- Remove patches for 2.2
* Wed Jan 30 2008 - jeff.cai@sun.com
- Currently the security team will take over ownership of GnuTLS. Therefore
  rollback to 1.6.3 and stop upgrading.
* Wed Nov 28 2007 - jeff.cai@sun.com
- Bump to 2.0.4
- Add patch -02-ext-authz.diff. Fix build error #106103
* Tue Nov 06 2007 - jeff.cai@sun.com
- Back to 1.6.3
* Mon Nov 05 2007 - jeff.cai@sun.com
- Rename patch file name.
* Mon Nov 05 2007 - jeff.cai@sun.com
- Bump to 2.0.1
- Add patch -02-inline.
* Tue Jul 03 2007 - jeff.cai@sun.com
- Bump to 1.6.3
* Tue Mar 27 2007 - laca@sun.com
- clean up
* Tue Jan 16 2007 - jedy.wang@sun.com
- Bump to 1.6.1.
* Thu Apr 20 2006 - halton.huo@sun.com
- Bump to 1.2.10.
* Tue Apr 04 2006 - halton.huo@sun.com
- Remove .a/.la files part in linux spec. 
* Thu Mar 30 2006 - halton.huo@sun.com
- Alter "remove *.a/*.la files part" to SUNWgnutls.spec
* Thu Dec 22 2005 - damien.carbery@sun.com
- Bump to 1.2.9.
* Wed Oct 26 2005 - halton.huo@sun.com
- undelete files under /usr/bin to enable SSL in libsoup.
* Mon Oct 10 2005 - halton.huo@sun.com
- Bump to 1.2.8.
* Tue Sep 6 2005 - halton.huo@sun.com
- Bump to 1.2.6.
- Fix Source error.
* Wed Aug 31 2005 - halton.huo@sun.com
- Correct URL and Source
- Change Version to 1.1.23 (<1.0.0), or evolution2.x SSL will be disabled.
- Change Distribution to Java Desktop System
- Remove obsoleted patch gnutls-01-forte-build.diff
* Tue Sep 21 2004 - ghee.teo@sun.com
- moved spec file from spec-files to spec-files/Solaris/extra-specs.
  The patch also moved from spec-files/patches to spec-files/Solaris/patches
  Now Solaris and Linux uses different version of gnutls.
* Sun Aug 29 2004 - laca@sun.com
- remove unpackaged files
* Wed Jul 07 2004 - dermot.mccluskey@sun.com
- added "-j $CPUS" to make to speed up builds
