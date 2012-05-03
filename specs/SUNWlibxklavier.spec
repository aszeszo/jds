#
# spec file for package SUNWlibxklavier
#
# includes module(s): libxklavier
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner ja208388
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define _sysconfdir /etc/%{_arch64}
%use libxklavier_64 = libxklavier.spec
%endif

%include base.inc
%use libxklavier = libxklavier.spec

Name:                    SUNWlibxklavier
IPS_package_name:        library/desktop/libxklavier
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                 XKB utility library
Version:                 %{libxklavier.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{libxklavier.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include gnome-incorporation.inc
%include default-depend.inc
Requires: SUNWgtk2
Requires: image/library/libart
Requires: SUNWlibmsr
Requires: SUNWxorg-xkb
BuildRequires: SUNWlibm
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWlibart-devel
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWxorg-xkb
Requires: SUNWiso-codes

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libxklavier_64.prep -d %name-%version/%_arch64
%endif

mkdir -p %name-%version/%{base_arch}
%libxklavier.prep -d %name-%version/%{base_arch}
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%ifarch amd64 sparcv9
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="$FLAG64"
export PKG_CONFIG_PATH="%{_pkg_config_path64}"
%libxklavier_64.build -d %name-%version/%_arch64
%endif

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH="%{_pkg_config_path}"
%libxklavier.build -d %name-%version/%{base_arch}

%install
%ifarch amd64 sparcv9
%libxklavier_64.install -d %name-%version/%_arch64
%endif

%libxklavier.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d  %{base_arch} libxklavier-%{libxklavier.version}/README
%doc -d  %{base_arch} libxklavier-%{libxklavier.version}/AUTHORS
%doc(bzip2) -d  %{base_arch} libxklavier-%{libxklavier.version}/COPYING.LIB
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/girepository-1.0
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%{_libdir}/%{_arch64}/girepository-1.0
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gir-1.0
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %dir %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gtk-doc

%changelog
* Thu May 03 2012 - brian.cameron@oracle.com
- Fix packaging after update to 5.2.
* Thu May 12 2011 - javier.acosta@oracle.com
- Fix 64-bit support
* Mon Aug 02 2010 - javier.acosta@sun.com
- second version for release - remove l10n build plus corrections and
  modifications
* Thu Oct 08 2009 - suresh.chandrasekharan@sun.com
- 64-bit support
* Fri Sep 04 2009 - suresh.chandrasekharan@sun.com
- initial version

