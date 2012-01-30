#
# spec file for package SUNWseahorse
#
# includes module(s): seahorse
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc

%use seahorse = seahorse.spec

Name:                    SUNWseahorse
License: GPL v2, LGPL v2, FDL v1.1
IPS_package_name:        gnome/security/seahorse
Meta(info.classification): %{classification_prefix}:System/Security
Summary:                 Seahorse is a GNOME application for managing encryption keys.
Version:                 %{seahorse.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Source1:	%{name}-manpages-0.1.tar.gz
Requires: SUNWlibglade
Requires: SUNWlibgnome-keyring
Requires: SUNWgnome-config
Requires: SUNWgnome-panel
Requires: SUNWgnome-desktop-prefs
Requires: SUNWsshcu
Requires: SUNWdesktop-cache
Requires: SUNWgnupg
Requires: library/security/gpgme
Requires: SUNWpth
Requires: %{name}-root
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWlibgnome-keyring-devel
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWgnupg
BuildRequires: SUNWpth

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:       %{summary} - development files
SUNW_BaseDir:  %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version
%seahorse.prep -d %name-%version

cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="%optflags -I%{_includedir}"
export RPM_OPT_FLAGS="$CFLAGS"
export LD="$CC"
export LDFLAGS="%_ldflags"

%seahorse.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%seahorse.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%doc -d seahorse-%{seahorse.version} AUTHORS README
%doc(bzip2) -d seahorse-%{seahorse.version} ChangeLog
%doc(bzip2) -d seahorse-%{seahorse.version} COPYING COPYING-LIBCRYPTUI COPYING-DOCS
%doc(bzip2) -d seahorse-%{seahorse.version} NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*

%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libcryptui.*
%dir %attr (0755, root, bin) %{_libdir}/seahorse
%{_libdir}/seahorse/*

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/seahorse
%{_datadir}/seahorse/*
%dir %attr (0755, root, bin) %{_datadir}/gtk-doc
%{_datadir}/gtk-doc/*

%{_datadir}/dbus-1/services/*
%{_datadir}/omf/seahorse/*-C.omf
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16/apps/
%{_datadir}/icons/hicolor/16x16/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/22x22/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/22x22/apps/
%{_datadir}/icons/hicolor/22x22/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/apps/
%{_datadir}/icons/hicolor/24x24/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/apps/
%{_datadir}/icons/hicolor/32x32/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/apps/
%{_datadir}/icons/hicolor/48x48/apps/*

%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/C
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

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
%{_datadir}/omf/*/*-[a-z][a-z].omf
%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z][A-Z].omf
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/[a-z]*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/seahorse.schemas
#%{_sysconfdir}/xdg/autostart/*.desktop

%changelog
* Tue Feb 09 2010 - jeff.cai@sun.com
- Since the .desktop for autostart has been removed, no need to move it.
* Tue Jan 26 2010 - jeff.cai@sun.com
- Add dependency on SUNWlibgnome-keyring
* Wed Oct 13 2009 - jeff.cai@sun.com
- Disable autostart. Fix #11618
* Thu Jun 25 2009 - jeff.cai@sun.com
- Change the summary to fix #6854627
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Wed Feb 04 2008 - jeff.cai@sun.com
- Not ship /usr/share/cryptui/ui/*.ui
- Move seahorse-daemon.desktop to /etc/xdg/autostart
- Ship documents for libcryptui
* Tue Dec 30 2008 - jeff.cai@sun.com
- Ship some new files: seahorse-daemon.desktop and
  /usr/share/cryptui/ui/*.ui
* Thu Oct 30 2008 - jeff.cai@sun.com
- Change the section of l10n, make
  /gnome/help/* as "other" group. This 
  becomes same with SUNWevolution.spec. 
* Mon Oct 27 2008 - jeff.cai@sun.com
- Add man pages.
- Remove libcryptui.a and libcryptui.la
* Fri Oct 17 2008 - jeff.cai@sun.com
- Add package dependency on SUNWsshcu
* Mon Sep 22 2008 - jeff.cai@sun.com
- Not ship scalable icons since community remove them.
* Wed Sep 16 2008 - jeff.cai@sun.com
- Add copyright.
* Wed Aug 20 2008 - dave.lin@sun.com
- Add 16x16, 24x24, 32x32 icons when bump to 2.23.90.
* Fri Jul 22 2008 - jeff.cai@sun.com
- Initial spec



