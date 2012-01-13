#
# spec file for package SUNWgnome-img-editor-help
#
# includes module(s): gimp-help
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner leon.sha
#
%include Solaris.inc

%use gimp_help = gimp-help.spec

Name:                    SUNWgnome-img-editor-help
IPS_package_name:        image/editor/gimp/gimp-help
Meta(info.classification): %{classification_prefix}:Applications/Graphics and Imaging
Summary:                 The Gimp image editor - on-line help documents
Version:                 %{gimp_help.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gimp_help.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-img-editor
BuildRequires: SUNWgnome-img-editor-devel
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWgnome-xml-share
BuildRequires: SUNWgsed

%package                 de
Summary:                 Gimp on-line help in German
Requires:                SUNWgnome-img-editor-help

%package                 es
Summary:                 Gimp on-line help in Spanish
Requires:                SUNWgnome-img-editor-help

%package                 fr
Summary:                 Gimp on-line help in French
Requires:                SUNWgnome-img-editor-help

%package                 it
Summary:                 Gimp on-line help in Italian
Requires:                SUNWgnome-img-editor-help

%package                 ko
Summary:                 Gimp on-line help in Korean
Requires:                SUNWgnome-img-editor-help

%package                 pl
Summary:                 Gimp on-line help in Polish
Requires:                SUNWgnome-img-editor-help

%package                 ru
Summary:                 Gimp on-line help in Russian
Requires:                SUNWgnome-img-editor-help

%package                 sv
Summary:                 Gimp on-line help in Swedish
Requires:                SUNWgnome-img-editor-help

%package                 cs
Summary:                 Gimp on-line help in Czech
Requires:                SUNWgnome-img-editor-help

%package                 zhCN
Summary:                 Gimp on-line help in Simplified Chinese
Requires:                SUNWgnome-img-editor-help

%package                 extra
Summary:                 Gimp on-line help in other languages
Requires:                SUNWgnome-img-editor-help

%package                 -n gimp_help_de
IPS_package_name:        image/editor/gimp/locale/de
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_es
IPS_package_name:        image/editor/gimp/locale/es
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_fr
IPS_package_name:        image/editor/gimp/locale/fr
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_it
IPS_package_name:        image/editor/gimp/locale/it
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_ko
IPS_package_name:        image/editor/gimp/locale/ko
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_pl
IPS_package_name:        image/editor/gimp/locale/pl
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_ru
IPS_package_name:        image/editor/gimp/locale/ru
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_sv
IPS_package_name:        image/editor/gimp/locale/sv
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_cs
IPS_package_name:        image/editor/gimp/locale/cs
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_zhCN
IPS_package_name:        image/editor/gimp/locale/zh_cn
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%package                 -n gimp_help_extra
IPS_package_name:        image/editor/gimp/locale/extra
SUNW_Pkg:                SUNWgnome-img-editor-help
IPS_component_version: %{gimp_help.version}
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.0.0
IPS_legacy: false
Meta(pkg.obsolete): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
PkgBuild_Make_Empty_Package: true

%prep
rm -rf %name-%version
mkdir %name-%version
%gimp_help.prep -d %name-%version

%build
%gimp_help.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gimp_help.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):unsupported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/en
%{_datadir}/gimp/*/help/images/*.png
%{_datadir}/gimp/*/help/images/callouts/*.png
%{_datadir}/gimp/*/help/images/dialogs/*.png
%{_datadir}/gimp/*/help/images/dialogs/examples/*.{png,gif,jpg,mng}
%{_datadir}/gimp/*/help/images/filters/*.png
%{_datadir}/gimp/*/help/images/filters/examples/*.{png,jpg,mng,xcf}
%{_datadir}/gimp/*/help/images/glossary/*.png
%{_datadir}/gimp/*/help/images/math/*.png
%{_datadir}/gimp/*/help/images/menus/*.png
%{_datadir}/gimp/*/help/images/menus/*.jpg
%{_datadir}/gimp/*/help/images/preferences/*.png
%{_datadir}/gimp/*/help/images/tool-options/*.png
%{_datadir}/gimp/*/help/images/toolbox/*.png
%{_datadir}/gimp/*/help/images/tutorials/*.{png,jpg}
%{_datadir}/gimp/*/help/images/using/*.{png,jpg}
%{_datadir}/gimp/2.0/help/images/menus/file/new/logos/chrome.jpg
%{_datadir}/gimp/2.0/help/images/filters/alpha-to-logo/*
%doc -d gimp-help-%{gimp_help.version} AUTHORS README quickreference/README
%doc(bzip2) -d gimp-help-%{gimp_help.version} COPYING ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%files de
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/de
%{_datadir}/gimp/*/help/images/dialogs/de
%{_datadir}/gimp/*/help/images/filters/de
%{_datadir}/gimp/*/help/images/filters/examples/de
%{_datadir}/gimp/*/help/images/math/de
%{_datadir}/gimp/*/help/images/menus/de
%{_datadir}/gimp/*/help/images/preferences/de
%{_datadir}/gimp/*/help/images/toolbox/de
%{_datadir}/gimp/*/help/images/using/de

%files es
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/es
%{_datadir}/gimp/*/help/images/dialogs/es
%{_datadir}/gimp/*/help/images/filters/es
%{_datadir}/gimp/*/help/images/menus/es
%{_datadir}/gimp/*/help/images/preferences/es
%{_datadir}/gimp/*/help/images/tool-options/es
%{_datadir}/gimp/*/help/images/toolbox/es
%{_datadir}/gimp/*/help/images/using/es

