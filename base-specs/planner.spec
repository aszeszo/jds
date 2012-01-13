#
# spec file for package planner
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jat
#

%define OSR 8705:0.14.2

Name:         planner
License:      GPLv2
Group:        Application/Devel
Version:      0.14.4
Vendor:       http://live.gnome.org/Planner
Release:      1
Distribution: Java Desktop System
Vendor:       Sun Microsystems, Inc.
Summary:      Planner is a project managment tool for the Gnome desktop
Source:       http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.14/%{name}-%{version}.tar.bz2
URL:          http://live.gnome.org/Planner
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_docdir}/%{name}
Autoreqprov:  on

# date:2008-09-17 owner:jat type:bug bugster:6749027
Patch1:         planner-01-acinclude.m4.diff
# date:2008-09-17 owner:jat type:bug bugster:6749027
Patch2:         planner-02-Makefile.am.diff
# date:2008-09-17 owner:jat type:bug bugster:6749027
Patch3:         planner-03-Makefile.am.diff
# date:2008-09-23 owner:davelam type:bug 
Patch4:         planner-04-gtype.diff
# date:2009-02-20 owner:mattman type:branding
Patch5:         planner-05-manpage.diff

%description
Planner is a project managment tool for the Gnome desktop

%package devel
Summary:	Planner development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Planner development files.

%prep

%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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

intltoolize --force --automake
libtoolize --force
aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf

CFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
            --mandir=%{_mandir} \
            --disable-update-mimedb

make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Fri Feb 20 2009 - matt.keenan@sun.com
- Add attributes/ARC manpage patch
* Fri Jan 16 2008 - brian.cameron@sun.com
- Fix download link.
* Tue Sep 23 2008 - dave.lin@sun.com
- Added patch planner-04-gtype.diff to make it build with Gnome2.24
* Monday, June 30, 2008 - joseph.townsend@sun.com
- Initial spec-file created

