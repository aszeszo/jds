# This is a special spec file used for generating IPS package stubs
# for renamed/obsoleted IPS packages.

# Copyright (c) 2011 Oracle and/or its affiliates. All rights reserved.
#
%define owner laca

Name: SUNWobsolete-gnome
Version: 1.0
Summary: Obsolete IPS packages in the GNOME consolidation

%package -n gnome-incorporation
IPS_Package_Name: consolidation/gnome/gnome-incorporation
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation >= 0.5.11-0.175.0.0.0.0.0
Renamed_To: consolidation/desktop/desktop-incorporation >= 0.5.11-0.175.0.0.0.0.0
PkgBuild_Make_Empty_Package: true

%package -n gnome_l10n-incorporation
IPS_Package_Name: consolidation/gnome_l10n/gnome_l10n-incorporation
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWneutral-plus-cursors
IPS_Package_Name: SUNWneutral-plus-cursors
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWespeak
IPS_Package_Name: SUNWespeak
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/speech/espeak >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-mm-applets
IPS_Package_Name: SUNWgnome-mm-applets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/applet/gnome-mm-applets >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWliboil
IPS_Package_Name: SUNWliboil
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/liboil >= 0.3.16-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-base-libs
IPS_Package_Name: SUNWgnome-base-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/gnome/base-libs >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor
IPS_Package_Name: SUNWgnome-img-editor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/editor/gimp >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWjokosher
IPS_Package_Name: SUNWjokosher
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/studio/jokosher >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWcompiz-fusion-extra
IPS_Package_Name: SUNWcompiz-fusion-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/compiz/plugin/compiz-fusion-extra >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWgnome-time-slider
IPS_Package_Name: SUNWgnome-time-slider
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/time-slider >= 0.2.10-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWgnome-media-center
IPS_Package_Name: SUNWgnome-media-center
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWgnome-python26-libs
IPS_Package_Name: SUNWgnome-python26-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-gnome-libs-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWlibcompizconfig
IPS_Package_Name: SUNWlibcompizconfig
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/compiz/library/libcompizconfig >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWpython24-simplejson
IPS_Package_Name: SUNWpython24-simplejson
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-panel
IPS_Package_Name: SUNWgnome-panel
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-panel >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWxchat
IPS_Package_Name: SUNWxchat
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/irc/xchat >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWcodeina
IPS_Package_Name: SUNWcodeina
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-devhelp
IPS_Package_Name: SUNWgnome-devhelp
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: developer/gnome/devhelp >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-python-extras
IPS_Package_Name: SUNWgnome-python-extras
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWspeex
IPS_Package_Name: SUNWspeex
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: codec/speex >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython-xdg
IPS_Package_Name: SUNWpython-xdg
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgobject-introspection
IPS_Package_Name: SUNWgobject-introspection
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/gobject/gobject-introspection >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-camera
IPS_Package_Name: SUNWgnome-camera
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-camera >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-tsoljdsselmgr
IPS_Package_Name: SUNWtgnome-tsoljdsselmgr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/trusted/selection-manager >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpangomm
IPS_Package_Name: SUNWpangomm
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/c++/pangomm >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-remote-desktop
IPS_Package_Name: SUNWgnome-remote-desktop
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-remote-desktop >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWslocate
IPS_Package_Name: SUNWslocate
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: file/slocate >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWncurses
IPS_Package_Name: SUNWncurses
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/ncurses >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWprint-monitor
IPS_Package_Name: SUNWprint-monitor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWevolution-webcal
IPS_Package_Name: SUNWevolution-webcal
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: mail/evolution/connector/evolution-webcal >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdmz-cursor
IPS_Package_Name: SUNWdmz-cursor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/theme/cursor/dmz-cursor >= 0.4-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-system-monitor
IPS_Package_Name: SUNWgnome-system-monitor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/system-monitor/gnome-system-monitor >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-media-apps
IPS_Package_Name: SUNWgnome-media-apps
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: gnome/media/gnome-media >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWdcraw
IPS_Package_Name: SUNWdcraw
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 8.81
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/dcraw >= 8.81-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-doc-utils
IPS_Package_Name: SUNWgnome-doc-utils
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: developer/gnome/gnome-doc-utils >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-commander
IPS_Package_Name: SUNWgnome-commander
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/file-manager/gnome-commander >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefox
IPS_Package_Name: SUNWfirefox
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: web/browser/firefox >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-libs
IPS_Package_Name: SUNWgnome-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/gnome/gnome-libs >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-cssutils
IPS_Package_Name: SUNWpython26-cssutils
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/cssutils-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk-vnc
IPS_Package_Name: SUNWgtk-vnc
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/gtk-vnc >= 0.3.10-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-desklets-extra
IPS_Package_Name: SUNWgnome-desklets-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibunique
IPS_Package_Name: SUNWlibunique
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/libunique >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpyyaml26
IPS_Package_Name: SUNWpyyaml26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/pyyaml-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgkrellm
IPS_Package_Name: SUNWgkrellm
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/system-monitor/gkrellm >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibvisual
IPS_Package_Name: SUNWlibvisual
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/libvisual >= 0.4.0-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWevolution-exchange
IPS_Package_Name: SUNWevolution-exchange
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: mail/evolution/connector/evolution-exchange >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-libs
IPS_Package_Name: SUNWgnome-a11y-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/accessibility/gnome-a11y-libs >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWnimbus-hires
IPS_Package_Name: SUNWnimbus-hires
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/nimbus-hires >= 0.1.4-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-search
IPS_Package_Name: SUNWdesktop-search
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/desktop/search/tracker >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk2-engines-extra
IPS_Package_Name: SUNWgtk2-engines-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: gnome/theme/gtk2-engines-extra >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-games
IPS_Package_Name: SUNWgnome-games
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: games/gnome-games >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-meeting
IPS_Package_Name: SUNWgnome-meeting
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: communication/conferencing/ekiga >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-media
IPS_Package_Name: SUNWgnome-media
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/audio/gstreamer >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWopensp
IPS_Package_Name: SUNWopensp
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: developer/documentation-tool/opensp >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-backgrounds
IPS_Package_Name: SUNWgnome-backgrounds
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/gnome-backgrounds >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-speech-freetts
IPS_Package_Name: SUNWgnome-a11y-speech-freetts
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibpigment
IPS_Package_Name: SUNWlibpigment
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-search-thunderbird
IPS_Package_Name: SUNWdesktop-search-thunderbird
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgoffice
IPS_Package_Name: SUNWlibgoffice
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/goffice >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgqview
IPS_Package_Name: SUNWgqview
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/viewer/gqview >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdbus-bindings
IPS_Package_Name: SUNWdbus-bindings
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: SUNWdbus-glib >= 0.5.11-0.130
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibproxy
IPS_Package_Name: SUNWlibproxy
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/libproxy >= 0.3.1-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWzfs-auto-snapshot
IPS_Package_Name: SUNWzfs-auto-snapshot
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: service/storage/zfs-auto-snapshot >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-themes-hires
IPS_Package_Name: SUNWgnome-themes-hires
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: SUNWnimbus-hires >= 0.5.11-0.130
Renamed_To: SUNWhicolor-icon-theme >= 0.5.11-0.130
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWglib2
IPS_Package_Name: SUNWglib2
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/glib2 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWopensolaris-gdm-themes
IPS_Package_Name: SUNWopensolaris-gdm-themes
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWclutter-gst
IPS_Package_Name: SUNWclutter-gst
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/clutter/clutter-gst >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWgnome-applets
IPS_Package_Name: SUNWgnome-applets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/applet/gnome-applets >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWplanner
IPS_Package_Name: SUNWplanner
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/project-management/planner >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibsexy
IPS_Package_Name: SUNWlibsexy
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/desktop/libsexy >= 0.1.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWflac
IPS_Package_Name: SUNWflac
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: codec/flac >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWsigcpp
IPS_Package_Name: SUNWsigcpp
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/c++/sigcpp >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibsoup
IPS_Package_Name: SUNWlibsoup
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/libsoup >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-imaging
IPS_Package_Name: SUNWpython26-imaging
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-imaging-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbird
IPS_Package_Name: SUNWthunderbird
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: mail/thunderbird >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefox-apoc-adapter
IPS_Package_Name: SUNWfirefox-apoc-adapter
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgst-python
IPS_Package_Name: SUNWgst-python
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWblueprint
IPS_Package_Name: SUNWblueprint
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/blueprint >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWsolaris-devel-docs
IPS_Package_Name: SUNWsolaris-devel-docs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWo3read
IPS_Package_Name: SUNWo3read
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: text/o3read >= 0.0.4-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibrsvg
IPS_Package_Name: SUNWlibrsvg
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: image/library/librsvg >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-vfs
IPS_Package_Name: SUNWgnome-vfs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/gnome/gnome-vfs >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibtheora
IPS_Package_Name: SUNWlibtheora
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: codec/libtheora >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWccsm
IPS_Package_Name: SUNWccsm
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/compiz/ccsm >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWdmz-cursor-aa
IPS_Package_Name: SUNWdmz-cursor-aa
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/cursor/dmz-cursor-aa >= 0.4-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWevolution-libs
IPS_Package_Name: SUNWevolution-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/desktop/gtkhtml >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibical
IPS_Package_Name: SUNWlibical
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/libical >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtkperf
IPS_Package_Name: SUNWgtkperf
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: benchmark/gtkperf >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWrdesktop
IPS_Package_Name: SUNWrdesktop
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/remote-desktop/rdesktop >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWrss-glx
IPS_Package_Name: SUNWrss-glx
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.90
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/xscreensaver/hacks/rss-glx >= 0.90-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-cd
IPS_Package_Name: SUNWgnome-cd
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/cd-ripping/sound-juicer >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgpg-error
IPS_Package_Name: SUNWlibgpg-error
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/security/libgpg-error >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-session
IPS_Package_Name: SUNWgnome-session
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-session >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-disk-analyzer
IPS_Package_Name: SUNWgnome-disk-analyzer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/disk-analyzer/baobab >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWnwam-manager
IPS_Package_Name: SUNWnwam-manager
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/administration/nwam-manager >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpostrun
IPS_Package_Name: SUNWpostrun
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: service/postrun >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgegl
IPS_Package_Name: SUNWgegl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/library/gegl >= 0.1.0-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWIPython
IPS_Package_Name: SUNWIPython
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/python-2/ipython-26 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-tsoljdsdevmgr
IPS_Package_Name: SUNWtgnome-tsoljdsdevmgr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: gnome/trusted/device-manager >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWjpg
IPS_Package_Name: SUNWjpg
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/library/libjpeg >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWevolution
IPS_Package_Name: SUNWevolution
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: mail/evolution >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibcroco
IPS_Package_Name: SUNWlibcroco
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/libcroco >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWogg-vorbis
IPS_Package_Name: SUNWogg-vorbis
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: codec/ogg-vorbis >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWopenjade
IPS_Package_Name: SUNWopenjade
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: developer/documentation-tool/openjade >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-mousetweaks
IPS_Package_Name: SUNWgnome-a11y-mousetweaks
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/accessibility/mousetweaks >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWnimbus
IPS_Package_Name: SUNWnimbus
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.1.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/nimbus >= 0.1.4-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-twisted-web2
IPS_Package_Name: SUNWpython26-twisted-web2
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-twisted-web2-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-ui-designer
IPS_Package_Name: SUNWgnome-ui-designer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: developer/ui-designer/glade >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWrrdtool
IPS_Package_Name: SUNWrrdtool
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/rrdtool >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWlibpigment-python25
IPS_Package_Name: SUNWlibpigment-python25
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWgnome-gtksourceview
IPS_Package_Name: SUNWgnome-gtksourceview
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/gtksourceview >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibsdl
IPS_Package_Name: SUNWlibsdl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/sdl >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgcrypt
IPS_Package_Name: SUNWlibgcrypt
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: system/library/security/libgcrypt >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpango
IPS_Package_Name: SUNWpango
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/pango >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWcontact-lookup-applet
IPS_Package_Name: SUNWcontact-lookup-applet
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/applet/contact-lookup-applet >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-calculator
IPS_Package_Name: SUNWgnome-calculator
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/calculator/gcalctool >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-print
IPS_Package_Name: SUNWgnome-print
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWcompizconfig-gconf
IPS_Package_Name: SUNWcompizconfig-gconf
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/compiz/library/compizconfig-gconf >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWseahorse-plugins
IPS_Package_Name: SUNWseahorse-plugins
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/security/seahorse/seahorse-plugins >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWtransmission
IPS_Package_Name: SUNWtransmission
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/torrent/transmission >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-devel-docs
IPS_Package_Name: SUNWgnome-devel-docs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: documentation/gnome/gnome-devel-docs >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-viewer
IPS_Package_Name: SUNWgnome-img-viewer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/viewer/eog >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWxsane
IPS_Package_Name: SUNWxsane
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: image/scanner/xsane >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk-vnc-python24
IPS_Package_Name: SUNWgtk-vnc-python24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWmysql-python
IPS_Package_Name: SUNWmysql-python
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-system-tools
IPS_Package_Name: SUNWgnome-system-tools
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-xml
IPS_Package_Name: SUNWgnome-xml
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: data/docbook >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython24-cssutils
IPS_Package_Name: SUNWpython24-cssutils
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnutls
IPS_Package_Name: SUNWgnutls
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/gnutls >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWdrivel
IPS_Package_Name: SUNWdrivel
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: editor/blog/drivel >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWpython-twisted
IPS_Package_Name: SUNWpython-twisted
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-text-editor
IPS_Package_Name: SUNWgnome-text-editor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: editor/gedit >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWperl-authen-pam
IPS_Package_Name: SUNWperl-authen-pam
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/perl-5/authen-pam >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-media-player
IPS_Package_Name: SUNWgnome-media-player
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/media/gnome-media-player >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpysqlite
IPS_Package_Name: SUNWpysqlite
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.4.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-python-libs
IPS_Package_Name: SUNWgnome-python-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibffi
IPS_Package_Name: SUNWlibffi
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/libffi >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-desklets
IPS_Package_Name: SUNWgnome-desklets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWgnome-freedb-libs
IPS_Package_Name: SUNWgnome-freedb-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWgnome-themes
IPS_Package_Name: SUNWgnome-themes
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: SUNWblueprint >= 0.5.11-0.133
Renamed_To: SUNWdmz-cursor >= 0.5.11-0.133
Renamed_To: SUNWdmz-cursor-aa >= 0.5.11-0.133
Renamed_To: SUNWgnome-backgrounds >= 0.5.11-0.133
Renamed_To: SUNWgnome-icon-theme >= 0.5.11-0.133
Renamed_To: SUNWgnome-themes-only >= 0.5.11-0.133
Renamed_To: SUNWgnome-themes-only-extra >= 0.5.11-0.133
Renamed_To: SUNWgtk2-engines >= 0.5.11-0.133
Renamed_To: SUNWgtk2-engines-extra >= 0.5.11-0.133
Renamed_To: SUNWhicolor-icon-theme >= 0.5.11-0.133
Renamed_To: SUNWnimbus >= 0.5.11-0.133
Renamed_To: SUNWnimbus-hires >= 0.5.11-0.133
Renamed_To: SUNWopensolaris-backgrounds >= 0.5.11-0.133
Renamed_To: SUNWopensolaris-backgrounds-xtra >= 0.5.11-0.133
Renamed_To: SUNWtango-icon-theme >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgroff
IPS_Package_Name: SUNWgroff
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: text/groff >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgc
IPS_Package_Name: SUNWlibgc
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/gc >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgobby
IPS_Package_Name: SUNWgobby
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: editor/gobby >= 0.4.10-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibart
IPS_Package_Name: SUNWlibart
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: image/library/libart >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibpopt
IPS_Package_Name: SUNWlibpopt
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/popt >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWPython-extra
IPS_Package_Name: SUNWPython-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-tsol-libs
IPS_Package_Name: SUNWtgnome-tsol-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/trusted/libgnometsol >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgsf
IPS_Package_Name: SUNWlibgsf
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/desktop/libgsf >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-twisted
IPS_Package_Name: SUNWpython26-twisted
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.1.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-twisted-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibglade
IPS_Package_Name: SUNWlibglade
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/libglade >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-nettool
IPS_Package_Name: SUNWgnome-nettool
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/network/gnome-nettool >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-fun-applets
IPS_Package_Name: SUNWgnome-fun-applets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/applet/gnome-fun-applets >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWPython25
IPS_Package_Name: SUNWPython25
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.5
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-crash-report
IPS_Package_Name: SUNWgnome-crash-report
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/crash-report/bug-buddy >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-notify
IPS_Package_Name: SUNWpython26-notify
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-notify-26 >= 0.1.1-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWcairomm
IPS_Package_Name: SUNWcairomm
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/c++/cairomm >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWxwsvr
IPS_Package_Name: SUNWxwsvr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: SUNWxscreensaver >= 5.1-0.130
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWxscreensaver
IPS_Package_Name: SUNWxscreensaver
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 5.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/xscreensaver >= 5.1-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-power-manager
IPS_Package_Name: SUNWgnome-power-manager
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/gnome-power-manager >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-display-mgr
IPS_Package_Name: SUNWgnome-display-mgr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: system/display-manager/gdm >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-speech-espeak
IPS_Package_Name: SUNWgnome-a11y-speech-espeak
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/speech/gnome-speech/driver/gnome-speech-espeak >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWdiveintopython
IPS_Package_Name: SUNWdiveintopython
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: documentation/diveintopython >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-organizer
IPS_Package_Name: SUNWgnome-img-organizer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/viewer/gthumb >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWxdg-user-dirs-gtk
IPS_Package_Name: SUNWxdg-user-dirs-gtk
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: desktop/xdg/xdg-user-dirs-gtk >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWlibpigment-python24
IPS_Package_Name: SUNWlibpigment-python24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWgtk2
IPS_Package_Name: SUNWgtk2
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/gtk2 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWbrltty
IPS_Package_Name: SUNWbrltty
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/accessibility/brltty >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibdiscid
IPS_Package_Name: SUNWlibdiscid
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/musicbrainz/libdiscid >= 0.2.2-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-themes-only
IPS_Package_Name: SUNWgnome-themes-only
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/gnome-themes >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWcairo
IPS_Package_Name: SUNWcairo
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/desktop/cairo >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWcheese
IPS_Package_Name: SUNWcheese
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: image/webcam/cheese >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-audio
IPS_Package_Name: SUNWgnome-audio
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-audio >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-search-tool
IPS_Package_Name: SUNWgnome-search-tool
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-search-tool >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlynx
IPS_Package_Name: SUNWlynx
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: web/browser/lynx >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-pilot
IPS_Package_Name: SUNWgnome-pilot
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: communication/pda/gnome-pilot >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-character-map
IPS_Package_Name: SUNWgnome-character-map
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/character-map/gucharmap >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtkspell
IPS_Package_Name: SUNWgtkspell
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/gtkspell >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWnet6
IPS_Package_Name: SUNWnet6
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/c++/net6 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtango-icon-theme
IPS_Package_Name: SUNWtango-icon-theme
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/theme/tango-icon-theme >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWclutter-cairo
IPS_Package_Name: SUNWclutter-cairo
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWlibmikmod
IPS_Package_Name: SUNWlibmikmod
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/audio/libmikmod >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-tstripe
IPS_Package_Name: SUNWtgnome-tstripe
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/trusted/trusted-stripe >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-python26-extras
IPS_Package_Name: SUNWgnome-python26-extras
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-gnome-extras-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-component
IPS_Package_Name: SUNWgnome-component
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/gnome/gnome-component >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-im-client
IPS_Package_Name: SUNWgnome-im-client
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: communication/im/pidgin >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtsclient
IPS_Package_Name: SUNWtsclient
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/remote-desktop/tsclient >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdbus-python24
IPS_Package_Name: SUNWdbus-python24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-desktop-prefs
IPS_Package_Name: SUNWgnome-desktop-prefs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/preferences/control-center >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWxdg-user-dirs
IPS_Package_Name: SUNWxdg-user-dirs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/xdg/xdg-user-dirs >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-dtstart
IPS_Package_Name: SUNWgnome-dtstart
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: SUNWdesktop-startup >= 0.5.11-0.130
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-intranet-applets
IPS_Package_Name: SUNWgnome-intranet-applets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/applet/gnome-intranet-applets >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgksu
IPS_Package_Name: SUNWgksu
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/gksu >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk-doc
IPS_Package_Name: SUNWgtk-doc
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: developer/documentation-tool/gtk-doc >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWsun-gdm-themes
IPS_Package_Name: SUNWsun-gdm-themes
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-libs-python24
IPS_Package_Name: SUNWgnome-a11y-libs-python24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython-zope-interface
IPS_Package_Name: SUNWpython-zope-interface
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-file-mgr
IPS_Package_Name: SUNWgnome-file-mgr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/file-manager/nautilus >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-startup
IPS_Package_Name: SUNWdesktop-startup
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: system/display-manager/desktop-startup >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWicon-naming-utils
IPS_Package_Name: SUNWicon-naming-utils
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/desktop/xdg/icon-naming-utils >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWvinagre
IPS_Package_Name: SUNWvinagre
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/remote-desktop/vinagre >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython-imaging
IPS_Package_Name: SUNWpython-imaging
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-cd-burner
IPS_Package_Name: SUNWgnome-cd-burner
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/cd-burning/brasero >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWiso-codes
IPS_Package_Name: SUNWiso-codes
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: data/iso-codes >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdialog
IPS_Package_Name: SUNWdialog
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: terminal/dialog >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdbus
IPS_Package_Name: SUNWdbus
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: system/library/dbus >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-poke
IPS_Package_Name: SUNWgnome-a11y-poke
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/accessibility/accerciser >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-terminal-java
IPS_Package_Name: SUNWgnome-terminal-java
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.1.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/java/java-gnome/java-libvte >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWobby
IPS_Package_Name: SUNWobby
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/c++/obby >= 0.4.7-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibexif
IPS_Package_Name: SUNWlibexif
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/library/libexif >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-tsoljdslabel
IPS_Package_Name: SUNWtgnome-tsoljdslabel
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/trusted/login-label-selector >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWraptor
IPS_Package_Name: SUNWraptor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/raptor >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-sound-recorder
IPS_Package_Name: SUNWgnome-sound-recorder
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/media/sound-recorder >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWconsolekit
IPS_Package_Name: SUNWconsolekit
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/xdg/consolekit >= 0.4.1-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-print-papi
IPS_Package_Name: SUNWgnome-print-papi
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWirssi
IPS_Package_Name: SUNWirssi
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: network/chat/irssi >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWmoovida-plugins
IPS_Package_Name: SUNWmoovida-plugins
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
%endif
PkgBuild_Make_Empty_Package: true

