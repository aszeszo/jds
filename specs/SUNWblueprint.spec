#
# spec file for package SUNWblueprint
#
# includes module(s): blueprint
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
%use blueprint_64 = blueprint.spec
%endif

%include base.inc

%use blueprint = blueprint.spec

Name:                    SUNWblueprint
IPS_package_name:        gnome/theme/blueprint
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Engine for GTK2 Blue Print Theme
Version:                 %{blueprint.version}
License:                 %{blueprint.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWicon-naming-utils

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%blueprint_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%blueprint.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%ifarch amd64 sparcv9
%blueprint_64.build -d %name-%version/%_arch64
%endif

%blueprint.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%blueprint_64.install -d %name-%version/%_arch64
%endif

%blueprint.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root,bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/blueprint
%dir %attr (0755, root, other) %{_datadir}/icons/blueprint/48x48
%dir %attr (0755, root, other) %{_datadir}/icons/blueprint/48x48/apps
%{_datadir}/icons/blueprint/*/apps/*.png
%{_datadir}/icons/blueprint/stock/*/*.png
%{_datadir}/icons/blueprint/index.theme
%{_datadir}/icons/blueprint/*/stock/generic/stock_timezone.png
%{_datadir}/icons/blueprint/*/stock/generic/config-language.png
%{_datadir}/icons/blueprint/*/filesystems/*.png
%{_datadir}/icons/blueprint/*/filesystems/*.icon
%{_datadir}/icons/blueprint/*/mimetypes/*.png
%{_datadir}/icons/blueprint/*/devices/*.png
%{_datadir}/icons/blueprint/*/emblems/*.png
%{_datadir}/icons/blueprint/*/emblems/*.icon
%{_libdir}/gtk-2.0/*/engines/*.so
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/*
%endif
%{_datadir}/themes/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*

%{_defaultdocdir}/blueprint-engine/ChangeLog
%{_defaultdocdir}/blueprint-engine/AUTHORS
%{_defaultdocdir}/blueprint-engine/COPYING
%{_defaultdocdir}/blueprint-engine/README
%{_defaultdocdir}/blueprint-engine/NEWS

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Fri Nov 20 2009 - christian.kelly@sun.com
- Add %changelog, fix directory permissions.


