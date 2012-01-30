# Special spec file for obsoleted firefox l10n packages.

# Copyright (c) 2011 Oracle and/or its affiliates. All rights reserved.
#
# Owner: laca
#

%define owner laca

Name:           SUNWfirefoxl10n
Summary:        Obsolete Firefox Localization Package stubs
Version:        6.0
                                                                                
%package  zh-CN 
IPS_package_name: web/browser/firefox/locale/zh_cn
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package zh-TW 
IPS_package_name: web/browser/firefox/locale/zh_tw
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package ja-JP 
IPS_package_name: web/browser/firefox/locale/ja_jp
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package ko-KR 
IPS_package_name: web/browser/firefox/locale/ko_kr
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package de-DE 
IPS_package_name: web/browser/firefox/locale/de_de
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package es-ES 
IPS_package_name: web/browser/firefox/locale/es_es
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package fr-FR 
IPS_package_name: web/browser/firefox/locale/fr_fr
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package it-IT 
IPS_package_name: web/browser/firefox/locale/it_it
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package sv-SE 
IPS_package_name: web/browser/firefox/locale/sv_se
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package pl-PL 
IPS_package_name: web/browser/firefox/locale/pl_pl
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package pt-BR 
IPS_package_name: web/browser/firefox/locale/pt_br
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package ru-RU 
IPS_package_name: web/browser/firefox/locale/ru_ru
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package hi-IN
IPS_package_name: web/browser/firefox/locale/hi_in
SUNW_Pkg: SUNWfirefoxl10n
IPS_component_version: %{version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package extra 
IPS_package_name: web/browser/firefox/locale/extra
SUNW_Pkg: SUNWfirefoxl10n
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
- obsolete all firefoxl10n packages as the are becoming facets of the firefox
  package
* Tue Feb 22 2011 - jacky.cao@oracle.com
- Initial spec
* Thu Apr 7 2011 - rebecca.l.liu@oracle.com
- Update for firefox 4.0
