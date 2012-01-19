#
# spec file for package SUNWcairomm
#
# includes module(s): cairomm
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet

%include Solaris.inc
%use cairomm = cairomm.spec

Name:                    SUNWcairomm
IPS_package_name:        library/desktop/c++/cairomm
License:                 LGPL v2.1
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 cairomm - C++ API for the Cairo Graphics Library
Version:                 %{cairomm.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWcairo
BuildRequires: SUNWcairo-devel
BuildRequires: SUNWsigcpp
BuildRequires: SUNWsigcpp-devel

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name
Requires: SUNWcairo-devel
Requires: SUNWsigcpp-devel

%prep
rm -rf %name-%version
mkdir %name-%version
%cairomm.prep -d %name-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"
export PERL_PATH=/usr/perl5/bin/perl
%cairomm.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%cairomm.install -d %name-%version
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc(bzip2) -d cairomm-%{cairomm.version} COPYING NEWS ChangeLog
%doc -d cairomm-%{cairomm.version} README AUTHORS
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/cairomm/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Sun Mar 02 2008 - simon.zheng@sun.com
- Correct package version number.
* Tue Feb 19 2008 - ghee.teo@sun.com
- Updated after review.
* Fri Jan 08 2008 - ghee.teo@sun.com
- Modified SFEcairomm.spec to make SUNWcairomm.spec and cairomm.spec
* Mon Nov 12 2007 - daymobrew@users.sourceforge.net
- Bump to 1.4.6.
* Wed Sep 19 2007 - trisk@acm.jhu.edu
- Bump to 1.4.4
* Fri Aug 17 2007 - trisk@acm.jhu.edu
- Bump to 1.4.2
* Sun Feb 25 2007 - laca@sun.com
- create



