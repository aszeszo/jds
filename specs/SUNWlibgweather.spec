#
# spec file for package SUNWlibgweather
#
# includes module(s): libgweather
#
# Copyright (c) 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc
%use libgweather = libgweather.spec

Name:                    SUNWlibgweather
IPS_package_name:        library/desktop/libgweather
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:                 Library to access weather information from online services
Version:                 %{libgweather.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GPLv2

BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           SUNWgnome-doc-utils
BuildRequires:           SUNWlibsoup
BuildRequires:           SUNWgnome-config
BuildRequires:           SUNWlibgnome-keyring

%include default-depend.inc
%include gnome-incorporation.inc

%package root
%include default-depend.inc
%include gnome-incorporation.inc
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
Requires:                %{name}

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%libgweather.prep -d %name-%version

%build
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%libgweather.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT

%libgweather.install -d %name-%version

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/libgweather/locations.dtd
%{_datadir}/libgweather/Locations.xml
%{_datadir}/gtk-doc/*
%{_libdir}/libgweather*
%{_libdir}/girepository-1.0
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/gweather-3.0.pc
%{_includedir}/libgweather-3.0/*
%doc libgweather-%{libgweather.version}/data/README
%doc libgweather-%{libgweather.version}/data/README.timezones
%doc(bzip2) libgweather-%{libgweather.version}/COPYING
%doc(bzip2) libgweather-%{libgweather.version}/ChangeLog
%doc(bzip2) libgweather-%{libgweather.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/gir-1.0
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/*
%dir %attr (0755, root, other) %{_datadir}/icons/*/*
%{_datadir}/icons/gnome/*/status/*.png
%{_datadir}/icons/gnome/*/status/*.svg

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/gweather.schemas

%files l10n
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale


%changelog
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Fix packaging for libgweather 3.1.3 release.
* Fri Jan 15 2010 - jeff.cai@sun.com
- Remove locale files without l10n build
- Not run libtoolize
* Wed Jan 13 2010 - christian.kelly@sun.com
- Fix %files.
* Thu Dec 10 2009 - christian.kelly@sun.com
- Separate into own spec (from gnome-panel).

