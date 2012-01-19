#
# spec file for package SUNWdmz-cursor
#
# includes module(s): dmz-cursor
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#
%include Solaris.inc
%include base.inc

%use dmz = dmz-cursor.spec

Name:                    SUNWdmz-cursor
IPS_package_name:        gnome/theme/cursor/dmz-cursor
License:                 MIT
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 DMZ cursor themes
Version:                 %{dmz.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%dmz.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%dmz.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%dmz.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/icons/*

%changelog
* Thu Nov 19 2009 - Christian.Kelly@sun.com
- Where's the %changelog? Fixing directory permissions.


