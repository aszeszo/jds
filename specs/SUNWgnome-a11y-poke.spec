#
# spec file for package SUNWgnome-a11y-poke
#
# includes module(s): accerciser
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan
#
%include Solaris.inc
%use accerciser = accerciser.spec

Name:              SUNWgnome-a11y-poke
License:	   BSD
IPS_package_name:  gnome/accessibility/accerciser
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
Summary:           Interactive Python Accessibility Explorer
Version:           %{accerciser.version}
Source:            %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:      %{_basedir}
SUNW_Copyright:    %{name}.copyright
BuildRoot:         %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: library/python-2/pygtk2-26
Requires: library/python-2/python-gnome-desktop-26
Requires: runtime-python-26
Requires: library/python-2/ipython-26
Requires: gnome/config/gconf
Requires: service/gnome/desktop-cache
BuildRequires: runtime/python-26
BuildRequires: library/python-2/pygtk2-26
BuildRequires: library/python-2/python-gnome-desktop-26
BuildRequires: developer/gnome/gettext
BuildRequires: developer/gnome/gnome-doc-utils
BuildRequires: library/python-2/pyatspi-26

%package l10n
Summary:                 %{summary} - l10n files

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%prep
rm -rf %name-%version
mkdir %name-%version
%accerciser.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export PYTHON="/usr/bin/python2.6"

%accerciser.build -d %name-%version

%install
%accerciser.install -d %name-%version

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache icon-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr(0755, root, sys) %{_datadir}
%{_datadir}/accerciser
%dir %attr (0755, root, bin) %{_datadir}/omf
%{_datadir}/omf/*
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*.desktop
%doc -d accerciser-%{accerciser.version} README AUTHORS
%doc(bzip2) -d accerciser-%{accerciser.version} COPYING NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/*
%dir %attr (0755, root, other) %{_datadir}/gnome
%dir %attr (0755, root, bin) %{_datadir}/gnome/help
%{_datadir}/gnome/help/*
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files root
%defattr (-, root, sys)
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, sys) %{_sysconfdir}/gconf
%dir %attr (0755, root, sys) %{_sysconfdir}/gconf/schemas
%{_sysconfdir}/gconf/schemas/*.schemas

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Mon Feb 13 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Mon Feb 08 2009 - li.yuan@sun.com
- Remove build require.
* Wed Dec 16 2009 - li.yuan@sun.com
- Build require SUNWpyatspi.
* Wed Oct 14 2009 - li.yuan@sun.com
- Update dependencies.
* Wed Oct 14 2009 - li.yuan@sun.com
- Use Python 2.6.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Thu Sep 18 2008 - li.yuan@sun.com
- Added %doc to %files for copyright.
* Mon Mar 31 2008 - li.yuan@sun.com
- Add copyright file
* Thu Jan 10 2008 - li.yuan@sun.com
- change owner to liyuan.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Mon Nov 12 2007 - li.yuan@sun.com
- Use script for post and postun.
* Thu Oct  4 2007 - laca@sun.com
- delete unneeded env vars; set PYTHON to the versioned binary
* Tue Sep 18 2007 - laca@sun.com
- add missing %defattr in %files root
* Thu Sep 06 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-python-desktop/-devel for wnck and other python
  modules.
* Tue Sep 04 2007 - damien.carbery@sun.com
- Correct dir perms in root package.
* Sun Sep 02 2007 - li.yuan@sun.com
- Use accerciser to replace at-poke.
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Sat May 13 2006 - laca@sun.com
- Remove /usr/lib/jds-private from LDFLAGS
* Tue May 09 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Thu Jan  2 2006 - damien.carbery@sun.com
- Update Build/Requires to fix 6319720/2129498.
* Wed Oct 13 2004 - laca@sun.com
- define share subpkg, move existing %files to %files share and
  add %files for bindir/at-poke
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Sep 20 2004 - damien.carbery@sun.com
- Correct syntax for addition of manpage.
* Thu Sep 09 2004 - matt.keenan@sun.com
- Added at-poke.1 manpage
* Tue Jul 20 2004 - damien.carbery@sun.com
- Remove SUNWgnome-xml BuildRequires. Failed in test build.
* Tue Jul 20 2004 - damien.carbery@sun.com
- Initial version.


