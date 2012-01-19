#
# spec file for package SUNWgnome-python26-libs
#
# includes module(s): none (obsolete, renamed)
#
# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#

%include Solaris.inc

# the Solaris build this Obsolete package is first delivered to:
%define obsbld 160

Name:              SUNWgnome-python26-libs
IPS_package_name:  library/python-2/python-gnome-libs-26
Summary:           Python 2.6 support libraries for GNOME (obsolete)
Version:           %{default_pkg_version}
SUNW_BaseDir:      %{_basedir}
SUNW_Copyright:    %{name}.copyright
BuildRoot:         %{_tmppath}/%{name}-%{version}-build
IPS_component_version: 0.5.11
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true
Obsoleted_by: library/python-2/pygobject-26 = 2.21.1-0.%{obsbld}
Obsoleted_by: library/python-2/python-gnome-26 = 2.28.1-0.%{obsbld}
Obsoleted_by: library/python-2/pyorbit-26 = 2.24.0-0.%{obsbld}
Obsoleted_by: library/python-2/pygtk2-26 = 2.17.0-0.%{obsbld}
Obsoleted_by: library/python-2/pycairo-26 = 1.8.8-0.%{obsbld}
Obsoleted_by: library/python-2/pygtksourceview2-26 = 2.10.1-0.%{obsbld}
# so that gnome-incorporation is updated
BuildRequires: SUNWgtk2
# so that entire is updated
BuildRequires: consolidation/desktop/gnome-incorporation = *

%changelog
* Fri Feb  4 2011 - laszlo.peter@oracle.com
- create
