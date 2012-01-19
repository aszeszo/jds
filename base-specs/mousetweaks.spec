#
# spec file for package mousetweaks
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan

%define OSR 9489:2.23.4

Name:           mousetweaks
License:        GPL v3
Vendor:         Gnome Community
Group:          System/Library
Version:        2.30.2
Release:        1
Summary:        A program that provides mouse accessibility enhancements.
URL:            https://launchpad.net/mousetweaks
Source:         http://ftp.gnome.org/pub/GNOME/sources/mousetweaks/2.30/%{name}-%{version}.tar.bz2
%if %build_l10n
Source1:                 l10n-configure.sh
%endif
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Mousetweaks provides mouse accessibility enhancements for the GNOME Desktop.

Current features are dwell-click which simulates different mouse clicks
without using physical buttons and delay-click which opens context menus by
holding the primary mouse button for a specified amount of time.

Additionally there are two gnome-panel applets:

* pointer-capture: provides an area on the panel which temporarily locks the pointer
* dwell-click: simple applet to switch between dwell-click types

%prep
%setup

%build
intltoolize --force --copy --automake

%if %build_l10n
bash -x %SOURCE1 --enable-copyright
%endif

aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}

make 

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%clean
rm -rf $RPM_BUILD_ROOT

# update database
%post
gconfd-2 --shutdown

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/mousetweaks
%{_bindir}/mousetweaks-preferences
%{_bindir}/dwell-click-applet
%{_bindir}/pointer-capture-applet

%{_datadir}/mousetweaks/ctw.glade
%{_datadir}/mousetweaks/dwell-click-applet.glade
%{_datadir}/mousetweaks/human-double.png
%{_datadir}/mousetweaks/human-drag.png
%{_datadir}/mousetweaks/human-right.png
%{_datadir}/mousetweaks/human-single.png
%{_datadir}/mousetweaks/mousetweaks.glade
%{_datadir}/mousetweaks/pointer-capture-applet.glade

%{_datadir}/applications/mousetweaks-preferences.desktop
%{_datadir}/gnome/autostart/mousetweaks.desktop

%{_datadir}/locale/de/LC_MESSAGES/mousetweaks.mo
%{_datadir}/locale/fr/LC_MESSAGES/mousetweaks.mo
%{_datadir}/locale/it/LC_MESSAGES/mousetweaks.mo

%{_libdir}/bonobo/servers/DwellClick_Factory.server
%{_libdir}/bonobo/servers/PointerCapture_Factory.server

%{_sysconfdir}/gconf/schemas/mousetweaks.schemas
%{_sysconfdir}/gconf/schemas/pointer-capture-applet.schemas

%{_datadir}/omf/*

%changelog
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Bump to 2.30.2.
* Tue Apr 26 2010 - christian.kelly@oracle.com
- Bump to 2.30.1.
* Mon Mar 29 2010 - christian.kelly@sun.com
- Bump to 2.30.0.
* Tue Mar 09 2010 - li.yuan@sun.com
- Bump to 2.29.92.
* Tue Feb 23 2010 - li.yuan@sun.com
- Bump to 2.29.91.
* Wed Feb 10 2010 - li.yuan@sun.com
- Bump to 2.29.90.
* Tue Jan 26 2010 - li.yuan@sun.com
- Bump to 2.29.6.
* Tue Jan 12 2010 - li.yuan@sun.com
- Bump to 2.29.5.
* Tue Dec 22 2009 - li.yuan@sun.com
- Bump to 2.29.4
* Mon Nov 30 2009 - li.yuan@sun.com
- Bump to 2.29.3
* Tue Nov 17 2009 - li.yuan@sun.com
- Bump to 2.29.2
* Tue Oct 20 2009 - dave.lin@sun.com
- Bump to 2.28.1
* Wed Sep 23 2009 - dave.lin@sun.com
- Bump to 2.28.0
* Tue Sep 08 2009 - dave.lin@sun.com
- Bump to 2.27.92
* Wed Aug 26 2009 - li.yuan@sun.com
- Bump to 2.27.91.
* Tue Aug 11 2009 - li.yuan@sun.com
- Bump to 2.27.90.
* Wed Jul 29 2009 - li.yuan@sun.com
- Bump to 2.27.5.
* Sun Jul 19 2009 - christian.kelly@sun.com
- Bump to 2.27.4.
* Tue Jun 16 2009 - christian.kelly@sun.com
- Bump to 2.27.3.
* Mon Jun 15 2009 - christian.kelly@sun.com
- Bump to 2.27.2.
* Tue Mar 17 2009 - dave.lin@sun.com
- Bump to 2.26.0
* Fri Mar 06 2009 - li.yuan@sun.com
- Bump to 2.25.92.
* Thu Feb 19 2009 - li.yuan@sun.com
- Bump to 2.25.91.
* Fri Feb 06 2009 - li.yuan@sun.com
- Bump to 2.25.90.
* Thu Jan 22 2009 - li.yuan@sun.com
- Bump to 2.25.5.
* Thu Jan 08 2009 - li.yuan@sun.com
- Bump to 2.25.4.
* Wed Dec 03 2008 - dave.lin@sun.com
- Bump to 2.25.2
* Wed Nov 05 2008 - li.yuan@sun.com
- Change copyright information.
* Tue Oct 28 2008 - li.yuan@sun.com
- Bump to 2.24.1.
* Tue Sep 02 2008 - christian.kelly@sun.com
- Bump to 2.23.91.
- Fix packaging issue with /usr/share/omf
* Tue Aug 19 2008 - dave.lin@sun.com
- Bump to 2.23.90
* Tue Aug 05 2008 - damien.carbery@sun.com
- Bump to 2.23.6.
* Mon Jul 21 2008 - damien.carbery@sun.com
- Bump to 2.23.5.
* Tue Jun 17 2008 - damien.carbery@sun.com
- Bump to 2.23.4.
* Tue Jun 03 2008 - damien.carbery@sun.com
- Bump to 2.23.3.
* Tue Jun 03 2008 - damien.carbery@sun.com
- Bump to 2.23.3.
* Wed May 28 2008 - damien.carbery@sun.com
- Bump to 2.23.2.
* Tue May 27 2008 - li.yuan@sun.com
- Bump to 2.22.2.
* Tue Mar 11 2008 - damien.carbery@sun.com
- Bump to 2.22.0.
* Mon Feb 25 2008 - damien.carbery@sun.com
- Bump to 2.21.92.
* Mon Feb 11 2008 - brian.cameron@sun.com
- Bump to 2.21.91. Remove upstream patch 01-cflags.
* Mon Feb 04 2008 Li Yuan <li.yuan@sun.com>
- Add launchpad bug number 188872 to the cflags patch.
* Mon Feb 04 2008 Li Yuan <li.yuan@sun.com>
- Remove mfversion patch and use autoconf/automake to avoid
  build errors. Remove some unnecessary script.
* Mon Oct 29 2007 Gerd Kohlberger <lowfi@chello.at> 
- Initial revision


