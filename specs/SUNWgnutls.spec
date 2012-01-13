#
# spec file for package SUNWgnutls
#
# includes module(s): gnutls
#
# Copyright (c) 2004 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use gnutls64 = gnutls.spec
%endif

%include base.inc
%use gnutls = gnutls.spec

Name:          SUNWgnutls
License: 	LGPL v2.1
IPS_package_name: library/gnutls
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:       GNU transport layer security library
Version:       %{gnutls.version}
SUNW_BaseDir:  %{_basedir}
SUNW_Copyright:%{name}.copyright
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:      SUNWzlibr
Requires:      SUNWlibgcrypt
Requires:      SUNWzlib
Requires:      SUNWlibC
BuildRequires: SUNWlibtasn1
BuildRequires: SUNWlibtasn1-devel

Source1:    %{name}-manpages-0.1.tar.gz

%package devel
%include default-depend.inc
%include desktop-incorporation.inc
Summary:       %{summary} - development files
SUNW_BaseDir:  %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnutls

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%ifarch amd64 sparcv9
mkdir -p %name-%version/%_arch64
%gnutls64.prep -d %name-%version/%_arch64
%endif

mkdir -p %name-%version/%base_arch
%gnutls.prep -d %name-%version/%base_arch

# Expand manpages tarball
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif

%ifarch amd64 sparcv9
%gnutls64.build -d %name-%version/%_arch64
%endif

%gnutls.build -d %name-%version/%base_arch

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%gnutls64.install -d %name-%version/%_arch64
rm -r $RPM_BUILD_ROOT%{_bindir}/%_arch64/
rm  $RPM_BUILD_ROOT%{_libdir}/%_arch64/libgnutls-extra*
rm  $RPM_BUILD_ROOT%{_libdir}/%_arch64/libgnutls-openssl*
rm  $RPM_BUILD_ROOT%{_libdir}/%_arch64/pkgconfig/gnutls-extra.pc
rm  $RPM_BUILD_ROOT%{_includedir}/gnutls/openssl.h
rm  $RPM_BUILD_ROOT%{_includedir}/gnutls/extra.h
%endif

%gnutls.install -d %name-%version/%base_arch
rm -rf $RPM_BUILD_ROOT%{_datadir}/man
rm -rf $RPM_BUILD_ROOT%{_datadir}/info
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm  $RPM_BUILD_ROOT%{_libdir}/libgnutls-extra*
rm  $RPM_BUILD_ROOT%{_libdir}/libgnutls-openssl*
rm  $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gnutls-extra.pc
rm  $RPM_BUILD_ROOT%{_includedir}/gnutls/extra.h
rm  $RPM_BUILD_ROOT%{_includedir}/gnutls/openssl.h

%ifarch amd64 sparcv9
cd $RPM_BUILD_ROOT%{_libdir}/%_arch64
%endif
cd $RPM_BUILD_ROOT%{_libdir}/

cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files

%doc -d %{base_arch}/gnutls-%{gnutls.version} AUTHORS README
%doc(bzip2) -d  %{base_arch}/gnutls-%{gnutls.version} ChangeLog
%doc(bzip2) -d  %{base_arch}/gnutls-%{gnutls.version} lib/COPYING
%doc(bzip2) -d  %{base_arch}/gnutls-%{gnutls.version} NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/lib*.so*
%endif

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch sparcv9 amd64
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Set Sep 26 2009 - dave.lin@sun.com
- Remove %{_data_dir}/man/man1 from %files section.
* Fir Aug 20 2009 - jeff.cai@sun.com
- Remove the temporary softlink libgnutls.so.13 
* Mon Jun 01 2009 - jeff.cai@sun.com
- Since COPYING.lib is moved to lib/COPYING, change the
  spec to ship it.
* Sun May 31 2009 - jeff.cai@sun.com
- Changed some files based on 2.8.
* Thu Oct 15 2008 - jeff.cai@sun.com
- Remove the temporary softlink libgnutls.so.13 
* Wed Sep 16 2008 - jeff.cai@sun.com
- Add copyright.
* Thu Jul 31 2008 - jeff.cai@sun.com
- Add man pages.
- Add dependency on libtasn1
* Wed Jul 23 2008 - damien.carbery@sun.com
- Remove %option_with_gnu_iconv around %files l10n to match the package
  definition.
* Tue Jul 08 2008 - jeff.cai@sun.com
- Add a temporary softlink libgnutls.so.13 
  Will be removed after snv_101.
* Mon Jun 30 2008 - jeff.cai@sun.com
- Ship /usr/bin/libgnutls-config
* Thu Jun 12 2008 - jeff.cai@sun.com
- Fix attr error.
* Thu Jun 12 2008 - jeff.cai@sun.com
- Don't ship files that under GPLv3 which include some command tools and
  header files.
* Thu Apr 26 2007 - laca@sun.com
- set CXX to $CXX -norunpath because libtool swallows this option sometimes
  and leaves compiler paths in the binaries
* Thu Apr 05 2007 - damien.carbery@sun.com
- Remove code in %install that creates the libgnutls.so.12 symlink. The symlink
  was added as a workaround for 6519334 and is no longer needed. Removing the
  symlink fixes 6521160, a reminder bug to remove the symlink.
* Tue Mar 27 2007 - laca@sun.com
- enable 64-bit build
* Mon Feb  5 2007 - damien.carbery@sun.com
- Add Requires SUNWlibC after check-deps.pl run.
* Tue Jan 16 2007 - jedy.wang@sun.com
- Do not ship psktool right now.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu May 11 2006 - halton.huo@sun.com
- Change %defattr to (-, root, other).
* Thu May 04 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue Apr 04 2006 - halton.huo@sun.com
- Alter remove .a/.la files part into linux spec. 
* Thu Mar 30 2006 - halton.huo@sun.com
- Remove all *.a/*.la files.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Wed Oct 26 2005 - <halton.huo@sun.com>
- ship files under /usr/bin to enable SSL in libsoup.
* Fri Sep 09 2005 - <laca@sun.com>
- remove unpackaged files or add to %files
* Wed Aug 31 2005 - halton.huo@sun.com
- Change SUNW_Category for open solaris
* Thu Jul 07 2005 - laca@sun.com
- define devel-share subpkg
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Tue Aug 31 2004 - shirley.woo@sun.com
- Bug 5091588 : include files should be in a separate devel package
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Thu Mar 11 2004 - <laca@sun.com>
- initial version created