%package -n SUNWbabl
IPS_Package_Name: SUNWbabl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/library/babl >= 0.1.0-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWswt
IPS_Package_Name: SUNWswt
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/java/swt >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-libs-python26
IPS_Package_Name: SUNWgnome-a11y-libs-python26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/pyatspi-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWopensolaris-welcome
IPS_Package_Name: SUNWopensolaris-welcome
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-hex-editor
IPS_Package_Name: SUNWgnome-hex-editor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-utility-applets
IPS_Package_Name: SUNWgnome-utility-applets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/applet/gnome-utility-applets >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdia
IPS_Package_Name: SUNWdia
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: editor/diagram/dia >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWxdg-utils
IPS_Package_Name: SUNWxdg-utils
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/xdg/xdg-utils >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWavant
IPS_Package_Name: SUNWavant
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/avant-window-navigator >= 0.3.2.1-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWpython25-simplejson
IPS_Package_Name: SUNWpython25-simplejson
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWbrasero
IPS_Package_Name: SUNWbrasero
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWpython26-coherence
IPS_Package_Name: SUNWpython26-coherence
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/python-2/coherence-26 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWavahi-bridge-dsd
IPS_Package_Name: SUNWavahi-bridge-dsd
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: system/network/avahi >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWconsolekit-pam
IPS_Package_Name: SUNWconsolekit-pam
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/security/pam/module/pam-consolekit >= 0.4.1-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-reader
IPS_Package_Name: SUNWgnome-a11y-reader
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/accessibility/orca >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-archive-mgr
IPS_Package_Name: SUNWgnome-archive-mgr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/archive-manager/file-roller >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgst-python26
IPS_Package_Name: SUNWgst-python26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/python-2/python-gst-26 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibdaemon
IPS_Package_Name: SUNWlibdaemon
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/libdaemon >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-zope-interface
IPS_Package_Name: SUNWpython26-zope-interface
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/python-2/python-zope-interface-26 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWsun-backgrounds
IPS_Package_Name: SUNWsun-backgrounds
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtotem-pl-parser
IPS_Package_Name: SUNWtotem-pl-parser
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/media-player/totem-pl-parser >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-fonts
IPS_Package_Name: SUNWgnome-fonts
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: system/font/gnome-fonts >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWhamster
IPS_Package_Name: SUNWhamster
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-wm
IPS_Package_Name: SUNWgnome-wm
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/window-manager/metacity >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWPython
IPS_Package_Name: SUNWPython
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.4.6
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-search-firefox
IPS_Package_Name: SUNWdesktop-search-firefox
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/search/tracker/tracker-firefox >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWvirt-manager
IPS_Package_Name: SUNWvirt-manager
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.6.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
%endif
PkgBuild_Make_Empty_Package: true

