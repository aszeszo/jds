#
# spec file for package SUNWevolution-libs
#
# includes module(s): gtkhtml
#
# Copyright (c) 2004, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc
%use gtkhtml = gtkhtml.spec

Name:          SUNWevolution-libs
License: GPL v2, LGPL v2
IPS_package_name: library/desktop/gtkhtml
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       Evolution Email and Calendar - support libraries
Version:       %{gtkhtml.version}
SUNW_Category: EVO25,%{default_category}
SUNW_BaseDir:  %{_basedir}
SUNW_Copyright:%{name}.copyright
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Source1:       %{name}-manpages-0.1.tar.gz
Requires:       library/desktop/libgnomecanvas
Requires:       gnome/config/gconf
Requires:       library/libxml2
Requires:       library/zlib
Requires:       library/gnutls
Requires:       library/gnome/gnome-component
Requires:       library/gnome/gnome-libs
Requires:       system/library/security/libgcrypt
Requires:       system/library/math
Requires:       library/libsoup
Requires:       library/spell-checking/enchant
Requires:       data/iso-codes
BuildRequires:       library/desktop/libgnomecanvas
BuildRequires:       library/gnome/gnome-component
BuildRequires:       library/gnome/gnome-libs
BuildRequires:       system/library/security/libgcrypt
BuildRequires:       gnome/config/gconf
BuildRequires:       library/gnome/gnome-component
BuildRequires:       library/libsoup
BuildRequires:       library/spell-checking/enchant
BuildRequires:       data/iso-codes
BuildRequires:       gnome/theme/gnome-icon-theme
BuildRequires:       system/header
#BuildRequires:       developer/icu
BuildRequires:       library/pcre

%package l10n
Summary:		%{summary} - l10n files
Requires:		%{name}

%package devel
Summary:		%{summary} - development files
SUNW_BaseDir:		%{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:       library/desktop/gtkhtml

%prep
rm -rf %name-%version
mkdir -p %name-%version
%gtkhtml.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
%if %debug_build
# Omit '-xO4 -xspace' from sparc flags as it crashes libgnome-gtkhtml-editor.
# See #6461613.
%else
%ifarch sparc
%define optflags           -i -xstrconst -xarch=v8a -mr
%define cxx_optflags       -i -xarch=v8a -mr -norunpath
%define optflags64	   -i -xstrconst -xarch=v9 -xcode=pic32 -mr
%endif
%endif
export LDFLAGS="%_ldflags -L%{_libdir} -R%{_libdir}"
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export PKG_CONFIG_PATH=%{_pkg_config_path}
%gtkhtml.build -d %name-%version

%install
%gtkhtml.install -d %name-%version
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files

%doc -d gtkhtml-%{gtkhtml.version} AUTHORS README
%doc(bzip2) -d gtkhtml-%{gtkhtml.version} ChangeLog
%doc(bzip2) -d gtkhtml-%{gtkhtml.version} COPYING COPYING.LIB
%doc(bzip2) -d gtkhtml-%{gtkhtml.version} NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gtkhtml-editor-test
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtkhtml-%{gtkhtml.major_version}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Fri May 18 2012 - jeff.cai@oracle.com
- Add patch -030-libtool to use the new libtool
* Sun Jan 17 2010 - christian.kelly@sun.com
- Add dep on SUNWgnome-icon-theme.
* Mon Dec 21 2009 - ghee.teo@sun.com
- Remove SUNWgnome-print dependency.
* Tue Sep 16 2008 - jeff.cai@sun.com
- Add copyright
* Mon Jul 28 2008 - jeff.cai@sun.com
- Add manpages.
* Thu Jun 12 2008 - jeff.cai@sun.com
  libsoup has been moved from this file, thus SUNWgnutls-devel is not needed.
* Fri May 30 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-spell/-devel and SUNWiso-codes/-devel because
  gtkhtml requires enchant and iso-codes.
* Thu May 29 2008 - damien.carbery@sun.com
- Add %{_bindir}/gtkhtml-editor-test
* Wed Apr 02 2008 - jeff.cai@sun.com
- Add copyright file.
* Tue Mar 04 2008- damien.carbery@sun.com
- Move libsoup to SUNWlibsoup.spec.
* Wed Feb 13 2008 - damien.carbery@sun.com
- Update %install to delete libsoup html docs.
* Tue Nov 13 2007 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-themes/-devel because gtkhtml requires
  gnome-icon-theme.
* Wed Sep 05 2007 - damien.carbery@sun.com
- Remove references to SUNWgnome-a11y-base-libs as its contents have been
  moved to SUNWgnome-base-libs.
* Tue Aug 22 2006 - damien.carbery@sun.com
- Only change compiler options for non-debug builds.
* Tue Aug 22 2006 - jeff.cai@sun.com
- remove optimization compiler options to fix 6461613.
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu May 11 2006 - halton.huo@sun.com
- Merge -share pkg(s) into the base pkg(s).
- Change %defattr to (-, root, other).
* Tue Apr 04 2006 - halton.huo@sun.com
- Alter remove .a/.la files part into linux spec. 
* Thu Mar 30 2006 - halton.huo@sun.com
- Remove all *.a/*.la files.
* Thu Feb 23 2006 - damien.carbery@sun.com
- Use default pkg version to match other pkgs; add EVO25 to default category.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Sep 09 2005 - <laca@sun.com>
- remove unpackaged files
* Wed Aug 31 2005 - halton.huo@sun.com
- Bump to 2.4.0 for evolution version changed.
* Wed Aug 31 2005 - halton.huo@sun.com
- Change SUNW_Category and Version for open solaris
* Wed Aug 31 2005 - damien.carbery@sun.com
- Remove the obsoleted libgal.
* Tue Jul 12 2005 - damien.carbery@sun.com
- Correct version numbers in dir names in share package.
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Tue Sep 27 2004 - halton.huo@sun.com
- changed the version from "2.6.0" to "1.4.6" for consistent with SUNWevolution
* Tue Aug 31 2004 - shirley.woo@sun.com
- Bug 5091588 : Added BuildRequires SUNWgnutls-devel since SUNWgnutils was
  split
* Thu Aug 26 2004 - dave.lin@sun.com
- changed the spec file name from 'gal.spec' to 'libgal.spec' to keep
  consistent with file name and package name it defines
* Tue Jul 27 2004 - damien.carbery@sun.com
- Add SUNWgnome-component-devel as BuildRequires, for ORBit-2.0.
* Fri Jul 23 2004 - laca@sun.com
- use evolution-libs-copyright.txt as copyright notice
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Tue Apr 20 2004 - <laca@sun.com>
- Add libgnomeprint dependencies
* Thu Mar 11 2004 - <laca@sun.com>
- initial version created