%files fr
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/fr
%{_datadir}/gimp/*/help/images/dialogs/fr
%{_datadir}/gimp/*/help/images/filters/fr
%{_datadir}/gimp/*/help/images/filters/examples/fr
%{_datadir}/gimp/*/help/images/menus/fr
%{_datadir}/gimp/*/help/images/preferences/fr
%{_datadir}/gimp/*/help/images/using/fr
%{_datadir}/gimp/*/help/images/toolbox/fr
%{_datadir}/gimp/*/help/images/tutorials/fr

%files it
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/it
%{_datadir}/gimp/*/help/images/dialogs/it
%{_datadir}/gimp/*/help/images/filters/it
%{_datadir}/gimp/*/help/images/filters/examples/it
%{_datadir}/gimp/*/help/images/menus/it
%{_datadir}/gimp/*/help/images/preferences/it
%{_datadir}/gimp/*/help/images/tool-options/it
%{_datadir}/gimp/*/help/images/toolbox/it
%{_datadir}/gimp/*/help/images/tutorials/it
%{_datadir}/gimp/*/help/images/using/it

%files ko
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/ko
%{_datadir}/gimp/*/help/images/dialogs/ko
%{_datadir}/gimp/*/help/images/preferences/ko
%{_datadir}/gimp/*/help/images/toolbox/ko
%{_datadir}/gimp/*/help/images/tutorials/ko
%{_datadir}/gimp/*/help/images/using/ko

%files pl
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/pl

%files ru
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/ru
%{_datadir}/gimp/*/help/images/dialogs/ru
%{_datadir}/gimp/*/help/images/filters/ru
%{_datadir}/gimp/*/help/images/preferences/ru
%{_datadir}/gimp/*/help/images/toolbox/ru
%{_datadir}/gimp/*/help/images/using/ru

%files sv
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gimp/*/help/sv

%files cs
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}

%files zhCN
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}

%files extra
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
# nl locale
%{_datadir}/gimp/*/help/nl
%{_datadir}/gimp/*/help/images/dialogs/nl
%{_datadir}/gimp/*/help/images/preferences/nl
%{_datadir}/gimp/*/help/images/using/nl
%{_datadir}/gimp/*/help/images/toolbox/nl
# no locale
%{_datadir}/gimp/*/help/no
%{_datadir}/gimp/*/help/images/dialogs/no
%{_datadir}/gimp/*/help/images/filters/no
%{_datadir}/gimp/*/help/images/filters/examples/no
%{_datadir}/gimp/*/help/images/math/no
%{_datadir}/gimp/*/help/images/menus/no
%{_datadir}/gimp/*/help/images/preferences/no
%{_datadir}/gimp/*/help/images/using/no
%{_datadir}/gimp/*/help/images/toolbox/no
%{_datadir}/gimp/*/help/images/tutorials/no

%changelog
* Fri Aug 28 2009 - leon.sha@sun.com
- Remove ko and ru locale files if no "--with-l10n" specified.
* Thu Aug 27 2009 - leon.sha@sun.com
- Change own to leon.sha.
* Thu Aug 06 2009 - dave.lin@sun.com
- Remove pl locale files if no "--with-l10n" specified.
* Wed Nov 05 2008 - takao.fujiwara@sun.com
- Updated pkgmap

* Mon Sep 15 2008 - matt.keenan@sun.com
- Update copyright

* Fri Apr 25 2008 - damien.carbery@sun.com
- Add pl package after bump to 2.4.1. Remove obsoleted images.

* Fri Jan 11 2008 - laca@sun.com
- create - split from SUNWgnome-img-editor.spec



