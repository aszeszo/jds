#
# spec file for package SUNWlibsoup
#
# includes module(s): libsoup
#
# Copyright (c) 2004, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libsoup64 = libsoup.spec
%endif

%include base.inc
%use libsoup = libsoup.spec

Name:          SUNWlibsoup
License:       LGPL v2
IPS_package_name: library/libsoup
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:       Libsoup is an HTTP client/server library for GNOME.
Version:       %{libsoup.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_Category: EVO25,%{default_category}
SUNW_BaseDir:  %{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

Requires: library/desktop/gobject/gobject-introspection
Requires: library/gnome/gnome-libs

BuildRequires: database/sqlite-3
BuildRequires: gnome/config/gconf
BuildRequires: library/desktop/gobject/gobject-introspection
BuildRequires: library/glib2
BuildRequires: library/gnome/gnome-keyring
BuildRequires: library/gnome/gnome-libs
BuildRequires: library/gnutls
BuildRequires: library/libproxy/libproxy-gnome
BuildRequires: library/libtasn1
BuildRequires: library/libxml2
BuildRequires: library/security/libgpg-error
BuildRequires: library/zlib
BuildRequires: system/library/dbus
BuildRequires: system/library/libdbus
BuildRequires: system/library/libdbus-glib
BuildRequires: system/library/security/libgcrypt
BuildRequires: system/library/math

%package devel
Summary:		%{summary} - development files
SUNW_BaseDir:		%{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir -p %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libsoup64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%libsoup.prep -d %name-%version/%{base_arch}
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export RPM_OPT_FLAGS="$CFLAGS"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

%ifarch amd64 sparcv9
%libsoup64.build -d %name-%version/%_arch64
%endif

%libsoup.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libsoup64.install -d %name-%version/%_arch64
%endif

%libsoup.install -d %name-%version/%{base_arch}

# Verbose deletion to show the dirs being targetted.
rm -r $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/libsoup-*
rmdir $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html
rmdir $RPM_BUILD_ROOT%{_datadir}/gtk-doc

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%doc %{base_arch}/libsoup-%{libsoup.version}/README
%doc %{base_arch}/libsoup-%{libsoup.version}/AUTHORS
%doc(bzip2) %{base_arch}/libsoup-%{libsoup.version}/COPYING
%doc(bzip2) %{base_arch}/libsoup-%{libsoup.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/*.gir
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}/girepository-1.0
%{_libdir}/%{_arch64}/girepository-1.0/*
%endif
%{_mandir}/*/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Fri Feb 17 2012 - brian.cameron@oracle.com
- Add 64-bit support.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Sun Jan  3 2010 - christian.kelly@sun.com
- Add dep on SUNWgnome-libs.
* Thu Dec 17 2009 - ke.wang@sun.com
- Bump to 2.28.2
- Add SUNWzlib as BuildRequires.
* Thu Jul 02 2009 - ke.wang@sun.com
- Remove "-L%{_libdir} -R%{_libdir}" from LDFLAGS
- Add dependency on SUNWsqlite3
* Thu May 21 2009 - ke.wang@sun.com
- remove ChangeLog since the absence of this file in 2.26.2
* Tue Mar 10 2009 - harry.lu@sun.com
- change owner to Ke Wang.
* Wed Feb 18 2009 - ke.wang@sun.com
- Add dependency on libproxy
* Wed Jul 30 2008 - simon.zheng@sun.com
- Add manpage.
* Thu Mar 27 2008 - simon.zheng@sun.com
- Add SUNWlibsoup.copyright.
* Thu Mar 06 2008 - damien.carbery@sun.com
- Remove unnecessary code left over from SUNWevolution-libs.spec.
* Tue Mar 04 2008 - <jedy.wang@sun.com>
- Initial version created. Splited from SUNWevolution-libs.

