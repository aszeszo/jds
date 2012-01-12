#
# spec file for package SUNWvala
#
# Copyright (c) 2007, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s): vala
#
%define owner jouby

%define OSR LFI#105446 (gnome Exec. summary):n/a

%define	src_name vala
%define	src_url	http://download.gnome.org/sources/vala/0.14

Name:                vala 
Summary:             Vala programming language
License:             LGPL v2
Version:             0.14.0
Distribution:        Java Desktop System
Vendor:              Gnome Community
Group:               System/Libraries

Source:              %{src_url}/%{src_name}-%{version}.tar.bz2
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

%package devel
Summary:                 %{summary} - development files
%description devel
This package contains the header files and documentation
needed to develop applications with vala.

%prep
%setup -q -n %{src_name}-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

aclocal-1.11
libtoolize --copy --force 
automake-1.11 -a -f
autoconf -f 
./configure --prefix=%{_prefix}			\
            --bindir=%{_bindir}			\
            --libdir=%{_libdir}			\
            --sysconfdir=%{_sysconfdir}		\
            --includedir=%{_includedir} 	\
            --mandir=%{_mandir}			\
	    --infodir=%{_infodir}		\
	    --disable-static			\
	    --enable-shared

make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_bindir}
%{_bindir}/vala
%{_bindir}/vala-0.14
%{_bindir}/valac-0.14
%ifarch amd64 sparcv9
%{_bindir}/${_arch64}/vala
%{_bindir}/${_arch64}/vala-0.14
%{_bindir}/${_arch64}/valac-0.14
%endif

%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/aclocal
%{_datadir}/devhelp
%{_datadir}/vala-0.14
%{_mandir}

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 0.14.0.
* Wed Jul 06 2011 - brian.cameron@oracle.com
- Bump to 0.12.0.
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Bump to 0.8.1.
* Sat Mar  3 2010 - christian.kelly@sun.com
- Bump to 0.8.0.
* Tus Oct 20 2009 - jerry.tan@sun.com
- import to solaris
* Fri Jul 27 2007 - dougs@truemail.co.th
- Initial spec
