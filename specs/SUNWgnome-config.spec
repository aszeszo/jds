#
# spec file for package SUNWgnome-config
#
# includes module(s): GConf
#
# Copyright (c) 2004, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner stephen
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use gconf_64 = GConf.spec
%endif

%include base.inc
%use gconf = GConf.spec

Name:                    SUNWgnome-config
IPS_package_name:        gnome/config/gconf
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GNOME configuration framework
Version:                 %{gconf.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gconf.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Source1:                 svc-gconf-multi-user-desktop
Source2:                 gconf-multi-user-desktop.xml
Source3:                 gconf-defaults-optimizations.xml
Source4:                 gconf-mandatory-optimizations.xml

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWgtk3-devel
Requires: SUNWgtk3
Requires: SUNWgnome-config-root
Requires: SUNWlxml
Requires: SUNWgnome-component
Requires: SUNWlibpopt
Requires: SUNWdbus
Requires: SUNWdbus-glib
Requires: SUNWdesktop-cache
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWdbus-devel
BuildRequires: SUNWdbus-glib-devel
BuildRequires: SUNWgobject-introspection
BuildRequires: SUNWuiu8

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWgtk3-devel

%package -n              SUNWgnome-config-multi-user
IPS_package_name:        gnome/config/gconf/multi-user-desktop
Meta(info.classification): %{classification_prefix}:System/Administration and Configuration
Summary:                 Multi User Desktop - optimization SMF service
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-xml-share
Requires: SUNWgnome-config-root

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%gconf_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%gconf.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%ifarch amd64 sparcv9
%gconf_64.build -d %name-%version/%_arch64
%endif

export EXTRA_LDFLAGS=""
%gconf.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

# Sun Ray Optimization files
install -m 755 -d $RPM_BUILD_ROOT/lib/svc/method
install -m 555 %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method/svc-gconf-multi-user-desktop
install -m 755 -d $RPM_BUILD_ROOT/lib/svc/manifest/application/multi-user-desktop
install -m 444 %{SOURCE2} $RPM_BUILD_ROOT/lib/svc/manifest/application/multi-user-desktop/gconf-multi-user-desktop.xml
install -m 755 -d $RPM_BUILD_ROOT/usr/share/multi-user-desktop
install -m 444 %{SOURCE3} $RPM_BUILD_ROOT/usr/share/multi-user-desktop/gconf-defaults-optimizations.xml
install -m 444 %{SOURCE4} $RPM_BUILD_ROOT/usr/share/multi-user-desktop/gconf-mandatory-optimizations.xml

%ifarch amd64 sparcv9
%gconf_64.install -d %name-%version/%_arch64
%endif

%gconf.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_datadir}/man
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%ifarch amd64 sparcv9
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gconfd-2
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gconf-sanity-check-2
%endif

rm -f $RPM_BUILD_ROOT%{_bindir}/gconf-merge-tree

find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec rm {} \;

# Multi User Desktop Optimization directory
mkdir -p $RPM_BUILD_ROOT/etc/gconf/gconf.xml.multi.user.desktop.defaults
cat >> $RPM_BUILD_ROOT/etc/gconf/2/local-multi-user-desktop-defaults.path <<EOF
# Multi User Desktop Optimization directory
xml:readonly:/etc/gconf/gconf.xml.multi.user.desktop.defaults
EOF
mkdir -p $RPM_BUILD_ROOT/etc/gconf/gconf.xml.multi.user.desktop.mandatory
cat >> $RPM_BUILD_ROOT/etc/gconf/2/local-multi-user-desktop-mandatory.path <<EOF
# Multi User Desktop Optimization directory
xml:readonly:/etc/gconf/gconf.xml.multi.user.desktop.mandatory
EOF

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d %{base_arch}/GConf-%{gconf.version} README
%doc(bzip2) -d %{base_arch}/GConf-%{gconf.version} COPYING NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gconftool-2
%{_bindir}/gsettings-schema-convert
%{_bindir}/gsettings-data-convert
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libgconf-2.so*
%{_libdir}/GConf/2/lib*.so
%{_libdir}/gio
%{_libexecdir}/gconf-sanity-check-2
%{_libexecdir}/gconfd-2
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/gconf-merge-tree
%{_bindir}/%{_arch64}/gconftool-2
%{_bindir}/%{_arch64}/gsettings-schema-convert
%{_bindir}/%{_arch64}/gsettings-data-convert
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libgconf-2.so*
%{_libdir}/%{_arch64}/GConf/2/lib*.so
%{_libdir}/%{_arch64}/gio
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/dbus-1
%{_datadir}/sgml/gconf/gconf-1.0.dtd
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%{_libdir}/girepository-1.0/GConf-2.0.typelib
%{_libdir}/%{_arch64}/girepository-1.0/GConf-2.0.typelib
%{_datadir}/gir-1.0/GConf-2.0.gir
%{_datadir}/GConf/schema

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%config %ips_tag(original_name=SUNWgnome-config:%{@}) %{_sysconfdir}/gconf/2/path
%{_sysconfdir}/gconf/2/evoldap.conf
%dir %{_sysconfdir}/gconf/gconf.xml.defaults
%dir %{_sysconfdir}/gconf/gconf.xml.mandatory
%{_sysconfdir}/xdg

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files -n SUNWgnome-config-multi-user
%defattr (-, root, sys)
%dir %{_sysconfdir}/gconf/gconf.xml.multi.user.desktop.defaults
%config %ips_tag(original_name=SUNWgnome-config:%{@}) %{_sysconfdir}/gconf/2/local-multi-user-desktop-defaults.path
%dir %{_sysconfdir}/gconf/gconf.xml.multi.user.desktop.mandatory
%config %ips_tag(original_name=SUNWgnome-config:%{@}) %{_sysconfdir}/gconf/2/local-multi-user-desktop-mandatory.path
%attr (0755, root, bin) %{_datadir}/multi-user-desktop
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%class (manifest) /lib/svc/manifest
%attr (0755, root, bin) /lib/svc/method


