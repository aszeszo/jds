#
# spec file for package SUNWgnome-crash-report
#
# includes module(s): bug-buddy
#
# Copyright 2009, 2012 Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#temporarily taken from mattman
%define owner stephen
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
#%define _sysconfdir /etc/%{_arch64}
%use bug_buddy_64 = bug-buddy.spec
%endif

%include base.inc

%use bug_buddy = bug-buddy.spec

Name:                    SUNWgnome-crash-report
IPS_package_name:        gnome/crash-report/bug-buddy
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:                 GNOME crash report generator
Version:                 %{bug_buddy.version}
License:		 %{bug_buddy.license}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       library/desktop/gtk2
Requires:       library/gnome/gnome-vfs
Requires:       library/gnome/gnome-component
Requires:       library/gnome/gnome-libs
Requires:       gnome/gnome-panel
Requires:       gnome/config/gconf
Requires:       library/libxml2
Requires:       service/gnome/desktop-cache
Requires:       library/libgtop
BuildRequires:       library/desktop/gtk2
BuildRequires:       library/gnome/gnome-vfs
BuildRequires:       library/gnome/gnome-component
BuildRequires:       library/gnome/gnome-libs
BuildRequires:       gnome/gnome-panel
BuildRequires:       gnome/config/gconf
BuildRequires:       library/libxml2
BuildRequires: 	     library/libgtop

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%bug_buddy_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%bug_buddy.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%ifarch amd64 sparcv9
%bug_buddy_64.build -d %name-%version/%_arch64
%endif

%bug_buddy.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%bug_buddy_64.install -d %name-%version/%_arch64
%endif

%bug_buddy.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/applications

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (-, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/HighContrastLargePrint
%dir %attr (-, root, other) %{_datadir}/icons/HighContrastLargePrint/*
%dir %attr (-, root, other) %{_datadir}/icons/HighContrastLargePrint/*/*
%{_datadir}/icons/HighContrastLargePrint/48x48/apps/bug-buddy.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/bug-buddy.svg
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/*
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/*
%{_datadir}/icons/hicolor/16x16/apps/bug-buddy.png
%{_datadir}/icons/hicolor/22x22/apps/bug-buddy.png
%{_datadir}/icons/hicolor/24x24/apps/bug-buddy.png
%{_datadir}/icons/hicolor/32x32/apps/bug-buddy.png
%{_datadir}/icons/hicolor/48x48/apps/bug-buddy.png
%{_datadir}/bug-buddy
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/*
%{_libdir}/*/*/*
%doc -d %{base_arch}/bug-buddy-%{bug_buddy.version} AUTHORS README
%doc -d %{base_arch}/bug-buddy-%{bug_buddy.version} google-breakpad/AUTHORS
%doc -d %{base_arch}/bug-buddy-%{bug_buddy.version} google-breakpad/COPYING
%doc -d %{base_arch}/bug-buddy-%{bug_buddy.version} google-breakpad/ChangeLog
%doc -d %{base_arch}/bug-buddy-%{bug_buddy.version} google-breakpad/README
%doc(bzip2) -d %{base_arch}/bug-buddy-%{bug_buddy.version} COPYING ChangeLog po/ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/bug-buddy.schemas

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Thu Nov 26 2009 - christian.kelly@sun.com
- Fix directory perms.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 23 2009 - matt.keenn@sun.com
- Add delivery of 64bit version of libgnomebreakpad.so #6819745
* Thu Sep 11 2008 - matt.keenn@sun.com
- Update copyright
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Thu Oct  4 2007 - laca@sun.com
- delete unneeded env vars
* Fri Sep 28 2007 - damien.carbery@sun.com
- Add -norunpath to CXX path so that Sun internal runpaths are not embedded in
  libgnomebreakpad.so.
* Tue Aug 28 2007 - matt.keenan@sun.com
- update files for 2.19.91 tarball
* Fri Aug 10 2007 - damien.carbery@sun.com
- Unbump to 2.18.1 so that it builds.
* Thu Aug 09 2007 - damien.carbery@sun.com
- Change to use gcc.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Fri Sep 08 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Tue Sep 05 2006 - damien.carbery@sun.com
- Update packaging for new tarball.
* Wed Aug 16 2006 - damien.carbery@sun.com
- Change 'icons' line in %files to pick up files.
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
* Wed Jul 26 2006 - damien.carbery@sun.com
- Update packaging for new tarball (icons moved).
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu May 25 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Sun Feb 19 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Fri Oct 28 2005 - damien.carbery@sun.com
- Complete dependency listing.
* Wed Oct 26 2005 - glynn.foster@sun.com
- Resurrect bug-buddy, and get it to work with pstack



