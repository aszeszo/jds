#
# spec file for package SUNWgnome-nettool
#
# includes module(s): gnome-nettool
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#
%include Solaris.inc
%define makeinstall make install
%use nettool = gnome-nettool.spec

Name:          SUNWgnome-nettool
IPS_package_name: desktop/network/gnome-nettool
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       GNOME Network Tools
License:       GPLv2
Version:       %{nettool.version}
Source:        %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:  %{_basedir}
SUNW_Copyright:  %{name}.copyright
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:      library/libgtop
Requires:      library/desktop/libglade
Requires:      library/gnome/gnome-libs
Requires:      gnome/config/gconf
Requires:      service/gnome/desktop-cache
BuildRequires: library/desktop/libglade
BuildRequires: gnome/config/gconf
BuildRequires: developer/gnome/gnome-doc-utils

%package l10n
Summary:       %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir -p %name-%version
%nettool.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="%optflags" 
export RPM_OPT_FLAGS="$CFLAGS"
%nettool.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%nettool.install -d %name-%version
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):supported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache

%postun
%restart_fmri desktop-mime-cache

%files
%doc -d gnome-nettool-%{nettool.version} README AUTHORS
%doc(bzip2) -d gnome-nettool-%{nettool.version} COPYING NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (-, root, sys) %{_datadir}
%dir %attr (-, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/*.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%dir %attr (0755, root, other) %{_datadir}/%{nettool.name}
%dir %attr (0755, root, other) %{_datadir}/%{nettool.name}/dialogs
%{_datadir}/%{nettool.name}/dialogs/*
%dir %attr (0755, root, other) %{_datadir}/%{nettool.name}/pixmaps
%{_datadir}/%{nettool.name}/pixmaps/*
%dir %attr (-, root, other) %{_datadir}/gnome
%dir %attr (-, root, bin) %{_datadir}/gnome/help
#%dir %attr (-, root, other) %{_datadir}/gnome/help/%{nettool.name}
#%dir %attr (-, root, other) %{_datadir}/gnome/help/%{nettool.name}/C
%{_datadir}/gnome/help/%{nettool.name}/C/*
%dir %attr (-, root, bin) %{_datadir}/omf
#%dir %attr (-, root, other) %{_datadir}/omf/%{nettool.name}
%{_datadir}/omf/%{nettool.name}/*-C.omf
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (-, root, other) %{_datadir}/gnome
%dir %attr (-, root, bin) %{_datadir}/gnome/help
#%dir %attr (-, root, other) %{_datadir}/gnome/help/%{nettool.name}
#%dir %attr (-, root, other) %{_datadir}/gnome/help/%{nettool.name}/C
%{_datadir}/gnome/help/*/[a-z]*
%dir %attr (-, root, bin) %{_datadir}/omf
#%dir %attr (-, root, other) %{_datadir}/omf/%{nettool.name}
%{_datadir}/omf/%{nettool.name}/*-[a-z]*.omf

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Tue Sep 23 2008 - dave.lin@sun.com
- Change attribute conflict with SUNWgnome-l10n*
    %{_datadir}/gnome/help/%{nettool.name}
    %{_datadir}/omf/%{nettool.name}
* Wed Sep 10 2008 - ghee.teo@sun.com
- add %doc for copyright files.
* Wed Sep 10 2008 - takao.fujiwara@sun.com
- Updated for l10n omf files.
* Mon Aug 25 2008 - ghee.teo@sun.com
- initial version created



