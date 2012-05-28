#
# spec file for package SUNWlibtheora
#
# includes module(s): libtheora 
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libtheora_64 = libtheora.spec
%endif

%include base.inc
%use libtheora = libtheora.spec

Name:                    SUNWlibtheora
License:                 Xiph.org BSD-style, LGPL v2.1
IPS_package_name:        codec/libtheora
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 Theora video compression codec
Version:                 %{libtheora.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Autoreqprov: on

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: developer/gnome/gettext
BuildRequires: codec/ogg-vorbis
Requires: codec/ogg-vorbis

%package devel
Summary:      %{summary} - development files
SUNW_BaseDir: %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libtheora_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%libtheora.prep -d %name-%version/%base_arch

cd %{_builddir}/%name-%version*
gzcat %SOURCE0 | tar xf -

%build
export ACLOCAL_FLAGS="-I /usr/share/aclocal"

%ifarch amd64 sparcv9
export PKG_CONFIG_LIBDIR=%{_pkg_config_path64}
%libtheora_64.build -d %name-%version/%_arch64
%endif

export PKG_CONFIG_LIBDIR=%{_pkg_config_path}
%libtheora.build -d %name-%version/%base_arch

%install
%ifarch amd64 sparcv9
%libtheora_64.install -d %name-%version/%_arch64
%endif

%libtheora.install -d %name-%version/%base_arch

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man3/*.3

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/*.so*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%doc -d %{base_arch}/libtheora-%{libtheora.tarball_version} AUTHORS README
%doc(bzip2) -d %{base_arch}/libtheora-%{libtheora.tarball_version} COPYING CHANGES
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*.pc
%endif
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/libtheora-%{libtheora.tarball_version}
%{_datadir}/doc/libtheora-%{libtheora.tarball_version}/*
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%changelog
* Mon Oct 19 2009 - ke.wang@sun.com
- Add 64-bit support.
* Fri Sep 12 2008 - brian.cameron@sun.com
- Add new copyright files.
* Wed Apr 02 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Sun Jun 11 2006 - laca@Sun.com
- change group from other to bin/sys
* Tue Sep 13 2005 - brian.cameron@sun.com
- Now use theora version number.
* Tue Jul 26 2005 - balamurali.viswanathan@wipro.com
- Add ogg and vorbis dependency
* Tue Jul 26 2005 - balamurali.viswanathan@wipro.com
- Initial spec-file created


