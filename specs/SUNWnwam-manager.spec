#
# spec file for package SUNWnwam-manager
#
# includes module(s): nwam-manager
#
# Copyright (c) 2009, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#
%include Solaris.inc

%use nwam_manager = nwam-manager.spec

Name:                    SUNWnwam-manager
IPS_package_name:        desktop/administration/nwam-manager
Meta(info.classification): %{classification_prefix}:System/Administration and Configuration
Summary:                 Network Auto-Magic User Interface
Version:                 %{nwam_manager.version}
Source:                  %{name}-manpages-0.1.tar.gz
Source1:                 %{name}-exec_attr
SUNW_BaseDir:            %{_prefix}
License:                 %{nwam_manager.license}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWlibgnomecanvas-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWcslr
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWlibunique
BuildRequires: SUNWlibnotify

Requires: SUNWlibgnomecanvas
Requires: %{name}-root
Requires: SUNWgnome-libs
Requires: SUNWgnome-session
Requires: SUNWcslr
Requires: SUNWdesktop-cache
Requires: SUNWlibgnome-keyring

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%nwam_manager.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%nwam_manager.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%nwam_manager.install -d %name-%version
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/security/exec_attr.d
install --mode=0644 %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/security/exec_attr.d/desktop-administration-nwam-manager

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):unsupported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri icon-cache gconf-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libexecdir}
%{_libexecdir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, bin) %{_datadir}/nwam-manager
%dir %attr (0755, root, bin) %{_datadir}/nwam-manager/icons
%attr (-, root, bin) %{_datadir}/nwam-manager/*.*
%attr (-, root, bin) %{_datadir}/nwam-manager/icons/*
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16/status
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/status
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/emblems
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/status
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/emblems
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/status
%attr (-, root, other) %{_datadir}/icons/hicolor/16x16/status/*
%attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/24x24/status/*
%attr (-, root, other) %{_datadir}/icons/hicolor/24x24/emblems/*
%attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/32x32/status/*
%attr (-, root, other) %{_datadir}/icons/hicolor/32x32/emblems/*
%attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps/*
%attr (-, root, other) %{_datadir}/icons/hicolor/48x48/status/*
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/nwam-manager/C
%{_datadir}/omf/nwam-manager/*-C.omf
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc -d nwam-manager-%{nwam_manager.version} AUTHORS README 
%doc(bzip2) -d nwam-manager-%{nwam_manager.version} ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files root
%defattr(-, root, sys)
%attr(0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/nwam-manager.schemas
%dir %attr (-, root, sys) %{_sysconfdir}/xdg
%dir %attr (-, root, sys) %{_sysconfdir}/xdg/autostart
%attr (-, root, sys) %{_sysconfdir}/xdg/autostart/*
%dir %attr(0755, root, sys) /etc/security
%dir %attr(0755, root, sys) /etc/security/exec_attr.d
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %attr (0444, root, sys) /etc/security/exec_attr.d/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
#%{_datadir}/gnome/help/*/[a-z]*
#%{_datadir}/omf/*/*-[a-z][a-z].omf
#%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z]*.omf

%changelog
* Mon Mar 14 2011 - brian.cameron@oracle.com
- Add exec_attr entries.
* Thu Aug 19 2010 - lin.ma@sun.com
- Update license.
* Fri Feb 24 2010 - lin.ma@sun.com
- Update for phase 1.0
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Sep 15 2008 - darren.kenny@sun.com
- Update copyright (thanks to Matt for the changes).
* Mon Sep 8 2008 - darren.kenny@sun.com
- Fix some icon file attributes.
* Fri Sep 5 2008 - darren.kenny@sun.com
- Comment more l10n dirs until there is something to deliver, it's
  causing build failures.
* Thu Sep 4 2008 - darren.kenny@sun.com
- Fix some issues in spec, add preun for schema and fix l10n build..
* Wed Sep 3 2008 - darren.kenny@sun.com
- Initial delivery.



