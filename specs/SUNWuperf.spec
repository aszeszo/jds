#
# spec file for package uperf
#
# Copyright (c) 2009, 2011, Oracle and/or its affiliates. All rights reserved.  # This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use uperf_64 = uperf.spec
%endif

%include base.inc
%use uperf = uperf.spec

Name:                    uperf
License: GPL v3
IPS_package_name:        benchmark/uperf
Meta(info.classification): %{classification_prefix}:Development/System
Summary:                 %{uperf.summary}
Version:                 1.0.3
%define src_dir          uperf-1.0.3-beta
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
#Source1:	%{name}-manpages-0.1.tar.gz

%prep
rm -rf %name-%{version}

mkdir -p %name-%{version}
%ifarch amd64 sparcv9
mkdir %name-%{version}/%_arch64
%uperf_64.prep -d %name-%{version}/%_arch64
%endif

mkdir %name-%{version}/%{base_arch}
%uperf.prep -d %name-%{version}/%{base_arch}

#cd %{_builddir}/%name-%version
#gzcat %SOURCE1 | tar xf -

%build

%ifarch amd64 sparcv9
%uperf_64.build -d %name-%{version}/%_arch64
%endif

%uperf.build -d %name-%{version}/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%uperf_64.install -d %name-%{version}/%_arch64
%endif

%uperf.install -d %name-%{version}/%{base_arch}

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/uperf
cp %{_builddir}/%name-%version/%{base_arch}/%{src_dir}/AUTHORS $RPM_BUILD_ROOT/usr/share/doc/uperf
cp %{_builddir}/%name-%version/%{base_arch}/%{src_dir}/README $RPM_BUILD_ROOT/usr/share/doc/uperf
cp %{_builddir}/%name-%version/%{base_arch}/%{src_dir}/ChangeLog $RPM_BUILD_ROOT/usr/share/doc/uperf
cp %{_builddir}/%name-%version/%{base_arch}/%{src_dir}/COPYING $RPM_BUILD_ROOT/usr/share/doc/uperf
cp %{_builddir}/%name-%version/%{base_arch}/%{src_dir}/NEWS $RPM_BUILD_ROOT/usr/share/doc/uperf

mkdir -p $RPM_BUILD_ROOT/usr/share/uperf
cp %{_builddir}/%name-%version/%{base_arch}/%{src_dir}/*.pem $RPM_BUILD_ROOT/usr/share/uperf

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%ifarch amd64 sparcv9
%{_bindir}/%{_arch64}/uperf
%endif

%{_bindir}/uperf

%dir %attr (0755, root, other) %{_datadir}/uperf
%{_datadir}/uperf/*
%{_datadir}/doc/uperf/*

%changelog
* Thu Jul 07 2011 - jeff.cai@oracle.com
- Initial spec
