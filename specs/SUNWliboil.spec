#
# spec file for package SUNWliboil
#
# includes module(s): liboil
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use liboil64 = liboil.spec
%endif

%include base.inc
%use liboil = liboil.spec

Name:                    SUNWliboil
IPS_package_name:        library/liboil
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 Library of Optimized Inner Loops
Version:                 %{liboil.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{liboil.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlibms
BuildRequires: data/sgml-common
BuildRequires: data/xml-common
BuildRequires: data/docbook/docbook-dtds
BuildRequires: data/docbook/docbook-style-xsl

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%liboil64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%liboil.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
# Note that liboil uses MMX/SSE/SSE2/etc. code which does not run properly
# with Sun Studio unless you build with -xO#.  This means if you build with
# debug, then expect programs which use some liboil functions to crash.
#
%ifarch amd64 sparcv9
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="$FLAG64"
export PKG_CONFIG_PATH="%{_pkg_config_path64}"
%liboil64.build -d %name-%version/%_arch64
%endif

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH="%{_pkg_config_path}"
%liboil.build -d %name-%version/%{base_arch}

%install

%ifarch amd64 sparcv9
%liboil64.install -d %name-%version/%_arch64
%endif

%liboil.install -d %name-%version/%{base_arch}

#Clean up unpackaged files
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/oil-bugreport
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr(0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/oil-bugreport
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%doc %{base_arch}/liboil-%{liboil.version}/AUTHORS
%doc %{base_arch}/liboil-%{liboil.version}/README
%doc(bzip2) %{base_arch}/liboil-%{liboil.version}/COPYING
%doc(bzip2) %{base_arch}/liboil-%{liboil.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/*
%{_mandir}/man3/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%dir %attr (0755, root, sys) %{_datadir}
%{_includedir}/*
%{_datadir}/gtk-doc/html/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%changelog
* Fri Jan 08 2009 - brian.cameron@sun.com
- Fix Summary.
* Mon Sep 15 2008 - christian.kelly@sun.com
- Remove /usr/share/doc from %files.
* Thu Mar 27 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Mon Mar 19 2007 - dougs@truemail.co.th
- Fixed -fno-omit-frame-pointer flag
* Thu Mar 15 2007 - damien.carbery@sun.com
- Add Requires SUNWgccruntime after check-deps.pl run.
* Mon Feb 12 2007 - brian.cameron@sun.com
- Fix building with gcc based on Laca's comments.
* Wed Jan 31 2007 - brian.cameron@sun.com
- Build with gcc so that on x86 we compile hardware acceleration GCC asm code.
* Wed Jun 14 2007 - brian.cameron@sun.com
- Add new bindir files included in 0.3.9.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu May 11 2006 - damien.carbery@sun.com
- Change build dependency on SUNWgnome-base-libs-share. That pkg is obsolete
  with files now in the base package.
* Thu Mar 23 2006 - shirley.woo@sun.com
- Updated Package Summary
* Fri Mar 17 2006 - shirley.woo@sun.com
- Updated Package Summary
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Wed Oct 26 2005 - brian.cameron@sun.com
- Created.