%package -n SUNWjre-config-plugin
IPS_Package_Name: SUNWjre-config-plugin
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: web/browser/firefox/plugin/plugin-java >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-log-viewer
IPS_Package_Name: SUNWgnome-log-viewer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-log-viewer >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpyyaml24
IPS_Package_Name: SUNWpyyaml24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWmusicbrainz
IPS_Package_Name: SUNWmusicbrainz
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/musicbrainz/libmusicbrainz >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-cache
IPS_Package_Name: SUNWdesktop-cache
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: service/gnome/desktop-cache >= 0.2.2-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-user-docs
IPS_Package_Name: SUNWgnome-user-docs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: documentation/gnome/gnome-user-docs >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWhicolor-icon-theme
IPS_Package_Name: SUNWhicolor-icon-theme
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/hicolor-icon-theme >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-gok
IPS_Package_Name: SUNWgnome-a11y-gok
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-internet-applets
IPS_Package_Name: SUNWgnome-internet-applets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/applet/gnome-internet-applets >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnonlin
IPS_Package_Name: SUNWgnonlin
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/audio/gstreamer/plugin/gnonlin >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-terminal
IPS_Package_Name: SUNWgnome-terminal
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.1.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: terminal/gnome-terminal >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtack
IPS_Package_Name: SUNWtack
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: terminal/tack >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgamin
IPS_Package_Name: SUNWgamin
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/file-monitor/gamin >= 0.1.10-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWsexy-python
IPS_Package_Name: SUNWsexy-python
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/python-2/python-sexy-24 >= 0.1.9-0.133
PkgBuild_Make_Empty_Package: true
%endif

