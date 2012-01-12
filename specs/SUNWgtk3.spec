#
# spec file for package SUNWgtk3
#
# includes module(s): gtk3
#
# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define _sysconfdir /etc/%{_arch64}
%use gtk_64 = gtk3.spec
%endif

%include base.inc

%use gtk = gtk3.spec

Name:                    SUNWgtk3
IPS_package_name:        library/desktop/gtk3
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GTK+ - GIMP toolkit libraries
Version:                 %{gtk.version}
License:                 %{gtk.license}
#Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWglib2
Requires: SUNWgdk-pixbuf
Requires: SUNWcairo
Requires: SUNWpango
Requires: SUNWlibatk
Requires: SUNWjpg
Requires: SUNWpng
BuildRequires: SUNWTiff
Requires: SUNWTiff
Requires: SUNWlibms
Requires: SUNWdesktop-cache
Requires: x11/library/libxinerama
BuildRequires: SUNWxwplt
BuildRequires: SUNWxwrtl
BuildRequires: SUNWgobject-introspection
BuildRequires: SUNWuiu8
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWgdk-pixbuf-devel
BuildRequires: SUNWcairo-devel
BuildRequires: SUNWpango-devel
BuildRequires: SUNWlibatk-devel
BuildRequires: SUNWpng-devel
BuildRequires: SUNWjpg-devel
BuildRequires: SUNWTiff-devel
BuildRequires: SUNWxorg-headers
BuildRequires: SUNWlibm

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWlibms
Requires: SUNWpng-devel
Requires: SUNWglib2-devel
Requires: SUNWcairo-devel
Requires: SUNWpango-devel
Requires: SUNWlibatk-devel

%package print-cups
IPS_package_name:        library/desktop/gtk3/gtk-backend-cups
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 %{summary} - CUPS Print Backend
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
# static dependencies needed in this package as some of the libraries
# needed to detect the dependencies are built in the same spec but are
# not in the same package (e.g. libatk)
Requires: SUNWglib2
Requires: SUNWcairo
Requires: SUNWpango
Requires: SUNWlibatk
Requires: SUNWgtk3
Requires: SUNWcupsr
BuildRequires: SUNWxwplt
BuildRequires: SUNWxwrtl
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWcairo-devel
BuildRequires: SUNWcupsr

%if %build_l10n
%package l10n
Summary:                 %{summary} - l10n content
Requires: %{name}
%endif

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64

%gtk_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%gtk.prep -d %name-%version/%{base_arch}

#cd %{_builddir}/%name-%version
#gzcat %SOURCE0 | tar xf -

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%ifarch amd64 sparcv9
%gtk_64.build -d %name-%version/%_arch64
%endif

%gtk.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%gtk_64.install -d %name-%version/%_arch64
%endif

%gtk.install -d %name-%version/%{base_arch}

#rm -rf $RPM_BUILD_ROOT%{_mandir}
#cd %{_builddir}/%name-%version/sun-manpages
#make install DESTDIR=$RPM_BUILD_ROOT

# Move demo to demo directory.
#
install -d $RPM_BUILD_ROOT%{_prefix}/demo/jds/bin
mv $RPM_BUILD_ROOT%{_bindir}/gtk3-demo $RPM_BUILD_ROOT%{_prefix}/demo/jds/bin

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/*/immodules/im-[a-wyz]*.so

# on linux, these config files are created in %post
# that would be more complicated on Solaris, especially
# during jumpstart or live upgrade, so it's better to do
# it during the build
$RPM_BUILD_ROOT%{_bindir}/gtk-query-immodules-3.0 \
    $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/*/immodules/im-xim.so \
    | sed -e "s%%$RPM_BUILD_ROOT%%%%" \
    > $RPM_BUILD_ROOT%{_sysconfdir}/gtk-3.0/gtk.immodules

