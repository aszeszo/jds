#
# spec file for package SUNWogg-vorbis.spec
#
# includes module(s): libogg, libvorbis
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use libogg64 = libogg.spec
%use libvorbis64 = libvorbis.spec
%endif

%include base.inc
%use libogg = libogg.spec
%use libvorbis = libvorbis.spec

Name:                    SUNWogg-vorbis
IPS_package_name:        codec/ogg-vorbis
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 Ogg bitstream and Vorbis audio codec libraries
Version:                 %{default_pkg_version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 Xiph.org BSD-style
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

Requires: system/library/math
BuildRequires: developer/gnome/gettext
BuildRequires: developer/parser/bison
BuildRequires: runtime/python-26

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
%libogg64.prep -d %name-%version/%_arch64
%libvorbis64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%libogg.prep -d %name-%version/%{base_arch}
%libvorbis.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%ifarch amd64 sparcv9
export PKG_CONFIG_PATH="/usr/lib/%{_arch64}/pkgconfig:%{_pkg_config_path}"
%libogg64.build -d %name-%version/%_arch64

export PKG_CONFIG_PATH="%{_builddir}/%name-%version/%{_arch64}/libogg-%{libogg.version}:/usr/lib/%{_arch64}/pkgconfig:%{_pkg_config_path}"
%libvorbis64.build -d %name-%version/%_arch64
unset PKG_CONFIG_PATH
%endif

export PKG_CONFIG_PATH="%{_pkg_config_path}"
%libogg.build -d %name-%version/%{base_arch}
export PKG_CONFIG_PATH=%{_builddir}/%name-%version/%{base_arch}/libogg-%{libogg.version}:%{_pkg_config_path}
%libvorbis.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libogg64.install -d %name-%version/%_arch64
%libvorbis64.install -d %name-%version/%_arch64
%endif

%libogg.install -d %name-%version/%{base_arch}
%libvorbis.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a
%ifarch amd64 sparcv9
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/lib*a
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
%dir %attr (0755, root, sys) %{_datadir}
%doc %{base_arch}/libogg-%{libogg.version}/AUTHORS
%doc %{base_arch}/libogg-%{libogg.version}/README
%doc(bzip2) %{base_arch}/libogg-%{libogg.version}/COPYING
%doc(bzip2) %{base_arch}/libogg-%{libogg.version}/CHANGES
%doc %{base_arch}/libvorbis-%{libvorbis.version}/AUTHORS
%doc %{base_arch}/libvorbis-%{libvorbis.version}/README
%doc(bzip2) %{base_arch}/libvorbis-%{libvorbis.version}/COPYING
%doc(bzip2) %{base_arch}/libvorbis-%{libvorbis.version}/CHANGES
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%changelog
* Wed Feb 08 2012 - brian.cameron@oracle.com
- Update Requires/BuildRequires.
* Tue Jan 05 2010 - dave.lin@sun.com
- Changed the dependency from CBEbison to SUNWbison.
* Wed Sep 17 2008 - christian.kelly@sun.com
- Fix up pkg'ing section.
* Mon Sep 15 2008 - christian.kelly@sun.com
- Remove /usr/share/doc from %files.
* Fri Sep 12 2008 - brian.cameron@sun.com
- Add new copyright files.
* Wed May 07 2008 - damien.carbery@sun.com
- Remove PERL5LIB setting as it is not necessary.
* Mon May 05 2008 - brian.cameron@sun.com
- Port amd64 building from SFEogg-vorbis.spec
* Wed Apr 02 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Mon Sep 12 2005 - laca@sun.com
- remove unpackaged files
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Thu Sep 09 2004 - matt.keenan@sun.com
- Added libogg.3, libvorbis.3 manpages
* Sat Jun 26 2004 - shirley.woo@sun.com
- changed install location to /usr/lib and /usr/bin
* Fri Jun 04 - brian.cameron@sun.com
- Initial spec-file created


