#
# spec file for package SUNWicon-naming-utils
#
# includes module(s): icon-naming-utils
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc

%include base.inc

%use icon_naming = icon-naming-utils.spec

Name:                    SUNWicon-naming-utils
IPS_package_name:        library/desktop/xdg/icon-naming-utils
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Icon naming utils
Version:                 %{icon_naming.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{icon_naming.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel
Requires: library/perl-5/xml-simple

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%icon_naming.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%icon_naming.build -d %name-%version/%{base_arch}
export INU_DATA_DIR=%{_builddir}/%name-%version/%base_arch/icon-naming-utils-%{icon_naming.version}
chmod a+x $INU_DATA_DIR/icon-name-mapping
export PATH=$INU_DATA_DIR:$PATH

%install
rm -rf $RPM_BUILD_ROOT

%icon_naming.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/icon-naming-utils
%{_datadir}/dtds
%{_datadir}/pkgconfig
%{_libdir}/*

%doc -d %{base_arch} icon-naming-utils-%{icon_naming.version}/README
%doc -d %{base_arch} icon-naming-utils-%{icon_naming.version}/AUTHORS
%doc(bzip2) -d %{base_arch} icon-naming-utils-%{icon_naming.version}/COPYING
%doc(bzip2) -d %{base_arch} icon-naming-utils-%{icon_naming.version}/NEWS
%doc(bzip2) -d %{base_arch} icon-naming-utils-%{icon_naming.version}/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Thu Nov 19 2009 - christian.kelly@sun.com
- Fix directory permissions.