%ifarch i386
%package -n SUNWgnome-keyring-manager
IPS_Package_Name: SUNWgnome-keyring-manager
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWxscreensaver-hacks
IPS_Package_Name: SUNWxscreensaver-hacks
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/xscreensaver/hacks >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-config-java
IPS_Package_Name: SUNWgnome-config-java
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/java/java-gnome/java-libgconf >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-xagent
IPS_Package_Name: SUNWtgnome-xagent
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/trusted/xagent >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWevolution-data-server
IPS_Package_Name: SUNWevolution-data-server
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/evolution-data-server >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-ps-viewer
IPS_Package_Name: SUNWgnome-ps-viewer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/ggv >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpyyaml25
IPS_Package_Name: SUNWpyyaml25
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgftp
IPS_Package_Name: SUNWgftp
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/gftp >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk-vnc-python26
IPS_Package_Name: SUNWgtk-vnc-python26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-gtk-vnc-26 >= 0.3.10-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpng
IPS_Package_Name: SUNWpng
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/library/libpng >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibcanberra
IPS_Package_Name: SUNWlibcanberra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/desktop/xdg/libcanberra >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-gvfs
IPS_Package_Name: SUNWgnome-gvfs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/gnome/gvfs >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-dialog
IPS_Package_Name: SUNWgnome-dialog
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/zenity >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWopensolaris-backgrounds
IPS_Package_Name: SUNWopensolaris-backgrounds
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/background/opensolaris-backgrounds >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-config-editor
IPS_Package_Name: SUNWgnome-config-editor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/config/gconf/gconf-editor >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbird-calendar
IPS_Package_Name: SUNWthunderbird-calendar
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: mail/thunderbird/plugin/plugin-lightning >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk2-engines
IPS_Package_Name: SUNWgtk2-engines
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/gtk2-engines >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdbus-python26
IPS_Package_Name: SUNWdbus-python26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/python-2/python-dbus-26 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-simplejson
IPS_Package_Name: SUNWpython26-simplejson
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/simplejson-devel-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython24-ctypes
IPS_Package_Name: SUNWpython24-ctypes
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibtasn1
IPS_Package_Name: SUNWlibtasn1
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/libtasn1 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWclutter
IPS_Package_Name: SUNWclutter
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/clutter >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWPython26-extra
IPS_Package_Name: SUNWPython26-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-extra-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk2-print-papi
IPS_Package_Name: SUNWgtk2-print-papi
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWw3m
IPS_Package_Name: SUNWw3m
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: web/browser/w3m >= 0.5.2-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWseahorse
IPS_Package_Name: SUNWseahorse
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/security/seahorse >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help
IPS_Package_Name: SUNWgnome-img-editor-help
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: image/editor/gimp/gimp-help >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-dasher
IPS_Package_Name: SUNWgnome-a11y-dasher
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/accessibility/dasher >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWterminator
IPS_Package_Name: SUNWterminator
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: terminal/terminator >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-a11y-speech
IPS_Package_Name: SUNWgnome-a11y-speech
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/speech/gnome-speech >= 0.4.25-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWopenproj
IPS_Package_Name: SUNWopenproj
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/project-management/openproj >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnu-findutils
IPS_Package_Name: SUNWgnu-findutils
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: file/gnu-findutils >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-menu-editor
IPS_Package_Name: SUNWgnome-menu-editor
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/xdg/menu-editor/alacarte >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtk2-print-cups
IPS_Package_Name: SUNWgtk2-print-cups
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/desktop/gtk2/gtk-backend-cups >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWid3lib
IPS_Package_Name: SUNWid3lib
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/id3lib >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-base-libs-java
IPS_Package_Name: SUNWgnome-base-libs-java
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/java/java-gnome >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWclutter-gtk
IPS_Package_Name: SUNWclutter-gtk
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/clutter/clutter-gtk >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%ifarch i386
%package -n SUNWGParted
IPS_Package_Name: SUNWGParted
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/administration/gparted >= 0.4.5-0.133
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWpython25-twisted-web2
IPS_Package_Name: SUNWpython25-twisted-web2
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdbus-libs
IPS_Package_Name: SUNWdbus-libs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: system/library/libdbus >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython-twisted-web2
IPS_Package_Name: SUNWpython-twisted-web2
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWgnome-sys-suspend
IPS_Package_Name: SUNWgnome-sys-suspend
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWTiff
IPS_Package_Name: SUNWTiff
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/library/libtiff >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-python-desktop
IPS_Package_Name: SUNWgnome-python-desktop
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgtop
IPS_Package_Name: SUNWlibgtop
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/libgtop >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWcompizconfig-python
IPS_Package_Name: SUNWcompizconfig-python
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-compizconfig-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWgnome-python26-desktop
IPS_Package_Name: SUNWgnome-python26-desktop
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/python-gnome-desktop-26 >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWopensolaris-backgrounds-xtra
IPS_Package_Name: SUNWopensolaris-backgrounds-xtra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/background/opensolaris-backgrounds-extra >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefox-bookmark
IPS_Package_Name: SUNWfirefox-bookmark
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: web/data/firefox-bookmarks >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpilot-link
IPS_Package_Name: SUNWpilot-link
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: communication/pda/pilot-link >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-dictionary
IPS_Package_Name: SUNWgnome-dictionary
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/gnome-dictionary >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-screenshot
IPS_Package_Name: SUNWgnome-screenshot
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: gnome/gnome-screenshot >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgir-repository
IPS_Package_Name: SUNWgir-repository
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-icon-theme
IPS_Package_Name: SUNWgnome-icon-theme
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/gnome-icon-theme >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-spell
IPS_Package_Name: SUNWgnome-spell
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/spell-checking/enchant >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-en
IPS_Package_Name: SUNWmyspell-dictionary-en
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/en >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmoovida
IPS_Package_Name: SUNWmoovida
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWxdg-sound-theme
IPS_Package_Name: SUNWxdg-sound-theme
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/sound/xdg-sound-theme >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWbluefish
IPS_Package_Name: SUNWbluefish
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: web/editor/bluefish >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n SUNWcompiz-fusion-main
IPS_Package_Name: SUNWcompiz-fusion-main
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/compiz/plugin/compiz-fusion-main >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true
%endif

