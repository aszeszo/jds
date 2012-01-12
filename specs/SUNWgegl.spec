#
# spec file for package SUNWgegl
#
# includes module(s):gegl
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner leon.sha

%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use gegl_64 = gegl_64.spec
%endif
%include base.inc
%use gegl = gegl.spec

Name:                    SUNWgegl
License:                 Library is LGPLv3, binaries are GPLv3
IPS_package_name:        image/library/gegl
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 GEGL (Generic Graphics Library) is a graph based image processing framework.
Version:                 %{gegl.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWgegl.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:                SUNWgtk2
Requires:                SUNWgnome-libs
Requires:                SUNWbabl
Requires:                SUNWlibsdl
Requires:                SUNWlibrsvg
Requires:                SUNWlua
BuildRequires:           SUNWgtk2-devel
BuildRequires:           SUNWgnome-libs-devel
BuildRequires:           SUNWbabl-devel
BuildRequires:           SUNWlua

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name
Requires: SUNWglib2-devel

%prep
rm -rf %name-%version
mkdir %name-%version
%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%gegl_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%gegl_64.prep -d %name-%version/%{base_arch}
cd %{_builddir}/%name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar -xf -

%build
%gegl.build -d %name-%version/%{base_arch}
%ifarch amd64 sparcv9
%gegl_64.build -d %name-%version/%_arch64
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%gegl_64.install -d %name-%version/%_arch64
%endif

%gegl.install -d %name-%version/%{base_arch}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d %{base_arch} gegl-%{gegl.version}/AUTHORS
%doc -d %{base_arch} gegl-%{gegl.version}/README
%doc(bzip2) -d %{base_arch} gegl-%{gegl.version}/ChangeLog
%doc(bzip2) -d %{base_arch} gegl-%{gegl.version}/COPYING
%doc(bzip2) -d %{base_arch} gegl-%{gegl.version}/NEWS
%doc(bzip2) -d %{base_arch} gegl-%{gegl.version}/COPYING.LESSER
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}/gegl-0.1
%{_libdir}/%{_arch64}/gegl-0.1/*.so*
%endif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, bin) %{_libdir}/gegl-0.1
%{_libdir}/gegl-0.1/*.so*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%{_mandir}/*/*
%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%dir %attr (0755, root, bin) %{_includedir}/gegl-0.1
%{_includedir}/gegl-0.1/*.h
%dir %attr (0755, root, bin) %{_includedir}/gegl-0.1/operation
%{_includedir}/gegl-0.1/operation/*.h
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %dir %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %dir %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/gtk-doc
%dir %attr (0755, root, bin) %{_datadir}/gtk-doc/html
%dir %attr (0755, root, bin) %{_datadir}/gtk-doc/html/gegl
%{_datadir}/gtk-doc/html/gegl/*

%changelog
* Tue Jun 08 2010 - brian.cameron@oracle.com
- Update again to 0.1.2 after addressing the compiler issue.
* Fri Jun 04 2010 - brian.cameron@oracle.com
- Backout to 0.1.0 since the cmpiler has problems building 0.1.2.
* Fri Jun 26 2009  chris.wang@sun.com
- Change owner to leon.sha
* Thu May 21 2009  chris.wang@sun.com
- In Require section, change SUNWgnome-base-libs-devel to SUNWglib2-devel
  as the original package has been divided into small packages
* Thu Mar 26 2009  chris.wang@sun.com
- Correct copyright file
* Fri Feb 20 2009  chris.wang@sun.com
- Add manpage
* Thu Feb 6  2008 - chris.wang@sun.com
- Add SUNWsdl and SUNWrsvg as required packages
* Tue Dec 16 2008 - chris.wang@sun.com
- Fix SparcV9 file section problem
* Wed Nov 26 2008 - chris.wang@sun.com
- Initial Create



