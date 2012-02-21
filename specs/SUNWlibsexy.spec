#
# spec file for package SUNWlibsexy
#
# includes module(s): libsexy
#
# Copyright (c) 2006, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%define owner erwannc

%define OSR 10058:0.11.1

%include Solaris.inc

Name:         SUNWlibsexy
IPS_package_name: library/desktop/libsexy
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
License:      LGPL
Version:      0.1.11
Summary:      libsexy is a collection of GTK+ widgets that extend the functionality of such standard widget.
Source:       http://releases.chipx86.com/libsexy/libsexy/libsexy-%{version}.tar.gz
URL:          http://www.chipx86.com/wiki/Libsexy
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:	      %{_defaultdocdir}/doc
SUNW_BaseDir: %{_basedir}
SUNW_Copyright: %{name}.copyright

# date:2009-07-16 type:bug owner:chrisk
Patch1:       libsexy-01-gtk-includes.diff

Autoreqprov:  on
BuildRequires: library/desktop/gtk2
BuildRequires: library/libxml2
BuildRequires: data/iso-codes
Requires: library/desktop/gtk2
Requires: library/libxml2
Requires: data/iso-codes

%include desktop-incorporation.inc

%package devel
Summary:       %{summary} - development files
SUNW_BaseDir:  %{_basedir}

%prep
%setup -q -n libsexy-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export LDFLAGS="%{_ldflags}"

libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f 
autoconf
./configure --prefix=%{_prefix} \
		--libdir=%{_libdir} \
        --disable-gtk-doc
make -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/lib*.a
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%doc README AUTHORS
%doc(bzip2) COPYING NEWS ChangeLog
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%{_libdir}/*.so*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_includedir}
%dir %attr (0755, root, bin) %dir %{_includedir}/libsexy
%{_includedir}/libsexy/*
%dir %attr (0755, root, sys) %dir %{_datadir}
%dir %attr (0755, root, bin) %dir %{_datadir}/gtk-doc
%{_datadir}/gtk-doc/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Tue Apr 20 2010 - christian.kelly@oracle.com
- Set LDFLAGS, otherwise stuff in /usr/lib ends up as 64bit versions.
* Sat Jul 18 2009 - christian.kelly@sun.com
- Add missing patch line.
* Thu Jul 16 2009 - christian.kelly@sun.com
- Add patch to work around problem trying to include gtk headers.
* Thu Sep 18 2008 - christian.kelly@sun.com
- Fix up pkg'ing section.
* Wed Jun 18 2008 - jedy.wang@sun.com
- enalbe this component on SPARC
* Wed Mar 26 2008 - dave.lin@sun.com
- change to not build this component on SPARC
* Wed Feb 13 2008 - erwann@sun.com
- moved to SFO
* Fri Aug 24 2007 Erwann Chenede <erwann@sun.com>
- bumped to 0.1.11 and removed patch
* Fri Feb 16 2007 - Doug Scott <dougs@truemail.co.th>
- Fixed perm for gtk-doc directory
* Wed Nov 22 2006 - jedy.wang@sun.com
- Initial spec