%package -n SUNWmysql-python26
IPS_Package_Name: SUNWmysql-python26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/python-2/python-mysql-26 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWevolution-jescs
IPS_Package_Name: SUNWevolution-jescs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-pdf-viewer
IPS_Package_Name: SUNWgnome-pdf-viewer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/pdf-viewer/evince >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWsongbird
IPS_Package_Name: SUNWsongbird
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-themes-only-extra
IPS_Package_Name: SUNWgnome-themes-only-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/gnome-themes-extra >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWcups-manager
IPS_Package_Name: SUNWcups-manager
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: print/cups/system-config-printer >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-gui-test
IPS_Package_Name: SUNWgnome-gui-test
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibpigment-python26
IPS_Package_Name: SUNWlibpigment-python26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWxscreensaver-hacks-gl
IPS_Package_Name: SUNWxscreensaver-hacks-gl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/xscreensaver/hacks/hacks-gl >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython26-xdg
IPS_Package_Name: SUNWpython26-xdg
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/gnome-incorporation = *
Renamed_To: library/python-2/python-xdg-26 >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython25-cssutils
IPS_Package_Name: SUNWpython25-cssutils
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibatk
IPS_Package_Name: SUNWlibatk
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/atk >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWglibmm
IPS_Package_Name: SUNWglibmm
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/c++/glibmm >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-common-devel
IPS_Package_Name: SUNWgnome-common-devel
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: developer/gnome/gettext >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-camera-gimp-plugin
IPS_Package_Name: SUNWgnome-camera-img-editor-plugin
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: image/editor/gimp/plugin/gimp-gtkam >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWdbus-glib
IPS_Package_Name: SUNWdbus-glib
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: system/library/libdbus-glib >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython25-twisted
IPS_Package_Name: SUNWpython25-twisted
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgnomecanvas
IPS_Package_Name: SUNWlibgnomecanvas
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/libgnomecanvas >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWpython-notify
IPS_Package_Name: SUNWpython-notify
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-config
IPS_Package_Name: SUNWgnome-config
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/config/gconf >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibxmlpp
IPS_Package_Name: SUNWlibxmlpp
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/c++/libxml++ >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgtkmm
IPS_Package_Name: SUNWgtkmm
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/c++/gtkmm >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-help-viewer
IPS_Package_Name: SUNWgnome-help-viewer
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/help-viewer/yelp >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWcompiz
IPS_Package_Name: SUNWcompiz
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: desktop/compiz >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-cs
IPS_Package_Name: SUNWdesktop-other-l10n-cs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-de
IPS_Package_Name: SUNWdesktop-other-l10n-de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-es
IPS_Package_Name: SUNWdesktop-other-l10n-es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-extra
IPS_Package_Name: SUNWdesktop-other-l10n-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-fr
IPS_Package_Name: SUNWdesktop-other-l10n-fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-hu
IPS_Package_Name: SUNWdesktop-other-l10n-hu
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-it
IPS_Package_Name: SUNWdesktop-other-l10n-it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-ja
IPS_Package_Name: SUNWdesktop-other-l10n-ja
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-ko
IPS_Package_Name: SUNWdesktop-other-l10n-ko
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-noinst
IPS_Package_Name: SUNWdesktop-other-l10n-noinst
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-pl
IPS_Package_Name: SUNWdesktop-other-l10n-pl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-ptBR
IPS_Package_Name: SUNWdesktop-other-l10n-ptBR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-rtl
IPS_Package_Name: SUNWdesktop-other-l10n-rtl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-ru
IPS_Package_Name: SUNWdesktop-other-l10n-ru
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-sv
IPS_Package_Name: SUNWdesktop-other-l10n-sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-zhCN
IPS_Package_Name: SUNWdesktop-other-l10n-zhCN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-zhHK
IPS_Package_Name: SUNWdesktop-other-l10n-zhHK
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWdesktop-other-l10n-zhTW
IPS_Package_Name: SUNWdesktop-other-l10n-zhTW
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-de-DE
IPS_Package_Name: SUNWfirefoxl10n-de-DE
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-es-ES
IPS_Package_Name: SUNWfirefoxl10n-es-ES
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-extra
IPS_Package_Name: SUNWfirefoxl10n-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-fr-FR
IPS_Package_Name: SUNWfirefoxl10n-fr-FR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-hi-IN
IPS_Package_Name: SUNWfirefoxl10n-hi-IN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-it-IT
IPS_Package_Name: SUNWfirefoxl10n-it-IT
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-ja-JP
IPS_Package_Name: SUNWfirefoxl10n-ja-JP
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-ko-KR
IPS_Package_Name: SUNWfirefoxl10n-ko-KR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-pl-PL
IPS_Package_Name: SUNWfirefoxl10n-pl-PL
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-pt-BR
IPS_Package_Name: SUNWfirefoxl10n-pt-BR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-ru-RU
IPS_Package_Name: SUNWfirefoxl10n-ru-RU
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-sv-SE
IPS_Package_Name: SUNWfirefoxl10n-sv-SE
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-zh-CN
IPS_Package_Name: SUNWfirefoxl10n-zh-CN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfirefoxl10n-zh-TW
IPS_Package_Name: SUNWfirefoxl10n-zh-TW
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWfsexam
IPS_Package_Name: SUNWfsexam
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-cs
IPS_Package_Name: SUNWgnome-img-editor-help-cs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-de
IPS_Package_Name: SUNWgnome-img-editor-help-de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-es
IPS_Package_Name: SUNWgnome-img-editor-help-es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-extra
IPS_Package_Name: SUNWgnome-img-editor-help-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-fr
IPS_Package_Name: SUNWgnome-img-editor-help-fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-it
IPS_Package_Name: SUNWgnome-img-editor-help-it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-ko
IPS_Package_Name: SUNWgnome-img-editor-help-ko
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-pl
IPS_Package_Name: SUNWgnome-img-editor-help-pl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-ru
IPS_Package_Name: SUNWgnome-img-editor-help-ru
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-sv
IPS_Package_Name: SUNWgnome-img-editor-help-sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-img-editor-help-zhCN
IPS_Package_Name: SUNWgnome-img-editor-help-zhCN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-cs
IPS_Package_Name: SUNWgnome-l10ndocument-cs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-de
IPS_Package_Name: SUNWgnome-l10ndocument-de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-es
IPS_Package_Name: SUNWgnome-l10ndocument-es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-extra
IPS_Package_Name: SUNWgnome-l10ndocument-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-fr
IPS_Package_Name: SUNWgnome-l10ndocument-fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-hi
IPS_Package_Name: SUNWgnome-l10ndocument-hi
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-hu
IPS_Package_Name: SUNWgnome-l10ndocument-hu
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-it
IPS_Package_Name: SUNWgnome-l10ndocument-it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-ja
IPS_Package_Name: SUNWgnome-l10ndocument-ja
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-ko
IPS_Package_Name: SUNWgnome-l10ndocument-ko
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-noinst
IPS_Package_Name: SUNWgnome-l10ndocument-noinst
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-pl
IPS_Package_Name: SUNWgnome-l10ndocument-pl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-ptBR
IPS_Package_Name: SUNWgnome-l10ndocument-ptBR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-rtl
IPS_Package_Name: SUNWgnome-l10ndocument-rtl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-sv
IPS_Package_Name: SUNWgnome-l10ndocument-sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-zhCN
IPS_Package_Name: SUNWgnome-l10ndocument-zhCN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-zhHK
IPS_Package_Name: SUNWgnome-l10ndocument-zhHK
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10ndocument-zhTW
IPS_Package_Name: SUNWgnome-l10ndocument-zhTW
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-cs
IPS_Package_Name: SUNWgnome-l10nmessages-cs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-de
IPS_Package_Name: SUNWgnome-l10nmessages-de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-es
IPS_Package_Name: SUNWgnome-l10nmessages-es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-extra
IPS_Package_Name: SUNWgnome-l10nmessages-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-fr
IPS_Package_Name: SUNWgnome-l10nmessages-fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-hi
IPS_Package_Name: SUNWgnome-l10nmessages-hi
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-hu
IPS_Package_Name: SUNWgnome-l10nmessages-hu
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-it
IPS_Package_Name: SUNWgnome-l10nmessages-it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-ja
IPS_Package_Name: SUNWgnome-l10nmessages-ja
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-ko
IPS_Package_Name: SUNWgnome-l10nmessages-ko
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-noinst
IPS_Package_Name: SUNWgnome-l10nmessages-noinst
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-pl
IPS_Package_Name: SUNWgnome-l10nmessages-pl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-ptBR
IPS_Package_Name: SUNWgnome-l10nmessages-ptBR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-rtl
IPS_Package_Name: SUNWgnome-l10nmessages-rtl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-ru
IPS_Package_Name: SUNWgnome-l10nmessages-ru
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-sv
IPS_Package_Name: SUNWgnome-l10nmessages-sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-zhCN
IPS_Package_Name: SUNWgnome-l10nmessages-zhCN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-zhHK
IPS_Package_Name: SUNWgnome-l10nmessages-zhHK
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnome-l10nmessages-zhTW
IPS_Package_Name: SUNWgnome-l10nmessages-zhTW
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWlibgmime
IPS_Package_Name: SUNWlibgmime
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/gmime >= 0.5.11-0.133
Renamed_To: consolidation/desktop/gnome-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-cs
IPS_Package_Name: SUNWmyspell-dictionary-cs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/myspell/dictionary/cs >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-de
IPS_Package_Name: SUNWmyspell-dictionary-de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/myspell/dictionary/de >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-es
IPS_Package_Name: SUNWmyspell-dictionary-es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/es >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-extra
IPS_Package_Name: SUNWmyspell-dictionary-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/extra >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-fr
IPS_Package_Name: SUNWmyspell-dictionary-fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/fr >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-hu
IPS_Package_Name: SUNWmyspell-dictionary-hu
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/hu >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-it
IPS_Package_Name: SUNWmyspell-dictionary-it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/it >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-noinst
IPS_Package_Name: SUNWmyspell-dictionary-noinst
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/noinst >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-pl
IPS_Package_Name: SUNWmyspell-dictionary-pl
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/myspell/dictionary/pl >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-ptBR
IPS_Package_Name: SUNWmyspell-dictionary-ptBR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/myspell/dictionary/pt_br >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-ru
IPS_Package_Name: SUNWmyspell-dictionary-ru
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: library/myspell/dictionary/ru >= 0.5.11-0.133
PkgBuild_Make_Empty_Package: true

