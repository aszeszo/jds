#
# spec file for package libgc
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby
#

%define OSR 7136:7.x

%define real_name gc

Name:			libgc
License:		GPL v2,MIT
Group:			System/Libraries
Version:		7.2
Release:	 	4
Distribution:		Java Desktop System
Vendor:			Other
Summary:		Boehm-Demers-Weiser garbage collector for C/C++
Source:			http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/gc-%{version}alpha6.tar.gz
URL:			http://www.hpl.hp.com/personal/Hans_Boehm/gc/
#date:2008-07-31 owner:jouby type:branding
Patch1:                 libgc-01-man.diff
#date:2009-02-16 owner:jouby type:branding
Patch2:                 libgc-02-rename-libbgc.diff
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
Docdir:			%{_defaultdocdir}/doc
Autoreqprov:		on
Prereq:                 /sbin/ldconfig

%description
Boehm's GC is a garbage collecting storage allocator that is
intended to be used as a plug-in replacement for C's malloc.

%package devel
Summary:		Header files, libraries and development documentation for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{real_name}-%{version}alpha6
%patch1 -p1
%patch2 -p1

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

libtoolize --force
aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf

./configure --prefix=%{_prefix}         \
            --mandir=%{_mandir}         \
            --libdir=%{_libdir}         \
            --libexecdir=%{_libexecdir} \
            --sysconfdir=%{_sysconfdir} \
            --enable-threads=posix      \
            --with-libatomic-ops=no     \
            %gtk_doc_option

make -j $CPUS
make -j $CPUS -C libatomic_ops

%install
make install DESTDIR=$RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C libatomic_ops

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
cp $RPM_BUILD_ROOT%{_datadir}/gc/gc.man $RPM_BUILD_ROOT%{_mandir}/man3/gc.3

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README.QUICK
%{_libdir}/lib*.so*

%files devel
%defattr(-, root, root)
%doc doc/*
%doc %{_mandir}/man?/*
%{_libdir}/libgc.so
%{_libdir}/libgccpp.so
%{_libdir}/libcord.so
%{_includedir}/gc/
%{_includedir}/libgc/
%{_libdir}/pkgconfig/bdw-gc.pc

%changelog
* Fri Sep 09 2011 - brian.cameron@oracle.com
- Bump to 7.2 alpha6 and build libatomic-ops.
* Fri Apr 30 2010 - yuntong.jin@sun.com
- Change the ownership to jouby
* Mon Feb 16 2009 - jerry.tan@sun.com
- change libgc.so to libbgc.so to avoid conflict with sunstudio
* Tue May 27 2008 - halton.huo@sun.com
- Bump to 7.1
* Wed Jan 02 2008 - halton.huo@sun.com
- spilit from SFEbdw-gc.spec
