#
# spec file for package libxklavier
#
# Copyright (c) 2010, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: ja208388
#

Name:		libxklavier
License:	LGPLv2+
Group:		Development/Libraries
Version:	5.1
Release:	1
Vendor:		http://www.freedesktop.org/
Summary:	libXklavier library
Url:		http://gswitchit.sourceforge.net/
Source:		http://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
# date:2010-08-02 owner:ja208388 type:bug
Patch1:		libxklavier-01-compile-makefile.diff
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gtk-doc
BuildRequires:  dbus-glib >= 0.34

%description
This library allows you simplify XKB-related development.

%package devel
Summary: Libraries, includes, etc to develop libxklavier applications
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

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


%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING.LIB
%{_libdir}/lib*.so*
%{_datadir}/libxklavier
%{_mandir}/man3/*

%files devel
%defattr(-, root, root)

%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/libxklavier

%changelog
* Wed Jul 06 2011 - brian.cameron@oracle.com
- Bump to 5.1.
* Mon Aug 02 2010 - javier.acosta@sun.com
- Initial version