%package -n SUNWmyspell-dictionary-sv
IPS_Package_Name: SUNWmyspell-dictionary-sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/myspell/dictionary/sv >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWstardict
IPS_Package_Name: SUNWstardict
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: system/desktop/stardict >= 0.5.11-0.133
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-de
IPS_Package_Name: SUNWtgnome-l10n-ui-de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-es
IPS_Package_Name: SUNWtgnome-l10n-ui-es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-fr
IPS_Package_Name: SUNWtgnome-l10n-ui-fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-it
IPS_Package_Name: SUNWtgnome-l10n-ui-it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-ja
IPS_Package_Name: SUNWtgnome-l10n-ui-ja
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-ko
IPS_Package_Name: SUNWtgnome-l10n-ui-ko
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-ptBR
IPS_Package_Name: SUNWtgnome-l10n-ui-ptBR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-ru
IPS_Package_Name: SUNWtgnome-l10n-ui-ru
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-sv
IPS_Package_Name: SUNWtgnome-l10n-ui-sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-zhCN
IPS_Package_Name: SUNWtgnome-l10n-ui-zhCN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-zhHK
IPS_Package_Name: SUNWtgnome-l10n-ui-zhHK
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWtgnome-l10n-ui-zhTW
IPS_Package_Name: SUNWtgnome-l10n-ui-zhTW
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-de-DE
IPS_Package_Name: SUNWthunderbirdl10n-de-DE
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-es-ES
IPS_Package_Name: SUNWthunderbirdl10n-es-ES
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-extra
IPS_Package_Name: SUNWthunderbirdl10n-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-fr-FR
IPS_Package_Name: SUNWthunderbirdl10n-fr-FR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-it-IT
IPS_Package_Name: SUNWthunderbirdl10n-it-IT
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-ja-JP
IPS_Package_Name: SUNWthunderbirdl10n-ja-JP
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-ko-KR
IPS_Package_Name: SUNWthunderbirdl10n-ko-KR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-pl-PL
IPS_Package_Name: SUNWthunderbirdl10n-pl-PL
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-pt-BR
IPS_Package_Name: SUNWthunderbirdl10n-pt-BR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-ru-RU
IPS_Package_Name: SUNWthunderbirdl10n-ru-RU
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-sv-SE
IPS_Package_Name: SUNWthunderbirdl10n-sv-SE
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-zh-CN
IPS_Package_Name: SUNWthunderbirdl10n-zh-CN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWthunderbirdl10n-zh-TW
IPS_Package_Name: SUNWthunderbirdl10n-zh-TW
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n codeina
IPS_Package_Name: codec/install/codeina
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n moovida
IPS_Package_Name: desktop/media-player/moovida
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n moovida-plugins
IPS_Package_Name: desktop/media-player/moovida/moovida-plugins
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n songbird
IPS_Package_Name: desktop/media-player/songbird
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n virt-manager
IPS_Package_Name: desktop/virt-manager
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.6.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n gdesklets
IPS_Package_Name: gnome/desklet/gdesklets
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n gdesklets-extra
IPS_Package_Name: gnome/desklet/gdesklets-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n opensolaris-backgrounds
IPS_Package_Name: gnome/theme/background/opensolaris-backgrounds
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/background/os-backgrounds >= 0.5.11-0.148
PkgBuild_Make_Empty_Package: true

