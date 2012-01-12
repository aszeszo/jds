#
# spec file for package SUNWvala
#
# includes module(s): vala
#
# Copyright (c) 2007, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use vala_64 = vala.spec
%endif

%include base.inc
%use vala  = vala.spec

Name:                SUNWvala
IPS_package_name:    developer/vala
Meta(info.classification): %{classification_prefix}:Development/Other Languages
Summary:             Vala programming language
Version:             %{vala.version}

SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
License:             LGPL v2
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires:       SUNWglib2
BuildRequires:       SUNWglib2-devel

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name


%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%vala_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%vala.prep -d %name-%version/%base_arch


%build
%ifarch amd64 sparcv9
export PKG_CONFIG_LIBDIR=%{_pkg_config_path64}
%vala_64.build -d %name-%version/%_arch64
unset PKG_CONFIG_LIBDIR
%endif

export PKG_CONFIG_LIBDIR=%{_pkg_config_path}
%vala.build -d %name-%version/%base_arch
unset PKG_CONFIG_LIBDIR

%install
%ifarch amd64 sparcv9
%vala_64.install -d %name-%version/%_arch64
%endif

%vala.install -d %name-%version/%base_arch


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc -d %{base_arch} vala-%{vala.version}/README
%doc -d %{base_arch} vala-%{vala.version}/AUTHORS
%doc(bzip2) -d %{base_arch} vala-%{vala.version}/NEWS
%doc(bzip2) -d %{base_arch} vala-%{vala.version}/COPYING
%doc(bzip2) -d %{base_arch} vala-%{vala.version}/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/vala
%{_bindir}/valac
%{_bindir}/vapicheck
%{_bindir}/vapigen
%{_bindir}/vala-gen-introspect
%{_bindir}/vala-0.14
%{_bindir}/valac-0.14
%{_bindir}/vapicheck-0.14
%{_bindir}/vapigen-0.14
%{_bindir}/vala-gen-introspect-0.14
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/vala-0.14

%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_bindir}/%{_arch64}/vala
%{_bindir}/%{_arch64}/valac
%{_bindir}/%{_arch64}/vapicheck
%{_bindir}/%{_arch64}/vapigen
%{_bindir}/%{_arch64}/vala-gen-introspect
%{_bindir}/%{_arch64}/vala-0.14
%{_bindir}/%{_arch64}/valac-0.14
%{_bindir}/%{_arch64}/vapicheck-0.14
%{_bindir}/%{_arch64}/vapigen-0.14
%{_bindir}/%{_arch64}/vala-gen-introspect-0.14
%{_libdir}/%{_arch64}/lib*.so*
%{_libdir}/%{_arch64}/vala-0.14
%endif

%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/devhelp
%{_datadir}/vala-0.14
%{_mandir}

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%endif

%changelog
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Fix packaging for 0.14.0 release.
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Fix packaging for vala 0.12.1 release.
* Sun Feb 14 2010 - christian.kelly@sun.com
- Bump to 0.7.10.
* Tus Oct 20 2009 - jerry.tan@sun.com
- import to solaris
* Fri Jul 27 2007 - dougs@truemail.co.th
- Initial spec

