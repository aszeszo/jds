#
# spec file for package SUNWlibgnomecanvas
#
# includes module(s): libgnomecanvas
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc
%include base.inc

%use libgnomecanvas = libgnomecanvas.spec

Name:                    SUNWlibgnomecanvas
IPS_package_name:        library/desktop/libgnomecanvas
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GNOME canvas library
Version:                 %{libgnomecanvas.version}
License:                 %{libgnomecanvas.license}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWgtk2
Requires: SUNWlibglade
Requires: SUNWlibart
Requires: SUNWlibmsr
BuildRequires: SUNWlibm
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWlibart-devel
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWgnome-xml-share

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n content
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%libgnomecanvas.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

#	we need this because libgnomecanvas-scan cannot find libXrand
#	without it - this seems solairs specific so it is here
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/X11/lib"
%libgnomecanvas.build -d %name-%version/%{base_arch}


%install
rm -rf $RPM_BUILD_ROOT

%libgnomecanvas.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d  %{base_arch} libgnomecanvas-%{libgnomecanvas.version}/README
%doc -d  %{base_arch} libgnomecanvas-%{libgnomecanvas.version}/AUTHORS
%doc(bzip2) -d  %{base_arch} libgnomecanvas-%{libgnomecanvas.version}/ChangeLog
%doc(bzip2) -d  %{base_arch} libgnomecanvas-%{libgnomecanvas.version}/po/ChangeLog
%doc(bzip2) -d  %{base_arch} libgnomecanvas-%{libgnomecanvas.version}/COPYING.LIB
%doc(bzip2) -d  %{base_arch} libgnomecanvas-%{libgnomecanvas.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/libglade
%dir %attr (0755, root, sys) %{_datadir}

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gtk-doc
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %dir %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Tue Mar 31 2009 - dave.lin@sun.com
- initial version(split from SUNWgnome-base-libs)


