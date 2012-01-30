# Special spec file for obsoleted firefox l10n packages.

# Copyright (c) 2011 Oracle and/or its affiliates. All rights reserved.
#
# Owner: laca
#

%define owner laca

Name:           SUNWthunderbirdl10n
Summary:        Obsolete Thunderbird Localization Package stubs
Version:        5.0

%package  zh-CN 
IPS_package_name: mail/thunderbird/locale/zh_cn
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package zh-TW 
IPS_package_name: mail/thunderbird/locale/zh_tw
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package ja-JP 
IPS_package_name: mail/thunderbird/locale/ja
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package ko-KR 
IPS_package_name: mail/thunderbird/locale/ko
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package de-DE 
IPS_package_name: mail/thunderbird/locale/de
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package es-ES 
IPS_package_name: mail/thunderbird/locale/es
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package fr-FR 
IPS_package_name: mail/thunderbird/locale/fr
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package it-IT 
IPS_package_name: mail/thunderbird/locale/it
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package sv-SE 
IPS_package_name: mail/thunderbird/locale/sv
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package pl-PL
IPS_package_name: mail/thunderbird/locale/pl
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package pt-BR
IPS_package_name: mail/thunderbird/locale/pt_br
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package ru-RU
IPS_package_name: mail/thunderbird/locale/ru
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package extra 
IPS_package_name: mail/thunderbird/locale/extra
SUNW_Pkg: SUNWthunderbirdl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%changelog
* Fri Aug 26 2011 - laszlo.peter@oracle.com
- obsolete all thunderbirdl10n packages as the are becoming facets of the
  thunderbird package
* Tue Feb 22 2011 - jacky.cao@oracle.com
- Initial spec
* Mon Jul 25 2011 - rebecca.l.liu@oracle.com
- Updates for Thunderbird 5.0 & Lightning 1.0b5rc1
