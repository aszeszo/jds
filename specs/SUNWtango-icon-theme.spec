#
# spec file for package SUNWtango-icon-theme
#
# includes module(s): tango-icon-theme
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#
%include Solaris.inc
%include base.inc

%use tango = tango-icon-theme.spec

Name:                    SUNWtango-icon-theme
IPS_package_name:        gnome/theme/tango-icon-theme
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Tango icon theme
Version:                 %{tango.version}
License:                 %{tango.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWicon-naming-utils
BuildRequires: SUNWimagick

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

mkdir %name-%version/%{base_arch}
%tango.prep -d %name-%version/%{base_arch}

%build
export PKG_CONFIG=/usr/bin/pkg-config
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

%tango.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%tango.install -d %name-%version/%{base_arch}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/icons/Tango
%{_datadir}/icons/Tango/*/emotes/*
%{_datadir}/icons/Tango/*/categories/*
%{_datadir}/icons/Tango/*/devices/*
%{_datadir}/icons/Tango/*/status/*
%{_datadir}/icons/Tango/*/places/*
%{_datadir}/icons/Tango/*/mimetypes/*
%{_datadir}/icons/Tango/*/actions/*
%{_datadir}/icons/Tango/*/apps/*
%{_datadir}/icons/Tango/*/animations/*
%{_datadir}/icons/Tango/*/emblems/*
%{_datadir}/icons/Tango/index.theme
%doc -d %{base_arch} tango-icon-theme-%{tango.version}/README
%doc -d %{base_arch} tango-icon-theme-%{tango.version}/AUTHORS
%doc(bzip2) -d %{base_arch} tango-icon-theme-%{tango.version}/COPYING
%doc(bzip2) -d %{base_arch} tango-icon-theme-%{tango.version}/NEWS
%doc(bzip2) -d %{base_arch} tango-icon-theme-%{tango.version}/ChangeLog
%doc(bzip2) -d %{base_arch} tango-icon-theme-%{tango.version}/po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/icons

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Sun Jan  3 2010 - christian.kelly@sun.com
- Fix %files.
* Fri Nov 20 2009 - christian.kelly@sun.com
- Fix %files, add %changelog.


