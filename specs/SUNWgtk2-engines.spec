#
# spec file for package SUNWgtk2-engines
#
# includes module(s): gtk2-engines
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
%use engines_64 = gtk2-engines.spec
%endif

%include base.inc

%use engines = gtk2-engines.spec

Name:                    SUNWgtk2-engines
IPS_package_name:        gnome/theme/gtk2-engines
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Engines for GTK2 Themes
Version:                 %{engines.version}
License:                 %{engines.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWicon-naming-utils

Requires: SUNWgtk2
Requires: SUNWcairo
Requires: SUNWglib2
Requires: SUNWlibmsr

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
Requires:                %{name}

%package extra
IPS_package_name:        gnome/theme/gtk2-engines-extra
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 %{summary} - extra themes
SUNW_BaseDir:            %{_basedir}
Requires:                %{name}
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

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

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin)
%{_libdir}/gtk-2.0/*/engines/libclearlooks.so
%{_libdir}/gtk-2.0/*/engines/libhcengine.so
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libclearlooks.so
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libhcengine.so
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/themes/Clearlooks/*
%{_datadir}/gtk-engines/clearlooks.xml
%{_datadir}/gtk-engines/hcengine.xml

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
%{_libdir}/gtk-2.0/*/engines/libcrux-engine.so 
%{_libdir}/gtk-2.0/*/engines/libglide.so 
%{_libdir}/gtk-2.0/*/engines/libindustrial.so 
%{_libdir}/gtk-2.0/*/engines/libmist.so 
%{_libdir}/gtk-2.0/*/engines/libredmond95.so 
%{_libdir}/gtk-2.0/*/engines/libthinice.so 
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libcrux-engine.so 
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libglide.so 
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libindustrial.so 
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libmist.so 
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libredmond95.so 
%{_libdir}/%{_arch64}/gtk-*/2.*/engines/libthinice.so 
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/themes/Crux/*
%{_datadir}/themes/Industrial/*
%{_datadir}/themes/Mist/*
%{_datadir}/themes/Redmond/*
%{_datadir}/themes/ThinIce/*
%{_datadir}/gtk-engines/crux-engine.xml
%{_datadir}/gtk-engines/glide.xml
%{_datadir}/gtk-engines/industrial.xml
%{_datadir}/gtk-engines/mist.xml
%{_datadir}/gtk-engines/redmond95.xml
%{_datadir}/gtk-engines/thinice.xml

%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/crux/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/glide/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/industrial/AUTHORS
%doc -d %{base_arch} gtk-engines-%{engines.version}/engines/lua/AUTHORS
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

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Fri Nov 20 2009 - christian.kelly@sun.com
- Add %changelog. Fix %files.