%package -n opensolaris-backgrounds-extra
IPS_Package_Name: gnome/theme/background/opensolaris-backgrounds-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: gnome/theme/background/os-backgrounds-extra >= 0.5.11-0.148
PkgBuild_Make_Empty_Package: true

%package -n neutral_plus_inv
IPS_Package_Name: gnome/theme/cursor/neutral_plus_inv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n gir-repository
IPS_Package_Name: library/desktop/gobject/gir-repository
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n pigment
IPS_Package_Name: library/desktop/pigment
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.3.17
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n cssutils-24
IPS_Package_Name: library/python-2/cssutils-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n pysqlite-24
IPS_Package_Name: library/python-2/pysqlite-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.4.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-dbus-24
IPS_Package_Name: library/python-2/python-dbus-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-gnome-desktop-24
IPS_Package_Name: library/python-2/python-gnome-desktop-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-gnome-extras-24
IPS_Package_Name: library/python-2/python-gnome-extras-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-gnome-libs-24
IPS_Package_Name: library/python-2/python-gnome-libs-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-gst-24
IPS_Package_Name: library/python-2/python-gst-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-gtk-vnc-24
IPS_Package_Name: library/python-2/python-gtk-vnc-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.3.10
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-imaging-24
IPS_Package_Name: library/python-2/python-imaging-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-notify-24
IPS_Package_Name: library/python-2/python-notify-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.1.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-pigment-26
IPS_Package_Name: library/python-2/python-pigment-26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.3.12
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-twisted-24
IPS_Package_Name: library/python-2/python-twisted-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-twisted-web2-24
IPS_Package_Name: library/python-2/python-twisted-web2-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-xdg-24
IPS_Package_Name: library/python-2/python-xdg-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n pyyaml-24
IPS_Package_Name: library/python-2/pyyaml-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n simplejson-24
IPS_Package_Name: library/python-2/simplejson-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n simplejson-devel-26
IPS_Package_Name: library/python-2/simplejson-devel-26
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/python-2/simplejson-26 >= 0.5.11-0.135
PkgBuild_Make_Empty_Package: true

