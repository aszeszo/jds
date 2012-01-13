# 
# spec file for package SUNWgnome-xml-root and SUNWgnome-xml-share
#
# includes module(s): sgml-common docbook-dtds docbook-style-dsssl
#                     docbook-style-xsl
#                     all of the above originally taken from Fedora Core 6
#
# Copyright 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#

Name:    data/docbook
Version: 1.0
Summary: Obsolete data/docbook
IPS_Package_Name: data/docbook
SUNW_Pkg: SUNWgnome-xml
IPS_component_version: 2.30.0
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
Renamed_To: data/sgml-common >= 0.6.3-0.169
Renamed_To: data/xml-common >= 0.6.3-0.169
Renamed_To: data/docbook/docbook-dtds >=1.0-0.169
Renamed_To: data/docbook/docbook-style-dsssl >=1.79-0.169
Renamed_To: data/docbook/docbook-style-xsl >=1.75.2-0.169
Renamed_To: consolidation/desktop/desktop-incorporation = *

%changelog
* Thu Jun 09 2011 - ghee.teo@oracle.com
- Initial version. Replaced those modules from Fedora Core 6 to OEL 6.
  as to fix bugster#7018512.
