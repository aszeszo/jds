#
# spec file for package nautilus-open-terminal
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner stephen

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         nautilus-open-terminal
License:      GPL
Group:        System/GUI/GNOME
Version:      0.18
Release:      1
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      Nautilus terminal extension
Source:       http://ftp.gnome.org/pub/GNOME/sources/nautilus-open-terminal/0.18/nautilus-open-terminal-%{version}.tar.bz2
#owner:gman date:2005-10-17 type:bug
Patch1:       nautilus-open-terminal-01-werror.diff
#owner:padraig date:2008-08-08 type:branding bugster:6725262
Patch2:      nautilus-open-terminal-02-home-dir.diff
#owner:stephen date:2009-08-24 type:branding doo:10803
Patch3:      nautilus-open-terminal-03-mc.diff

URL:          http://www.gnome.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on

%define nautilus_version 2.6.0
%define gnome_desktop_version 2.9.91

Requires:	nautilus >= %{nautilus_version}
Requires:	gnome-desktop >= %{gnome_desktop_version}
BuildRequires:  nautilus-devel >= %{nautilus_version}
BuildRequires:  gnome-desktop-devel >= %{gnome_desktop_version}

%description
Nautilus extension allowing you to open a terminal in arbitrary folders.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
libtoolize --force
aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf

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
rm -rf $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-2.0/*.a
rm -rf $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-2.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_libdir}/nautilus/extensions-2.0/*.so
%{_datadir}/locale/*/LC_MESSAGES/*.mo

%changelog
* Tue Apr 13 2008 - padraig.obriain@sun.com
- Remove references to eel to fix d.o.o. 15000
* Mon Jan 04 2009 - brian.cameron@sun.com
- Bump to 0.18.  Remove upstream patch
  nautilus-open-terminal-04-launch-terminal.diff
* Mon Nov 16 2009 - brian.cameron@sun.com
- Add patch nautilus-open-terminal-04-launch-terminal.diff to fix bug that was
  causing the terminal to not launch when selected from the background
  right-click menu.
* Mon Aug 17 2009 - jeff.cai@sun.com
- Change the download URL.
* Wed Aug 12 2009 - christian.kelly@sun.com
- Bump to 0.17.
* Mon Aug 11 2008 - padraig.obriain@sun.com
- Changed patch 03-home-dir to be a branding patch.
* Fri Aug 08 2008 - padraig.obriain@sun.com
- Add patch 03-home-dir so that terminal opens in user's home directory
  by default. Fixed 6725262.
* Fri Feb 29 2008 - damien.carbery@sun.com
- Bump to 0.9. Remove upstream patch 03-dir.
* Fri Jan 11 2008 - padraig.obriain@sun.sun
- Add patch 03-dir until we get new tarball as nautilus has changed location
  of extensions dir.
* Thu Nov 22 2007 - padraig.obriain@sun.sun
- Add patch 02-lockdown for #6630884.
* Sun Mar 11 2007 - dougs@truemail.co.th
- Fixed URL for nautilus-open-terminal.
* Mon Mar 05 2007 - damien.carbery@sun.com
- Bump to 0.8.
* Thu Nov 30 2006 - glynn.foster@sun.com
- Bump to 0.7 which includes multihead fix for
  #6469722.
* Mon Oct 17 2005 - glynn.foster@sun.com
- Add werror patch.
* Mon Oct 17 2005 - glynn.foster@sun.com
- Initial spec file.

