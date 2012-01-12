#
# spec file for package atk
#
# Copyright (c) 2003, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         atk
License:      LGPL v2
Group:        System/Libraries
Version:      2.2.0
Release:      1
Distribution: Java Desktop System
Vendor:	      Gnome Community
Summary:      ATK - Accesibility Toolkit Libraries
Source:       http://ftp.gnome.org/pub/GNOME/sources/atk/2.2/%{name}-%{version}.tar.bz2
Patch1:       atk-01-libtool.diff
URL:          http://www.gtk.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:	      %{_defaultdocdir}/doc
AutoReqProv:  on
Prereq:	      /sbin/ldconfig

%define glib2_version 2.5.7

Requires:      glib2 >= %{glib2_version}
BuildRequires: glib2-devel >= %{glib2_version}

%description
The ATK Library provides a set of interfaces for accesibility. By supporting the ATK interfaces, an application or toolkit can be used with such tools as screen readers, magnifiers, and alternate input devices.

%package devel
Summary:      ATK - Accessibility Toolkit Developer Libraries
Group:        Development/Libraries/GNOME
Requires:     %{name} = %{version}
Requires:     glib2-devel >= %{glib2_version}

%description devel
The ATK Library provides a set of interfaces for accesibility. By supporting the ATK interfaces, an application or toolkit can be used with such tools as screen readers, magnifiers, and alternate input devices.

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

export PATH=/usr/sfw/bin:/usr/gnu/bin:$PATH
libtoolize -f
aclocal $ACLOCAL_FLAGS
gtkdocize
autoheader
automake -a -c -f
autoconf

export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
./configure \
            --prefix=%{_prefix}         \
            --sysconfdir=%{_sysconfdir}	\
            --libdir=%{_libdir}         \
            --bindir=%{_bindir}         \
	    %{gtk_doc_option}
make -j $CPUS

%install
export PATH=/usr/sfw/bin:/usr/gnu/bin:$PATH
make DESTDIR=$RPM_BUILD_ROOT install

