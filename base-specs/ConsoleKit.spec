#
# spec file for package ConsoleKit
#
# Copyright (c) 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: bugs.freedesktop.org
#
%define OSR 10394:3.0

Name:         ConsoleKit
License:      GPL v2, MIT, BSD
Group:        Libraries
Version:      0.4.5
Release:      1
Distribution: Java Desktop System
Vendor:       Freedesktop.org
Summary:      Framework for tracking users, login sessions, and seats.
URL:          http://www.freedesktop.org/wiki/Software/ConsoleKit
Source:       http://www.freedesktop.org/software/ConsoleKit/dist/%{name}-%{version}.tar.bz2
# date:2008-12-30 owner:yippi type:bug bugzilla:19333
Patch1:       ConsoleKit-01-ck-dynamic.diff
# date:2009-07-23 owner:yippi type:branding
Patch2:       ConsoleKit-02-add-sunray-type.diff
# date:2009-07-23 owner:yippi type:branding
Patch3:       ConsoleKit-03-sol-novt.diff
# date:2009-11-03 owner:yippi type:branding doo:12395
Patch4:       ConsoleKit-04-sol-xserver.diff
# date:2009-11-10 owner:jedy type:bug bugzilla:24749
Patch5:       ConsoleKit-05-fastreboot.diff
# date:2009-12-04 owner:yippi type:bug bugzilla:25436
Patch6:       ConsoleKit-06-ck-history.diff
# date:2010-02-23 owner:yippi type:bug bugster:7003908
Patch7:       ConsoleKit-07-suppress-warning.diff
# This relates to GDM upstream bugzilla bug #618047.
# date:2010-07-20 owner:yippi type:bug bugster:7032861
Patch8:       ConsoleKit-08-vt-switch.diff

BuildRequires:  PolicyKit-devel >= 0.7
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake >= 1:1.9
BuildRequires:  dbus-glib-devel >= 0.30
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel >= 1:2.8.0
# for <sys/inotify.h>
BuildRequires:  glibc-devel >= 6:2.4
BuildRequires:  libtool >= 1.4
BuildRequires:  pam-devel >= 0.80
BuildRequires:  pkgconfig
BuildRequires:  rpmbuild(macros) >= 1.268
BuildRequires:  xmlto
BuildRequires:  xorg-lib-libX11-devel >= 1.0.0
BuildRequires:  zlib-devel
Requires:       /sbin/chkconfig
Requires:       %{name}-libs = %{version}-%{release}
Requires:       dbus-glib >= 0.30
Requires:       glib2 >= 1:2.8.0
Requires:       rc-scripts
Requires:       xorg-lib-libX11 >= 1.0.0
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConsoleKit is a framework for defining and tracking users, login
sessions, and seats.

%package libs
Summary:        ConsoleKit library
Summary(pl.UTF-8):      Biblioteka ConsoleKit
License:        AFL v2.1 or GPL v2
Group:          Libraries
Requires:       dbus-libs >= 0.30
Conflicts:      ConsoleKit < 0.1-0.20061203.6

%description libs
ConsoleKit library.

%package devel
Summary:        Header files for ConsoleKit
Summary(pl.UTF-8):      Pliki nagłówkowe ConsoleKit
License:        AFL v2.1 or GPL v2
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       dbus-devel >= 0.30

%description devel
Header files for ConsoleKit.

%package static
Summary:        Static ConsoleKit library
Summary(pl.UTF-8):      Statyczna biblioteka ConsoleKit
License:        AFL v2.1 or GPL v2
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static ConsoleKit library.

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
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

glib-gettextize -f
libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f
autoconf

./configure --prefix=%{_prefix}                     \
            --libdir=%{_libdir}                     \
            --libexecdir=%{_libexecdir}             \
            --localstatedir=%{_localstatedir}       \
            --sysconfdir=%{_sysconfdir}             \
            --mandir=%{_mandir}                     \
%if %build_pam_module
            --enable-pam-module                     \
            --with-pam-module-dir=%{_libdir}/security   \
%endif
            --enable-rbac-shutdown=solaris.system.shutdown
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
%if %build_pam_module
%else
# delete useless directory /usr/man/man8 which stores pam_ck_connector.8 
#
rm -rf $RPM_BUILD_ROOT/%{_mandir}
%endif

