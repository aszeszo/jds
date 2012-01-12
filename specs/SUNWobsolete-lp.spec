#
# spec file for generating IPSpackage stubs to remove 
# library/desktop/gtk2/gtk-backend-papi
# library/gnome/print/gnome-print
# library/gnome/print/gnome-print/gnome-print-papi
# print/lp/print-manager
#
# Copyright 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#
Name: SUNWobsolete-lp
Version: 1.0
Summary: Obsolete IPS packages for LP related packages

# This package is part of SUNWgtk2.spec
%package -n gtk-backend-papi
IPS_Package_Name: library/desktop/gtk2/gtk-backend-papi
IPS_component_version: 2.20.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

# This package is in SUNWgnome-print.spec
%package -n gnome-print
IPS_Package_Name: library/gnome/print/gnome-print
IPS_component_version: 2.18.8
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

# This package is in SUNWgnome-print.spec
%package -n gnome-print-papi
IPS_Package_Name: library/gnome/print/gnome-print/gnome-print-papi 
IPS_component_version: 2.18.8
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

# This package is in SUNWprint-monitor.spec
%package -n print-manager
IPS_Package_Name: print/lp/print-manager
IPS_component_version: 1.4.21
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

# This package is in SUNWgnome-hex-editor.spec
%package -n ghex
IPS_Package_Name: editor/ghex
IPS_component_version: 2.24.0
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%changelog
* Mon 15 Aug 2011 - ghee.teo@oracle.com
- Modified with initial feedbacks from Laca.
* Fri 12 Aug 2011 - ghee.teo@oracle.com
- Remove papi GTK+ print backend as to fix bugster#7076227.

