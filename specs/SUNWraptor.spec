#
# Spec file for package SUNWraptor
#
# include module(s): raptor
#
# Copyright (c) 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
# 

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use raptor_64 = raptor.spec
%endif

%include base.inc
%use raptor = raptor.spec

Name:                 SUNWraptor
IPS_package_name:     library/raptor
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:              RDF Parser Library - RDF parser utility
Version:              %{raptor.version}

SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
License:             %{raptor.license}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

Requires: SUNWlxsl
Requires: SUNWlxml
Requires: SUNWcurl
Requires: SUNWgss
Requires: SUNWgnu-idn
Requires: SUNWopensslr


%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%raptor_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%raptor.prep -d %name-%version/%base_arch

%build
%ifarch amd64 sparcv9
export PKG_CONFIG_LIBDIR=%{_pkg_config_path64}
%raptor_64.build -d %name-%version/%_arch64
unset PKG_CONFIG_LIBDIR
%endif

export PKG_CONFIG_LIBDIR=%{_pkg_config_path}
%raptor.build -d %name-%version/%base_arch
unset PKG_CONFIG_LIBDIR

%install

%ifarch amd64 sparcv9
%raptor_64.install -d %name-%version/%_arch64
%endif

%raptor.install -d %name-%version/%base_arch

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc -d %{base_arch} raptor-%{raptor.version}/README
%doc -d %{base_arch} raptor-%{raptor.version}/AUTHORS
%doc(bzip2) -d %{base_arch} raptor-%{raptor.version}/NEWS
%doc(bzip2) -d %{base_arch} raptor-%{raptor.version}/COPYING
%doc(bzip2) -d %{base_arch} raptor-%{raptor.version}/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libraptor*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libraptor*.so*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*.1
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*.3

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%changelog
* Sun Sep 13 2009 - dave.lin@sun.com
- Add "Summary" line.
* Thu Aug 06 2009 - christian.kelly@sun.com
- Many lines commented out for some reason. Un-comment them to allow package to 
  build.
* Fri Jul 31 2009 <jerry.tan@sun.com>
- add raptor into spec-files
* Tue Feb 12 2008 <pradhap (at) gmail.com>
- Bumped up the version to 1.4.14
* Mon Nov 06 2006 - Eric Boutilier
- Fixed attributes and created devel sub pkg
* Wed Sep 27 2006 - Eric Boutilier
- Initial spec


