#
#
# spec file for package SUNWclutter
#
# includes module(s): clutter
#
# Copyright (c) 2008, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
%include Solaris.inc
%use clutter = clutter.spec

Name:                    SUNWclutter
License:                 %{clutter.license} 
IPS_package_name:        library/desktop/clutter
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 clutter - a library for creating fast, visually rich and animated graphical user interfaces.
Version:                 %{clutter.version}
URL:                     http://www.clutter-project.org/
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:		 SUNWclutter.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWgobject-introspection
Requires: SUNWgtk3
Requires: SUNWglib-json
Requires: SUNWcogl
Requires: SUNWxorg-mesa
BuildRequires: SUNWgobject-introspection-devel
BuildRequires: SUNWgtk3-devel
BuildRequires: SUNWglib-json-devel
BuildRequires: SUNWcogl-devel
BuildRequires: SUNWuiu8
BuildRequires: SUNWxwinc
BuildRequires: SUNWxorg-headers
BuildRequires: SUNWxorg-mesa

%package devel
Summary:                 %{summary} - developer files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name
Requires: SUNWgtk3-devel

%if %build_l10n
%package l10n
IPS_package_name:        library/desktop/clutter/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}
%endif

%prep
rm -rf %name-%version
mkdir %name-%version
%clutter.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar -xf -

# Force building with mesa headers & libraries to make sure we build the
# same on all systems, whether or not proprietary GL from Sun or nVidia is
# also installed and don't end up accidentally depending on those.
# Unfortunately, xscreensaver is hardcoded to use <GL/gl.h> style paths,
# so we create local install path to work around that.
mkdir -p mesa/GL
ln -s /usr/include/mesa/*.h mesa/GL
%define mesa_includes -I%{_builddir}/%name-%version/mesa
%define mesa_libpath -L/usr/lib/mesa

%build
export CFLAGS="%{optflags} %mesa_includes -I/usr/X11/include"
export CXXFLAGS="%{?cxx_optflags} %mesa_includes"
export LDFLAGS="%mesa_libpath %{?_ldflags} -L/usr/X11/lib -R/usr/X11/lib -lX11"
%clutter.build -d %name-%version

%install
%clutter.install -d %name-%version
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/girepository-1.0/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gir-1.0/*
%dir %attr (0755, root, bin) %{_mandir}
%{_mandir}/*/*
%doc -d clutter-%{clutter.version} README
%doc(bzip2) -d clutter-%{clutter.version} ChangeLog COPYING NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif
 
%changelog
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Update packaging for clutter 1.6.16 release.
* Fri Oct 22 2010 - brian.cameron@oracle.com
- Remove gir-repository dependency.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Mar 05 2010 lin.ma@sun.com
- Copy from xscreensaver, enable SPARC build
* Mon Jan 04 2009 - halton.huo@sun.com
- Move CFLAGS and LDFLAGS from base-specs/clutter.spec
* Tue Aug 25 2009 - lin.ma@sun.com
- Add SUNWgir-repository dependency
* Tue Aug 25 2009 - halton.huo@sun.com
- Update files when version bump to 1.0.2
- Add dependency to SUNWgobject-introspection
* Fri Jun 26 2009  Chris.wang@sun.com
- Change owner to lin
* Thu Mar 26 2009  Chris.wang@sun.com
- Correct copyright file in file section
* Tue Mar 24 2009  chris.wang@sun.com
- Add SUNWxorg-mesa to Require
* Fri Feb 20 2009  chris.wang@sun.com
- Add manpage
* Tue Jul  1 2008  chris.wang@sun.com 
- Initial build.