%ifarch amd64 sparcv9
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gtk-3.0/*/immodules/im-[a-wyz]*.so

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}/%{_arch64}

mkdir  -p $RPM_BUILD_ROOT%{_sysconfdir}/%{_arch64}/gtk-3.0

$RPM_BUILD_ROOT%{_bindir}/%{_arch64}/gtk-query-immodules-3.0 \
    $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gtk-3.0/*/immodules/im-xim.so \
    | sed -e "s%%$RPM_BUILD_ROOT%%%%" \
    > $RPM_BUILD_ROOT%{_sysconfdir}/%{_arch64}/gtk-3.0/gtk.immodules

mkdir -p $RPM_BUILD_ROOT%{_prefix}/demo/jds/bin/%{_arch64}
mv $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/gtk3-demo \
    $RPM_BUILD_ROOT%{_prefix}/demo/jds/bin/%{_arch64}
%endif

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

find $RPM_BUILD_ROOT%{_libdir} -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT%{_libdir} -name "*.a" -exec rm {} \;

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri pixbuf-loaders-installer input-method-cache

%files
%doc -d %{base_arch} gtk+-%{gtk.version}/README
%doc -d %{base_arch} gtk+-%{gtk.version}/AUTHORS
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.gtk-async-file-chooser
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.gtk-printing
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-1-0
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-1-2
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-2-0
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-2-2
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-2-4
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-2-6
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-2-8
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/ChangeLog.pre-2-10
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/po-properties/ChangeLog
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/po/ChangeLog
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/COPYING
%doc(bzip2) -d %{base_arch} gtk+-%{gtk.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gtk-update-icon-cache
%{_bindir}/gtk-*3.0
%{_bindir}/%{_arch64}/gtk-*3.0
%{_bindir}/%{_arch64}/gtk-update-icon-cache

%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/gtk*/*/printbackends/libprintbackend-file.so
%{_libdir}/gtk*/*/printbackends/libprintbackend-lpr.so
%{_libdir}/girepository-1.0/*
%{_libdir}/gtk-3.0/3.0.0/immodules
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%{_libdir}/%{_arch64}/gtk*/*/printbackends/libprintbackend-file.so
%{_libdir}/%{_arch64}/gtk*/*/printbackends/libprintbackend-lpr.so
%{_libdir}/%{_arch64}/gtk-3.0/3.0.0/immodules
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}/girepository-1.0
%{_libdir}/%{_arch64}/girepository-1.0/*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/glib-2.0
%{_datadir}/themes
%{_datadir}/gir-1.0/*
%{_datadir}/gtk-3.0/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_bindir}
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %dir %{_prefix}/demo
%dir %attr (0755, root, bin) %dir %{_prefix}/demo/jds
%dir %attr (0755, root, bin) %dir %{_prefix}/demo/jds/bin
%{_prefix}/demo/jds/bin/gtk3-demo
%ifarch amd64 sparcv9
%{_prefix}/demo/jds/bin/{%_arch64}/gtk3-demo
%dir %attr (0755, root, bin) %dir %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gtk-doc
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
#%dir %attr(0755, root, bin) %{_mandir}
#%dir %attr(0755, root, bin) %{_mandir}/man3
#%{_mandir}/man3/*
%dir %attr(0755, root, bin) %{_mandir}/man1

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%ghost %ips_tag(original_name=SUNWgtk3:%{@} preserve=true) %{_sysconfdir}/gtk-3.0/gtk.immodules
%ips_tag(original_name=SUNWgtk3:%{@} preserve=true) %{_sysconfdir}/gtk-3.0/im-multipress.conf
%ifarch amd64 sparcv9
%ghost %ips_tag(original_name=SUNWgtk3:%{@} preserve=true) %{_sysconfdir}/%{_arch64}/gtk-3.0/gtk.immodules
%ips_tag(original_name=SUNWgtk3:%{@} preserve=true) %{_sysconfdir}/%{_arch64}/gtk-3.0/im-multipress.conf
%endif

%files print-cups
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/gtk*/*/printbackends/libprintbackend-cups.so
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/gtk*/*/printbackends/libprintbackend-cups.so
%endif

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %dir %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Fri Aug 26 2011 - brian.cameron@oracle.com
- Fix packaging after updating to GTK3 3.1.12.
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Created.
