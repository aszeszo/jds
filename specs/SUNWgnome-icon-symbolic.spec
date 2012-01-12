#
# spec file for package SUNWgnome-icon-symbolic
#
# includes module(s): gnome-icon-theme-symbolic
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc
%include base.inc

%use gnome = gnome-icon-theme-symbolic.spec

Name:                    SUNWgnome-icon-symbolic
IPS_package_name:        gnome/theme/gnome-icon-theme-symbolic
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 GNOME Icon Themes
Version:                 %{gnome.version}
License:                 %{gnome.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk3
BuildRequires: SUNWgtk3-devel
BuildRequires: SUNWicon-naming-utils

%if %build_l10n
%package l10n
IPS_package_name:        gnome/theme/gnome-icon-theme-symbolic/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                %{name}
%endif

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%gnome.prep -d %name-%version/%{base_arch}

%build
%gnome.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%gnome.install -d %name-%version/%{base_arch}

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/gnome

%dir %attr (0755, root, other) %{_datadir}/icons/gnome/*
%dir %attr (0755, root, other) %{_datadir}/icons/gnome/*/apps

%{_datadir}/icons/gnome/*/*/*.svg

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Sun Feb 28 2010 - christian.kelly@sun.com
- Deliver .pc file.
* Sun Feb 28 2010 - christian.kelly@sun.com
- Bump to 2.29.0.
* Fri Nov 20 2009 - christian.kelly@sun.com
- Fix %files. Add %changelog.


