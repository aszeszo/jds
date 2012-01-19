#
# spec file for package SUNWgnome-menu-editor
#
# includes module(s): alacarte
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jedy
#
%include Solaris.inc
%use alacarte = alacarte.spec

Name:          SUNWgnome-menu-editor
IPS_package_name: desktop/xdg/menu-editor/alacarte
Meta(info.classification): %{classification_prefix}:Applications/Configuration and Preferences
Summary:       %alacarte.summary
Version:       %{alacarte.version}
Source:        %{name}-manpages-0.1.tar.gz
SUNW_Copyright: %{name}.copyright
License:       LGPLv2
SUNW_BaseDir:  %{_basedir}
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:      SUNWgnome-libs
Requires:      SUNWgnome-panel
Requires:      SUNWpygobject26
Requires:      SUNWpygtk2-26
Requires:      SUNWdesktop-cache
Requires:      SUNWPython26
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWpygobject26-devel
BuildRequires: SUNWpygtk2-26-devel
BuildRequires: SUNWPython26
BuildRequires: SUNWpython26-setuptools

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%alacarte.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export CFLAGS="%optflags"
export PYTHON="/usr/bin/python"%{default_python_version}
%alacarte.build -d %name-%version

%install
%alacarte.install -d %name-%version
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ${RPM_BUILD_ROOT}DISABLE

%post
%restart_fmri icon-cache

%files
%doc -d alacarte-%{alacarte.version} AUTHORS
%doc(bzip2) -d alacarte-%{alacarte.version} ChangeLog
%doc(bzip2) -d alacarte-%{alacarte.version} COPYING
%defattr(-, root, bin)
%{_bindir}/
%attr (-, root, bin) %{_libdir}/python*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/alacarte
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%attr (-, root, other) %{_datadir}/icons
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Oct 27 2009 - jedy.wang@sun.com
- Change to depend on python 2.6.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Fri Sep 19 2008 - christian.kelly@sun.com
- Set permissions on /usr/share/doc.
* Tue Sep 16 2008 - jedy.wang@sun.com
- Add copyright files.
* Tue Oct 12 2007 - jedy.wang@sun.com
- Take the ownership from harrylu and change the inline postinstall
  script to an include. 
* Tue Apr 24 2007 - laca@sun.com
- use $BASEDIR instead of $PKG_INSTALL_ROOT to fix diskless install
  (CR 6537817)
* Thu Nov 02 2006 - takao.fujiwara@sun.com
- Added l10n package. Fixes 6493499
* Fri Nov 16 2006 - damien.carbery@sun.com
- Add missing SUNWPython dependency (for /usr/bin/alacarte).
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Tue Aug 22 2006 - halton.huo@sun.com
- Divide SFEgnome-menu-editor.spec into alacarte.spec
  and SUNWgnome-menu-editor.spec
* Wed Aug 16 2006 - harry.lu@sun.com
- bump up to 0.9.90 and add patch alacarte-01-force-reload.diff to make
  it work on solaris.
* Wed Jul  5 2006 - laca@sun.com
- rename to SUNWgnome-menu-editor
- delete share subpkg
* Fri Apr 21 2006 - glynn.foster@sun.com
- Initial spec file


