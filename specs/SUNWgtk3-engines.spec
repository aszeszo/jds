#
# spec file for package SUNWgtk3-engines
#
# includes module(s): gtk3-engines
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use engines_64 = gtk3-engines.spec
%endif

%include base.inc

%use engines = gtk3-engines.spec

Name:                    SUNWgtk3-engines
IPS_package_name:        gnome/theme/gtk3-engines
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Engines for GTK3 Themes
Version:                 %{engines.version}
License:                 %{engines.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWgtk3
BuildRequires: SUNWgtk3-devel
BuildRequires: SUNWicon-naming-utils

Requires: SUNWgtk3
Requires: SUNWcairo
Requires: SUNWglib2
Requires: SUNWlibmsr

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
Requires:                %{name}

%package extra
IPS_package_name:        gnome/theme/gtk3-engines-extra
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 %{summary} - extra themes
SUNW_BaseDir:            %{_basedir}
Requires:                %{name}
%include gnome-incorporation.inc

%if %build_l10n
%package l10n
IPS_package_name:        gnome/theme/gtk3-engines/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}
%endif

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%engines_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%engines.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%ifarch amd64 sparcv9
%engines_64.build -d %name-%version/%_arch64
%endif

%engines.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%engines_64.install -d %name-%version/%_arch64
%endif

%engines.install -d %name-%version/%{base_arch}

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%{_libdir}/gtk-3.0/*/engines/libclearlooks.so
%{_libdir}/gtk-3.0/*/engines/libhcengine.so
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libclearlooks.so
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libhcengine.so
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-engines
%{_datadir}/themes/Clearlooks/*
%{_datadir}/themes/GNOME3/*

%doc -d %{base_arch} gtk-engines-%{engines.version}/README
%doc -d %{base_arch} gtk-engines-%{engines.version}/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/clearlooks/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/hc/AUTHORS
%doc(bzip2) -d %{base_arch} gtk-engines-%{engines.version}/COPYING
%doc(bzip2) -d %{base_arch} gtk-engines-%{engines.version}/NEWS
%doc(bzip2) -d %{base_arch} gtk-engines-%{engines.version}/ChangeLog
%doc(bzip2) -d %{base_arch} gtk-engines-%{engines.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files extra
%defattr(-, root, bin)
%{_libdir}/gtk-3.0/*/engines/libcrux-engine.so 
%{_libdir}/gtk-3.0/*/engines/libglide.so 
%{_libdir}/gtk-3.0/*/engines/libindustrial.so 
%{_libdir}/gtk-3.0/*/engines/libmist.so 
%{_libdir}/gtk-3.0/*/engines/libredmond95.so 
%{_libdir}/gtk-3.0/*/engines/libthinice.so 
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libcrux-engine.so 
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libglide.so 
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libindustrial.so 
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libmist.so 
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libredmond95.so 
%{_libdir}/%{_arch64}/gtk-*/3.*/engines/libthinice.so 
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/themes/Crux/*
%{_datadir}/themes/Industrial/*
%{_datadir}/themes/Mist/*
%{_datadir}/themes/Redmond/*
%{_datadir}/themes/ThinIce/*

%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/crux/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/glide/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/industrial/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/mist/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/redmond/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/thinice/AUTHORS

%files devel
%defattr(-, root, bin)
%ifarch amd64 sparcv9
%endif
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Thu Jul 07 2011 - brian.cameron@oracle.com
- Created.

