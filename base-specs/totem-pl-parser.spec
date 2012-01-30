#
# spec file for package totem-pl-parser
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

%include l10n.inc
Name:         totem-pl-parser
License:      LGPL v2
Group:        System/GUI/GNOME
Version:      2.32.1
Release:      1
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      Totem Multimedia Player
Source:       http://ftp.gnome.org/pub/GNOME/sources/totem-pl-parser/2.32/%{name}-%{version}.tar.bz2

#owner:yippi date:2008-11-27 type:branding 
Patch1:	      totem-pl-parser-01-ignore-cdda.diff
#owner:yippi date:2009-03-27 type:branding
Patch2:	      %{name}-02-replace-rdsk-with-dsk.diff
#owner:yippi date:2009-06-03 type:branding
Patch3:	      %{name}-03-token-size.diff
#owner:yippi date:2009-12-15 type:branding
Patch4:	      %{name}-04-memmem.diff


%if %build_l10n
Source1:                 l10n-configure.sh
%endif
URL:          http://www.gnome.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on

%define	libgnomeui_version			2.6.0
%define	gstreamer_version               	0.8.1
%define gstreamer_plugins_version       	0.8.1
%define gnome_desktop_version                   2.6.1

Requires:       libgnomeui >= %{libgnomeui_version}
Requires:       gstreamer >= %{gstreamer_version}
Requires:       gstreamer-plugins >= %{gstreamer_plugins_version}
Requires:       gnome-desktop >= %{gnome_desktop_version}
Requires:       iso-codes
BuildRequires:  libgnomeui-devel >= %{libgnomeui_version}
BuildRequires:  gstreamer-devel >= %{gstreamer_version}
BuildRequires:  gstreamer-plugins-devel >= %{gstreamer_plugins_version}
BuildRequires:  gnome-desktop-devel >= %{gnome_desktop_version}

%description
A simple GObject-based library to parse and save a variety of
playlist formats.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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

if test "x$x_includes" = "x"; then
 x_includes="/usr/X11/include"
fi

if test "x$x_libraries" = "x"; then
 x_libraries="/usr/X11/lib"
fi

libtoolize --force
intltoolize --force --copy --automake

%if %build_l10n
bash -x %SOURCE1 --enable-copyright
%endif

aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f
autoconf

export AR="/usr/sfw/bin/gar"
export MOZILLA_PLUGINDIR="%{_libdir}/firefox/plugins"
CFLAGS="$RPM_OPT_FLAGS"	\
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
        --libdir=%{_libdir}         \
        --bindir=%{_bindir}         \
	--libexecdir=%{_libexecdir} \
	--mandir=%{_mandir}         \
	--localstatedir=/var/lib
gmake -j $CPUS

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
gmake -i install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="totem.schemas totem-video-thumbnail.schemas"
for S in $SCHEMAS; do
        gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$S >/dev/null
done

%files
%defattr (-, root, root)
%{_bindir}/*
%{_sysconfdir}/gconf/schemas
%{_libdir}/*
%{_libexecdir}/*
%{_datadir}/applications
%{_datadir}/gnome/help/totem/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/omf/totem/*
%{_datadir}/pixmaps/*
%{_datadir}/totem/*
%{_mandir}/man1/totem*
%{_includedir}/totem/*

%changelog
* Mon Oct 25 2010 - brian.cameron@oracle.com
- Bump to 2.32.1.
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Bump to 2.30.4.
* Fri May 21 2010 - brian.cameron@oracle.com
- Bump to 2.30.1.
* Mon Apr 12 2010 - christian.kelly@oracle.com
- Bump to 2.30.0.
* Fri Mar 19 2010 - christian.kelly@sun.com
- Bump to 2.29.92.
* Thu Mar 11 2010 - christian.kelly@sun.com
- Bump to 2.29.91.
* Wed Oct 14 2009 - dave.lin@sun.com
- Bump to 2.28.1
* Thu Sep 24 2009 - brian.cameron@sun.com
- Bump to 2.28.0.
* Thu May 7 2009 - jerry.tan@sun.com
- Bump to 2.26.2
* Tue Apr 14 2009 - brian.cameron@sun.com
- Bump to 2.26.1.
* Fri Mar 27 2009 - jerry.tan@sun.com
- add totem-pl-parser-02-replace-rdsk-with-dsk.diff to fix the bug of rhythmbox
  unable to display playlist from cd
* Tue Mar 17 2009 - dave.lin@sun.com
- Bump to 2.26.0.
* Thu Mar 12 2009 - brian.cameron@sun.com
- Bump to 2.25.92.
* Wed Feb 11 2009 - dave.lin@sun.com
- set AR=/usr/sfw/bin/gar to fix build issue(bz571265).
* Thu Feb 05 2009 - christian.kelly@sun.com
- Bump to 2.25.90.
* Tue Jan 20 2009 - brian.cameron@sun.com
- Bump to 2.25.1.  Remove upstream patch totem-pl-parser-01-ignore-cdda.diff.
* Wed Sep 24 2008 - christian.kelly@sun.com
- Bump to 2.24.0.
* Mon Sep 01 2008 - christian.kelly@sun.com
- Bump to 2.23.91.
- Remove patch 01-stat-header, fixed upstream, bugzilla:543119.
- Remove patch 02-save-playlist-crash, fixed upstream, bugzilla:542178.
* Mon Jun 14 2008 - christian.kelly@sun.com
- Bump to 2.23.3.
* Sun Jul 06 2008 - damien.carbery@sun.com
- Add patch 01-stat-header to include sys/stat.h to get module to build.
* Thu Jun 12 2008 - damien.carbery@sun.com
- Bump to 2.23.2.
* Tue May 13 2008 - damien.carbery@sun.com
- Bump to 2.22.3.
* Wed Apr 09 2008 - damien.carbery@sun.com
- Bump to 2.22.2.
* Mon Mar 10 2008 - damien.carbery@sun.com
- Bump to 2.22.1.
* Mon Feb 25 2008 - damien.carbery@sun.com
- Bump to 2.21.92. Remove upstream patch, 01-memmem.
* Wed Jan 23 2008 - damien.carbery@sun.com
- Reintroduce patch 01-memmem as it is not actually upstream.
* Tue Jan 22 2008 - damien.carbery@sun.com
- Bump to 2.21.91. Remove upstream patch, 01-memmem.
* Wed Jan 09 2008 - damien.carbery@sun.com
- Add patch 01-memmem to fix build errors.
* Mon Jan 07 2008 - damien.carbery@sun.com
- Bump to 2.21.90.
* Mon Dec 03 2007 - brian.cameron@sun.com
- Initial Sun release
