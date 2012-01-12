#
# spec file for package gnome-icon-theme-symbolic
#
# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         		gnome-icon-theme-symbolic
License:      		GPL v2
Group:        		System/GUI/GNOME
BuildArchitectures:	noarch
Version:      		3.2.1
Release:      		1
Distribution: 		Java Desktop System
Vendor:       		Gnome Community
Summary:      		GNOME Icon Themes
Source:       		http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.2/%{name}-%{version}.tar.bz2
URL:          		http://www.gnome.org/
BuildRoot:    		%{_tmppath}/%{name}-%{version}-build
Docdir:	      		%{_defaultdocdir}/doc
Autoreqprov:  		on

%define hicolor_icon_theme_version 0.4

Requires:		hicolor-icon-theme >= %{hicolor_icon_theme_version}
BuildRequires:		glib2
BuildRequires:		hicolor-icon-theme >= %{hicolor_icon_theme_version}
BuildRequires:		automake >= 1.9

%description
Collection of Icon Themes for the GNOME Desktop

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

aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf

CFLAGS="$RPM_OPT_FLAGS"			\
./configure --prefix=%{_prefix}		\
%ifos linux
	    --sysconfdir=%{_sysconfdir}
%else
	    --sysconfdir=%{_sysconfdir} \
	    --disable-hicolor-check
%endif
make -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_datadir}/icons/gnome
%{_libdir}/pkgconfig/gnome-icon-theme.pc

%changelog
* Wed Oct 19 2011 - brian.cameron@oracle.com
- Bump to 3.2.1.
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 3.2.0.
* Thu Sep 08 2011 - brian.cameron@oracle.com
- Bump to 3.1.90.
* Sat Aug 06 2011 - brian.cameron@oracle.com
- Bump to 3.1.4.
* Fri Jul 08 2011 - brian.cameron@oracle.com
- Created with 3.0.0.

