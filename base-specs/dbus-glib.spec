#
# spec file for package dbus-glib
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: bugzilla.freedesktop.org
#

%define OSR 4092:0.60

Name:         dbus-glib
License:      GPL v2, AFL v2.1
Vendor:       freedesktop.org
Group:        System/Libraries
Version:      0.98
Release:      1
Distribution: Java Desktop System
Summary:      Glib bindings for D-Bus
Source:       http://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz
# date:2011-07-25 owner:yippi type:bug bugster:7034087
Patch1:       dbus-glib-01-avoid-crash.diff
URL:          http://www.freedesktop.org/wiki/Software_2fdbus
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:	      %{_defaultdocdir}/doc
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%define glib2_version 2.6.4
%define libxml2_version 2.6.19
BuildRequires: glib2-devel >= %glib2_version
BuildRequires: libxml2-devel >= %libxml2_version
# FIXME: get python rpm: BuildRequires: python >= %python_version
Requires: glib2 >= %glib2_version
Requires: libxml2 >= %libxml2_version

%description
Glib bindings for D-Bus.

%package devel
Summary:      Simple IPC library based on messages
Group:        Development/Libraries
Requires:     %{name} = %{version}

%description devel
Glib bindings for D-Bus.

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

libtoolize --force
aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf
export CFLAGS="%optflags -D_REENTRANT"
export LDFLAGS="%_ldflags"
./configure --prefix=%{_prefix}			\
            --includedir=%{_includedir}		\
            --sysconfdir=%{_sysconfdir}		\
            --libdir=%{_libdir}			\
            --bindir=%{_bindir}			\
            --libexecdir=%{_libexecdir}		\
            --localstatedir=%{_localstatedir}	\
            --with-dbus-user=root		\
            --with-dbus-daemondir=%{_basedir}/lib	\
            --mandir=%{_mandir}			\
            --datadir=%{_datadir}		\
            --disable-static
make -j $CPUS \
    pyexecdir=%{_libdir}/python%{python_version}/vendor-packages

%install
make DESTDIR=$RPM_BUILD_ROOT install \
    pyexecdir=%{_libdir}/python%{python_version}/vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_datadir}/dbus-1/services
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.pyo" -exec rm -f {} ';'

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%config %{_sysconfdir}/dbus-1/session.conf
%config %{_sysconfdir}/dbus-1/system.conf
%{_bindir}/*
%{_libdir}/libdbus*.so*
%{_datadir}/man/*
%{_datadir}/dbus-1/*

%files devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/dbus-1.0/*
%{_libdir}/dbus-1.0/*
%{_libdir}/pkgconfig/*
%{_libdir}/python?.?/vendor-packages/*

%changelog
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 0.98.
* Wed Sep 21 2011 - brian.cameron@oracle.com
- Bump to 0.96.
* Tue Sep 13 2011 - brian.cameron@oracle.com
- Bump to 0.94.
* Mon Jul 25 2011 - brian.cameron@oracle.com
- Add patch dbus-glib-01-avoid-crash.diff to fix CR #7034087.
* Fri Aug 13 2010 - brian.cameron@oracle.com
- Bump to 0.88.
* Thu Mar 25 2010 - brian.cameron@sun.com
- Bump to 0.86.
* Wed Jan 27 2010 - brian.cameron@sun.com
- Bump to 0.84.
* Fri Jul 17 2009 - brian.cameron@sun.com
- Bump to 0.82.
* Tue Feb 03 2009 - brian.cameron@sun.com
- Bump to 0.80.
* Wed Dec 10 2008 - brian.cameron@sun.com
- Bump to 0.78.
* Thu Jul 24 2008 - brian.cameron@sun.com
- Bump to 0.76.  Remove upstream patch dbus-glib-01-findlaunch.diff.
* Wed Nov 07 2007 - padraig.obriain@sun.com
- Add -D_REENTRANT. It was removed from SUNW spec file on Sep 28.
  See bugster 6615221
* Fri Sep 28 2007 - laca@sun.com
- convert to new style multi-ISA build
* Mon Aug 06 2007 - brian.cameron@sun.com
- Bump to 0.74.
* Sun Apr  1 2007 - laca@sun.com
- add missing aclocal calls
* Wed Mar 15 2007 - dougs@truemail.co.th
- Removed CC64 and CC32. They are not needed anymore
* Sun Feb 25 2007 - dougs@truemail.co.th
- updated to include 64-bit build RFE: #6480511
* Wed Feb 14 2007 - damien.carbery@sun.com
- Bump to 0.73. Remove upstream patch 01-uninstalled-pc. Rename remainder.
* Thu Nov 27 2006 - brian.cameron@sun.com
- Created.
