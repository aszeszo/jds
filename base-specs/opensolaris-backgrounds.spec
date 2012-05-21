#
# spec file for package opensolaris-backgrounds
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc

%define OSR developed in the open, no OSR needed:n/a

Name:			opensolaris-backgrounds
License:		GPL v2
Group:			System/GUI/GNOME
Version:		0.10
Release:		1
Distribution:		Java Desktop System
Vendor:			Sun Microsystems, Inc.
Summary:		Selection of backgrounds for the OpenSolaris desktop
#Source:			http://dlc.sun.com/osol/jds/downloads/extras/opensolaris-branding/%{name}-%{version}.tar.bz2
Source:			http://github.com/aszeszo/archives/raw/master/%{name}-%{version}.tar.bz2
URL:			http://www.opensolaris.org
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
BuildArchitectures:     noarch
Docdir:			%{_defaultdocdir}/%{name}
Autoreqprov:		on

Requires:	glib2
BuildRequires:  intltool
BuildRequires:  glib2

%description
Selection of backgrounds for the OpenSolaris desktop.

%prep
%setup -q

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

CFLAGS="$RPM_OPT_FLAGS" \
  ./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	--mandir=%{_mandir}
make -j $CPUS

%install
make -i install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_datadir}/gnome-background-properties
%{_datadir}/pixmaps/backgrounds/
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%changelog
* Fir Aug 29 2008 - jedy.wang@sun.com
- Bump to 0.4.
* Mon Jan 21 2008 - glynn.foster@sun.com
- Initial version
