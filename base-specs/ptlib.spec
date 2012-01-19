#
# spec file for package ptlib
#
# Copyright 2007 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner hawklu 

%define OSR 4034:2.0

Name:         ptlib
License:      MPL
Group:        System/Libraries
Version:      2.6.7
Release:      1
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      PTLib Class Library
Source:       http://ftp.gnome.org/pub/GNOME/sources/ptlib/2.6/%{name}-%{version}.tar.gz

# owner:davelam date:2006-04-14 type:branding
# use cxxflags to fix build problem
# updated by elaine
Patch1:       ptlib-01-cxxflags.diff

# owner:elaine date:2008-11-11 type:branding
# help ekiga to find the ptlib.pc
Patch3:       ptlib-03-no-public-pc.diff

# owner:elaine date:2009-07-14 type:bug
# sourceforge:2821205
Patch5:       ptlib-05-allocator-and-new.diff

# owner:elaine date:2009-07-16 type:bug
# bugster:6739228
Patch8:       ptlib-08-enable-mjpeg.diff

# owner:brian date:2011-02-13 type:bug
Patch9:       ptlib-10-operator-new-delete.diff

# temporary build fix, please find the root cause and fix properly
Patch11:      ptlib-11-tmp-bld.diff

URL:          http://www.ekiga.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on

%description
PTLib is a moderately large class library that was created many years
ago as a method to produce applications that run on both Microsoft
Windows and the X Window System.

%package devel
Summary: Headers for developing programs that will use ptlib
Group:      Development/Libraries
Requires:   %{name}

%description   devel
This package contains the headers that programmers will need to develop
applications which will use ptlib.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch3 -p1
%patch5 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1

# symlink the make dir to bin so that ptlib-config is found by ekiga
# ln -s make bin

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

cd plugins
aclocal
autoconf
cd ..
aclocal
autoconf

# unix.mak adds this to a STDCCFLAGS, which is also used for C++ builds
export RPM_OPT_FLAGS=""

export CFLAGS="%optflags"
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags"
./configure \
	--prefix=%{_prefix} \
        --libdir=%{?ekiga_libdir}%{?!ekiga_libdir:%{_libdir}} \
        --bindir=%{_bindir} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
        --enable-plugins \
        --enable-resolver \
        --enable-opal \
	--disable-openssl \
        --enable-sunaudio \
	--enable-url \
	--enable-http\
	--enable-httpforms\
	--enable-httpsvc\
        --enable-v4l2

make -j $CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT

# need the -f to remove write protected file
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr (-, root, root)
%{ekiga_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{ekiga_libdir}/*.so

%changelog
* Fri Jun 04 2010 - brian.lu@sun.com
- Bump to 2.6.7
* Thu Jan 07 2009 - brian.lu@sun.com
- Change the owner to hawklu
* Fri Sep 25 2009 - brian.lu@sun.com
- Add patch ptlib-09-build-fail.diff
- Enable following options
  --enable-http
  --enable-httpforms
  --enable-httpsvc

* Wed Sep 23 2009 - dave.lin@sun.com
- Bump to 2.6.5
* Thu Jul 16 2009 - elaine.xiong@sun.com
- Add a new patch to workaround CR#6739228 then Ekiga sticks to
  use MJPEG format instead of YUV format until this bug is 
  resolved.
* Tue Jul 14 2009 - elaine.xiong@sun.com
- Bump to 2.6.4. Update patches. Enable URL feature.
* Mon Jul 06 2009 - elaine.xiong@sun.com
- Disable openssl explicitly.
* Mon Mar 23 2009 - elaine.xiong@sun.com
- Add a new patch to fix bugzilla#576260.
* Thu Nov 20 2008 - elaine.xiong@sun.com
- Bump to 2.4.2.
* Fri Nov 14 2008 - elaine.xiong@sun.com
- Rename to ptlib.spec from pwlib.spec.
- Bump to 2.4.1. Add new patches and remove obsolete patches.
- update build options for new version.
* Wed Sep 03 2008 - elaine.xiong@sun.com
- Add note to not bump to 2.3.1 as ekiga depends on it.
* Sun Dec 23 2007 - patrick.ale@gmail.com
- Download tar.gz instead of tar.bz2 . bz2 tarball is N/A
* Mon Nov 19 2007 - elaine.xiong@sun.com
- Add pwlib-06-idct-mlib.diff to fix bugzilla#498082.
* Tue Sep 18 2007 - damien.carbery@sun.com
- Bump to 1.10.10. Remove upstream patches, 07-sunaudio-vol-range and
  05-medialib. Renumber rest.
* Tue Jun 26 2007 - elaine.xiong@sun.com
- Add pwlib-07-sunaudio-vol-range.diff to fix bugster6572725.
  Change pwlib-05-medialib.diff status to upstreamable.
* Tue Jun 12 2007 - elaine.xiong@sun.com
- Add pwlib-06-rm-flush.diff to fix bugzilla445066. 
* Wed Apr 25 2007 - elaine.xiong@sun.com
- Update owner name for pwlib-05-medialib.diff.
* Thu Apr 19 2007 - elaine.xiong@sun.com
- Bump to 1.10.7.
* Thu Apr  5 2007 - laca@sun.com
- Create
