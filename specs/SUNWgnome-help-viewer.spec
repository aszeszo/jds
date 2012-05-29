#
# spec file for package SUNWgnome-help-viewer
#
# includes module(s): yelp
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

#
%define owner leonfan
#
%include Solaris.inc

%use yelp = yelp.spec

Name:                    SUNWgnome-help-viewer
License:                 GPLv2
IPS_package_name:        gnome/help-viewer/yelp
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Documentation
Summary:                 GNOME help system
Version:                 %{yelp.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Requires:	library/desktop/libglade
Requires:	library/gnome/gnome-libs
Requires:       library/gnome/gnome-vfs
Requires:       library/gnome/gnome-component
Requires:       gnome/config/gconf
Requires:       library/libxml2
Requires:       library/libxslt
Requires:  	web/browser/firefox
Requires:       compress/bzip2
Requires:       system/library/c++-runtime
Requires:       library/popt
Requires:       library/zlib
Requires:       service/gnome/desktop-cache
Requires:       gnome/accessibility/orca
BuildRequires:  library/desktop/libglade
BuildRequires:  library/popt
BuildRequires:  web/browser/firefox
BuildRequires:  library/gnome/gnome-vfs
BuildRequires:  library/gnome/gnome-component
BuildRequires:  library/gnome/gnome-libs
BuildRequires:  gnome/config/gconf
BuildRequires:  developer/gnome/gnome-doc-utils
BuildRequires:  library/libxml2
BuildRequires:  library/libxslt
BuildRequires:  library/desktop/gtk2
BuildRequires:  system/library/dbus

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir %name-%version
%yelp.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export CFLAGS="%optflags -I%{_includedir}/mps -DANSICPP -DI_KNOW_RARIAN_0_8_IS_UNSTABLE"
export RPM_OPT_FLAGS="$CFLAGS"
export CXXFLAGS="%cxx_optflags -I%{_includedir}/mps"
export ACLOCAL_FLAGS="-I ./m4"
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export LDFLAGS="%_ldflags -lgthread-2.0"

%yelp.build -d %name-%version

%install
%yelp.install -d %name-%version
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%attr (-, root, other) %{_datadir}/icons
%{_datadir}/yelp
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc -d yelp-%{yelp.version} AUTHORS README
%doc(bzip2) -d yelp-%{yelp.version} COPYING ChangeLog NEWS
%doc(bzip2) -d yelp-%{yelp.version} stylesheets/ChangeLog po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/yelp.schemas

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Dec 01 2009 - ke.wang@sun.com
- Bump to 2.28.1
- Add -lgthread-2.0 to ldflags.
* Fri Jun 05 2009 - ginn.chen@sun.com
- Backout Dave's last change, it should be fixed in firefox-*.pc instead.
* Fri Jun 05 2009 - dave.lin@sun.com
- Add -L%{_libdir}/mps in LDFLAGS to make sure the bundled version of nspr is used.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Thu Sep 11 2008 - matt.keenn@sun.com
- Update copyright
* Fri Jul 18 2008 - dave.lin@sun.com
- Removed the self-dependency
* Fri May 16 2008 - evan.yan@sun.com
- Undo Evan's change - revert todepend on SUNWfirefox/-devel because FF3 is not
  stable enough to be the default browser in Nevada.
* Thu May 15 2008 - damien.carbery@sun.com
- Remove references to /usr/sfw because freetype2 is under /usr now.
* Thu May 08 2008 - evan.yan@sun.com
- Remove Build/Requires SUNWfirefox/-devel because we have moved dependence to
  firefox3 and will remove firefox2 from vermillion.
* Mon Apr 21 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWfirefox3/-devel because yelp has been patched to use
  firefox3.
* Thu Jan 24 2008 - glynn.foster@sun.com
- Fix up gconf install
* Wed Nov 28 2008 - damien.carbery@sun.com
- Add -DI_KNOW_RARIAN_0_8_IS_UNSTABLE to CFLAGS as required by rarian-info.h.
* Thu Oct 11 2007 - damien.carbery@sun.com
- Remove install dependency on SUNWgnome-doc-utils and change the build
  dependency from SUNWgnome-doc-utils-devel to SUNWgnome-doc-utils.
* Fri Sep 28 2007 - laca@sun.com
- delete SUNWxwrtl dep
- add -norunpath flag for CXX and fix LDFLAGS
* Fri Aug 17 2007 - damien.carbery@sun.com
- Move rarian to SUNWgnome-libs.spec, replacing scrollkeeper. Remove devel
  package and other rarian related changes.
* Wed Aug 01 2007 - damien.carbery@sun.com
- Add rarian module as required by yelp 2.19.1.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
* Wed Jul 26 2006 - matt.keenan@sun.com
- Bump to 2.15.5, update %files, bonobo support has been removed.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Sat May 13 2006 - laca@sun.com
- Remove /usr/lib/jds-private from LDFLAGS
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Thu Jan 05 2006 - damien.carbery@sun.com
- Complete the Build/Requires lists.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Fri Sep 30 2005 - damien.carbery@sun.com
- Add icons dir to %files; remove /etc dir before packaging.
* Thu Jul 21 2005 - damien.carbery@sun.com
- Add SUNWmozilla dependency as configure breaking without mozilla.
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Wed Aug 18 2004 - damien.carbery@sun.com
- Change manpage perms for Solaris integration.
* Fri Jul 09 2004 - damien.carbery@sun.com
- Return -R to LDFLAGS. I had incorrectly implemented the ARC decision.
* Thu Jul 08 2004 - damien.carbery@sun.com
- Remove -R from LDFLAGS because ARC said to use -norunpath.
* Fri Jul 02 2004 - damien.carbery@sun.com
- Add /usr/lib/jds-private to LDFLAGS.
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Fri May 14 2004 - laca@sun.com
- Added libxslt dependency
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Mon Mar 01 2004 - <laca@sun.com>
- define PERL5LIB.
- remove non-existant dirs from %files share
* Tue Feb 17 2004 - <niall.power@sun.com
- initial spec file created


