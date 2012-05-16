#
# spec file for package SUNWsigcpp
#
# includes module(s): libsigc++
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner elaine
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use sigcpp_64 = sigcpp.spec
%endif

%include base.inc
%use sigcpp = sigcpp.spec

Name:                    SUNWsigcpp
IPS_package_name:        library/c++/sigcpp
Meta(info.classification): %{classification_prefix}:Development/C++
Summary:                 Libsigc++ - a library that implements typesafe callback system for standard C++ 
Version:                 %{sigcpp.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GNU Lesser General Public License Version 2.1
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: system/library/c++-runtime

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%{_arch64}
%sigcpp_64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%sigcpp.prep -d %name-%version/%{base_arch}
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build

%ifarch amd64 sparcv9
export CFLAGS="%optflags64"
export CXX="${CXX} -norunpath -features=tmplife"
export CXXFLAGS="%cxx_optflags64"
export LDFLAGS="$FLAG64"
%sigcpp_64.build -d %name-%version/%{_arch64}
%endif

export CFLAGS="%optflags"
export CXX="${CXX} -norunpath -features=tmplife"
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags"
%sigcpp.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%sigcpp.install -d %name-%version/%{base_arch}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/libsigc-2.0/examples
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a

%ifarch amd64 sparcv9
%sigcpp_64.install -d %name-%version/%{_arch64}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/libsigc-2.0/examples/%{_arch64}
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/lib*a
%endif


# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/devhelp/books/libsigc++-2.0/libsigc++-2.0.devhelp2
%doc -d %{base_arch}/libsigc++-%{sigcpp.version} AUTHORS README
%doc(bzip2) -d %{base_arch}/libsigc++-%{sigcpp.version} COPYING NEWS
%doc(bzip2) -d %{base_arch}/libsigc++-%{sigcpp.version} ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%{_libdir}/%{_arch64}/sigc++*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/libsigc*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%changelog
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add "License" tag
* Thu Sep 18 2008 - elaine.xiong@sun.com
- Fix install files conflict. 
* Tue Sep 16 2008 - elaine.xiong@sun.com
- Add %doc to %files for new copyright.
* Mon Aug 04 2008 - elaine.xiong@sun.com
- Add manpage.
* Thu Mar 27 2008 - elaine.xiong@sun.com
- Add file SUNWsigcpp.copyright.
* Sun Mar 02 2008 - simon.zheng@sun.com
- Correct package version number.
* Fri Feb 01 2008 - elaine.xiong@sun.com
- create, split from SFEsigcpp.spec


