#
# spec file for package SUNWnimbus
#
# includes module(s): nimbus
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use nimbus_64 = nimbus.spec
%endif

%include base.inc

%use nimbus = nimbus.spec

Name:                    SUNWnimbus
IPS_package_name:        gnome/theme/nimbus
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Engine for Sun Nimbus GTK2 Theme
Version:                 %{nimbus.version}
License:                 %{nimbus.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWicon-naming-utils

%package hires
IPS_package_name:        gnome/theme/nimbus-hires
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 GNOME themes - high resolution icons
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%nimbus_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%nimbus.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%ifarch amd64 sparcv9
%nimbus_64.build -d %name-%version/%_arch64
%endif

%nimbus.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%nimbus_64.install -d %name-%version/%_arch64
%endif

%nimbus.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files hires
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, bin) %{_datadir}/icons/nimbus
%attr (-, root, bin) %{_datadir}/icons/nimbus/96x96
%attr (-, root, bin) %{_datadir}/icons/nimbus/192x192

%files
%defattr(-, root,bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/icons
%{_libdir}/gtk-2.0/*/engines/*.so
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/*
%endif
%{_datadir}/icons/nimbus/12x12/*
%{_datadir}/icons/nimbus/16x16/*
%{_datadir}/icons/nimbus/20x20/*
%{_datadir}/icons/nimbus/24x24/*
%{_datadir}/icons/nimbus/32x32/*
%{_datadir}/icons/nimbus/36x36/*
%{_datadir}/icons/nimbus/48x48/*
%{_datadir}/icons/nimbus/72x72/*
%{_datadir}/icons/nimbus/index.theme
%{_datadir}/themes/*

%doc -d %{base_arch} nimbus-%{nimbus.version}/README
%doc -d %{base_arch} nimbus-%{nimbus.version}/AUTHORS
%doc(bzip2) -d %{base_arch} nimbus-%{nimbus.version}/COPYING
%doc(bzip2) -d %{base_arch} nimbus-%{nimbus.version}/NEWS
%doc(bzip2) -d %{base_arch} nimbus-%{nimbus.version}/ChangeLog
%doc(bzip2) -d %{base_arch} nimbus-%{nimbus.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Wed Nov 25 2009 - christian.kelly@sun.com
- Add %changelog.
- Fix %files.


