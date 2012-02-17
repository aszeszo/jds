#
# spec file for package SUNWjson-c
#
# includes module(s): json-c
#
# Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use jsonc64 = json-c.spec
%endif

%include base.inc
%use jsonc = json-c.spec

Name:                      SUNWjson-c
IPS_package_name:          library/json-c
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                   %{jsonc.summary}
URL:                       http://live.gnome.org/JsonGlib
Version:                   %{jsonc.version}
License:                   %{jsonc.license}
SUNW_BaseDir:              %{_basedir}
SUNW_Copyright:            %{name}.copyright
BuildRoot:                 %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version
%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%jsonc64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%jsonc.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%jsonc64.build -d %name-%version/%_arch64
%endif

%jsonc.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%jsonc64.install -d %name-%version/%_arch64
%endif

%jsonc.install -d %name-%version/%{base_arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc %{base_arch}/json-c-%{jsonc.version}/AUTHORS
%doc %{base_arch}/json-c-%{jsonc.version}/README
%doc(bzip2) %{base_arch}/json-c-%{jsonc.version}/ChangeLog
%doc(bzip2) %{base_arch}/json-c-%{jsonc.version}/COPYING
%doc(bzip2) %{base_arch}/json-c-%{jsonc.version}/NEWS
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_docdir}

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%changelog
* Thu Feb 09 2012 - brian.cameron@oracle.com
- Created.
