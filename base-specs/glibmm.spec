#
# spec file for package glibmm
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#
%include Solaris.inc

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:                    glibmm
License:        	 LGPL
Group:                   System/Libraries
Version:                 2.24.1
Release:                 1
Distribution:            Java Desktop System
Vendor:                  Gnome Community
Summary:                 glibmm - C++ Wrapper for the Glib2 Library
URL:                     http://www.gtkmm.org/
Source:                  http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.24/%{name}-%{version}.tar.bz2
# date:2008-02-14 owner:gheet type:feature
Patch1:                  glibmm-01-build.diff
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
BuildRequires:           libsigc++-devel >= 2.0.0
BuildRequires:           glib2-devel >= 2.9.0

%package devel
Summary:                 Headers for developing programs that will use %{name}.
Group:                   System/Libraries
Requires:                libsigc++-devel >= 1.2.0
Requires:                glib2-devel >= 2.9.0

%prep
%setup -q -n glibmm-%version
%patch1 -p0

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

aclocal $ACLOCAL_FLAGS -Ibuild
automake --add-missing
autoconf
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir} 
make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Bump to 2.24.1.
* Tue Apr  6 2010 - christian.kelly@oracle.com
- Bump to 2.24.0.
* Sat Mar 13 2010 - christian.kelly@sun.com
- Bump to 2.23.3.
* Mon Feb 15 2010 - christian.kelly@sun.com
- Bump to 2.23.2.
* Tue Jan 26 2010 - christian.kelly@sun.com
- Bump to 2.23.1.
* Tue Jul 28 2009 - christian.kelly@sun.com
- Bump to 2.21.3.
* Wed Jul 15 2009 - christian.kelly@sun.com
- Bump to 2.21.2.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change owner to gheet
* Tue Mar 17 2009 - dave.lin@sun.com
- Bump to 2.20.0
* Fri Mar 13 2009 - dave.lin@sun.com
- Bump to 2.19.8
* Thu Feb 26 2009 - dave.lin@sun.com
- Bump to 2.19.3
* Fri Feb 20 2009 - chris.wang@sun.com
- bump to 2.19.2
* Mon Nov 10 2008 - chris.wang@sun.com
- Change the owner of the spec to chris wang
* Wed Nov 05 2008 - jedy.wang@sun.com
- Change the owner of 01-build.diff to chris.
* Tue Sep 23 2008 - simon.zheng@sun.com
- Bump to 2.18.0.
* Fri Sep 05 2008 - simon.zheng@sun.com
- Bump to 2.17.3.
* Mon Aug 07 2008 - simon.zheng@sun.com
- Bump to 2.17.2. Removed upstream patch 02-m4-macro.diff.
* Mon Jul 21 2008 - simon.zheng@sun.com
- Bump to 2.17.1.
* Tue Jun 17 2008 - simon.zheng@sun.com
- Bump to 2.17.0.
* Thu May 02 2008 - simon.zheng@sun.com
- Bump to 2.16.2.
* Mon Mar 31 2008 - damien.carbery@sun.com
- Bump to 2.16.1.
* Tue Mar 11 2008 - damien.carbery@sun.com
- Bump to 2.16.0. Remove upstream patch 03-overloading-ambiguity.
* Wed Mar  5 2008 - simon.zheng@sun.com
- To fix failure of building with SS11 compiler, add patch
  04-overloading-ambiguity. Add an explicit template specification
  to avoid ction to avoid ambiguity. Fix is from glibmm maintainer
  murrayc@murrayc.com, and also go upstream.
  available on next tarball.
* Tue Mar  4 2008 - damien.carbery@sun.com
- Bump to 2.15.8.
* Tue Feb 26 2008 - damien.carbery@sun.com
- Bump to 2.15.7.
* Mon Feb 25 2008 - damien.carbery@sun.com
- Bump to 2.15.6.
* Mon Feb 18 2008 - damien.carbery@sun.com
- Add patch 02-m4-macro to build on sparc. The GNU m4 check was failing because
  '[Mm]' in the aclocal code was losing the brackets when aclocal/autoconf
  created the configure script.
* Wed Feb 15 2008 - simon.zheng@sun.com
- Correct download URL.
* Tue Feb 14 2008 - simon.zheng@sun.com
- Bump to Version 2.15.5.
- Add glibmm-01-build.diff.
- Remove glimm-01-gtestutils.diff.
* Thu Feb 14 2008 - damien.carbery@sun.com
- Add patch 01-gtestutils to include glib/gtestutils.h in some source files to
  define g_assert macro.
* Tue Feb 12 2008 - ghee.teo@sun.com
- Added all the examples to the /usr/share/doc.
  Also cleaned out %files and %files-devel where are not used here.
* Mon Jan 28 2008 - simon.zheng@sun.com
- Create. Split from SFEglibmm and bump to version 2.14.2.
