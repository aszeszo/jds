#
# Copyright (c) 2008, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: laca
#
%include Solaris.inc

%define owner laca

Name:                SUNWos-welcome
IPS_package_name:    release/os-welcome
Meta(info.classification): %{classification_prefix}:System/Text Tools
Summary:             Oracle Solaris Welcome Pack
Version:             1.1.8
Source:              os-welcome-%{version}.tar.bz2
License:             cr_Oracle
SUNW_BaseDir:        /
SUNW_Copyright:      %{name}.copyright
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWdesktop-cache
Requires: runtime/python-26

%prep
%setup -q -n os-welcome-%{version}

rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Most .mo files include the translations of .desktop only.
# We do not want additional packages at the moment.
( \
  cd $RPM_BUILD_ROOT/%_datadir/locale; \
  /bin/ls | grep -v '^de$' | grep -v '^es$' | grep -v '^fr$' | grep -v '^it$' |\
  grep -v '^ja$' | grep -v '^ko$' | grep -v '^pt_BR$' | grep -v '^ru$' |\
  grep -v '^ar$' | grep -v '^ca$' | grep -v '^cs$' | grep -v '^el$' |\
  grep -v '^he$' | grep -v '^hu$' |\
  grep -v '^id$' | grep -v '^nl$' | grep -v '^pl$' | grep -v '^sk$' |\
  grep -v '^sv$' | grep -v '^zh_CN$' | grep -v '^zh_HK$' | grep -v '^zh_TW$' |\
  xargs /bin/rm -r; \
)


