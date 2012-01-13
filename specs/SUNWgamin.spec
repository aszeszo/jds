#
# spec file for package SUNWgamin, SUNWgamin-devel
#
# includes module(s): gamin
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%include Solaris.inc

%include base.inc
%use gamin = gamin.spec

Name:			SUNWgamin
License:                %{gamin.license} 
IPS_package_name: library/file-monitor/gamin
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:		%{gamin.summary}
Version:		%{gamin.version}
SUNW_Copyright:		%{name}.copyright
SUNW_BaseDir:		%{_basedir}
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
Source:			%{name}-manpages-0.1.tar.gz
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWglib2
BuildRequires: SUNWglib2-devel

%package devel
Summary:		%{summary} - developer files
SUNW_BaseDir:		%{_basedir}
Requires:		%{name}

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%base_arch
%gamin.prep -d %name-%version/%base_arch
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%gamin.build -d %name-%version/%base_arch

%install
rm -rf $RPM_BUILD_ROOT
%gamin.install -d %name-%version/%base_arch
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.pyo" -exec rm -f {} ';'
# move python stuff to vendor-packages
(
  cd $RPM_BUILD_ROOT%{_libdir}/python*
  mv site-packages vendor-packages
  rm vendor-packages/*.la
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d %{base_arch}/gamin-%{gamin.version} README AUTHORS
%doc(bzip2) -d %{base_arch}/gamin-%{gamin.version} ChangeLog NEWS COPYING
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libexecdir}/gam_server
%{_libdir}/python%{default_python_version}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files devel
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_includedir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
* Wed Oct 14 2009 - lin.ma@sun.com
- Remove .pyo
* Wed Sep 18 2008 - lin.ma@sun.com
- Update copyright
* Tue May 27 2008 - damien.carbery@sun.com
- Add %dir %attr for %{_datadir}.
* Mon May 26 2008 - lin.ma@sun.com
- CR#6683160, added manpages.
* Sat Oct 13 2007 - lin.ma@sun.com
- Initial FEN backend
* Sun Apr 15 2007 - dougs@truemail.co.th
- Initial version