%package -n evolution-jescs
IPS_Package_Name: mail/evolution/connector/evolution-jescs
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n plugin-lightning
IPS_Package_Name: mail/thunderbird/plugin/plugin-lightning
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: mail/thunderbird/plugin/thunderbird-lightning >= 0.5.11-0.134
PkgBuild_Make_Empty_Package: true

%package -n opensolaris-welcome
IPS_Package_Name: release/opensolaris-welcome
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n zfs-auto-snapshot
IPS_Package_Name: service/storage/zfs-auto-snapshot
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/time-slider >= 0.2.96-0.142
PkgBuild_Make_Empty_Package: true

%package -n opensolaris-gdm-themes
IPS_Package_Name: system/display-manager/opensolaris-gdm-themes
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n plugin-java
IPS_Package_Name: web/browser/firefox/plugin/plugin-java
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: consolidation/desktop/desktop-incorporation = *
Renamed_To: web/browser/firefox/plugin/firefox-java >= 0.5.11-0.134
PkgBuild_Make_Empty_Package: true

%ifarch i386
%package -n xvm-gui
IPS_Package_Name: xvm-gui
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%ifarch i386
%package -n system_xvm_xvm-gui
IPS_Package_Name: system/xvm/xvm-gui
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
%endif

%package -n python-25
IPS_Package_Name: runtime/python-25
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.5.4
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n ctypes-24
IPS_Package_Name: library/python-2/ctypes-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-extra-24
IPS_Package_Name: library/python-2/python-extra-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-mysql-24
IPS_Package_Name: library/python-2/python-mysql-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-zope-interface-24
IPS_Package_Name: library/python-2/python-zope-interface-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n python-24
IPS_Package_Name: runtime/python-24
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.4.6
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n gok
IPS_Package_Name: gnome/accessibility/gok
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.30.1
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-guide
IPS_Package_Name: SUNWgetting-started-guide
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-de
IPS_Package_Name: SUNWgetting-started-l10n-de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-es
IPS_Package_Name: SUNWgetting-started-l10n-es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-extra
IPS_Package_Name: SUNWgetting-started-l10n-extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-fr
IPS_Package_Name: SUNWgetting-started-l10n-fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-it
IPS_Package_Name: SUNWgetting-started-l10n-it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-ja
IPS_Package_Name: SUNWgetting-started-l10n-ja
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-ko
IPS_Package_Name: SUNWgetting-started-l10n-ko
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-ptBR
IPS_Package_Name: SUNWgetting-started-l10n-ptBR
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-ru
IPS_Package_Name: SUNWgetting-started-l10n-ru
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-sv
IPS_Package_Name: SUNWgetting-started-l10n-sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-zhCN
IPS_Package_Name: SUNWgetting-started-l10n-zhCN
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-zhHK
IPS_Package_Name: SUNWgetting-started-l10n-zhHK
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWgetting-started-l10n-zhTW
IPS_Package_Name: SUNWgetting-started-l10n-zhTW
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started
IPS_Package_Name: release/getting-started
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_de
IPS_Package_Name: release/getting-started/locale/de
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_es
IPS_Package_Name: release/getting-started/locale/es
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_extra
IPS_Package_Name: release/getting-started/locale/extra
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_fr
IPS_Package_Name: release/getting-started/locale/fr
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_it
IPS_Package_Name: release/getting-started/locale/it
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_ja
IPS_Package_Name: release/getting-started/locale/ja
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_ko
IPS_Package_Name: release/getting-started/locale/ko
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_pt_br
IPS_Package_Name: release/getting-started/locale/pt_br
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_ru
IPS_Package_Name: release/getting-started/locale/ru
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_sv
IPS_Package_Name: release/getting-started/locale/sv
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_zh_cn
IPS_Package_Name: release/getting-started/locale/zh_cn
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_zh_hk
IPS_Package_Name: release/getting-started/locale/zh_hk
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n getting-started_zh_tw
IPS_Package_Name: release/getting-started/locale/zh_tw
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n gnome-system-tools
IPS_Package_Name: desktop/administration/gnome-system-tools
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.30.0
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n hamster
IPS_Package_Name: desktop/time-tracking/hamster
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 2.30.2
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package -n SUNWcompiz-bcop
IPS_Package_Name: SUNWcompiz-bcop
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.8.4
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: desktop/compiz/bcop >= 0.5.11-0.175
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWgnugetopt
IPS_Package_Name: SUNWgnugetopt
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 1.1.4
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: developer/gnu-getopt >= 0.5.11-0.175
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%package -n SUNWmm-common
IPS_Package_Name: SUNWmm-common
SUNW_Pkg: SUNWobsolete-gnome
IPS_component_version: 0.9.2
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Renamed_To: library/desktop/c++/mm-common >= 0.5.11-0.175
Renamed_To: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%changelog
* Wed May 18 2011 - Alan.Coopersmith@oracle.com
- SUNWxwsvr: add rename for pre-build-130 name of SUNWxscreensaver
  (moved from X)
* Thu Apr 14 2011 - Michal.Pryc@Oracle.Com
- desktop/administration/gnome-system-tools: Added as obsolete.
* Tue Jan 18 2011 - laszlo.peter@oracle.com
- create
