#
# spec file for package SUNWgnome-fonts
#
# includes module(s): ttf-baekmuk ttf-freefont
#
# Copyright (c) 2004, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner dermot
#
%include Solaris.inc
%define _prefix /usr

%use ttf_baekmuk = ttf-baekmuk.spec
%use ttf_freefont = ttf-freefont.spec

Name:                    SUNWgnome-fonts
IPS_package_name:        system/font/gnome-fonts
Meta(info.classification): %{classification_prefix}:System/Fonts
Summary:                 GNOME Unicode and Korean TrueType fonts
Version:                 %{default_pkg_version}
SUNW_BaseDir:            %{_prefix}
SUNW_Copyright:          %{name}.copyright
License:                 %{ttf_freefont.license}, %{ttf_baekmuk.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%define font_dir %{_datadir}/fonts/TrueType

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: system/library/fontconfig

%prep
rm -rf %name-%version
mkdir %name-%version
%ttf_baekmuk.prep -d %name-%version
%ttf_freefont.prep -d %name-%version

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export MSGFMT="/usr/bin/msgfmt"
export LDFLAGS="%_ldflags"
export CFLAGS="%optflags"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
%ttf_baekmuk.build -d %name-%version
%ttf_freefont.build -d %name-%version

%install
%ttf_baekmuk.install -d %name-%version
%ttf_freefont.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{font_dir}

%changelog
* Wed Mar 30 2011 - jan.hnatek@oracle.com
- update freefont to 20100919
* Thu Oct 22 2009 - dave.lin@sun.com
- Fixed the %{_datadir} attribute issue.
* Thu Oct 15 2009 - alan.coopersmith@sun.com
- move from /usr/openwin to /usr/share/fonts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Mon May 03 2004 - laca@sun.com
- move to /usr/openwin


