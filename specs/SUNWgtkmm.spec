#
#
# spec file for package SUNWgtkmm
#
# includes module(s): gtkmm
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet

%include Solaris.inc

%use gtkmm = gtkmm.spec

Name:                    SUNWgtkmm
IPS_package_name:        library/desktop/c++/gtkmm
License:                 GPLv2, LGPLv2.1
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 gtkmm - C++ Wrapper for the Gtk+ Library
Version:                 %{gtkmm.version}
Source:			 %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Requires: library/desktop/gtk2
Requires: library/c++/glibmm
Requires: library/desktop/c++/cairomm
Requires: system/library/math
Requires: library/c++/sigcpp
Requires: system/library/c++/sunpro
Requires: library/desktop/c++/pangomm
BuildRequires: library/desktop/gtk2
BuildRequires: library/c++/sigcpp
BuildRequires: library/c++/glibmm
BuildRequires: library/desktop/c++/cairomm
BuildRequires: library/desktop/c++/pangomm
BuildRequires: developer/gnome/gnome-doc-utils
BuildRequires: developer/documentation-tool/gtk-doc
BuildRequires: SUNWmm-common

%package devel
Summary:                 gtkmm - C++ Wrapper for the Gtk+ Library - developer files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: library/desktop/gtk2
Requires: library/c++/glibmm
Requires: library/c++/sigcpp

%prep
rm -rf %name-%version
mkdir %name-%version
%gtkmm.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar -xf -

%build
export ACLOCAL_FLAGS="-I /usr/share/aclocal"
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
%gtkmm.build -d %name-%version

%install
%gtkmm.install -d %name-%version

cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d gtkmm-%{gtkmm.version} AUTHORS README
%doc(bzip2) -d gtkmm-%{gtkmm.version} ChangeLog COPYING NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%{_mandir}/*/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%{_libdir}/gtkmm*
%{_libdir}/gdkmm*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtkmm-2.4/demo
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/gtkmm*
%{_datadir}/devhelp
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu Oct 22 2009 - dave.lin@sun.com
- Removed the obsoleted grogram ${_bindir}/demo/jds/bin/gtkmm-demo from %files devel.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change owner to gheet
* Fri Sep 19 2008 - dave.lin@sun.com
- Fix file conflicts in /usr/share/doc/* between base pkg and devel pkg.
* Wed Sep 18 2008 - chris.wang@sun.com
- Update copyright
* Mon Aug 18 2008 - chris.wang@sun.com
- Add manpage
* Thu Jul 30 2008 - chris.wang@sun.com
- Add SUNWpangomm as dependency
* Thu Mar 27 2008 - simon.zheng@sun.com
- Add file SUNWgtkmm.copyright.
* Sun Mar 02 2008 - simon.zheng@sun.com
- Correct package version number.
* Thu Feb 14 2008 - chris.wang@sun.com
- Move gtkmm-demo to /usr/demo/jds/bin per requested by ARC
* Tue Jan 29 2008 - chris.wang@sun.com
- create



