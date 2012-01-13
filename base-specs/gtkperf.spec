#
# spec file for package gtkperf
#
# Copyright (c) 2005 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner dermot
#

%define OSR 12725:0.40

Name:         gtkperf
License:      GPL
Group:        System/GUI/GNOME
Version:      0.40
Release:      1
Distribution: Java Desktop System
Vendor:	      Sourceforge
Summary:      GTK+ performance testing tool
Source:       http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}_%{version}.tar.gz
#owner:jedy date:2010-01-11 type:branding 
Patch1:       gtkperf-01-cflags.diff
URL:          http://sourceforge.net/projects/gtkperf
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Autoreqprov:  on

%define gtk2_version 2.5.3

Requires: gtk2 >= %{gtk2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}

%description
GTK+ performance testing tool. It is meant for measuring perfomance of
different widgets and themes. Can be also used to find out ways of
improving GTK+ application-level performance.

%prep
%setup -q -n %name
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

# create dummy config.rpath required by AC_REQUIRE_AUX_FILE
# otherwise automake complains and fails.
touch config.rpath

aclocal $ACLOCAL_FLAGS
autoheader
automake -a  -c -f
autoconf
./configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --sysconfdir=%{_sysconfdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=/var/lib	\
    --disable-nls
make -j $CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu Aug 24 2006 - laca@sun.com
- autotoolize to avoid weird autom4te error when configure runs autoheader
* Wed Nov 30 2005 - damien.carbery@sun.com
- Bump to 0.40. Remove upstream patch.
* Mon Oct 24 2005 - damien.carbery@sun.com
- Initial Sun release.
