#
# spec file for package SUNWpng
#
# includes module(s): libpng
#
# Copyright (c) 2007, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc

%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use png10_64 = libpng10.spec
%use png12_64 = libpng12.spec
%use png14_64 = libpng14.spec
%endif

%include base.inc
%use png10 = libpng10.spec
%use png12 = libpng12.spec
%use png14 = libpng14.spec

Name:                    SUNWpng
IPS_package_name:        image/library/libpng
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 Portable Network Graphics library
Version:                 %{png14.version}
License:                 libpng
Source1:                 %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_prefix}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires: library/zlib
Requires: system/library/math

%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: system/core-os

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%png10_64.prep -d %name-%version/%_arch64
%png12_64.prep -d %name-%version/%_arch64
%png14_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%png10.prep -d %name-%version/%base_arch
%png12.prep -d %name-%version/%base_arch
%png14.prep -d %name-%version/%base_arch

cd %name-%version
gzcat %SOURCE1 | tar xf -

%build
%ifarch amd64 sparcv9
%png10_64.build -d %name-%version/%_arch64
%png12_64.build -d %name-%version/%_arch64
%png14_64.build -d %name-%version/%_arch64
%endif

%png10.build -d %name-%version/%base_arch
%png12.build -d %name-%version/%base_arch
%png14.build -d %name-%version/%base_arch

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
# install png12 1st so that the versionless symlinks point to png12 and
# not png10
%png10_64.install -d %name-%version/%_arch64
%png12_64.install -d %name-%version/%_arch64
%png14_64.install -d %name-%version/%_arch64
%endif

%png10.install -d %name-%version/%base_arch
%png12.install -d %name-%version/%base_arch
%png14.install -d %name-%version/%base_arch

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_bindir}
rm libpng-config
ln -s libpng14-config libpng-config

cd $RPM_BUILD_ROOT%{_includedir}
ln -s libpng14 libpng
rm png.h pngconf.h
ln -s libpng14/png.h .
ln -s libpng14/pngconf.h .

cd $RPM_BUILD_ROOT%{_libdir}
rm libpng.so
ln -s libpng14.so libpng.so

%ifarch amd64 sparcv9
cd $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
rm libpng-config
ln -s libpng14-config libpng-config
cd $RPM_BUILD_ROOT%{_libdir}/%{_arch64}
rm libpng.so
ln -s libpng14.so libpng.so
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/libpng14-config
%{_bindir}/libpng12-config
%{_bindir}/libpng10-config
%{_bindir}/libpng-config
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/libpng
%{_includedir}/libpng10
%{_includedir}/libpng12
%{_includedir}/libpng14
%{_includedir}/*.h
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/*
%endif
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%dir %attr(0755, root, bin) %{_mandir}/man4
%{_mandir}/man3/*
%{_mandir}/man4/*

%changelog
* Tue May 01 2010 - padraig.obriain@oracle.com
- Change SVR4 package names to IPS package names.
* Wed Jul 21 2010 - laszlo.peter@oracle.com
- add libpng 1.4.x
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Wed Oct 10 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri May 18 2007 - laca@sun.com
- convert to new style multi-isa build while upgrading to 1.0.26/1.2.18
* Wed Mar 14 2007 - dougs@truemail.co.th
- Removed adding ccdir to PATH + changed // to /
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Sat Jun 10 2006 - laca@sun.com
- move .pc and libpng*-config files to -devel
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Thu Apr 06 2006 - brian.cameron@sun.com
- Now use tarball_version instead of png12_version.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Dec 23 2005 - muktha.narayan@wipro.com
- Redo the libpng-1.0.18-01-makefile.diff and libpng-1.2.8-01-makefile.diff 
  patches. Remove patches libpng-1.0.18-02-security.diff and 
  libpng-1.2.8-02-security.diff which are upstream.
* Mon Dec 19 2005 - damien.carbery@sun.com
- Bump to 1.0.18rc5 and 1.2.8.
* Fri Sep 02 2005 - laca@sun.com
- remove unpackaged files
* Fri Oct 29 2004 - laca@sun.com
- use $CC64 as the 64-bit C compiler, if defined
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Sat Oct  2 2004 - Joseph.Townsend@Sun.COM
- Create 64bit libraries for Solaris
* Mon Aug 30 2004 - shirley.woo@sun.com
- Bug 5091588 : include files and man3/4 files  should be in a separate devel
  packages
* Tue Aug 17 2004 - muktha.narayan@wipro.com
- Added patches libpng-1.0.15-02-security.diff and 
  libpng-1.2.5-02-security.diff to fix security issues.
* Thu Aug 12 2004 - shirley.woo@sun.com
- Updated Version to be 2.6.0 since delivering w/ G2.6
* Fri Apr 16 2004 - laca@sun.com
- add prefix=%_prefix arg to fix .pc file problem
* Sun Feb 22 2004 - Laszlo.Peter@sun.com
- initial version added to CVS


