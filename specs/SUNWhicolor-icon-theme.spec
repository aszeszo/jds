#
# spec file for package SUNWhicolor-icon-theme
#
# includes module(s): hicolor-icon-theme
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner calumb
#
%include Solaris.inc
%include base.inc

%use hicolor = hicolor-icon-theme.spec

Name:                    SUNWhicolor-icon-theme
IPS_package_name:        gnome/theme/hicolor-icon-theme
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 GNOME Hi Color Icon Theme
Version:                 %{hicolor.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GPLv2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%hicolor.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%hicolor.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%hicolor.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, other)
%dir %attr (0755, root, sys) %{_datadir}

%{_datadir}/icons/hicolor/*/animations
%{_datadir}/icons/hicolor/*/categories
%{_datadir}/icons/hicolor/*/emotes
%{_datadir}/icons/hicolor/*/mimetypes
%{_datadir}/icons/hicolor/*/intl
%{_datadir}/icons/hicolor/*/devices
%{_datadir}/icons/hicolor/*/status
%{_datadir}/icons/hicolor/*/places
%{_datadir}/icons/hicolor/*/filesystems
%dir %{_datadir}/icons/hicolor/*/actions
%{_datadir}/icons/hicolor/*/emblems
%{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/stock/object
%{_datadir}/icons/hicolor/*/stock/text
%{_datadir}/icons/hicolor/*/stock/image
%{_datadir}/icons/hicolor/*/stock/code
%{_datadir}/icons/hicolor/*/stock/navigation
%{_datadir}/icons/hicolor/*/stock/table
%{_datadir}/icons/hicolor/*/stock/io
%{_datadir}/icons/hicolor/*/stock/data
%{_datadir}/icons/hicolor/*/stock/media
%{_datadir}/icons/hicolor/*/stock/chart
%{_datadir}/icons/hicolor/*/stock/net
%{_datadir}/icons/hicolor/*/stock/form
%{_datadir}/icons/hicolor/index.theme

%doc -d %{base_arch} hicolor-icon-theme-%{hicolor.version}/README
%doc(bzip2) -d %{base_arch} hicolor-icon-theme-%{hicolor.version}/COPYING
%doc(bzip2) -d %{base_arch} hicolor-icon-theme-%{hicolor.version}/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Wed Nov 10 2010 - calum.benson@oracle.com
- Add License tag.
* Thu Nov 19 2009 - christian.kelly@sun.com
- Adding a %changelog. Fixing directory permissions.


