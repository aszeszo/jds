#
# spec file for package SUNWlibmikmod
#
# includes module(s): libmikmod
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wjs
#
%include Solaris.inc

%use libmikmod = libmikmod.spec

Name:           SUNWlibmikmod
IPS_package_name: library/audio/libmikmod
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:        libmikmod  - a portable sound library for Unix and other systems
Version:        %{libmikmod.version}
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
License:        %{libmikmod.license}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       SUNWlibms

%package devel
Summary:        %{summary} - development files
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:       %name

%prep
rm -rf %name-%version
mkdir %name-%version
%libmikmod.prep -d %name-%version

%build

%libmikmod.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%libmikmod.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/libmikmod-config
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*

%changelog
* Tue Sep 2 2008 - william.schoofs@sun.com
- Create


