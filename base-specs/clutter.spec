#
# spec file for package clutter
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
# bugdb: bugzilla.o-hand.com
#

%define OSR 12694 (new OSR for major rev not needed):1.0

Name:         clutter
License:      LGPLv2.1
Group:        System/Libraries
Version:      1.10.4
Release:      1
Distribution: Java Desktop System
Vendor:       clutter-project.org
Summary:      clutter - a library for creating fast, visually rich and animated graphical user interfaces.
Source:	      http://www.clutter-project.org/sources/%{name}/1.10/%{name}-%{version}.tar.xz
# date:2010-10-22 owner:yippi
Patch1:       clutter-01-json.diff
# Patch needed to make 1.2.8 build without libtool 2.2.6.
# date:2010-05-28 owner:yippi type:feature
Patch2:       clutter-02-m4.diff
Patch3:       clutter-03-configure.diff
Patch4:       clutter-04-void-return.diff
URL:          http://www.clutter-project.org/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
%description
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

%prep
%setup -q -n clutter-%version
#%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

# This is needed for the gobject-introspection compile to find libdrm.
export LD_LIBRARY_PATH=/usr/lib/xorg

gtkdocize
sed -e 's#) --mode=compile#) --tag=CC --mode=compile#' gtk-doc.make > gtk-doc.temp \
        && mv gtk-doc.temp gtk-doc.make
sed -e 's#) --mode=link#) --tag=CC --mode=link#' gtk-doc.make > gtk-doc.temp \
        && mv gtk-doc.temp gtk-doc.make
glib-gettextize -f
intltoolize --force --copy
export ACLOCAL="aclocal-1.11 $ACLOCAL_FLAGS"
export AUTOMAKE="automake-1.11"
autoreconf -v --install
./configure --prefix=%{_prefix}              \
            --libdir=%{_libdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --disable-static                 \
            --enable-gtk-doc			
make -j$CPUS 

%install
make -i install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*


%changelog
* Thu May 03 2012 - brian.cameron@oracle.com
- Bump to 1.10.4.
* Wed Oct 19 2011 - brian.cameron@oracle.com
- Bump to 1.8.2.
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 1.8.0.
* Wed Jul 06 2011 - brian.cameron@oracle.com
- Bump to 1.6.16.
* Fri Oct 22 2010 - brian.cameron@oracle.com
- Bump to 1.2.14.
* Tue Jun 01 2010 - brian.cameron@oracle.com
- Bump to 1.2.8, add patch clutter-02-m4.diff to fix compile issues and
  remove clutter-02-annotations.diff.
* Fri May 28 2010 - brian.cameron@oracle.com
- Add patch clutter-02-annotations.diff so clutter builds with 
  gobject-introspection > 0.6.10.
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Bump to 1.2.6.
* Fri Mar 26 2010 - christian.kelly@sun.com
- Bump to 1.2.4.
* Tue Mar 16 2009 - halton.huo@sun.com
- Bump to 1.2.2
* Wed Mar 03 2010 - halton.huo@sun.com
- Bump to 1.2.0
* Wed Feb 10 2010 - halton.huo@sun.com
- Bump to 1.1.10
- Remove upstreamed patch void-return.diff
* Tue Feb 09 2010 - halton.huo@sun.com
- Bump to 1.1.8
- Remove upstreamed patch suncc-redefine.diff
* Mon Jan 04 2010 - halton.huo@sun.com
- Bump to 1.1.4
- Add patch solaris-ld.diff to fix #1930
* Wed Dec 30 2009 - halton.huo@sun.com
- Bump to 1.1.2
- Add patch suncc-redefine.diff to fix #1928
- Add patch void-return.diff to fix #1929
* Wed Oct 21 2009 - dave.lin@sun.com
- Bump to 1.0.8
* Thu Sep 24 2009 - brian.cameron@sun.com
- Bump to 1.0.6.
* Sat Sep 05 2009 - brian.cameron@sun.com
- Bump to 1.0.4.
* Tue Aug 25 2009 - halton.huo@sun.com
- Bump to 1.0.2.
- Remove uesless patch remove-tests.diff.
- Remove upstreamed patch g11n-i18n-ui.diff.
- Add patch gi.diff to fix build issue on G-I 0.6.4
* Fri Jun 26 2009 - chris.wang@sun.com
- Change spec and patch owner to lin.
* Tue Apr 14 2009 - chris.wang@sun.com
- backup to 0.8.8 as 0.9 version is not competible with clutter-gtk.
* Tue Apr 07 2009 - chris.wang@sun.com
- Bump to 0.9.2, revised patch 01 and removed upstreamed patch 02.
* Mon Feb 23 2009 - chris.wang@sun.com
- Bump to 0.8.8 version.
* Tue Jan 06 2009 - takao.fujiwara@sun.com
- Add patch g11n-i18n-ui.diff for I18n UI.
* Wed Nov 26 2008  chris.wang@sun.com
- add patch cairo-01-remove-tests.diff, we don't ship tests to our package.
* Tue Jul 1  2008  chris.wang@sun.com 
- Initial build.

