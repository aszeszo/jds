#
# spec file for package SUNWgnome-backgrounds
#
# includes module(s): gnome-backgrounds
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc
%include base.inc

%use backgrounds = gnome-backgrounds.spec

Name:                    SUNWgnome-backgrounds
IPS_package_name:        image/gnome-backgrounds
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Selection of backgrounds for the GNOME desktop
Version:                 %{backgrounds.version}
License:                 %{backgrounds.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

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
%{_datadir}/gnome-background-properties/*.xml
%{_datadir}/pixmaps/backgrounds/gnome/nature/*.jpg
%{_datadir}/pixmaps/backgrounds/gnome/abstract/*.png
%doc -d %{base_arch} gnome-backgrounds-%{backgrounds.version}/README
%doc -d %{base_arch} gnome-backgrounds-%{backgrounds.version}/AUTHORS
%doc(bzip2) -d %{base_arch} gnome-backgrounds-%{backgrounds.version}/COPYING
%doc(bzip2) -d %{base_arch} gnome-backgrounds-%{backgrounds.version}/NEWS
%doc(bzip2) -d %{base_arch} gnome-backgrounds-%{backgrounds.version}/ChangeLog
%doc(bzip2) -d %{base_arch} gnome-backgrounds-%{backgrounds.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Thu Nov 19 2009 - christian.kelly@sun.com
- Adding a %changelog. Fixing directory permissions in %files.
* Mon Nov 30 2009 - christian.kelly@sun.com
- Fix %files.