%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_basedir}
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/os-about
%{_bindir}/os-next-steps
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/os-welcome
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*.desktop
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/os-welcome/html/C
%{_datadir}/doc/os-welcome/html/index.html
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*.png
%dir %attr (0755, root, bin) %{_datadir}/os-about
%{_datadir}/os-about/*.png
%{_datadir}/os-about/*.jpg

%dir %attr (0755, root, other) %{_datadir}/locale

%{_datadir}/doc/os-welcome/html/ar
%dir %attr (0755, root, other) %{_datadir}/locale/ar
%dir %attr (0755, root, other) %{_datadir}/locale/ar/LC_MESSAGES
%{_datadir}/locale/ar/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/ca
%dir %attr (0755, root, other) %{_datadir}/locale/ca
%dir %attr (0755, root, other) %{_datadir}/locale/ca/LC_MESSAGES
%{_datadir}/locale/ca/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/cs
%dir %attr (0755, root, other) %{_datadir}/locale/cs
%dir %attr (0755, root, other) %{_datadir}/locale/cs/LC_MESSAGES
%{_datadir}/locale/cs/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/de
%dir %attr (0755, root, other) %{_datadir}/locale/de
%dir %attr (0755, root, other) %{_datadir}/locale/de/LC_MESSAGES
%{_datadir}/locale/de/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/el
%dir %attr (0755, root, other) %{_datadir}/locale/el
%dir %attr (0755, root, other) %{_datadir}/locale/el/LC_MESSAGES
%{_datadir}/locale/el/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/es
%dir %attr (0755, root, other) %{_datadir}/locale/es
%dir %attr (0755, root, other) %{_datadir}/locale/es/LC_MESSAGES
%{_datadir}/locale/es/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/fr
%dir %attr (0755, root, other) %{_datadir}/locale/fr
%dir %attr (0755, root, other) %{_datadir}/locale/fr/LC_MESSAGES
%{_datadir}/locale/fr/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/he
%dir %attr (0755, root, other) %{_datadir}/locale/he
%dir %attr (0755, root, other) %{_datadir}/locale/he/LC_MESSAGES
%{_datadir}/locale/he/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/hu
%dir %attr (0755, root, other) %{_datadir}/locale/hu
%dir %attr (0755, root, other) %{_datadir}/locale/hu/LC_MESSAGES
%{_datadir}/locale/hu/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/id
%dir %attr (0755, root, other) %{_datadir}/locale/id
%dir %attr (0755, root, other) %{_datadir}/locale/id/LC_MESSAGES
%{_datadir}/locale/id/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/it
%dir %attr (0755, root, other) %{_datadir}/locale/it
%dir %attr (0755, root, other) %{_datadir}/locale/it/LC_MESSAGES
%{_datadir}/locale/it/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/ja
%dir %attr (0755, root, other) %{_datadir}/locale/ja
%dir %attr (0755, root, other) %{_datadir}/locale/ja/LC_MESSAGES
%{_datadir}/locale/ja/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/ko
%dir %attr (0755, root, other) %{_datadir}/locale/ko
%dir %attr (0755, root, other) %{_datadir}/locale/ko/LC_MESSAGES
%{_datadir}/locale/ko/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/nl
%dir %attr (0755, root, other) %{_datadir}/locale/nl
%dir %attr (0755, root, other) %{_datadir}/locale/nl/LC_MESSAGES
%{_datadir}/locale/nl/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/pl
%dir %attr (0755, root, other) %{_datadir}/locale/pl
%dir %attr (0755, root, other) %{_datadir}/locale/pl/LC_MESSAGES
%{_datadir}/locale/pl/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/pt_BR
%dir %attr (0755, root, other) %{_datadir}/locale/pt_BR
%dir %attr (0755, root, other) %{_datadir}/locale/pt_BR/LC_MESSAGES
%{_datadir}/locale/pt_BR/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/ru
%dir %attr (0755, root, other) %{_datadir}/locale/ru
%dir %attr (0755, root, other) %{_datadir}/locale/ru/LC_MESSAGES
%{_datadir}/locale/ru/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/sk
%dir %attr (0755, root, other) %{_datadir}/locale/sk
%dir %attr (0755, root, other) %{_datadir}/locale/sk/LC_MESSAGES
%{_datadir}/locale/sk/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/sv
%dir %attr (0755, root, other) %{_datadir}/locale/sv
%dir %attr (0755, root, other) %{_datadir}/locale/sv/LC_MESSAGES
%{_datadir}/locale/sv/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/zh_CN
%dir %attr (0755, root, other) %{_datadir}/locale/zh_CN
%dir %attr (0755, root, other) %{_datadir}/locale/zh_CN/LC_MESSAGES
%{_datadir}/locale/zh_CN/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/zh_HK
%dir %attr (0755, root, other) %{_datadir}/locale/zh_HK
%dir %attr (0755, root, other) %{_datadir}/locale/zh_HK/LC_MESSAGES
%{_datadir}/locale/zh_HK/LC_MESSAGES/*.mo

%{_datadir}/doc/os-welcome/html/zh_TW
%dir %attr (0755, root, other) %{_datadir}/locale/zh_TW
%dir %attr (0755, root, other) %{_datadir}/locale/zh_TW/LC_MESSAGES
%{_datadir}/locale/zh_TW/LC_MESSAGES/*.mo

%attr (0755, root, sys) %dir %{_sysconfdir}
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg/autostart
%attr (-, root, sys) %{_sysconfdir}/xdg/autostart/*

%changelog
* Thu Aug 11 2011 - glynn.foster@oracle.com
- Bump to 1.1.8, includes more l10n
* Thu Jun 23 2011 - glynn.foster@oracle.com
- Bump to 1.1.6, including l10ns
* Mon Jun 20 2011 - glynn.foster@oracle.com
- Bump to 1.1.5
* Mon May 09 2011 - glynn.foster@oracle.com
- Bump to 1.1.4, fixes what's new link
* Fri Apr 29 2011 - glynn.foster@oracle.com
- Bump to 1.1.3, which removes registration utility
  and updates the branding.
* Fri Jan 21 2011 - glynn.foster@oracle.com
- Bump to 1.1.2
* Fri Oct 15 2010 - glynn.foster@oracle.com
- Bump to 1.0.9
* Thu Oct 14 2010 - glynn.foster@oracle.com
- Bump to 1.0.8
* Mon Oct 05 2010 - glynn.foster@sun.com
- Bump to 1.0.7
* Fri Oct 01 2010 - glynn.foster@sun.com
- Bump to 1.0.6
* Thu Aug 26 2010 - glynn.foster@sun.com
- Bump to 1.0.3
* Wed Aug 25 2010 - glynn.foster@sun.com
- Bump to 1.0.2
* Mon Aug 23 2010 - glynn.foster@sun.com
- Bump, and fix so it builds
* Thu Aug 19 2010 - glynn.foster@sun.com
- New module, 1.0.0
