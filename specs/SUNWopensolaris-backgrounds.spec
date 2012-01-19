#
# spec file for package SUNWopensolaris-backgrounds
#
# includes module(s): opensolaris-backgrounds
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc
%include base.inc

%use backgrounds = opensolaris-backgrounds.spec

Name:                    SUNWopensolaris-backgrounds
IPS_package_name:        gnome/theme/background/os-backgrounds
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Selection of OpenSolaris backgrounds for the GNOME desktop
Version:                 %{backgrounds.version}
License:                 %{backgrounds.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel

%package xtra
IPS_package_name:        gnome/theme/background/os-backgrounds-extra
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 %{summary} - extra backgrounds
SUNW_BaseDir:            %{_basedir}
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%backgrounds.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%backgrounds.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%backgrounds.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/gnome-background-properties/opensolaris-backgrounds.xml
%{_datadir}/pixmaps/backgrounds/opensolaris/opensolaris-default.jpg

%files xtra 
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/backgrounds/opensolaris/grid-blue.jpg

%doc -d %{base_arch} opensolaris-backgrounds-%{backgrounds.version}/README
%doc -d %{base_arch} opensolaris-backgrounds-%{backgrounds.version}/AUTHORS
%doc(bzip2) -d %{base_arch} opensolaris-backgrounds-%{backgrounds.version}/COPYING
%doc(bzip2) -d %{base_arch} opensolaris-backgrounds-%{backgrounds.version}/NEWS
%doc(bzip2) -d %{base_arch} opensolaris-backgrounds-%{backgrounds.version}/ChangeLog
%doc(bzip2) -d %{base_arch} opensolaris-backgrounds-%{backgrounds.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Thu Nov 19 2009 - christian.kelly@sun.com
- Fix directory permissions.
* Wed Nov 25 2009 - christian.kelly@sun.com
- Fix directory perms.