# The /var/run directory should not be included with the packages.
# ConsoleKit will create it at run-time.
#
rmdir $RPM_BUILD_ROOT/var/run/ConsoleKit
rmdir $RPM_BUILD_ROOT/var/run

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ck-history
%attr(755,root,root) %{_bindir}/ck-launch-session
%attr(755,root,root) %{_bindir}/ck-list-sessions
%attr(755,root,root) %{_sbindir}/ck-log-system-restart
%attr(755,root,root) %{_sbindir}/ck-log-system-start
%attr(755,root,root) %{_sbindir}/ck-log-system-stop
%attr(755,root,root) %{_sbindir}/console-kit-daemon
%attr(755,root,root) %{_libdir}/ck-collect-session-info
%attr(755,root,root) %{_libdir}/ck-get-x11-server-pid
%attr(755,root,root) %{_libdir}/ck-get-x11-display-device
%dir %{_prefix}/lib/ConsoleKit/scripts
%attr(755,root,root) %{_prefix}/lib/ConsoleKit/scripts/*
%attr(755,root,root) /%{_lib}/security/pam_ck_connector.so
%{_datadir}/PolicyKit/policy/org.freedesktop.consolekit.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.ConsoleKit.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.ConsoleKit.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ConsoleKit.Seat.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.ConsoleKit.Session.xml
%{_sysconfdir}/dbus-1/system.d/ConsoleKit.conf
%dir %{_sysconfdir}/ConsoleKit
%dir %{_sysconfdir}/ConsoleKit/run-session.d
%dir %{_sysconfdir}/ConsoleKit/seats.d
%{_sysconfdir}/ConsoleKit/seats.d/00-primary.seat
%{_mandir}/man8/pam_ck_connector.8*
%dir %{_localstatedir}/run/ConsoleKit
%dir %{_localstatedir}/log/ConsoleKit

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libck-connector.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libck-connector.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libck-connector.so
%{_libdir}/libck-connector.la
%dir %{_includedir}/ConsoleKit
%dir %{_includedir}/ConsoleKit/ck-connector
%{_includedir}/ConsoleKit/ck-connector/*.h
%{_libdir}/pkgconfig/ck-connector.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libck-connector.a

%changelog
* Fri Jul 22 2011 - brian.cameron@oracle.com
- Add patch ConsoleKit-13-vt-switch.diff to fix CR #7032861.
* Thu Jul 07 2011 - brian.cameron@oracle.com
- Bump to 0.4.5.
* Fri Apr 29 2011 - brian.cameron@oracle.com
- Merge patch 14 into patch 1.
* Wed Feb 23 2011 - brian.cameron@oracle.com
- Add patch ConsoleKit-13-suppress-warning.diff.
* Fri Jun 18 2010 - halton.huo@sun.com
- Add patch -cores-srss.diff to fix bugzilla #28598, bugster #6951766.
* Fri Mar 26 2010 - halton.huo@sun.com
- Remove patch -actual-vt-on-switch.diff because we this issue fix
  inside GDM code base instead.
* Fri Jan 15 2010 - halton.huo@sun.com
- Add patch -sol-vtdaemon.diff to fix bugzilla #26055.
* Fri Dec 04 2009 - halton.huo@sun.com
- Add patch -ck-history.diff to fix bugzilla #25436.
* Mon Nov 30 2009 - halton.huo@sun.com
- Add patch -actual-vt-on-switch.diff to fix doo #12563.
* Tue Nov 10 2009 - jedy.wang@sun.com
- Add patch fastreboot.diff to fix bugzilla #24749.
* Tue Nov 10 2009 - jedy.wang@sun.com
- Add patch can-stop.diff to fix bugzilla #24992.
* Thu Nov 05 2009 - halton.huo@sun.com
- Add patch sol-xserver.diff to fix doo #12395.
- Add patch sol-vt-major.diff to fix doo #12322.
* Thu Oct 15 2009 - halton.huo@sun.com
- Add patch sol-sigpoll.diff to fix doo #11612.
* Fri Sep 25 2009 - halton.huo@sun.com
- Add patch sol-tty.diff to correct return value of
  /usr/lib/ck-get-x11-display-device after VT is integrated
- Remove tempory patch dev-console.diff
* Thu Sep 24 2009 - halton.huo@sun.com
- Bump to 0.4.1
- Remove upstreamed patch close-fp.diff
* Mon Sep 07 2009 - halton.huo@sun.com
- Remove obsoleted patch 01-ck-history.diff and reorder
* Fri Sep 04 2009 - halton.huo@sun.com
- Rework 02-ck-dynamic to fix console-kit-daemon core dump when
  second time login. Get more information from branch multi-seat.
* Tue Aug 11 2009 - halton.huo@sun.com
- Remove obsoleted patches: dynamic-tty.diff and solaris-vtdaemon.diff 
- Add sun branding patch sol-novt.diff
- Reorder patches
* Mon Jul 27 2009 - halton.huo@sun.com
- New from SFEconsolekit.spec

