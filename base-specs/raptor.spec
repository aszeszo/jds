#
# spec file for package raptor
# Copyright (c) 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%define owner jefftsai

%define OSR 12291:1.4.18

Name:                raptor
Summary:             RDF Parser Library - RDF parser utility
License:             LGPL v2
Version:             1.4.19
Distribution:        Java Desktop System
Vendor:              librdf.org
Group:               System/Libraries
URL:                 http://librdf.org/raptor
Source:              http://download.librdf.org/source/raptor-%{version}.tar.gz
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

# date:2009-09-17    owner:jefftsai type:branding
Patch1:              raptor-01-manpage.diff
# date:2012-02-17    bugster:7143950 owner:jefftsai type:bug
Patch2:              raptor-02-cve-2012-037.diff
Docdir:              %{_defaultdocdir}/doc

%description
Raptor is a free software C library that provides a set of parsers  and
serializers that generate Resource Description Framework (RDF)  triples
by parsing syntaxes or serialize the triples into a syntax.

%package devel
Summary:                 Development package for libraptor
%description devel
This package contains the header files and documentation
needed to develop applications with libraptor

%prep
%setup 
%patch1 -p1
%patch2 -p1

%build

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

./configure --prefix=%{_prefix}  \
            --libdir=%{_libdir} \
            --includedir=%{_includedir} \
            --mandir=%{_mandir} \
            --enable-static=no

make 

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libraptor.*
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
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%changelog
* Mon Feb 20 2012 - jeff.cai@oracle.com
- Add patch -02-cve-2012-037 to fix security bug #7143950
* Sat Aug 15 2009 - christian.kelly@sun.com
- Bump to 1.4.19.
* Fri Jul 31 2009 <jerry.tan@sun.com>
- add raptor into spec-files
* Tue Feb 12 2008 <pradhap (at) gmail.com>
- Bumped up the version to 1.4.14
* Mon Nov 06 2006 - Eric Boutilier
- Fixed attributes and created devel sub pkg
* Wed Sep 27 2006 - Eric Boutilier
- Initial spec
