#
# # spec file for package SUNWiso-codes.spec
#
# includes module(s): iso-codes
#
# Copyright (c) 2005 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc

%use iso_codes = iso-codes.spec

Name:                    SUNWiso-codes
IPS_package_name:        data/iso-codes
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 ISO code lists and translations
Version:                 %{iso_codes.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{iso_codes.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: runtime/python-26

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWiso-codes

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%iso_codes.prep -d %name-%version

%build
%iso_codes.build -d %name-%version

%install
%iso_codes.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/xml/iso-codes

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/pkgconfig
%{_datadir}/pkgconfig/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Mon Feb  5 2007 - laca@sun.com
- add Python dependency
* Sun Jan 21 2007 - laca@sun.com
- update %files for version 1.0
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
- Fri Jun  9 2006 - laca@sun.com
- separate the l10n stuff, fixes CR 6436771
* Thu Sep 15 2005 - laca@sun.com
- created


