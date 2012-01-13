#
# spec file for package SUNWseahorse-plugins
#
# includes module(s): seahorse-plugins
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc

%use sp = seahorse-plugins.spec

Name:                    SUNWseahorse-plugins
License: GPL v2, FDL v1.1
IPS_package_name:        gnome/security/seahorse/seahorse-plugins
Meta(info.classification): %{classification_prefix}:System/Security
Summary:                 Plugins for gedit and nautilus

Version:                 %{sp.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Source1:	%{name}-manpages-0.1.tar.gz
Requires: SUNWseahorse
Requires: %{name}-root
BuildRequires: SUNWseahorse-devel
BuildRequires: SUNWgnome-file-mgr-devel
BuildRequires: SUNWgnome-text-editor-devel
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWfirefox-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version
%sp.prep -d %name-%version

cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="%optflags -I%{_includedir}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%sp.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%sp.install -d %name-%version
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%doc -d seahorse-plugins-%{sp.version} AUTHORS README
%doc(bzip2) -d seahorse-plugins-%{sp.version} ChangeLog
%doc(bzip2) -d seahorse-plugins-%{sp.version} COPYING COPYING-DOCS
%doc(bzip2) -d seahorse-plugins-%{sp.version} NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*

%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/bonobo/servers
%{_libdir}/gedit-2/plugins
%{_libdir}/nautilus/extensions-2.0
%{_libdir}/seahorse

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/omf
%{_datadir}/omf/seahorse-plugins/*-C.omf
%{_datadir}/omf/seahorse-applet/*-C.omf
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, bin) %{_datadir}/gnome-2.0
%dir %attr (0755, root, bin) %{_datadir}/gnome-2.0/ui
%{_datadir}/gnome-2.0/ui/*.xml
%dir %attr (0755, root, bin) %{_datadir}/seahorse-plugins
%{_datadir}/seahorse-plugins/*
%dir %attr (-, root, root) %{_datadir}/mime
%dir %attr (-, root, root) %{_datadir}/mime/packages
%{_datadir}/mime/packages/seahorse.xml

%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/apps/
%{_datadir}/icons/hicolor/48x48/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*

%dir %attr (0755, root, other) %{_datadir}/gnome
%dir %attr (0755, root, bin) %{_datadir}/gnome/help
%{_datadir}/gnome/help/*/C
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

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
%{_sysconfdir}/gconf/schemas/*.schemas

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Oct 16 2009 - jeff.cai@sun.com
- Initial spec



