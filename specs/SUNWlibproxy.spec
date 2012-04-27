#
# spec file for package SUNWlibproxy
#
# includes module: libproxy
#
# Copyright (c) 2005, 2011, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner leonfan 
#

%include Solaris.inc

%define pythonver %{default_python_version}
%define build_module_gnome 0
%define build_module_mozjs 0

%ifarch amd64 sparcv9
%include arch64.inc
%use libproxy_64 = libproxy.spec
%endif

%include base.inc
%use libproxy = libproxy.spec

Name:                   SUNWlibproxy
License:                LGPL v2.1
IPS_package_name:       library/libproxy
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                Libproxy is a library that provides automatic proxy configuration management
Version:                %{libproxy.version}
Source1:                %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:         %{name}.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires:          library/glib2
BuildRequires:          runtime/python-26
BuildRequires:          library/libproxy/libproxy-mozjs

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libproxy_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%libproxy.prep -d %name-%version/%base_arch

cd %{_builddir}/%{name}-%{version}
gzcat %SOURCE1 | tar xf -

%build
export PYTHON=/usr/bin/python%{pythonver}

%ifarch amd64 sparcv9
export PKG_CONFIG_LIBDIR=%{_pkg_config_path64}
%libproxy_64.build -d %name-%version/%_arch64
%endif

export PKG_CONFIG_LIBDIR=%{_pkg_config_path}
%libproxy.build -d %name-%version/%base_arch

%install
%ifarch amd64 sparcv9
%libproxy_64.install -d %name-%version/%_arch64
%endif

%libproxy.install -d %name-%version/%base_arch

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python*

cd %{_builddir}/%{name}-%{version}/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d %{base_arch} libproxy-%{libproxy.version}/AUTHORS
%doc -d %{base_arch} libproxy-%{libproxy.version}/README
%doc(bzip2) -d %{base_arch} libproxy-%{libproxy.version}/COPYING
%doc(bzip2) -d %{base_arch} libproxy-%{libproxy.version}/ChangeLog
%doc(bzip2) -d %{base_arch} libproxy-%{libproxy.version}/NEWS
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/libproxy
%{_libdir}/*.so.*
%{_libdir}/*.so
%{_libdir}/libproxy/*
%{_libdir}/python*

%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/*.so.*
%{_libdir}/%{_arch64}/*.so
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}/libproxy
%{_libdir}/%{_arch64}/libproxy/*
%endif

%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%actions
depend type=group fmri=library/libproxy/libproxy-mozjs

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*.pc

%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*.pc
%endif

%dir %attr (0755, root, bin) %{_includedir}
%dir %attr (0755, root, bin) %{_includedir}/libproxy
%{_includedir}/libproxy/*
%{_prefix}/demo/*

%changelog
* Tue Dec 13 2011 - leon.fan@oracle.com
- Add group depend to library/libproxy/libproxy-mozjs to fix 7108701
* Thu Dec 17 2009 - ke.wang@sun.com
- Separated into three packages: SUNWlibproxy, SUNWlibproxy-gnome
  and SUNWlibproxy-mozjs
* Fri Sep 11 2009 - ke.wang@sun.com
- Bump to 0.3.0
* Mon Sep 07 2009 - dave.lin@sun.com
- set PYTHON to python2.6
* Thu Sep 03 2009 - dave.lin@sun.com
- Add 'BuildRequires: runtime/python-26-devel' to build python binding.
* Wed Feb 18, 2009 - ke.wang@sun.com
- Set PKG_CONFIG_LIBDIR to _pkg_config_path64 to make PKG_CHECK_MODULES
  work correctly when building 64-bit library
* Wed Feb 18, 2009 - ke.wang@sun.com
- Change attribute of _datadir
* Mon Feb 09, 2009 - ke.wang@sun.com
- Initial spec.



