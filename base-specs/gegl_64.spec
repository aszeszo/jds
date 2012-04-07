#
# spec file for package gegl
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner leon.sha
#

%define OSR 9549:0.0.18

Name:         gegl
License:      Library is LGPLv3, binaries are GPLv3
Group:        Applications/Multimedia
Version:      0.1.2
Release:      1
Distribution: Java Desktop System
Vendor:       Sun Microsystems, Inc.
Summary:      GEGL (Generic Graphics Library) is a graph based image processing framework.
Source:	      ftp://ftp.gimp.org/pub/gegl/0.1/%{name}-%{version}.tar.bz2
URL:          http://www.gegl.org/
#date:2009-01-06 owner:leon.sha type:branding
Patch1:	      gegl-01-build.diff
#date:2009-02-25 owner:leon.sha type:bug bugster:6802192 bugzilla:573073
Patch2:       gegl-02-info-null.diff
%package devel
Summary:      %{summary} - development files
Group:        System/GUI/GNOME
Requires:     %name 

%prep
%setup -q
%patch1 -p1
#%patch2 -p1

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
export CFLAGS="%{optflags} -features=extensions -xunroll=1"
export CXXFLAGS="%{?cxx_optflags}"
export LDFLAGS="%{?_ldflags}"
aclocal
libtoolize --force
glib-gettextize --force
automake -a -c -f
autoconf 
./configure --prefix=%{_prefix}			\
	    --libdir=%{_libdir}			\
	    --sysconfdir=%{_sysconfdir}         \
	    --mandir=%{_mandir}                 \
	    --datadir=%{_datadir}               \
	    --disable-docs			\
	    --infodir=%{_datadir}/info  	\
	    --without-libspiro			\
	    --without-libv4l			\
	    --without-openexr \
	    --enable-mmx=no			\
	    --enable-sse=no
	    		
make -j$CPUS

%install

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_bindir}/*
%{_libdir}/lib*.so*
%{_libdir}/pkgconfig/*
%{_libdir}/gimp
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%files devel
%defattr (-, root, root)
%{_includedir}/*
%{_datadir}/gtk-doc

%changelog
* Wed Jun 09 2010 - dave.lin@sun.com
- Add "-xunroll=1" to fix ube issue(CR6958494).
* Tue Jun 08 2010 - brian.cameron@oracle.com
- Update again to 0.1.2 after addressing the compiler issue.
* Fri Jun 04 2010 - brian.cameron@oracle.com
- Backout to 0.1.0 since the compiler has problems building 0.1.2.
* Wed Jun 02 2010 - brian.cameron@oracle.com
* Tue Sep 01 2009 - leon.sha@sun.com
- Bump to 0.1.0.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change spec and patch owner to leon.sha.
* The Feb 26 2009- chris.wang@sun.com
- Add patch gegl-05-info-null to fix bug 6802192.
* Tue Jan 20 2009 - chris.wang@sun.com
- bump to 0.22, add patch fprintf-null.
* Tue Jan 06 2009 - takao.fujiwara@sun.com
- Add patch g11n-textdomain.diff.
* Wed Nov 26 2008 - chris.wang@sun.com
- Initial create.
