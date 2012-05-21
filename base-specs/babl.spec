#
# spec file for package babl
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner leon.sha
#

%define OSR 9548:0.0.22

Name:         babl
License:      LGPLv3
Group:        Applications/Multimedia
Version:      0.1.2
Release:      1
Distribution: Java Desktop System
Vendor:       www.gegl.org
Summary:      Babl is a dynamic, any to any, pixel format conversion library.
Source:	      ftp://ftp.gtk.org/pub/babl/0.1/%{name}-%{version}.tar.bz2
# date:2010-06-02 owner:yippi type:bug
Patch1:       babl-01-no-pthread.diff
URL:          http://www.gegl.org/babl/
%package devel
Summary:      %{summary} - development files
Group:        System/GUI/GNOME
Requires:     %name 

%prep
%setup -q
%patch1 -p1

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
export CFLAGS="%{optflags}"
export CXXFLAGS="%{?cxx_optflags}"
export LDFLAGS="%{?_ldflags}"
aclocal
libtoolize --force
glib-gettextize --force
automake -a -c -f
autoconf
./configure --prefix=%{_prefix}			\
	    --libdir=%{_libdir}         \
            --sysconfdir=%{_sysconfdir}         \
	    --mandir=%{_mandir}                 \
	    --datadir=%{_datadir}               \
            --infodir=%{_datadir}/info \
        --enable-mmx=no \
        --enable-sse=no
	    		
make -j$CPUS

%install
#rm -rf $RPM_BUILD_ROOT
#rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_libdir}/lib*.so*
%{_libdir}/babl-0.0/*.so*
%{_libdir}/pkgconfig/*

%files devel
%defattr (-, root, root)
%{_includedir}/babl-0.0/babl/*

%changelog
* Tue Jun 08 2010 - brian.cameron@oracle.com
- Update again to 0.1.2 after addressing the compiler issue.
* Fri Jun 04 2010 - brian.cameron@oracle.com
- Backout to 0.1.0 since the compiler has problems building 0.1.2.
* Wed Jun 02 2010 - brian.cameron@oracle.com
- Bump to 0.1.2.
* Tue Sep 01 2009 - leon.sha@sun.com
- Bump to 0.1.0.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change owner of spec and patch to leon.sha.
* Wed Nov 26 2008 - chris.wang@sun.com
- Initial create.
