#
# spec file for package SUNWtotem-pl-parser
#
# includes module(s): totem-pl-parser
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%include Solaris.inc


%define makeinstall make install DESTDIR=$RPM_BUILD_ROOT
%use totemparser = totem-pl-parser.spec

Name:                    SUNWtotem-pl-parser
License:                 LGPLv2
IPS_package_name:        library/media-player/totem-pl-parser
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 a library to parse playlist
Version:                 %{totemparser.version}
SUNW_BaseDir:            %{_prefix}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: system/header
BuildRequires: library/libxml2
BuildRequires: library/desktop/evolution-data-server
BuildRequires: library/gmime
BuildRequires: archiver/gnu-tar
BuildRequires: developer/gnu-binutils
Requires: library/desktop/evolution-data-server
Requires: system/library
Requires: library/libxml2
Requires: library/gmime
Requires: crypto/gnupg
Requires: library/desktop/gobject/gobject-introspection

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir: %{_basedir}

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir %name-%version
%totemparser.prep -d %name-%version

%build
export CFLAGS="%optflags"
export CXXFLAGS="%cxx_optflags" 
export RPM_OPT_FLAGS="$CFLAGS"
export PKG_CONFIG_PATH=%{_datadir}/pkgconfig
%totemparser.build -d %name-%version


%install
rm -rf $RPM_BUILD_ROOT
%totemparser.install -d %name-%version

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):unsupported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}

%{_datadir}/gir-1.0/TotemPlParser-1.0.gir
%{_libdir}/girepository-1.0/TotemPlParser-1.0.typelib

%doc totem-pl-parser-%{totemparser.version}/AUTHORS
%doc totem-pl-parser-%{totemparser.version}/README
%doc(bzip2) totem-pl-parser-%{totemparser.version}/COPYING.LIB
%doc(bzip2) totem-pl-parser-%{totemparser.version}/NEWS
%doc(bzip2) totem-pl-parser-%{totemparser.version}/ChangeLog
%doc(bzip2) totem-pl-parser-%{totemparser.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc


%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale


%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Fri Mar 19 2010 - christian.kelly@sun.com
- Fix %files.
* Mon Sep 28 2009 - dave.lin@sun.com
- Add 'BuildRequires: SUNWlibgmime-devel'.
* Thu Mar 26 2009 -jerry.tan@sun.com
- seperate totem-pl-parser from SUNWgnome-media-player



