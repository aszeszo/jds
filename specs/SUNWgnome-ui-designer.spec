#
# spec file for package SUNWgnome-ui-designer
#
# includes module(s): glade
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner hawklu
#
%include Solaris.inc

%use glade = glade.spec

Name:                    SUNWgnome-ui-designer
IPS_package_name:        developer/ui-designer/glade
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:                 GNOME UI designer
Version:                 %{glade.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:%{name}.copyright
License:                 GNU GENERAL PUBLIC LICENSE v3
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlibgnomecanvas
Requires: SUNWgnome-libs
Requires: SUNWgnome-component
Requires: SUNWlibms
Requires: SUNWlibpopt
Requires: SUNWlxml
Requires: SUNWdesktop-cache
BuildRequires: SUNWlibgnomecanvas-devel
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWlibpopt-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWgnome-xml-share
BuildRequires: SUNWgnome-doc-utils

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%glade.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="%optflags -I%{_includedir}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%glade.build -d %name-%version

%install
%glade.install -d %name-%version
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):unsupported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*.so*
%{_libdir}/glade*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/glade*
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/glade/C
%{_datadir}/omf/glade/glade-C.omf
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/glade/[a-z][a-z]*
%{_datadir}/omf/glade/glade-[a-z][a-z]*.omf

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%changelog
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add 'License' tag
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Tue Jan 29 2008 - patrick.ale@gmail.com
- Remove without_gtk_doc validation. gtk-doc
  should always be packaged.
* Fri Oct  5 2007 - laca@sun.com
- delete unneeded env vars
* Thu May 03 2007 - damien.carbery@sun.com
- Add %if code so that %{_datadir}/gtk-doc is only packaged when requested.
* Thu Mar 22 2007 - halton.huo@sun.com
- Move %{_datadir}/gtk-doc to -devel package.
* Tue Mar 13 2007 - damien.carbery@sun.com
- Add %{_datadir}/gtk-doc to %files for new tarball.
* Wed Feb 28 2007 - halton.huo@sun.com
- Add package -devel and change files section since upgrade to glade3.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Mon Dec 13 2004 - damien.carbery@sun.com
- Move to /usr/bin to implement ARC decision.
* Fri Nov 12 2004 - laca@sun.com
- move to /usr/demo/jds
* Wed Oct 06 2004 - matt.keenan@sun.com
- Add localized help files to l10n section
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Wed Aug 18 2004 - damien.carbery@sun.com
- Change manpage perms for Solaris integration.
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Fri Mar 26 2004 - brian.cameron@sun.com
- Created,



