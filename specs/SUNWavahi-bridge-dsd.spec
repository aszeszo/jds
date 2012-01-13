#
# spec file for package SUNWavahi-bridge-dsd
#
# includes module(s): avahi
#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner padraig
#

%include Solaris.inc

%define pythonver 2.6

%use avahi = avahi.spec 

Name:                    SUNWavahi-bridge-dsd
IPS_package_name:        system/network/avahi
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:                 Avahi client and bridge to SUNWdsd
Version:                 %{avahi.version}
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_copyright:          %{name}.copyright
License:                 %{avahi.license}
Source1:        avahi-bridge-dsd.xml
Source2:        svc-avahi-bridge-dsd

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires:  SUNWgtk2-devel
BuildRequires:  SUNWpygtk2-26-devel
BuildRequires:  SUNWdbus-python26
BuildRequires:  SUNWpython26-setuptools
BuildRequires:  SUNWdbus
Requires:       SUNWgobject-introspection
Requires:       SUNWgtk2
Requires:       SUNWdsdu
Requires:       SUNWpygtk2-26
Requires:       SUNWPython26
Requires:       SUNWdbus-python26
Requires:       SUNWavahi-bridge-dsd-root
Requires:       SUNWlibdaemon
Requires:       SUNWlexpt
Requires:       SUNWdsdr
Requires:       SUNWdbus

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %{name}

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%avahi.prep -d %name-%version

%build
export PYTHON=/usr/bin/python%{pythonver}

PKG_CONFIG_DISABLE_UNISTALLED=
unset PKG_CONFIG_DISABLE_UNISTALLED
export PKG_CONFIG_PATH=../avahi-%{avahi.version}:%{_pkg_config_path}
export CFLAGS="%optflags -I/usr/sfw/include"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags -ldns_sd -lsocket -lnsl -L/usr/sfw/lib -R/usr/sfw/lib -lexpat"

%avahi.build -d %name-%version

%install
%avahi.install -d %name-%version
mkdir -p $RPM_BUILD_ROOT/lib/svc/manifest/system
mkdir -p $RPM_BUILD_ROOT/lib/svc/method
chmod -R 755 $RPM_BUILD_ROOT/lib
cp %SOURCE1 $RPM_BUILD_ROOT/lib/svc/manifest/system/
cp %SOURCE2 $RPM_BUILD_ROOT/lib/svc/method/

mv $RPM_BUILD_ROOT%{_sbindir}/avahi-daemon $RPM_BUILD_ROOT%{_sbindir}/avahi-daemon-bridge-dsd
%if %option_with_indiana_branding
rm -rf $RPM_BUILD_ROOT%{_datadir}/applications
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%doc -d avahi-%{avahi.version} README LICENSE
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_sbindir}
%{_sbindir}/avahi-daemon-bridge-dsd
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libavahi*.so*
%{_libdir}/avahi/service-types.db.pag
%{_libdir}/avahi/service-types.db.dir
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/avahi/service-types
%if %option_with_indiana_branding
%else
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/avahi-discover.desktop
%{_datadir}/applications/bssh.desktop
%{_datadir}/applications/bvnc.desktop
%endif
%{_datadir}/avahi/interfaces/avahi-discover.ui
%{_datadir}/dbus-1/interfaces/*
%{_datadir}/gir-1.0/*
%{_libdir}/girepository-1.0/*
%dir %attr (0755, root, bin) %{_mandir}
%{_mandir}/man1/*
%attr (-, root, bin) %{_libdir}/python*

%files root
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_sysconfdir}
%config %ips_tag(original_name=SUNWavahi-bridge-dsd:%{@}) %{_sysconfdir}/*
%dir %attr (0755, root, sys) /lib/svc/manifest
%dir %attr (0755, root, sys) /lib/svc/manifest/system
%class(manifest) %attr (0444, root, sys) /lib/svc/manifest/system/avahi-bridge-dsd.xml
%attr (0555, root, bin) /lib/svc/method/svc-avahi-bridge-dsd

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed May 18 2011 - padraig.obriain@oracle.com
- Remove reference to /usr/share/avahi/avahi-service.dtd to fix CR 6804922.
* Fri Jan 21 2011 - padraig.obriain@oracle.com
- Update to 0.6.28.
* Thu Dec  2 2010 - christian.kelly@oracle.com
- Add dependency on SUNWdbus.
* Wed Nov 10 2010 - padraig.obriain@oracle.com
- Add License tag.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu Dec 03 2009 - padraig.obriain@sun.com
- Remove postinstall script to enable system/avahi-bridge-dsd on reboot
* Mon Nov 09 2009 - padraig.obriain@sun.com
- Change dependency SUNWPython to SUNWPython26
* Mon Oct 05 2009 - padraig.obriain@sun.com
- Update python dependencies to 2.6.
* Mon Mar 23 2009 - jeff.cai@sun.com
- Because /usr/bin/avahi-discover (SUNWavahi-bridge-dsd) requires
  /usr/bin/i86/isapython2.4 which is found in SUNWPython, add the dependency.
* Thu Mar 05 2009 - brian.cameron@sun.com
- Change SUNWdbus-bindings to SUNWdbus-python.
* Wed Sep 10 2008 - padraig.obriain@sun.com
- Add %doc in %files for copyright
* Wed Aug 06 2008- padraig.obriain@sun.com
- add pre and post scripts for enabling the avahi-bridge-dsd svc upon 
  installation but leaving it as is upon upgrade (based on dbus spec file)
* Fri Jun 06 2008 - damien.carbery@sun.com
- Add l10n package.
* Wed Oct 31 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWdbus-bindings/-devel as the dbus python module is used.
* Wed Oct 31 2007 - damien.carbery@sun.com
- Remove references to /usr/lib/mdns from LDFLAGS as the dir doesn't exist.
* Fri Sep 07 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-base-libs/-devel for glib.
- Add Build/Requires SUNWgnome-python-libs/-devel for gtk Python module.
* Wed Jun 28 2007 - padraig.obriain@sun.com
- Initial spec file created.



