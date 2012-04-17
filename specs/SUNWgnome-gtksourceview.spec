#
# spec file for package SUNWgnome-gtksourceview
#
# includes module(s): gtksourceview
#
# Copyright (c) 2003, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner hawklu
#
%include Solaris.inc
%use gsv2 = gtksourceview2.spec

Name:                    SUNWgnome-gtksourceview
IPS_package_name:        library/desktop/gtksourceview
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GNOME syntax highlighting text widget
Version:                 %{gsv2.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GNU Lesser General Public License, version 2.1
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: library/desktop/gtk2
Requires: runtime/python-26
BuildRequires: library/desktop/gtk2
BuildRequires: developer/documentation-tool/gtk-doc

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir %name-%version
%gsv2.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%gsv2.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gsv2.install -d %name-%version

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man3/*.3

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtksourceview-2.0

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Aug 16 2011 - ghee.teo@oracle.com
- Removed gtksourceview-1 for good. Part of LP removal.
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add 'License' tag
* Mon Mar 23 2009 - jeff.cai@sun.com
- Since /usr/share/gtksourceview-2.0/language-specs/convert.py
  (SUNWgnome-gtksourceview) requires /usr/bin/i86/isapython2.4 which is
  found in SUNWPython, add the dependency.
* Thu Apr 03 2008 - elaine.xiong@sun.com
- Add file SUNWgnome-gtksourceview.copyright.
* Wed May 30 2007 - damien.carbery@sun.com
- Add gtksourceview2.spec to support version 2.x of gtksourceview which is not
  ABI/API compatible with version 1.x.
* Wed May 30 2007 - damien.carbery@sun.com
- Revert dir name in %files, s/2.0/1.0/ as gtksourceview has been reverted from
  1.90.0 to 1.8.5 so that gedit and gnome-python-desktop can build.
* Mon May 28 2007 - damien.carbery@sun.com
- Update dir name in %files, s/1.0/2.0/.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Thu Jun 29 2006 - laca@sun.com
- move gtksourceview into its own pkg due to dependency issues.



