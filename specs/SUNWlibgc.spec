#
# spec file for package SUNWlibgc
#
# includes module(s): libgc
#
# Copyright (c) 2006, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libgc64 = libgc.spec
%endif

%include base.inc
%use libgc = libgc.spec

Name:                    SUNWlibgc
IPS_package_name:        library/gc
Meta(info.classification): %{classification_prefix}:Development/C++
Summary:                 Boehm-Demers-Weiser garbage collector for C/C++
Version:                 %{libgc.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GPL v2,MIT
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: system/library/math

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libgc64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%libgc.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%libgc64.build -d %name-%version/%_arch64
%endif

%libgc.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libgc64.install -d %name-%version/%_arch64
%endif

%libgc.install -d %name-%version/%{base_arch}

# Deliver atomic_ops headers into the /usr/include/gc directory, so they do
# not confuse users with the system atomic_ops(3C) interfaces.
#
mv $RPM_BUILD_ROOT%{_includedir}/atomic_ops $RPM_BUILD_ROOT%{_includedir}/gc
mv $RPM_BUILD_ROOT%{_includedir}/atomic_ops.h $RPM_BUILD_ROOT%{_includedir}/gc
mv $RPM_BUILD_ROOT%{_includedir}/atomic_ops_malloc.h $RPM_BUILD_ROOT%{_includedir}/gc
mv $RPM_BUILD_ROOT%{_includedir}/atomic_ops_stack.h $RPM_BUILD_ROOT%{_includedir}/gc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{base_arch}/gc-%{libgc.version}alpha6/doc/README
%doc %{base_arch}/gc-%{libgc.version}alpha6/README.QUICK
%doc(bzip2) %{base_arch}/gc-%{libgc.version}alpha6/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, sys) %{_datadir}
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%{_datadir}/libatomic_ops

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_mandir}/man?/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gc

%changelog
* Fri Sep 09 2011 - brian.cameron@oracle.com
- Add libatomic-ops to the package.
* Fri Apr 30 2010 - yuntong.jin@sun.com
- Change the ownership to jouby 
* Thu Mar 27 2008 - halton.huo@sun.com
- Add copyright file
* Sun Mar 02 2008 - simon.zheng@sun.com
- Correct package version number.
* Thu Jan 03 2008 - nonsea@users.sourceforge.net
- Use base spec libgc.spec
* Mon Oct 15 2007 - nonsea@users.sourceforge.net
- Bump to 7.0
- s/gc%{version}/gc-%{version}/g
- Add *.pc to %files devel
* Thu Jul  6 2006 - laca@sun.com
- rename to SFEhp-gc
- delete -share subpkg
- update file attributes
- delete unnecessary env variables
* Mon Jan 30 2006 - glynn.foster@sun.com
- Initial version

