#
# spec file for package SUNWgksu
#
# includes module(s): gksu, libgksu
#
# Copyright (c) 2006, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#
%include Solaris.inc

%use gksu = gksu.spec
%use libgksu = libgksu.spec
Name:                    SUNWgksu
License: GPL v2, LGPL v2
IPS_package_name:        desktop/gksu
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:                 Gksu CLI and libraries
Version:                 %{gksu.version}
SUNW_Copyright:          %{name}.copyright
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: library/desktop/gtk2
BuildRequires: gnome/gnome-panel
BuildRequires: library/gnome/gnome-libs
BuildRequires: gnome/config/gconf
BuildRequires: library/gnome/gnome-component
BuildRequires: system/library/iconv/utf-8
BuildRequires: library/libgtop
BuildRequires: gnome/file-manager/nautilus
Requires: library/desktop/gtk2
Requires: gnome/gnome-panel
Requires: library/gnome/gnome-libs
Requires: gnome/config/gconf
Requires: library/gnome/gnome-component
Requires: library/libgtop

%package devel
Summary:                 %{summary} - development files 
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir %name-%version
%libgksu.prep -d %name-%version
%gksu.prep -d %name-%version

%build
export CFLAGS="%optflags -I%{_includedir}"
export RPM_OPT_FLAGS="$CFLAGS"

%libgksu.build -d %name-%version

export PKG_CONFIG_TOP_BUILD_DIR=%{_builddir}/%name-%version/libgksu-%{libgksu.version}
export PKG_CONFIG_PATH=../libgksu-%{libgksu.version}/libgksu:%{_pkg_config_path}
%gksu.build -d %name-%version

%install
%libgksu.install -d %name-%version
%gksu.install -d %name-%version

# Remove the desktop file that runs /usr/bin/x-terminal-emulator
# since there is no such program on Solaris.
#
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/gksu.desktop

# The embedded_su code does not support the Advanced options, so no
# reason to ship the configuration program.
#
rm -f $RPM_BUILD_ROOT%{_bindir}/gksu-properties
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/gksu-properties.desktop
rmdir $RPM_BUILD_ROOT%{_datadir}/applications

# -f used because charset alias doesn't seem to be created when using
# gnu libiconv/libintl
rm -f $RPM_BUILD_ROOT%{_libdir}/charset.alias
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
rm $RPM_BUILD_ROOT%{_bindir}/gksudo
rm $RPM_BUILD_ROOT%{_mandir}/man1/gksudo.1

# Do not ship GConf files, gksu currently has all GConf features patched out.
rm -fR $RPM_BUILD_ROOT%{_sysconfdir}

#Clean up unpackaged files
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/libgksu/gksu-run-helper
%{_libdir}/nautilus
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/man1/gksu*.1
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gksu*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/libgksu
%{_datadir}/gksu
%attr (0755, root, other) %dir %{_datadir}/pixmaps
%{_datadir}/pixmaps/gksu*.png
%doc gksu-%{gksu.version}/AUTHORS
%doc gksu-%{gksu.version}/README
%doc(bzip2) gksu-%{gksu.version}/COPYING
%doc(bzip2) gksu-%{gksu.version}/ChangeLog
%doc(bzip2) gksu-%{gksu.version}/po/ChangeLog
%doc libgksu-%{libgksu.version}/AUTHORS
%doc(bzip2) libgksu-%{libgksu.version}/COPYING
%doc(bzip2) libgksu-%{libgksu.version}/ChangeLog
%doc(bzip2) libgksu-%{libgksu.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, bin) %{_datadir}/gtk-doc
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/libgksu2.pc
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/libgksu

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Aug 19 2009 - lin.ma@sun.com
- Add no bump flag.
* Wed Sep 17 2008 - jim.li@sun.com
- Revised new format copyright file
* Wed Oct  3 2007 - laca@sun.com
- use rm -f to delete charset.alias/locale.alias because they do not get
  created in the indiana build
* Wed May 03 2007 - darren.kenny@sun.com
- Restore correct permissons on /etc/gksu.conf to be root:root
* Tue Apr 24 2007 - laca@sun.com
- fix default attributes
* Thu Sep 18 2006 - darren.kenny@sun.com
- Change the group for /etc/gksu.conf to be as the app expects (i.e. root:root)
* Fri Aug 30 2006 - damien.carbery@sun.com
- Delete %{_datadir}/locale/locale.alias as it caused a packaging conflict.
* Thu Aug 10 2006 - Jim.li@sun.com
- initial Sun release.