find $RPM_BUILD_ROOT%{_libdir} -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT%{_libdir} -name "*.a" -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_libdir}/libatk*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/atk-1.0/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libatk*.so
%{_datadir}/gtk-doc/html/atk
%{_mandir}/man3/*

%changelog
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 2.2.0.
* Tue Sep 13 2011 - brian.cameron@oracle.com
- Bump to 2.1.91.
* Thu Aug 18 2011 - brian.cameron@oracle.com
- Bump to 2.1.5.
* Mon Aug 15 2011 - lee.yuan@oracle.com
- Bump to 2.1.0.
* Wed Jul 06 2011 - brian.cameron@oracle.com
- Bump to 2.0.1.
* Tue Mar 30 2010 - christian.kelly@sun.com
- Bump to 1.30.0.
* Thu Mar 11 2010 - christian.kelly@sun.com
- Bump to 1.29.92.
* Tue Mar 09 2010 - li.yuan@sun.com
- Bump to 1.29.92.
* Mon Mar  8 2010 - christian.kelly@sun.com
- Make sure we use gnu make.
* Fri Mar  5 2010 - christian.kelly@sun.com
- Bump to 1.29.4.
* Mon Nov 30 2009 - li.yuan@sun.com
- Bump to 1.29.3
* Fri Nov 13 2009 - li.yuan@sun.com
- Correct download url.
* Fri Nov 13 2009 - li.yuan@sun.com
- Bump to 1.29.2
* Wed Sep 23 2009 - dave.lin@sun.com
- Bump to 1.28.0
* Thu Aug 27 2009 - li.yuan@sun.com
- Run aclocal and related commands before configure.
* Tue Aug 11 2009 - li.yuan@sun.com
- Bump to 1.27.90.
* Tue Mar 17 2009 - dave.lin@sun.com
- Bump to 1.26.0
* Wed Dec 03 2008 - dave.lin@sun.com
- Bump to 1.25.2
* Wed Nov 05 2008 - li.yuan@sun.com
- Change copyright information.
* Mon Oct 27 2008 - li.yuan@sun.com
- Correct the url of tarball.
* Mon Sep 29 2008 - christian.kelly@sun.com
- Bump to 1.24.0.
* Mon Jul 21 2008 - damien.carbery@sun.com
- Bump to 1.23.5.
* Mon Mar 10 2008 - damien.carbery@sun.com
- Bump to 1.22.0.
* Mon Feb 25 2008 - damien.carbery@sun.com
- Bump to 1.21.92.
* Mon Jan 14 2008 - damien.carbery@sun.com
- Bump to 1.21.5.
* Thu Jan 10 2008 - li.yuan@sun.com
- change owner to liyuan.
* Tue Sep 18 2007 - damien.carbery@sun.com
- Bump to 1.20.0.
* Mon Jul 30 2007 - damien.carbery@sun.com
- Bump to 1.19.6.
* Wed Jun 06 2007 - damien.carbery@sun.com
- Bump to 1.19.3. Remove upstream patch, 01-mkenums.
* Thu May 10 2007 - damien.carbery@sun.com
- Bump to 1.19.1.
* Tue May 01 2007 - brian.cameron@sun.com
- Add patch to use $(GLIB_MKENUMS) rather than glib-mkenums.
* Thu Mar 15 2007 - laca@sun.com
- convert to new style of building multiple ISAs as per docs/multi-ISA.txt
* Wed Mar 15 2007 - dougs@truemail.co.th
- Removed adding ccdir to PATH
* Mon Mar 12 2007 - damien.carbery@sun.com
- Bump to 1.18.0.
* Tue Feb 13 2007 - damien.carbery@sun.com
- Bump to 1.17.0.
* Mon Jan 22 2007 - damien.carbery@sun.com
- Bump to 1.13.2.
* Tue Jan 09 2007 - damien.carbery@sun.com
- Bump to 1.13.1.
* Mon Jan 08 2007 - damien.carbery@sun.com
- Bump to 1.13.0.
* Tue Dec 19 2006 - damien.carbery@sun.com
- Bump to 1.12.4.
* Fri Nov  3 2006 - laca@sun.com
- use %gtk_doc_option in configure so that it can be disabled using
  --without-gtk-doc
* Mon Oct 02 2006 - damien.carbery@sun.com
- Bump to 1.12.3.
* Tue Aug 22 2006 - damien.carbery@sun.com
- Bump to 1.12.2.
* Wed Jul 19 2006 - dermot.mccluskey@sun.com
- Bump to 1.12.1.
* Fri Mar 31 2006 - damien.carbery@sun.com
- Bump to 1.11.4.
* Mon Mar 13 2006 - damien.carbery@sun.com
- Bump to 1.11.3.
* Tue Jan 17 2006 - glynn.foster@sun.com
- Bump to 1.11.0
* Thu Sep 08 2005 - damien.carbery@sun.com
- Bump to 1.10.3.
* Mon Sep 05 2005 - damien.carbery@sun.com
- Bump to 1.10.2.
* Mon Aug 15 2005 - glynn.foster@sun.com
- Bump to 1.10.1
* Fri May 06 2005 - glynn.foster@sun.com
- Bump to 1.9.1
* Fri Oct 29 2004 - laca@sun.com
- use $CC64 for the 64-bit build if defined
* Sat Oct  2 2004 - Joseph.Townsend@Sun.COM
- Create 64bit libraries for Solaris
* Wed Aug 18 2004 - brian.cameron@sun.com
- added --enable-gtk-doc.
* Wed Jul 28 2004 - <padraig.obriain@sun.com>
- Bump to 1.7.3
* Mon Jul 26 2004 - <padraig.obriain@sun.com>
- Bump to 1.7.2
* Thu Jul 08 2004 - damien.donlon@sun.com
- Updated l10n content to atk-l10n-po-1.2.tar.bz2
* Wed Jul 07 2004 - niall.power@sun.com
- ported to rpm4
* Wed Jul 07 2004 - dermot.mccluskey@sun.com
- added "-j $CPUS" to make to speed up builds
* Tue Jun 08 2004 - <padraig.obriain@sun.com>
- Bump to 1.7.1
* Wed May 12 2004 - damien.donlon@sun.com
- Updated l10n content to atk-l10n-po-1.1.tar.bz2
* Thu Apr 22 2004 - <padraig.obriain@sun.com>
- Bump to 1.7.0
* Mon Mar 29 2004 - damien.donlon@sun.com
- Updated l10n content to atk-l10n-po-1.0.tar.bz2
* Mon Mar 15 2004 - <damien.carbery@sun.com>
- Change '1.5' in URL to '1.6'.
* Thu Mar 11 2004 - <damien.carbery@sun.com>
- Reset release to 1.
* Wed Mar 10 2004 - <damien.carbery@sun.com>
- Bump to 1.6.0
* Wed Feb 18 2004 - <matt.keenan@sun.com>
- Bump to 1.5.4, remove pc patch
* Fri Jan 09 2004 - <laca@sun.com>
- add patch to fix a broken .pc file
- clean up for Solaris builds
* Mon Dec 15 2003 - <glynn.foster@sun.com>
- upgrade to 1.5.1 tarball
* Mon Oct 6 2003 - <laszlo.kovacs@sun.com>
- upgrade to 1.4 tarball
* Thu Aug 14 2003 - <laca@sun.com>
- move lib*.so to -devel, remove *.a, *.la
* Tue May 13 2003 - Stephen.Browne@sun.com
- initial Sun release
