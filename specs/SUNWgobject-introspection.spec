#
# spec file for package SUNWgobject-introspection
#
# includes module(s): gobject-introspection
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
# Note that there are some issues that you need to address to avoid build
# issues when building this module:
#
# 1) For some reason SUNWPython26.spec has a problem with ctypes that causes
#    gobject-introspection to fail to build.  Uninstalling and rebuilding this
#    package from spec-files seems to fix this problem. Need to figure this
#    out and get it fixed in the SUNWPython26 package.
#

%include Solaris.inc

%define pythonver 2.6

%ifarch amd64 sparcv9
%include arch64.inc
%use gi_64 = gobject-introspection.spec
%endif

%include base.inc
%use gi = gobject-introspection.spec

Name:               SUNWgobject-introspection
Summary:            gobject-introspection - GObject introspection support
Version:            %{gi.version}
SUNW_Pkg:            SUNWgobject-introspection
IPS_package_name:   library/desktop/gobject/gobject-introspection
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
SUNW_Copyright:     %{name}.copyright
License:            %{gi.license}
SUNW_BaseDir:       %{_basedir}
BuildRoot:          %{_tmppath}/%{name}-%{version}-build

BuildRequires:      library/glib2
BuildRequires:      library/libffi
BuildRequires:      system/library/iconv/utf-8
BuildRequires:      runtime/python-26
%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:            %{summary} - development files
SUNW_BaseDir: %{_basedir}

%prep
rm -rf %name-%version
mkdir -p %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%{_arch64}
%gi_64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%gi.prep -d %name-%version/%{base_arch}

%build

%ifarch amd64 sparcv9
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="$FLAG64"
export PKG_CONFIG_PATH="%_pkg_config_path64"
%gi_64.build -d %name-%version/%{_arch64}
%endif

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export PKG_CONFIG_PATH="%_pkg_config_path"
%gi.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%gi_64.install -d %name-%version/%{_arch64}
%endif

%gi.install -d %name-%version/%{base_arch}

%ifarch amd64 sparcv9
# Move the .so file into /usr/lib/gobject-introspection/giscanner/64.
#
mkdir $RPM_BUILD_ROOT%{_libdir}/gobject-introspection/giscanner/64
mv $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gobject-introspection/giscanner/_giscanner.so $RPM_BUILD_ROOT%{_libdir}/gobject-introspection/giscanner/64

# Remove the rest of the amd64 version of the Python code.  No need to deliver
# it twice.
#
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gobject-introspection
rm $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/g-ir-scanner
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/g-ir-annotation-tool
%{_bindir}/g-ir-compiler
%{_bindir}/g-ir-generate
%{_bindir}/g-ir-scanner
%{_bindir}/g-ir-doc-tool
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*.so*
%{_libdir}/girepository-1.0/*
%{_libdir}/gobject-introspection/*
%ifarch amd64 sparcv9
%dir %attr(0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/g-ir-annotation-tool
%{_bindir}/%{_arch64}/g-ir-compiler
%{_bindir}/%{_arch64}/g-ir-generate
%{_bindir}/%{_arch64}/g-ir-doc-tool
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/*.so*
%{_libdir}/%{_arch64}/girepository-1.0/*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gir-1.0
%{_datadir}/gobject-introspection-1.0/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc -d %{base_arch}/gobject-introspection-%{version} AUTHORS README COPYING
%doc(bzip2) -d %{base_arch}/gobject-introspection-%{version} COPYING.GPL COPYING.LGPL NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc

%changelog
* Mon Feb 13 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Wed Oct 20 2010 - brian.cameorn@oracle.com
- Fix packaging after bumptin to 0.9.12.
* Sat Aug 14 2010 - brian.cameron@oracle.com
- Fix packaging after bumping to 0.9.3.
* Thu Jul 15 2010 - christian.kelly@oracle.com
- Update %files due to bump.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Apr 09 2010 - brian.cameron@sun.com
- Do not deliver the Python files for both 32-bit and 64-bit.  Move the 64-bit
  _giscanner.so file to /usr/lib/amd64/gobject-introspection/giscanner/64.  The
  64-bit version will not load if it is not in a subdirectory named 64.
* Fri Dec 18 2009 - brian.cameron@sun.com
- Fix packaging for 0.6.7.
* Mon Aug 31 2009 - halton.huo@sun.com
- Enable 64 bit 
* Mon Aug 24 2009 - halton.huo@sun.com
- Move from SFE, spilit base part to base-specs/gobject-introspection
* Wed Aug 05 2009 - Halton Huo  <halton.huo@sun.com>
- Use 0.6.3 tarball release 
- Add crash-compiler.diff to fix #587823
* Fri Jul 03 2009 - Brian Cameron  <brian.cameron@sun.com
- Remove upstream patch gobject-introspection-01-union.diff,
  renumber rest.
* Sat Apr 04 2009 - Brian Cameron  <brian.cameron@sun.com>
- Created.


