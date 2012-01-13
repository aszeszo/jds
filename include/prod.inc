#
# Default settings for GNOME packages on Solaris
#
# Copyright (c) 2007, 2011, Oracle and/or its affiliates. All rights reserved.
#
SUNW_ProdName:             GNOME
SUNW_ProdVers:             2.30.0

%define default_pkg_version 2.30.0
%define default_python_version 2.6

%define __spec_install_post spec-install-post.sh
%define __pkgbuild_default_mogrify_rules desktop.trans

%{?sf_download:#}%define sf_download http://downloads.sourceforge.net

%{?jds_version:#}%define jds_version JDSosol
%define default_category   GNOME2,application,%{jds_version}
%{?support_level:#}%define support_level      unsupported

Vendor:			   Oracle Corporation
%{?desktop_build:IPS_Vendor_Version:        0.%{desktop_build}}

%define                    pkg_prefix SUNW

%define                    restart_fmri $BASEDIR/share/desktop-cache/restart_fmri

# ChangeLog:
#
# 2011-02-15  Laszlo (Laca) Peter  <laca@sun.com>
# - define IPS_Vendor_Version if the desktop_build macro is defined
# 2009-10-08  Laszlo (Laca) Peter  <laca@sun.com>
# - define default_python_version
# 2009-04-03  Laszlo (Laca) Peter  <laca@sun.com>
# - define restart_fmri
# 2007-09-27  Laszlo (Laca) Peter  <laca@sun.com>
# - move tjds build option to options.inc
# 2007-03-15  Laszlo (Laca) Peter  <laca@sun.com>
# - create by moving product specific stuff out of Solaris.inc
