#
# spec file for package SUNWlibgoffice
#
# includes module(s): goffice
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%include Solaris.inc

%use goffice = goffice.spec

Name:                    SUNWlibgoffice
Summary:                 goffice - Document centric set of APIs
Version:                 %{goffice.version}
SUNW_Pkg:                SUNWlibgoffice
IPS_package_name:        library/desktop/goffice
Meta(info.classification): %{classification_prefix}:Development/System
SUNW_Copyright:          %{name}.copyright
License:                 %{goffice.license}
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Source1:                 %{name}-manpages-0.1.tar.gz

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       library/desktop/libglade
Requires:       library/libxml2
Requires:       library/zlib
Requires:       library/desktop/libgsf
Requires:       system/library/math
Requires:       library/gnome-libs
BuildRequires:  library/desktop/libglade
BuildRequires:  library/libxml2
BuildRequires:  library/gnome/gnome-libs
%if %option_with_gnu_iconv
Requires:       SUNWgnu-libiconv
Requires:       SUNWgnu-gettext
%else
Requires:       system/library/iconv/utf-8
%endif

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}

%package l10n
Summary:                 %{summary} - l10n files

%prep
rm -rf %name-%version
mkdir -p %name-%version
%goffice.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export CFLAGS="%optflags"
%if %option_with_gnu_iconv
export CFLAGS="$CFLAGS -I/usr/gnu/include -L/usr/gnu/lib -R/usr/gnu/lib -lintl"
%endif
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%goffice.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%goffice.install -d %name-%version

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d goffice-%{goffice.version} README AUTHORS
%doc(bzip2) -d goffice-%{goffice.version} COPYING ChangeLog po/ChangeLog tools/ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libgoffice*.so*
%{_libdir}/goffice
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/goffice
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gtk-doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Wed Nov 05 2008 - halton.huo@sun.com
- Add po/ChangeLog to %files
* Wed Sep 10 2008 - halton.huo@sun.com
- Add %doc to %files for new copyright
* Wed Aug 06 2008 - halton.huo@sun.com
- Use sgml format instead for man pages.
* Tue Aug 05 2008 - halton.huo@sun.com
- Add man page for libgoffice
* Tue Jul 01 2008 - halton.huo@sun.com
- Add copyright
* Mon Jun 30 2008 - halton.huo@sun.com
- Copied from SFEgoffice and rename to SUNWlibgoffice
* Tue Jun 24 2008 - nonsea@users.sourceforge.net
- Split base part to base/goffice.spec
- Bump to 0.6.4
* Mon Apr 14 2008 - trisk@acm.jhu.edu
- Bump to 0.6.2, update dependencies
* Tue Sep 04 2007  - Thomas Wagner
- bump to 0.15.1, add %{version} to Download-Dir (might change again)
- conditional !%build_l10n rmdir $RPM_BUILD_ROOT/%{_datadir}/locale
* Sat May 26 2007  - Thomas Wagner
- bump to 0.15.0
- set compiler to gcc
- builds with Avahi, if present
* Thu Apr 06 2007  - Thomas Wagner
- Initial spec



