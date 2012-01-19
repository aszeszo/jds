#
# spec file for package SUNWgnome-theme-only
#
# includes module(s): gnome-theme-only
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner calumb
#
%include Solaris.inc
%include base.inc

%use gnome_theme = gnome-themes.spec

Name:                    SUNWgnome-themes-only
IPS_package_name:        gnome/theme/gnome-themes
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Gnome themes 
Version:                 %{gnome_theme.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 LGPLv2.1
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWgtk2-engines
BuildRequires: SUNWicon-naming-utils

%package extra
IPS_package_name:        gnome/theme/gnome-themes-extra
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 %{summary} - extra themes
SUNW_BaseDir:            %{_basedir}
Requires:                %{name}
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%gnome_theme.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%gnome_theme.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%gnome_theme.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast
%{_datadir}/themes/HighContrast/*
%{_datadir}/themes/LargePrint/*
%{_datadir}/themes/Inverted/*
%dir %attr (0755, root, bin) %{_datadir}/themes
%dir %attr (0755, root, bin) %{_datadir}/themes/Clearlooks
%{_datadir}/themes/Clearlooks/*
#%{_datadir}/themes/ClearlooksTest/*

%doc -d %{base_arch} gnome-themes-%{gnome_theme.version}/README
%doc -d %{base_arch} gnome-themes-%{gnome_theme.version}/AUTHORS
%doc(bzip2) -d %{base_arch} gnome-themes-%{gnome_theme.version}/COPYING
%doc(bzip2) -d %{base_arch} gnome-themes-%{gnome_theme.version}/NEWS
%doc(bzip2) -d %{base_arch} gnome-themes-%{gnome_theme.version}/ChangeLog
%doc(bzip2) -d %{base_arch} gnome-themes-%{gnome_theme.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files extra
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse/*/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastLargePrint
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastLargePrint/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastLargePrint/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastLargePrintInverse/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastLargePrintInverse/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastLargePrintInverse/*/*/*
%{_datadir}/icons/HighContrast/*/*/*
%dir %attr (0755, root, bin) %{_datadir}/icons/Crux
%{_datadir}/icons/Crux/*
%{_datadir}/icons/HighContrastLargePrint/*/*/*
%dir %attr (0755, root, bin) %{_datadir}/icons/Mist
%{_datadir}/icons/Mist/*
%dir %attr (0755, root, bin) %{_datadir}/icons/HighContrast-SVG
%{_datadir}/icons/HighContrast-SVG/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastLargePrintInverse
%dir %attr (0755, root, bin) %{_datadir}/themes
%dir %attr (0755, root, bin) %{_datadir}/themes/Clearlooks
%dir %attr (0755, root, bin) %{_datadir}/themes/Crux
%dir %attr (0755, root, bin) %{_datadir}/themes/Mist
%{_datadir}/icons/LargePrint/index.theme
%{_datadir}/themes/HighContrastInverse/index.theme
%{_datadir}/themes/HighContrastInverse/gtk-2.0/gtkrc
%{_datadir}/themes/LowContrast/gtk-2.0/gtkrc
%{_datadir}/themes/LowContrast/index.theme
%{_datadir}/themes/Glossy/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Glossy/gtk-2.0/gtkrc
%{_datadir}/themes/Glossy/index.theme
%{_datadir}/themes/Simple/gtk-2.0/gtkrc
%{_datadir}/themes/Crux/index.theme
%{_datadir}/themes/LowContrastLargePrint/gtk-2.0/gtkrc
%{_datadir}/themes/LowContrastLargePrint/pixmaps/*.png
%{_datadir}/themes/LowContrastLargePrint/pixmaps/*.xpm
%{_datadir}/themes/LowContrastLargePrint/index.theme
%{_datadir}/themes/HighContrastLargePrintInverse/pixmaps/*.png
%{_datadir}/themes/HighContrastLargePrintInverse/pixmaps/*.xpm
%{_datadir}/themes/HighContrastLargePrintInverse/index.theme
%{_datadir}/themes/HighContrastLargePrintInverse/gtk-2.0/gtkrc
%{_datadir}/themes/ClearlooksClassic/gtk-2.0/gtkrc
%{_datadir}/themes/ClearlooksClassic/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Glider/index.theme
%{_datadir}/themes/Glider/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Glider/gtk-2.0/gtkrc
%{_datadir}/themes/Mist/index.theme
%{_datadir}/themes/Mist/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/HighContrastLargePrint/pixmaps/*.png
%{_datadir}/themes/HighContrastLargePrint/pixmaps/*.xpm
%{_datadir}/themes/HighContrastLargePrint/gtk-2.0/gtkrc
%{_datadir}/themes/HighContrastLargePrint/index.theme

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Nov 10 2010 - calum.benson@oracle.com
- Add License tag.
* Sun Jan  3 2010 - christian.kelly@sun.com
- Fix %files.
* Wed Dec  9 2009 - christian.kelly@sun.com
- Fix %files.
* Wed Nov 25 2009 - christian.kelly@sun.com
- Add %changelog.
- Add dependency on SUNWgtk-engines.
- Fix %files.


