#
# spec file for package SUNWlibunique
#
# includes module(s): libunique
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libunique_64 = libunique.spec
%endif

%include base.inc
%use libunique = libunique.spec

Name:           SUNWlibunique
Summary:        libunique - library for writing single instance applications
Version:        %{libunique.version}
SUNW_Pkg:       SUNWlibunique
IPS_package_name: library/libunique
Meta(info.classification): %{classification_prefix}:System/Libraries
SUNW_Copyright: %{name}.copyright
License:        %{libunique.license}
SUNW_BaseDir:   %{_basedir}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source1:        %{name}-manpages-0.1.tar.gz

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       SUNWgtk2
Requires:       SUNWdbus-glib
BuildRequires:  SUNWxwplt
BuildRequires:  SUNWgtk2-devel
BuildRequires:  SUNWdbus-glib-devel

%package devel
Summary:        %{summary} - development files
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:       %name
Requires:       SUNWgtk2-devel

%prep
rm -rf %name-%version
mkdir -p %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%{_arch64}
%libunique_64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%libunique.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build

%ifarch amd64 sparcv9
export CFLAGS="%optflags64"
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH="%_pkg_config_path64"
export RPM_OPT_FLAGS="$CFLAGS"
%libunique_64.build -d %name-%version/%{_arch64}
%endif

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH="%_pkg_config_path"
export RPM_OPT_FLAGS="$CFLAGS"

%libunique.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libunique_64.install -d %name-%version/%{_arch64}
%endif

%libunique.install -d %name-%version/%{base_arch}

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d %{base_arch}/libunique-%{libunique.version} README AUTHORS NEWS
%doc(bzip2) -d %{base_arch}/libunique-%{libunique.version} COPYING ChangeLog po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libunique*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libunique*.so*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gtk-doc

%changelog
* Thu Apr 01 2010 - halton.huo@sun.com
- Add PKG_CONFIG_PATH to fix build issue for 64bit
* Mon Sep 28 2009 - halton.huo@sun.com
- Add manpage for libunique-1.0
* Thu Mar 05 2009 - brian.cameron@sun.com
- Change SUNWdbus-bindings to SUNWdbus-glib.
* Mon Feb 16 2009 - halton.huo@sun.com
- Add 64-bit support
* Sat Jan 24 2009 - halton.huo@sun.com
- Spilit unique.spec for possible 64-bit build
- Move .h and pkgconfig and gtk-doc into -devel package
 Thu Jan 08 2009 - christian.kelly@sun.com
- Initial spec



