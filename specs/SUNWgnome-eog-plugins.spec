#
# spec file for package: eog-plugins
#
# includes module(s): eog-plugins
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%{?!pythonver:%define pythonver 2.6}
%use eog_plugins = eog-plugins.spec

Name:                    SUNWgnome-eog-plugins
IPS_package_name:        image/viewer/eog/eog-plugins
Meta(info.classification): %{classification_prefix}:Applications/Graphics and Imaging
Summary:                 A collection of extra eog plugins 
Version:                 %{eog_plugins.version}
SUNW_Copyright:          %{name}.copyright
License:                GPL v2
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-img-viewer
Requires: SUNWlibchamplain
Requires: SUNWgnome-python26
Requires: SUNWpygtk2-26
Requires: SUNWglib2 
Requires: runtime/python-26

BuildRequires: SUNWlibexif
BuildRequires: SUNWgnome-img-viewer-devel
BuildRequires: SUNWgnome-common-devel

%description
eog-plugins is a collection of plugins for use with the Eye of GNOME Image Viewer.
The included plugins provide a map view for where the picture was taken,
display of Exif information, Zoom to fit, etc. 

#%if %build_l10n
#%package l10n
#Summary:                 %{summary} - l10n files
#SUNW_BaseDir:            %{_basedir}
#%include default-depend.inc
#%include gnome-incorporation.inc
#Requires:                %{name}
#%endif

%prep
rm -rf %name-%version
mkdir %name-%version
%eog_plugins.prep -d %name-%version
cd %{_builddir}/%name-%version


%build
export PYTHON=/usr/bin/python%{pythonver}
%eog_plugins.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%eog_plugins.install -d %name-%version

find $RPM_BUILD_ROOT -name "*.pyc" -exec rm {} \;
find $RPM_BUILD_ROOT -name "*.pyo" -exec rm {} \;

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}(eog_plugins):$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a"  -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%defattr (-, root, sys)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/eog
%dir %attr (0755, root, bin) %{_libdir}/eog/plugins
/usr/lib/eog/plugins/*.py
/usr/lib/eog/plugins/*.eog-plugin
/usr/lib/eog/plugins/lib*.so
/usr/lib/eog/plugins/exif-display/*.ui
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/locale/*
%dir %attr (0755, root, other) %{_datadir}/locale/*/*
/usr/share/locale/*/LC_MESSAGES/eog-plugins.mo

%doc  -d eog-plugins-%{eog_plugins.version}  AUTHORS  NEWS README 
%doc(bzip2)  -d eog-plugins-%{eog_plugins.version} ChangeLog COPYING 
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Wen Mar 31 2010 - yuntong.jin@sun.com
- Fix files attr
* Mon Mar 22 2010 - christian.kelly@sun.com
- Grr, typo in libchamplain dep.
* Mon Mar 22 2010 - christian.kelly@sun.com
- s/Requires: SUNWpython26/Requires: runtime/python-26/
* Fri Jan 29 2010 - yuntong.jin@sun.com
- Init 



