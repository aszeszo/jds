#
# spec file for package libgnomekbd
#
# Copyright (c) 2010, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: ja208388
#

Name:         libgnomekbd
License:      LGPLv2+
Group:        System/Libraries/GNOME
Version:      3.2.0
Release:      1
Distribution: Java Desktop System
Vendor:       http://www.gnome.org
Summary:      A keyboard configuration library
URL:          http://gswitchit.sourceforge.net
Source:       http://download.gnome.org/sources/libgnomekbd/3.2/%{name}-%{version}.tar.bz2
# date:2010-08-02 owner:ja208388 type:bug
Patch1:       libgnomekbd-01-compile-makefile.diff
# date:2011-05-06 owner:gheet type:bug bugster:7022446
Patch2:       libgnomekbd-02-gconf-schema.diff

BuildRequires:  dbus-devel >= 0.92
BuildRequires:  dbus-glib >= 0.34
BuildRequires:  GConf2-devel >= 2.14.0
BuildRequires:  gtk2-devel >= 2.10.3
BuildRequires:  cairo-devel
BuildRequires:  libglade2-devel >= 2.6.0
BuildRequires:  libgnome-devel >= 2.16.0
BuildRequires:  libgnomeui-devel >= 2.16.0
BuildRequires:  libxklavier-devel >= 3.4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool

%description
The libgnomekbd package contains a GNOME library which manages
keyboard configuration and offers various widgets related to
keyboard configuration.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libxklavier-devel >= 2.91
Requires:       libgnome-devel >= 2.16.0
Requires:       pkgconfig

%description    devel
The libgnomekbd-devel package contains libraries and header files for
developing applications that use libgnomekbd.

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

CFLAGS="$RPM_OPT_FLAGS"

aclocal $ACLOCAL_FLAGS
libtoolize --force --copy
autoheader
autoconf
automake
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
            --mandir=%{_mandir} \
            --libdir=%{_libdir} \
            --bindir=%{_bindir}
make -j $CPUS

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
rm $RPM_BUILD_ROOT%{_libdir}/*.a $RPM_BUILD_ROOT%{_libdir}/*.la


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB
%{_libdir}/*.so.*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/libgnomekbd/*/*.ui
%{_mandir}/man3/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 3.2.0.
* Sat Aug 06 2011 - brian.cameron@oracle.com
- Bump to 3.0.0.1.
* Wed Jul 06 2011 - brian.cameron@oracle.com
- Bump to 3.0.0.
* Mon Aug 02 2010 - <javier.acosta@sun.com>
- Initial version
