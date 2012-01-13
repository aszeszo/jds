# This is a special spec file used for generating IPS package stubs
# for renamed/obsoleted IPS packages.

# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
%define owner laca

Name: sys_t_trusted-extensions
IPS_Package_Name: system/trusted/trusted-extensions
Version: 0.5.11
Summary: Trusted Extensions
Ips_Legacy: false
%{?desktop_build:IPS_Vendor_Version:        0.%{desktop_build}}
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Meta(info.classification): "org.opensolaris.category.2008:Desktop (GNOME)/Trusted Extensions"
Requires: gnome/trusted/xagent >= 0.5.11-0.150
Requires: system/trusted >= 0.5.11-0.150
Requires: system/trusted/global-zone >= 0.5.11-0.150
Requires: x11/trusted/trusted-xorg >= 1.7.7-0.150
Requires: x11/trusted/libxtsol >= 0.5.11-0.150
Requires: gnome/trusted/device-manager >= 0.5.11-0.150
Requires: gnome/trusted/selection-manager >= 0.5.11-0.150
Requires: gnome/trusted/login-label-selector >= 0.5.11-0.150
Requires: gnome/trusted/libgnometsol >= 0.5.11-0.150
Requires: gnome/trusted/trusted-stripe >= 0.5.11-0.150
Requires: consolidation/desktop/gnome-incorporation = *
Requires: group/feature/trusted-desktop = *
PkgBuild_Make_Empty_Package: true
BuildRequires: consolidation/desktop/desktop-incorporation

%package -n trusted-extensions
IPS_Package_Name: trusted-extensions
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.1.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Obsoleted_By: system/trusted/trusted-extensions >= 0.5.11-0.134
Obsoleted_By: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true


%changelog
* Tue Jan 18 2011 - laszlo.peter@oracle.com
- create
