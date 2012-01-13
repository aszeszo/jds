#
# spec file for package opal
#
# Copyright 2007 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner hawklu 

%define OSR 4034:2.0

Name:         opal
License:      MPL
Group:        System/Libraries
Version:      3.6.8
Vendor:       Gnome Community
Release:      1
Distribution: Java Desktop System
Vendor:       Sun Microsystems, Inc.
Summary:      OPAL - Open Phone Abstraction Library
Source:       http://ftp.gnome.org/pub/GNOME/sources/opal/3.6/%{name}-%{version}.tar.gz

# owner:davelam date:2006-04-14 type:branding
# change library naming rule to fit unix style
Patch1:       opal-01-libname.diff

# owner:elaine date:2008-11-11 type:branding
# help ekiga find opal.pc
Patch2:       opal-02-no-public-pc.diff

# owner:hawklu date:2006-05-15 type:bug
# bugster:6416969
# updated by elaine
Patch3:       opal-03-jitter.diff

# owner:hawklu date:2009-09-18 type:bug doo:11250
Patch4:       opal-04-ekiga-hang.diff

# owner:hawklu date:2009-09-23 type:bug 
Patch5:       opal-05-build-fail.diff
# owner:lin date:2011-04-28 bugster:7038822 type:bug
Patch6:       opal-06-t140-session-error.diff

URL:          http://www.ekiga.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on
Requires:     speex
Requires:     ptlib

%description
OPAL is an Open Source class library for the development of
applications that use SIP / H.323 protocols for multimedia
communications over packet based networks.

%package devel
Summary: Headers for developing programs that will use opal
Group:      Development/Libraries
Requires:   %{name}

%description   devel
This package contains the headers that programmers will need to develop
applications which will use opal.

%prep
%setup -q -n %{name}-%{version}
cp include/opal.h include/opal/
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0

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
export CXXFLAGS="%cxx_optflags -DSOLARIS"
export LDFLAGS="%_ldflags"
%{?ekiga_libdir:export LDFLAGS="$LDFLAGS -R%{ekiga_libdir}"}

cd plugins
aclocal
autoconf
cd ..
aclocal
autoconf
./configure \
	--prefix=%{_prefix} \
        --libdir=%{?ekiga_libdir}%{?!ekiga_libdir:%{_libdir}} \
        --bindir=%{_bindir} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir} \
	--disable-iax

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

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
* Thu Apr 28 2011 - lin.ma@oracle.com
- fixed bugster 7038822
* Fri Jun 04 2010 - brian.lu@sun.com
- Bump to 3.6.8
* Thu Jan 07 2009 - brian.lu@sun.com
- Change the owner to hawklu
* Fri Sep 25 2009 - brian.lu@sun.com
- Add patch opal-05-build-fail.diff
* Wed Sep 23 2009 - dave.lin@sun.com
- Bump to 3.6.6
* Fri Sep 17 2009 - brian.lu@sun.com
- Add patch opal-04-ekiga-hang.diff
* Tue Jul 14 2009 - elaine.xiong@sun.com
- Bump to 3.6.4. Remove Opal-05-option-err upstream patch.
* Thu Nov 20 2008 - elaine.xiong@sun.com
- Bump to 3.4.2. Remove upstreamed opal-04-endian patch.
* Fri Nov 14 2008 - elaine.xiong@sun.com
- Bump to 3.4.1. Add new patches and remove obsolete patches.
- Update build options for new version.
* Wed Sep 03 2008 - elaine.xiong@sun.com
- Add note to not bump to 3.3.1 as ekiga depends on it.
* Sun Dec 23 2007 - patrick.ale@gmail.com
- Download tar.gz instead of tar.bz2. bz2 tarball is N/A
* Fri Nov 02 2007 - elaine.xiong@sun.com
- Fix a typo.
* Tue Sep 18 2007 - damien.carbery@sun.com
- Bump to 2.2.11.
* Thu May 17 2007 - elaine.xiong@sun.com
- Disable IAX feature support per OPAL ECCN requirement.
* Wed Apr 25 2007 - elaine.xiong@sun.com
- Update owner name for opal-04-pack-addr.diff
* Thu Apr 19 2007 - elaine.xiong@sun.com
- Bump to 2.2.8, move upstream patch opal-02-illegal-payloadtype.diff.
* Tue Apr 17 2007 - elaine.xiong@sun.com
- move the -Lpath that could specify the /usr/lib/ as the search directory
  when link time.
* Fri Apr  6 2007 - elaine.xiong@sun.com
- Add patch opal-04-pack-addr.diff to fix bugster6538068
  Actually it works for pwlib-05-medialib.diff. It makes the YUV420P payload
  buffer packed by 8 Byte. If pwlib-05-media.diff is upstream, it should be
  upstream. If not, the performance brougnt by medialib is hurt.
* Thu Apr  5 2007 - laca@sun.com
- Create
