#
# spec file for package SUNWgnome-devel-docs
#
# includes module(s): GNOME Devel Docs
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner davelam
#
#
%include Solaris.inc

%use gdd = gnome-devel-docs.spec

Name:               SUNWgnome-devel-docs
IPS_package_name:   documentation/gnome/gnome-devel-docs
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:            GNOME developer documentation
Version:            %{gdd.version}
SUNW_BaseDir:       %{_basedir}
SUNW_Copyright:     %{name}.copyright
License:            %{gdd.license}
BuildRoot:          %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: library/python-2/libxml2-26
BuildRequires: SUNWlxsl
BuildRequires: SUNWgnome-libs
BuildRequires: SUNWgnome-doc-utils
Requires: SUNWgnome-help-viewer
Requires: SUNWgnome-libs

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%gdd.prep -d %name-%version

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export MSGFMT="/usr/bin/msgfmt"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export LDFLAGS="%_ldflags"
export CFLAGS="%optflags"
%gdd.build -d %name-%version

%install
%gdd.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

# Remove scrollkeeper files before packaging.
rm -rf $RPM_BUILD_ROOT/var

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/C
%{_datadir}/omf/*/*-C.omf

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z][a-z].omf
%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z]*.omf

%changelog
* Tue Jun 09 2009 - brian.cameron@sun.com
- Fix packaging when building without l10n.
* Fri Apr 03 2009 - laca@sun.com
- stop using postrun.
* Tue Mar 17 2009 - dave.lin@sun.conm
- Uncomment %{_datadir}/omf/*/*-[a-z][a-z]_[A-Z]*.omf in %file l10n.
* Mon Sep 10 2007 - Damien Carbery <damien.carbery@sun.com>
- Update dependencies.
* Sat Sep 01 2007 - Dave Lin <dave.lin@sun.com>
- initial version.



