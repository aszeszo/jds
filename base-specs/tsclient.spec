#
# spec file for package tsclient
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
# bugdb: http://sourceforge.net/tracker/index.php?func=detail&group_id=192483&atid=941574&aid=
#

%define OSR 9334:0.x


Name:           tsclient
Summary:        a frontend for rdesktop and other remote desktop tools for the GNOME2 platform.
License:        GPL v2
Group:          User Interface/Desktops
Version:        0.150
Release:        1
Distribution:   Java Desktop System
Vendor:         sourceforge.net/projects/tsclient
URL:            http://sourceforge.net/projects/tsclient
Source:         %{sf_download}/%{name}/%{name}-%{version}.tar.gz
%if %build_l10n
Source1:        l10n-configure.sh
%endif
# date:2008-06-19 owner:jefftsai type:bug bugid:1997801
Patch1:         %{name}-01-libsocket.diff
# date:2008-07-01 owner:jefftsai type:bug bugid:2007323
Patch2:         %{name}-02-xnest-xephyr.diff
# date:2008-07-08 owner:jefftsai type:bug bugid:2013149
Patch3:         %{name}-03-s11-O0.diff
# date:2008-07-10 owner:jefftsai type:feature bugid:2014845 
Patch4:         %{name}-04-uttsc.diff
# date:2008-07-10 owner:jefftsai type:bug bugid:2014822
Patch5:         %{name}-05-print-null.diff
# date:2008-07-24 owner:jefftsai type:bug bugid:2026506
Patch6:         %{name}-06-desktop.diff
# date:2008-08-05 owner:jefftsai type:bug bugster:6733133 state:upstream
Patch7:         %{name}-07-save-rdp.diff
# date:2009-02-10 owner:davelam type:bug bugster:n/a
Patch8:         %{name}-08-libgnomeui.diff
BuildRoot:      %{tmpdir}/%{name}-%{version}-root

Requires:	glib2 >= 2.0.0, gtk2 >= 2.0.0, rdesktop >= 1.3.0, vnc >= 4.0
BuildRequires:	glib2-devel >= 2.0.0, gtk2-devel >= 2.0.0


%description
Terminal Server Client is a frontend for rdesktop, vnc and other remote desktop tools.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1


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
intltoolize --force --automake --copy

%if %build_l10n
sh %SOURCE1 --enable-copyright
%endif

aclocal $ACLOCAL_FLAGS
autoheader
automake -a -f -c --gnu
autoconf

CFLAGS="$RPM_OPT_FLAGS"
./configure  --prefix=%{_prefix}         \
             --libdir=%{_libdir}         \
             --libexecdir=%{_libexecdir} \
             --datadir=%{_datadir}       \
             --mandir=%{_mandir}         \
             --sysconfdir=%{_sysconfdir} \
%if %debug_build
             --enable-debug=yes
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
%doc README ChangeLog AUTHORS NEWS
%{_prefix}/bin/tsclient
%{_prefix}/libexec/tsclient-applet
%{_libdir}/bonobo/servers/GNOME_TSClientApplet.server
%{_datadir}/applications/tsclient.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/tsclient
%{_datadir}/locale/*/LC_MESSAGES/tsclient.mo
%{_datadir}/application-registry/tsclient.*
%{_datadir}/mime-info/tsclient.*
%{_datadir}/man/man1/tsclient.1*


%changelog
* Tue Feb 10 2009 - dave.lin@sun.com
- Add patch -08-libgnomeui.diff.
* Thu Aug 07 2008 - halton.huo@sun.com
- Use sgml format man pages.
* Tue Aug 05 2008 - halton.huo@sun.com
- Add patch save-rdp.diff to fix bugster #6733133
* Thu Jul 24 2008 - halton.huo@sun.com
- Add patch desktop.diff to fix #2026506
* Tue Jul 10 2008 - halton.huo@sun.com
- Add patch uttsc.diff to support uttsc
- Add patch print-null.diff to fix crash bug 2014822
* Tue Jul 08 2008 - halton.huo@sun.com
- Add patch s11-O0.diff to fix bug 2013149 
* Tue Jul 01 2008 - halton.huo@sun.com
- Add patch xnest-xephyr.diff to fix bug 2007323
* Fri Jun 27 2008 - nonsea@users.sourceforge.net
- Add debug option 
* Thu Jun 19 2008 - nonsea@users.sourceforge.net
- Initial version