%post
%restart_fmri gconf-cache

%changelog
* Fri Jul 29 2011 - Michal.Pryc@Oracle.Com
- Updated gconf-multi-user-desktop.xml to add SMF dependency on gdm
- Fixes CR:7071046
- gconf-mandatory-optimizations.xml, fixes CR7044452
* Thu Jul 07 2011 - brian.cameron@oracle.com
- Fix packaging for GConf 3.1.3 release.
* Thu Jun 30 2011 - Michal.Pryc@Oracle.Com
- Split of the gconf optimizations into defaults ones
- and mandatory ones.
* Mon Jan 16 2011 - Michal.Pryc@Oracle.Com
- Renamed server-desktop to Multi User Desktop
* Thu Jan 13 2011 - Michal.Pryc@Oracle.Com
- New package SUNWgnome-config-server-desktop, IPS name of this package:
  gnome/config/gconf/server-desktop. It's shipping SMF service that includes
  the required files for optimizing desktop for server / Sun Ray usage.
* Wed Nov 10 2010 - padraig.obriain@oracle.com
- Add license tag.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Oops, I put amd64 in %files instead of %{_arch64}.
* Wed Apr 21 2010 - christian.kelly@oracle.com
- Fix %files.
- Remove .la and .a files.
* Tue Apr 20 2010 - christian.kelly@oracle.com
- Fix %files.
* Wed Apr 29 2009 - laca@sun.com
- add desktop-cache dependency and ping gconf-cache after installation
* Tue Mar 24 2009 - jeff.cai@sun.com
- Since /usr/lib/amd64/pkgconfig/gconf-2.0.pc (SUNWgnome-config-devel)
  requires /usr/lib/amd64/pkgconfig/glib-2.0.pc which is found in
  SUNWgnome-base-libs-devel, add the dependency.
* Thu Mar 05 2009 - brian.cameron@sun.com
- Change SUNWdbus-bindings to SUNWdbus-glib.
* Fri Sep 19 2008 - dave.lin@sun.com
- Set attribute of /usr/share/doc in base pkg %files section.
* Mon Sep 15 2008 - christian.kelly@sun.com
- Remove /usr/share/doc from %files.
* Wed Sep 10 2008 - padraig.obriain@sun.com
- Add %doc to %files for copyright
* Wed Aug 06 2008 - dermot.mccluskey@sun.com
- Bug 6703986 : Remove references to /usr/lib/ST/64
* Wed Jun 04 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWdbus and SUNWdbus-bindings for GConf 2.23.1. Update
  %files for dbus files.
* Fri Sep 28 2007 - laca@sun.com
- convert to new style multi-ISA build
* Tue Jul 03 2007 - damien.carbery@sun.com
- Remove %{_datadir}/GConf from %files as it is no longer installed.
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Thu Jun 29 2006 - laca@sun.com
- don't include gconf-merge-tree.  Now that we're only using the merged
  data, gconf-merge-tree can only cause trouble
* Thu Jun 22 2006 - damien.carbery@sun.com
- Correct LDFLAGS64 to use %{_arch64} and move sparc-specific settings to
  a %ifarch sparcv9 section.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue Sep 20 2005 - laca@sun.com
- delete unpackaged files or add them to %files
* Tue Sep 06 2005 - laca@sun.com
- fix the 64-bit build
* Fri Sep 02 2005 - laca@sun.com
- remove unpackaged files
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Sat Oct  2 2004 - Joseph.Townsend@Sun.COM
- Create 64bit libraries for Solaris
* Mon Aug 30 2004 - shirley.woo@sun.com
- Bug 5091588 : sman3/4 files should be in a separate devel package
* Tue Aug 24 2004 - laca@sun.com
- set all files in /etc/gconf to volatile, fixes 5090975
* Sun Aug 22 2004 - laca@sun.com
- fix dependencies: don't depend on -devel pkgs
* Wed Aug 18 2004 - damien.carbery@sun.com
- Change manpage perms for Solaris integration.
* Mon Jul 05 2004 - damien.carbery@sun.com
- Add BuildRequires: SUNWgnome-base-libs-devel
* Sat Jun 26 2004 - shirley.woo@sun.com
- Changed install location to /usr/...
* Thu May 27 2004 - laca@sun.com
- added l10n subpkg
* Thu May 05 2004 - brian.cameron@sun.com
- removed aclocal files from share since they were already
  in devel-share.
* Sun Apr 04 2004 - laca@sun.com
- added some missing files to %files
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Mon Jan 26 2004 - Laszlo.Peter@sun.com
- initial version added to CVS

