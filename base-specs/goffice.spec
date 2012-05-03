#
# spec file for package goffice
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%define OSR gnome.org:0

Name:           goffice
Summary:        Set of document centric objects and utilities for glib/gtk
License:        GPL v2
Group:          System/Libraries
Version:        0.8.17
Vendor:         Gnome Community
Release:        1
Distribution:   Java Desktop System
Vendor:         Sun Microsystems, Inc.
URL:            http://www.gnome.org/
Source:         http://download.gnome.org/sources/%{name}/0.8/%{name}-%{version}.tar.bz2
%if %build_l10n
Source1:        l10n-configure.sh
%endif
BuildRoot:      %{tmpdir}/%{name}-%{version}-root

Patch1:         libgoffice-01-fixxref-modules.diff

BuildRequires:  automake1.8
BuildRequires:  intltool
BuildRequires: gtk+2-devel
BuildRequires: libgnomeprint-devel >= 2.8.2
BuildRequires: libgsf-devel >= 1:1.13.3
BuildRequires: libglade2.0-devel
BuildRequires: gtk-doc
BuildRequires: perl-XML-Parser


%description
GOffice -- A glib/gtk set of document centric objects and utilities

%prep
%setup -q
%patch1 -p1

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

libtoolize --force
intltoolize --force --automake

%if %build_l10n
sh %SOURCE1 --enable-copyright
%endif

aclocal $ACLOCAL_FLAGS
autoheader
automake -a -f -c --gnu
autoconf

CFLAGS="$RPM_OPT_FLAGS -I/usr/include/pcre"
./configure  --prefix=%{_prefix}                \
             --libdir=%{_libdir}                \
             --libexecdir=%{_libexecdir}        \
             --datadir=%{_datadir}              \
             --mandir=%{_mandir}                \
             --sysconfdir=%{_sysconfdir}        \
             --without-long-double              \
             %gtk_doc_option

make -j $CPUS


%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make -i install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS BUGS ChangeLog MAINTAINERS
%{_libdir}/lib*.so*
%dir %{_libdir}/%name/
%{_datadir}/%name
%{_datadir}/pixmaps/%name
%{_includedir}/libgoffice-0.3/
%attr(644,root,root) %{_libdir}/lib*a
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/goffice/


%changelog
* Wed May 02 2012 - brian.cameron@oracle.com
- Add -I/usr/include/pcre to CFLAGS.
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 0.8.17.
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Bump to 0.8.11.
* Thu Aug 26 2010 - brian.cameron@oracle.com
- Bump to 0.8.9.
* Mon Jul  5 2010 - christian.kelly@oracle.com
- Bump to 0.8.7.
* Mon May 31 2010 - halton.huo@sun.com
- Bump to 0.8.5
* Fri May 21 2010 - halton.huo@sun.com
- Bump to 0.8.4
* Sun May 09 2010 - halton.huo@sun.com
- Bump to 0.8.3
* Mon Apr 19 2010 - halton.huo@sun.com
- Bump to 0.8.2
* Sun Mar 14 2010 - christian.kelly@sun.com
- Add libgoffice-01-fixxref-modules.diff to fix build issue.
* Tue Mar 09 2010 - halton.huo@sun.com
- Bump to 0.8.1
* Mon Feb 22 2010 - halton.huo@sun.com
- Bump to 0.8.0
* Tue Jan 26 2010 - halton.huo@sun.com
- Bump to 0.7.18
- Remove upstreamed patch 01-unamed-union.diff
* Wed Dec 16 2009 - halton.huo@sun.com
- Bump to 0.7.17
* Mon Nov 30 2009 - halton.huo@sun.com
- Bump to 0.7.16
* Wed Nov 02 2009 - halton.huo@sun.com
- Bump to 0.7.15
* Wed Oct 14 2009 - dave.lin@sun.com
- Bump to 0.7.14
* Tue Seo 21 2009 - dave.lin@sun.com
- Bump to 0.7.13
* Sun Sep 06 2009 - dave.lin@sun.com
- Bump to 0.7.12
* Tue Sep 01 2009 - dave.lin@sun.com
- Bump to 0.7.11
* Mon Aug 31 2009 - halton.huo@sun.com
- Bump to 0.7.10
- Add patch -unamed-union.diff to fix bugzilla #593608
* Mon Aug 17 2009 - halton.huo@sun.com
- Bump to 0.7.9
* Mon Jun 22 2009 - halton.huo@sun.com
- Bump to 0.7.8
* Mon May 25 2009 - halton.huo@sun.com
- Bump to 0.7.7
* Thu Mar 07 2009 - halton.huo@sun.com
- Bump to 0.7.6
* Wed Apr 29 2009 - halton.huo@sun.com
- Bump to 0.7.5
* Mon Mar 23 2009 - halton.huo@sun.com
- Bump to 0.7.4
* Thu Feb 26 2009 - dave.lin@sun.com
- Bump to 0.7.3
* Mon Dec 29 2008 - halton.huo@sun.com
- Add --without-long-double to fix CR #6761452
* Mon Oct 20 2008 - halton.huo@sun.com
- Bump to 0.7.2
* Mon Sep 01 2008 - halton.huo@sun.com
- Bump to 0.7.1
- Remove upstreamed patch no-sunmath-lib.diff
* Wed Jun 25 2008 - nonsea@users.sourceforge.net
- Bump to 0.7.0
* Tue Jun 24 2008 - nonsea@users.sourceforge.net
- Initial version
