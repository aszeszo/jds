#
# spec file for package SUNWgnome-icon-theme
#
# includes module(s): gnome-icon-theme
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc
%include base.inc

%use gnome = gnome-icon-theme.spec

Name:                    SUNWgnome-icon-theme
IPS_package_name:        gnome/theme/gnome-icon-theme
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 GNOME Icon Themes
Version:                 %{gnome.version}
License:                 %{gnome.license}
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

mkdir %name-%version/%{base_arch}
%gnome.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%gnome.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%gnome.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/gnome

%doc -d %{base_arch} gnome-icon-theme-%{gnome.version}/README
%doc -d %{base_arch} gnome-icon-theme-%{gnome.version}/AUTHORS
%doc(bzip2) -d %{base_arch} gnome-icon-theme-%{gnome.version}/COPYING
%doc(bzip2) -d %{base_arch} gnome-icon-theme-%{gnome.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/icons/gnome/*
%dir %attr (0755, root, other) %{_datadir}/icons/gnome/*/apps
%dir %attr (0755, root, bin) %{_datadir}/pkgconfig

%{_datadir}/icons/gnome/*/status/*.png
%{_datadir}/icons/gnome/*/places/*.png
%{_datadir}/icons/gnome/*/actions/*.png
%{_datadir}/icons/gnome/*/emblems/*.png
%{_datadir}/icons/gnome/*/mimetypes/*.png
%{_datadir}/icons/gnome/*/apps/*.png
%{_datadir}/icons/gnome/*/categories/*.png
%{_datadir}/icons/gnome/*/devices/*.png
%{_datadir}/icons/gnome/*/emotes/*.png
%{_datadir}/icons/gnome/*/animations/*.png
%{_datadir}/pkgconfig/gnome-icon-theme.pc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Sun Feb 28 2010 - christian.kelly@sun.com
- Deliver .pc file.
* Sun Feb 28 2010 - christian.kelly@sun.com
- Bump to 2.29.0.
* Fri Nov 20 2009 - christian.kelly@sun.com
- Fix %files. Add %changelog.


