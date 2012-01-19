#
# spec file for package SUNWsqlite3
#
# includes module(s): sqlite3 
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner ginnchen
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use sqlite_64= sqlite.spec
%use sqlitetcl_64= sqlitetcl.spec
%endif

%include base.inc

%use sqlite= sqlite.spec
%use sqlitetcl= sqlitetcl.spec

Name:                    SUNWsqlite3
IPS_package_name:        database/sqlite-3
Meta(info.classification): %{classification_prefix}:System/Databases
Summary:                 SQL database engine library
Version:                 %{sqlite.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 Public Domain
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: SUNWunzip

%include default-depend.inc
%include desktop-incorporation.inc

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWsqlite3

%package -n SUNWsqlite3tcl 
IPS_package_name: runtime/tcl-8/tcl-sqlite-3
Meta(info.classification): %{classification_prefix}:Development/Databases
Summary: %{summary} - tcl files 
SUNW_BaseDIR: %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWsqlite3

%package -n SUNWsqlite3docs 
IPS_package_name: database/sqlite-3/documentation
Meta(info.classification): %{classification_prefix}:System/Databases
Summary: %{summary} - Documention 
SUNW_BaseDIR: %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWsqlite3

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64

%sqlite_64.prep -d %name-%version/%_arch64
%sqlitetcl_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%sqlite.prep -d %name-%version/%{base_arch}
%sqlitetcl.prep -d %name-%version/%{base_arch}

%build

%ifarch amd64 sparcv9
%sqlite_64.build -d %name-%version/%_arch64
%sqlitetcl_64.build -d %name-%version/%_arch64
%endif

%sqlite.build -d %name-%version/%{base_arch}
%sqlitetcl.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%sqlite_64.install -d %name-%version/%_arch64
%sqlitetcl_64.install -d %name-%version/%_arch64

rm -f $RPM_BUILD_ROOT/%{_libdir}/%{_arch64}/tcl8.4/sqlite%{version}/pkgIndex.tcl

mkdir -p $RPM_BUILD_ROOT/usr/lib/tcl8.4/sqlite%{version}/%{_arch64}
mv -f $RPM_BUILD_ROOT/usr/lib/%{_arch64}/tcl8.4/sqlite%{version}/libsqlite%{version}.so $RPM_BUILD_ROOT/usr/lib/tcl8.4/sqlite%{version}/%{_arch64}

rm -rf $RPM_BUILD_ROOT/%{_libdir}/%{_arch64}/tcl8.4
rm -rf $RPM_BUILD_ROOT/%{_bindir}/%{_arch64}/
%endif

%sqlite.install -d %name-%version/%{base_arch}
%sqlitetcl.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/sqlite3
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%attr (0444, root, bin) %{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%attr (0444, root, bin) %{_includedir}/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%attr (0444, root, bin) %{_libdir}/%{_arch64}/pkgconfig/*
%endif

%files -n  SUNWsqlite3tcl 
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/tcl8.4/sqlite%{version}/*

%files -n  SUNWsqlite3docs 
%defattr(0444, root, bin, 0755)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc 
%{_datadir}/doc/sqlite3/*                                                         
%changelog
* Wed Jul 13 2011 - ginn.chen@oracle.com
- Fix manpage.
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add 'License' tag
* Tue Nov 02 2010 - brian.lu@oracle.com
- Change permissions of the files under doc/sqlite3 to read only
* Wed May 19 2010 - brian.lu@sun.com
- Change permission mode of header files to 0444
* Fri Jan 15 2010 - brian.lu@sun.com
- initial spec created


