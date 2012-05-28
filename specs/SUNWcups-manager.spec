#
# spec file for package SUNWcups-manager
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

#
%define owner gheet
#

%include Solaris.inc 

%use scp = system-config-printer.spec

Name:                    SUNWcups-manager
IPS_package_name:        print/cups/system-config-printer
Meta(info.classification): %{classification_prefix}:System/Administration and Configuration
License:  		 GPL v2
Summary:                 Print Manager for CUPS
Version:                 %{scp.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                library/python-2/python-dbus-26
Requires:                runtime/python-26
Requires:                library/python-2/pycups
Requires:                print/cups
BuildRequires:           print/cups
BuildRequires:           developer/gnome/gnome-doc-utils
BuildRequires:           library/gnome/gnome-libs
BuildRequires:           gnome/preferences/control-center

%include default-depend.inc
%include desktop-incorporation.inc

%package root
Summary:		 %{summary} - / filesystem
SUNW_BaseDir:		 /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir -p %name-%version
%scp.prep -d %name-%version

%build
%scp.build -d %name-%version

%install
%scp.install -d %name-%version


%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/%{scp.name}/icons/*
%{_datadir}/%{scp.name}/*.glade
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/%{scp.name}.desktop
%doc -d %scp.name-%{scp.version} AUTHORS README NEWS
%doc(bzip2) -d %scp.name-%{scp.version} COPYING ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/%{scp.name}/C
%{_datadir}/omf/%{scp.name}

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%attr(0755, root, bin) %dir %{_sysconfdir}/dbus-1
%attr(0755, root, bin) %dir %{_sysconfdir}/dbus-1/system.d
%{_sysconfdir}/dbus-1/system.d/*
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg/autostart
%{_sysconfdir}/xdg/autostart/print-applet.desktop

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z][a-z].omf
%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z]*.omf

%changelog
* Thu Aug 18 2011 - ghee.teo@oracle.com
- Reclaim desktop file from ON, 7076227.
* Tue Dec 09 2008 - takao.fujiwara@sun.com
- Add l10n package.
* Thu Dec 04 2008 - dave.lin@sun.com
- Add BuildRequires on SUNWgnome-desktop-prefs(desktop-file-install)
* Tues Nov 18 2008 - ghee.teo@sun.com
- Initial version.



