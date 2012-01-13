#
# spec file for package nautilus-sendto
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner:halton
#

%define owner halton

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:		nautilus-sendto
License:	GPL v2
Group:		Development/Libraries
Version:	2.28.5
Release:	1
Distribution:   Java Desktop System
Vendor:         Gnome Community
URL:		http://www.gnome.org/
Summary:	Nautilus context menu for sending files
Source:		http://download.gnome.org/sources/%{name}/2.28/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

# date:2010-01-17 owner:chrisk type:bug
Patch1:         nautilus-sendto-01-fixxref-modules.diff
# date:2010-04-14 owner:halton type:bug doo:15332 bugzilla:614222
Patch2:         nautilus-sendto-02-mailcmd.diff

BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  evolution-data-server-devel >= 1.9.1
BuildRequires:  libgnomeui-devel
BuildRequires:  nautilus-devel >= 2.5.4
BuildRequires:  pidgin-devel >= 2.0.0
BuildRequires:  gettext
BuildRequires:  perl-XML-Parser intltool
BuildRequires:  dbus-glib-devel >= 0.70

%description
The nautilus-sendto package provides a Nautilus context menu for
sending files via other desktop applications.  These functions are
implemented as plugins, so nautilus-sendto can be extended with
additional features.  This package provides a default plugin for
Evolution integration.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

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
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f
autoconf

./configure --prefix=%{_prefix} \
	    --bindir=%{_bindir} \
	    --mandir=%{_mandir} \
	    --libdir=%{_libdir} \
	    --datadir=%{_datadir} \
	    --includedir=%{_includedir} \
	    --sysconfdir=%{_sysconfdir} \
	    %gtk_doc_option \
%if %debug_build
	    --enable-debug=yes \
%else
	    --enable-debug=no \
%endif

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
%doc AUTHORS ChangeLog COPYING NEWS
%{_libdir}/nautilus/extensions-2.0/libnautilus-sendto.so
%{_libdir}/nautilus-sendto
%{_datadir}/nautilus-sendto
%{_bindir}/nautilus-sendto
%{_sysconfdir}/gconf/schemas/nst.schemas
%{_mandir}/man1/nautilus-sendto.1.gz

%changelog
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 2.28.5.
* Wed Apr 14 2010 - halton.huo@sun.com
- Add to 02-mailcmd.diff fix doo #15332 
- Add to 03-unload-pidgin.diff fix doo #15112
* Tue Mar 30 2009 - halton.huo@sun.com
- Bump to 2.28.4
* Tue Mar 16 2009 - halton.huo@sun.com
- Bump to 2.28.3
* Sun Jan 17 2010 - christian.kelly@sun.com
- Add nautilus-sendto-01-fixxref-modules.
* Wed Nov 18 2009 - halton.huo@sun.com
- Bump to 2.28.2
- Remove upstramed patch gthread.diff
* Thu Nov 12 2009 - halton.huo@sun.com
- Initial spec.
