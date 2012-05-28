#
# spec file for package SUNWdia
#
# includes module(s): dia
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jeffcai 
#
%include Solaris.inc
%use dia = dia.spec

Name:             SUNWdia
IPS_package_name: editor/diagram/dia
Meta(info.classification): %{classification_prefix}:Applications/Graphics and Imaging
Summary:          Dia Diagram Editor
Source:           %{name}-manpages-0.1.tar.gz
Version:          %{dia.version}
SUNW_BaseDir:     %{_basedir}
SUNW_Copyright:   %{name}.copyright
License:          %{dia.license}
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       image/library/libart
Requires:       library/desktop/gtk2
Requires:       library/gnome/gnome-libs
Requires:       system/library/gcc-3-runtime
BuildRequires:       library/gnome/gnome-keyring
BuildRequires:       library/desktop/gtk2
BuildRequires:       system/library/gcc-3-runtime

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%dia.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%dia.build -d %name-%version

%install
%dia.install -d %name-%version

rm -r $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/dia.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/dia.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/dia.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/dia.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/dia.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/dia.svg
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/dia/C
%{_datadir}/gnome/help/dia/en
%{_datadir}/man/*
%dir %attr (0755, root, other) %{_datadir}/mime-info
%{_datadir}/mime-info/*
%{_datadir}/omf/*
%dir %attr (0755, root, other) %{_datadir}/dia
%{_datadir}/dia/*
%doc -d dia-%{dia.version} AUTHORS README
%doc(bzip2) -d dia-%{dia.version} COPYING ChangeLog NEWS po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/dia/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/dia/eu
# Comment this line out since no [a-d]* locale at this point
#%{_datadir}/gnome/help/dia/[a-d]*
%{_datadir}/gnome/help/dia/[f-z]*

%changelog
* Mon Jan 25 2010 - jerry.tan@sun.com
- bump to 0.97.1
* Wed Oct 22 2008 - matt.keenan@sun.com
- Created



