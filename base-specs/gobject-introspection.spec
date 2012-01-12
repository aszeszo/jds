#
# spec file for package gobject-introspection
#
# Copyright (c) 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi

%define OSR LFI#105446 (gnome Exec. summary):n/a

#
%{?!pythonver:%define pythonver 2.6}

Name:         gobject-introspection
License:      LGPL v2+ (giscanner), GPL v2+ (tools), MIT, BSD
Group:        Libraries
Version:      1.30.0
Release:      1
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      Introspection for GObject libraries
URL:          http://live.gnome.org/GObjectIntrospection
Source:       http://download.gnome.org/sources/%{name}/1.30/%{name}-%{version}.tar.bz2
# We only deliver one set of the Python files, so it is necessary to modify
# /usr/bin/amd64/g-ir-scanner to point to the right python files.
# date:2010-04-09 owner:yippi type:feature
Patch1:       gobject-introspection-01-amd64.diff
# date:2010-04-09 owner:yippi type:bug
Patch2:       gobject-introspection-02-fixcompile.diff

BuildRequires:  autoconf >= 2.59
BuildRequires:  automake >= 1:1.8
BuildRequires:  bison
BuildRequires:  glib2-devel >= 1:2.16.0
BuildRequires:  libffi-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python >= 1:2.5
BuildRequires:  python-devel >= 1:2.5

%description
Tools for introspecting GObject-based frameworks.

%package devel
Summary:        Header files for gobject-introspection
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       glib2-devel >= 2.16.0

%description devel
Header files for gobject-introspection.

%package static
Summary:        Static gobject-introspection library
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static gobject-introspection library.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export PYTHON=%{_bindir}/python%{pythonver}

#substitute python to 2.6, CR6924142
pyfiles="
giscanner/shlibs.py
giscanner/scannermain.py
"

for i in $pyfiles
do
  sed -e s,/usr/bin/env\ python,$PYTHON, $i > $i.new
  mv $i.new $i
done

aclocal-1.11 $ACLOCAL_FLAGS -I m4
autoheader
automake-1.11 -a -c -f
autoconf

./configure --prefix=%{_prefix}         \
            --bindir=%{_bindir}         \
            --libdir=%{_libdir}         \
            --includedir=%{_includedir} \
            --sysconfdir=%{_sysconfdir} \
            --mandir=%{_mandir} \
            --disable-tests

# disable parallel builds as it's broken for 0.6.10
#gmake -j $CPU
gmake

%install
gmake install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

find $RPM_BUILD_ROOT -type f -name "*.pyc" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.pyo" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libgirepository-everything-1.0.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libgirepository-everything-1.0.so.1
%attr(755,root,root) %{_libdir}/libgirepository-1.0.so.0.0.0
%attr(755,root,root) %ghost %{_libdir}/libgirepository-1.0.so.0
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/g-ir-compiler
%attr(755,root,root) %{_bindir}/g-ir-generate
%attr(755,root,root) %{_bindir}/g-ir-scanner
%{_mandir}/man1/g-ir-compiler.1*
%{_mandir}/man1/g-ir-generate.1*
%{_mandir}/man1/g-ir-scanner.1*
%attr(755,root,root) %{_libdir}/libgirepository-everything-1.0.so
%attr(755,root,root) %{_libdir}/libgirepository-1.0.so
%{_libdir}/pkgconfig/gobject-introspection-1.0.pc
%{_includedir}/gobject-introspection-1.0
%{_libdir}/libgirepository-1.0.la
%{_libdir}/libgirepository-everything-1.0.la
%{_datadir}/aclocal/introspection.m4
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir

%files static
%defattr(-,root,root)
%{_libdir}/libgirepository-1.0.a
%{_libdir}/libgirepository-everything-1.0.a

%changelog
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 1.30.0.
* Tue Jul 05 2011 - brian.cameron@oracle.com
- Bump to 0.10.8.
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Bump to 0.9.12.
* Mon Oct 04 2010 - brian.cameron@oracle.com
- Bump to 0.9.9.
* Mon Sep 20 2010 - christian.kelly@oracle.com
- Bump to 0.9.6.
* Sat Aug 07 2010 - brian.cameron@oracle.com
- Bump to 0.9.3.
* Thu Jul 15 2010 - christian.kelly@oracle.com
- Bump to 0.9.2.
* Mon Jul  5 2010 - christian.kelly@oracle.com
- Bump to 0.9.0.
* Mon Jun 21 2010 - brian.cameron@oracle.com
- Bump to 0.6.14.
* Fri May 28 2010 - brian.cameron@oracle.com
- Bump to 0.6.12.  I found a clutter patch to fix the build problem so it
  builds okay with the latest gobject-introspection.
* Fri May 28 2010 - brian.cameron@oracle.com
- Unbump to 0.6.10.  Turns out that the new version causes clutter to not
  compile.  I noticed 0.6.12 came out and tried that version, but it also fails
  to build clutter.
* Fri May 21 2010 - brian.cameron@oracle.com
- Bump to 0.6.11.
* Mon Apr 19 2010 - halton.huo@sun.com
- Bump to 0.6.10.
* Fri Apr 09 2010 - brian.cameron@sun.com
- Add patch gobject-introspection-01-amd64.diff.
* Fri Mar 19 2010 - halton.huo@sun.com
- Bump to 0.6.9.
* Thu Mar 11 2010 - halton.huo@sun.com
- Bump to 0.6.8.
- Remove upstreamed patches: 01-ginvoke.diff, 02-glib-compilation.dif
  03-ginfo.diff, 04-big-ending.diff.
* Mon Feb 08 2010 - halton.huo@sun.com
- Use python2.6 to scannermain.py and shlibs.py, fixes CR #6924142.
- Remove .pyc and .pyo files.
* Tue Jan 26 2010 - brian.cameron@sun.com
- Use gmake instead of make, fixes doo bug #14155.
* Fri Jan 08 2010 - halton.huo@sun.com
- Add patch ginfo.diff and big-ending.diff to fix bugzilla #606180.
* Wed Dec 23 2009 - halton.huo@sun.com
- Bump to 0.6.7.
- Add patch -glib-compilation.dif to fix bugzilla #605108.
* Fri Dec 11 2009 - halton.huo@sun.com
- Bump to 0.6.6. Remove upstream patch 64bit.diff.
* Sat Sep 05 2009 - brian.cameron@sun.com
- Bump to 0.6.5.  Remove upstream patches.
* Mon Aug 31 2009 - halton.huo@sun.com
- Add patch -64bit to fix 64 bit issue. Bugzilla #593639.
* Sat Aug 29 2009 - halton.huo@sun.com
- Add patch -LD.diff to fix build issue with CBE 1.6.x.
* Mon Aug 24 2009 - halton.huo@sun.com
- Initial version.

