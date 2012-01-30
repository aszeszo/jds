#
# spec file for package SUNWlibproxy-mozjs
#
# includes module: libproxy
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke 
#

%include Solaris.inc

%define pythonver %{default_python_version}
%define build_module_gnome 0
%define build_module_mozjs 1

%ifarch amd64 sparcv9
%include arch64.inc
%use libproxy_64 = libproxy.spec
%endif

%include base.inc
%use libproxy = libproxy.spec

Name:                   SUNWlibproxy-mozjs
License:                LGPL v2.1
IPS_package_name:       library/libproxy/libproxy-mozjs
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                Plugin of libproxy for mozjs
Version:                %{libproxy.version}
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:         SUNWlibproxy.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: consolidation/desktop/gnome-incorporation
Requires:               SUNWlibproxy
Requires:               SUNWfirefox
BuildRequires:          SUNWfirefox-devel

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libproxy_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%libproxy.prep -d %name-%version/%base_arch

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

find $RPM_BUILD_ROOT%{_libdir} -name "ignore_domain.so" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -name "ignore_ip.so" -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/*.so*
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so*
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/libproxy
%{_libdir}/libproxy/*

%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}/libproxy
%{_libdir}/%{_arch64}/libproxy/*
%endif

%changelog
* Fri Apr 23 2010 - ke.wang@sun.com
- Undo Chiristian's previous commit
* Wed Mar 10 2010 - christian.kelly@sun.com
- This pkg trying to deliver file which SUNWlibproxy delivers.
* Thu Dec 17 2009 - ke.wang@sun.com
- Initial spec.



