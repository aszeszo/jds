#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
# bugdb: savannah.gnu.org
#

%define OSR 11423:3.0

Name:     	libtasn1
Version: 	2.8
Release:        0
Vendor:		gnu.org
Distribution:	Java Desktop System
License:	Library is LGPLv2.1, binaries are GPLv3
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Docdir:         %{_datadir}/doc
Autoreqprov:	on
URL:		http://josefsson.org/libtasn1/
Epoch:		2
#Source:		ftp://ftp.gnutls.org/pub/gnutls/libtasn1/%{name}-%{version}.tar.gz
Source:		http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz


Summary:	Libtasn is a library C for manipulating ASN.1 objects.

# date:2011-09-02 owner:qc161282 bugster:7085293 type:bug
Patch1:       libtasn1-01-buffer-overflow.diff
# date:2011-04-06 owner:qc161282 bugster:7159416 type:bug
Patch2:       libtasn1-02-cve-2012-1569.diff

%description
Libtasn is a library written in C for manipulating ASN.1 objects including 
DER/BER encoding and DER/BER decoding. Libtasn is used by GnuTLS to manipulate X.509 objects and by GNU Shishi to handle Kerberos V5 packets.
%package -n libtasn1-devel
Summary:	Static libraries and header files for libtasn1
Group:		Applications/Text
Requires:	libtasn1 => %{version}-%{release}


%description -n libtasn1-devel
The libtasn1-devel package includes the static libraries and header 
files needed for tasn1 development.

%files -n libtasn1-devel
%defattr(-, root, root)
%{_libdir}/*.so*
%{_includedir}/*

%prep
%setup  -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1

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

./configure --prefix=%{_prefix}                        \
            --bindir=%{_bindir}                        \
            --libdir=%{_libdir}                        \
            --sysconfdir=%{_sysconfdir}                \
            --includedir=%{_includedir}        \
            --mandir=%{_mandir}                        \
           --infodir=%{_infodir}               \
           --disable-rpath                     \
           --disable-static                    \
           --enable-shared



make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT mkdir_p="mkdir -p"
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Apr 06 2012 - jeff.cai@oracle.com
- Add patch -02-cve-2012-1569
* Fri Sep 02 2011 - jeff.cai@oracle.com
- Add patch -01-buffer-overflow to fix security bug #7085293 and #7093667.
* Thu Oct 28 2010 - jeff.cai@oracle.com
- Bump to 2.8.
* Wed Jun 02 2010 - brian.cameron@oracle.com
- Bump to 2.7.
* Fri May 14 2010 - jeff.cai@sun.com
- Bump to 2.6.
- Upstream patch -01-build
* Tue Mar 17 2010 - jeff.cai@sun.com
- Bump to 2.5.
* Tue Jan 17 2010 - jeff.cai@sun.com
- Bump to 2.4.
* Tue Jan 12 2010 - jeff.cai@sun.com
- Change OSR which contains GPLv3.
* Sat Aug 15 2009 - christian.kelly@sun.com
- Bump to 2.3.
* Tue Jul 28 2009 - christian.kelly@sun.com
- Bump to 2.2.
* Mon Jan 19 2008 - jeff.cai@sun.com
- Bump to 1.8.
- Remove patch -01-asn1-deprecated, upstreamed.
* Fri Dec 26 2008 - jeff.cai@sun.com
- Change the bug db address
* Thu Nov 13 2008 - jeff.cai@sun.com
- Bump to 1.6.
- Add patch -01-asn1-deprecated to
  fix #106548.
* Fri Oct 31 2008 - jeff.cai@sun.com
- Change the license tag.
* Tue Jun 17 2008 - jeff.cai@sun.com
- change it according to review result.
* Mon Jun 16 2008 - jeff.cai@sun.com
- change url.
* Mon Jun 16 2008 - jeff.cai@sun.com
- Move spec files from SFE.
* Tue Mar 28 2007 - jeff.cai@sun.com
- Split to two spec files.
