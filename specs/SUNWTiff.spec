#
# spec file for package SUNWTiff
#
# includes module(s): tiff
#
# Copyright (c) 2004, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc

%define OSR 12272:3.8.1

%define _prefix /usr

%define tarball_version 3.9.5

Name:                    SUNWTiff
IPS_package_name:        image/library/libtiff
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 libtiff - library for reading and writing TIFF
Version:                 %{tarball_version}
License:                 bsd-like/libtiff
Source:                  http://download.osgeo.org/libtiff/tiff-%{tarball_version}.tar.gz
Source1:                 %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_prefix}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
# date:2012-04-19 owner:padraig type:bug bugster:7158160
Patch1: tiff-01-CVE-2012-1173.diff

%include default-depend.inc
%include desktop-incorporation.inc
Requires: system/library/math
Requires: library/zlib
BuildRequires: image/library/libjpeg

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}

%prep
%setup -c -n %name-%version
cd tiff-%{tarball_version}
%patch1 -p0
gzcat %SOURCE1 | tar -xf -

%ifarch amd64 sparcv9
cd ..
cp -pr tiff-%{tarball_version} tiff-%{tarball_version}-64
%endif

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="%_ldflags"

cd tiff-%{tarball_version}

%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

./configure \
	--prefix=%{_prefix} \
	--libexecdir=%{_libexecdir} \
	--disable-cxx
make -j$CPUS

%ifarch amd64 sparcv9
cd ../tiff-%{tarball_version}-64
export CFLAGS="%optflags64"
./configure \
	--prefix=%{_prefix} \
	--libexecdir=%{_libexecdir}/%{_arch64} \
	--libdir=%{_libdir}/%{_arch64} \
	--disable-cxx
make -j$CPUS
%endif

%install
%ifarch amd64 sparcv9
cd tiff-%{tarball_version}-64
make install DESTDIR=$RPM_BUILD_ROOT
if test -d sun-manpages; then
	cd sun-manpages
	make install DESTDIR=$RPM_BUILD_ROOT
	cd ..
fi
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/lib*a
cd ..
%endif

cd tiff-%{tarball_version}
make install DESTDIR=$RPM_BUILD_ROOT
if test -d sun-manpages; then
	cd sun-manpages
	make install DESTDIR=$RPM_BUILD_ROOT
	cd ..
fi

chmod 0755 $RPM_BUILD_ROOT%{_mandir}/man3tiff
chmod 0755 $RPM_BUILD_ROOT%{_mandir}/man1
chmod 0755 $RPM_BUILD_ROOT%{_mandir}/man3
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libtiff.so.3

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_prefix}/man

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%attr (0755, root, bin) %{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*
%dir %attr(0755, root, bin) %{_mandir}/man3tiff
%{_mandir}/man3tiff/*

%changelog
* Thu May 10 2012 - abhijit.nath@oracle.com
- Added patch tiff-01-CVE-2012-1173.
* Thu Mar 17 2011 - abhijit.nath@oracle.com
- Added patch tiff-01-CVE-2011-0192.diff & tiff-01-CVE-2011-1167.diff to fix security vulnerability CVE-2011-0192 & CVE-2011-1167. 
* Thu Jul 29 2010 - laszlo.peter@oracle.com
- update to 2.9.4, delete upstream patches
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu Aug 27 2009 - abhijit.nath@sun.com
- Fixes CR #6875065
* Mon Aug 17 2009 - abhijit.nath@sun.com
- Fixes CR #6872336
* Tue Jul 14 2009 - abhijit.nath@sun.com
- add patch libtiff-04-CVE-2009-2347.diff to fix bug CR6858149
* Tue Jun 02 2009 - dave.lin@sun.com
- add 'Requires: SUNWjpg' to fix bug CR6842550
* Thu Sep  4 2008 - john.fischer@sun.com
- add patch CVE-2008-2327.diff
* Mon Mar 24 2008 - laca@sun.com
- add copyright file
* Thu Apr 26 2007 - laca@sun.com
- add SUNWman dependency, fixes 6511213
* Wed Mar 15 2007 - dougs@truemail.co.th
- Removed adding ccdir to PATH
* Wed Nov 22 2006 - laca@sun.com
- add patches ormandy.diff and CVE-2006-2193.diff, fixes 6451119
* Fri Sep 01 2006 - matt.keenan@sun.com
- Add new man page tarball
* Fri Jul 28 2006 - laca@sun.com
- bump to 3.8.2
* Tue May 09 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Thu Apr 06 2006 - brian.cameron@sun.com
- Now use tarball_version.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Mon Dec 19 2005 - damien.carbery@sun.com
- Bump to 3.7.4.
* Thu Sep 22 2005 - laca@sun.com
- make install the 64-bit bits first so the executables in %{_bindir}
  get overwritten by the 32-bit ones and not the other way around.
* Fri Sep 02 2005 - laca@sun.com
- remove unpackaged files
* Tue Apr 26 2004 - laca@sun.com
- updated to version 3.7.2, fixes CR6203747
* Fri Oct 29 2004 - laca@sun.com
- use $CC64 as the 64-bit C compiler, if defined
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Sat Oct  2 2004 - Joseph.Townsend@Sun.COM
- Create 64bit libraries for Solaris
* Sun Sep 12 2004 - laca@sun.com
- Added %defattr for devel-share pkg
* Fri Sep 10 2004 - shirley.woo@sun.com
- Added Requires: SUNWTiff for devel and devel-share packages
* Mon Aug 30 2004 - shirley.woo@sun.com
- Bug 5091588 : include files and sman3 files should be in a separate devel
  package
* Wed Aug 18 2004 - damien.carbery@sun.com
- Update libtiff.so.3 perms for Solaris integration.
* Tue Aug 17 2004 - shirley.woo@sun.com
- Another Update mandir perms for Solaris integration.
* Tue Aug 17 2004 - damien.carbery@sun.com
- Update mandir perms for Solaris integration.
* Tue Aug 17 2004 - laca@sun.com
- update mandir permissions for Solaris integration
* Fri Aug 13 2004 - damien.carbery@sun.com
- Create symlinks to *.ent in ../entities. Fixes 5085622.
* Thu Aug 12 2004 - shirley.woo@sun.com
- Updated Version to be 2.6.0 since delivering w/ G2.6
* Thu Aug 12 2004 - damien.carbery@sun.com
- Add symlinks to ../entities/*.ent in the sman3tiff dir. Fixes 5085622.
* Sun Feb 23 2004 - Laszlo.Peter@sun.com
- initial version added to CVS


