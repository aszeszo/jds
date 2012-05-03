#
# spec file for package SUNWgdk-pixbuf
#
# includes module(s): gdk-pixbuf
#
# Copyright (c) 2011, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner chrisk
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define _sysconfdir /etc/%{_arch64}
%use gdkpixbuf_64 = gdk-pixbuf.spec
%endif

%include base.inc
%use gdkpixbuf = gdk-pixbuf.spec

Name:                    SUNWgdk-pixbuf
IPS_package_name:        library/desktop/gdk-pixbuf
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GNOME gdk-pixbuf
Version:                 %{gdkpixbuf.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gdkpixbuf.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:		 %{summary} - development files
SUNW_BaseDir:		 %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWpng-devel
Requires: SUNWglib2-devel

%if %build_l10n
%package l10n
IPS_package_name:        library/desktop/gdk-pixbuf/l10n
Summary:		 %{summary} - l10n content
SUNW_BaseDir:		 %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %{name}
%endif

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%gdkpixbuf_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%gdkpixbuf.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%ifarch amd64 sparcv9
%gdkpixbuf_64.build -d %name-%version/%_arch64
%endif

%gdkpixbuf.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%gdkpixbuf_64.install -d %name-%version/%_arch64
%endif

%gdkpixbuf.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir} -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT%{_libdir} -name "*.a" -exec rm {} \;

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}

$RPM_BUILD_ROOT%{_bindir}/gdk-pixbuf-query-loaders \
    $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so \
    | sed -e "s%%$RPM_BUILD_ROOT%%%%" \
    > $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache


%ifarch amd64 sparcv9
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}/%{_arch64}

$RPM_BUILD_ROOT%{_bindir}/%{_arch64}/gdk-pixbuf-query-loaders \
    $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gdk-pixbuf-2.0/*/loaders/*.so \
    | sed -e "s%%$RPM_BUILD_ROOT%%%%" \
    > $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gdk-pixbuf-2.0/2.10.0/loaders.cache

rm $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/gdk-pixbuf-csource
%endif

unset LD_LIBRARY_PATH

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

# The /lib/svc/method/pixbuf-loaders-installer doesn't seem to work anymore
#%post
#%restart_fmri pixbuf-loaders-installer

%files
%defattr (-, root, bin)

%{_libdir}/libgdk_pixbuf*
%{_libdir}/gdk-pixbuf-2.0/2.10.0/*

%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/girepository-1.0/GdkPixbuf-2.0.typelib
%{_libdir}/%{_arch64}/gdk-pixbuf-2.0/2.10.0/*
%{_libdir}/%{_arch64}/libgdk_pixbuf*
%{_bindir}/%{_arch64}/gdk-pixbuf-query-loaders
%{_bindir}/%{_arch64}/gdk-pixbuf-pixdata
%endif

%{_libdir}/girepository-1.0/GdkPixbuf-2.0.typelib
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-query-loaders
%{_bindir}/gdk-pixbuf-pixdata

%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gir-1.0/GdkPixbuf-2.0.gir

%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/*
%{_mandir}/man3/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %dir %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gtk-doc

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %dir %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Tue May 01 2012 - brian.cameron@oracle.com
- Fix packaging after updating to 2.26.1.  Add include gnome-incorporation.inc.
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Created.

