#
# spec file for package SUNWlibgdata
#
# includes module(s): libgdata
#
%define owner jouby 
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libgdata_64 = libgdata.spec
%endif

%include base.inc
%use libgdata= libgdata.spec

Name:                SUNWlibgdata
IPS_package_name:    library/desktop/libgdata
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:             libgdata is a collection library providing GObject-based interfaces and classes for commonly used data structures
Version:             %{libgdata.version}

SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
License:              LGPL v2
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc

Requires:            SUNWlibsoup
Requires:            SUNWglib2
Requires:            SUNWgnome-config
Requires:            SUNWgobject-introspection
BuildRequires:       SUNWglib2-devel
BuildRequires:       SUNWlibgnome-keyring
BuildRequires:       SUNWlibsoup

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name


%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libgdata_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%libgdata.prep -d %name-%version/%base_arch


%build
%ifarch amd64 sparcv9
export PKG_CONFIG_LIBDIR=%{_pkg_config_path64}
#disable it until libsoup2 64bit build ready
#%libgdata_64.build -d %name-%version/%_arch64
unset PKG_CONFIG_LIBDIR
%endif

export PKG_CONFIG_LIBDIR=%{_pkg_config_path}
%libgdata.build -d %name-%version/%base_arch
unset PKG_CONFIG_LIBDIR


%install
%ifarch amd64 sparcv9
#%libgdata_64.install -d %name-%version/%_arch64
%endif

%libgdata.install -d %name-%version/%base_arch


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
#%{_datadir}/*
%dir %attr (0755, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/locale/*
%dir %attr (0755, root, other) %{_datadir}/locale/*/*
%{_datadir}/gtk-doc/html/gdata/*.html
%{_datadir}/gtk-doc/html/gdata/*.png
%{_datadir}/gtk-doc/html/gdata/gdata.devhelp*
%{_datadir}/gtk-doc/html/gdata/index.sgml
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/gtk-doc/html/gdata/style.css
%{_datadir}/gir-1.0/GData-0.0.gir
%{_libdir}/girepository-1.0/GData-0.0.typelib

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Fri Apr 30 2010 - yuntong.jin@sun.com
- Change ownership to jouby
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Fix %files.
* Wed Jan 13 2010 - christian.kelly@sun.com
- Fix %files.
* Tus Oct 20 2009 - jerry.tan@sun.com
- import to solaris
* Fri Jul 27 2007 - dougs@truemail.co.th
- Initial spec


