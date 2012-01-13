#
# spec file for package SUNWlibxmlpp
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner kevmca

%define OSR LFI#105446 (gnome Exec. summary):n/a

%include Solaris.inc

%define OSR 9812:2.6

Name:           SUNWlibxmlpp
IPS_package_name: library/c++/libxml++
Meta(info.classification): %{classification_prefix}:Development/C++
License:        LGPLv2
Version:        2.26.1
Summary:        C++ Wrapper for the libxml2 XML Library
Source:         http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.26/libxml++-%{version}.tar.bz2
SUNW_Basedir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
URL:            http://libxmlplusplus.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       SUNWlxmlr
Requires:       SUNWglibmm
Requires:       SUNWlxml
Requires:       SUNWlibmsr
Requires:       SUNWsigcpp
Requires:       SUNWzlib
BuildRequires:  SUNWsigcpp-devel
BuildRequires:  SUNWglibmm-devel
BuildRequires:  SUNWbtool
BuildRequires:  consolidation/desktop/gnome-incorporation

%package devel
Summary:        %{summary} - development files
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:       %name
Requires:       SUNWglibmm-devel

%description
libxml++ is a C++ API for the popular libxml XML parser, written in C. 
libxml is famous for its high performance and compliance to standard 
specifications, but its C API is quite difficult even for common tasks. 

%prep
%setup -q -n libxml++-%version

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
export LDFLAGS="%_ldflags"

./configure --prefix=%{_prefix} \
            --mandir=%{_mandir} \
            --libdir=%{_libdir} \
            --libexecdir=%{_libexecdir} \
            --sysconfdir=%{_sysconfdir} \
            --disable-python

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING AUTHORS NEWS ChangeLog README
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/libxml*/include/*
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/libxml*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Tue Sep 01 2009 - dave.lin@sun.com
- Bump to 2.26.1
* Tue Mar 17 2009 - dave.lin@sun.com
- Bump to 2.26.0
* Fri Mar 13 2009 - dave.lin@sun.com
- Bump to 2.24.3
* Thu Sep 25 2008 - dave.lin@sun.com
- Define include dir under %{_libdir}.
* Wed Sep 24 2008 - dave.lin@sun.com
- Remove the following line in devel pkg which is already defined in base pkg.
    %{_libdir}/libxml++*
* Tue Sep 23 2008 - dave.lin@sun.com
- Define %{_datadir}/doc/libxml* explicitly to get rid of licensing/copyright files in devel pkg.
* Thu Sep 11 2008 - kevin.mcareavey@sun.com
- Add %doc to %files for copyright
* Wed Aug 27 2008 - kevin.mcareavey@sun.com
- Fixed source url
* Tue Aug 26 2008 - kevin.mcareavey@sun.com
- Cleanup for spec-files-other integration
- Bump to 2.23.2
* Fri Aug 17 2007 - trisk@acm.jhu.edu
- Bump to 2.19.1
* Fri Jun 30 2006 - laca@sun.com
- bump to 2.14.0
- rename to SFElibxmlpp
- update file attributes
* Thu Nov 17 2005 - laca@sun.com
- create



