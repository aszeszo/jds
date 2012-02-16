#
# spec file for package SUNWconsolekit
#
# includes module(s): ConsoleKit
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

# Option to decide whether or not build library pam_ck_connector,
# which implements pam_sm_open_session(3PAM) and pam_sm_close_session(3PAM).
# By default, we don't build it.
#
# Note: To enable this pam module, you have to manually add 
# an entry to /etc/pam.conf after installing SUNWconsolekit-pam,
# like this.
# "login   session required       pam_ck_connector.so debug"
#
%define build_pam_module 1

%use ck = ConsoleKit.spec

Name:                    SUNWconsolekit
Summary:                 Framework for tracking users, login sessions, and seats.
Version:                 %{ck.version}
SUNW_Pkg:                SUNWconsolekit
IPS_package_name:        library/xdg/consolekit
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Sessions
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{ck.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Source:			 %{name}-manpages-0.1.tar.gz
Source1:                 consolekit.xml
Source2:                 svc-consolekit

%include default-depend.inc
%include desktop-incorporation.inc

Requires: library/glib2
Requires: system/library/dbus
Requires: system/library/libdbus
Requires: system/library/libdbus-glib
BuildRequires: x11/server/xorg

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name

%if %build_pam_module
%package pam
Summary:		 %{summary} - PAM module to register simple text logins.
IPS_package_name:        library/security/pam/module/pam-consolekit
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Sessions
SUNW_BaseDir:		 %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name
%endif

%prep
rm -rf %name-%version
mkdir %name-%version
%ck.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
# FIXME: remove -D_POSIX_PTHREAD_SEMANTICS when not use CBE 1.6x
export CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%ck.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%ck.install -d %name-%version

# Port the man8 file to SGML and add back the below "rm".
#rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

# These programs are intended to be used if you want ConsoleKit to be
# like utmp/wtmp and log system start/restart/stop events.  There are
# no plans to support using ConsoleKit like utmp/wtmp, so do not
# install these for now.
#
rm $RPM_BUILD_ROOT/%{_sbindir}/ck-log-system-start
rm $RPM_BUILD_ROOT/%{_sbindir}/ck-log-system-restart
rm $RPM_BUILD_ROOT/%{_sbindir}/ck-log-system-stop

install -d $RPM_BUILD_ROOT/lib/svc/manifest/system
install --mode=0444 %SOURCE1 $RPM_BUILD_ROOT/lib/svc/manifest/system
install -d $RPM_BUILD_ROOT/lib/svc/method
cp %SOURCE2 $RPM_BUILD_ROOT/lib/svc/method/

%clean
rm -rf $RPM_BUILD_ROOT

%pre root
#!/bin/sh
#
# Copyright 2009 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.
#

# Presence of this temp file will tell postinstall script
# that the consolekit service is already installed, in which case
# the current service state will be preserved, be it enabled
# or disabled.
rm -f $PKG_INSTALL_ROOT/var/consolekit_installed.tmp > /dev/null 2>&1

if [ -f $PKG_INSTALL_ROOT/lib/svc/manifest/system/consolekit.xml ]; then
        touch $PKG_INSTALL_ROOT/var/consolekit_installed.tmp
fi

exit 0

%post root
#!/bin/sh
#
# Copyright 2009 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.
#

# Preinstall script will create this file if consolekit service was 
# already installed, in which case we preserve current service state,
# be it enabled or disabled.
if [ -f $PKG_INSTALL_ROOT/var/consolekit_installed.tmp ]; then
        rm -f $PKG_INSTALL_ROOT/var/consolekit_installed.tmp
else
        # enable consolekit:
        # - PKG_INSTALL_ROOT is / or empty when installing onto a live system
        #   and we can invoke svcadm directly;
        # - otherwise it's upgrade, so we append to the upgrade script
        if [ "${PKG_INSTALL_ROOT:-/}" = "/" ]; then
                if [ `/sbin/zonename` = global ]; then
                        /usr/sbin/svcadm enable -r svc:/system/consolekit:default
                fi
        else
                cat >> ${PKG_INSTALL_ROOT}/var/svc/profile/upgrade <<-EOF
                if [ \`/sbin/zonename\` = global ]; then
                        /usr/sbin/svcadm enable -r svc:/system/consolekit:default
                fi
EOF
        fi
fi

exit 0

%files
%doc -d ConsoleKit-%{ck.version} README AUTHORS
%doc(bzip2) -d ConsoleKit-%{ck.version} COPYING NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/lib*.so*
%{_libdir}/ConsoleKit
%{_libexecdir}/ck-collect-session-info
%{_libexecdir}/ck-get-x11-server-pid
%{_libexecdir}/ck-get-x11-display-device
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/dbus-1
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man1m
%{_mandir}/man1/*
%{_mandir}/man1m/*

%files root
%defattr (-, root, sys)
%{_sysconfdir}/ConsoleKit
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1/system.d
%{_sysconfdir}/dbus-1/system.d/ConsoleKit.conf
# SVC method file
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%dir %attr (0755, root, sys) /lib/svc/manifest
%dir %attr (0755, root, sys) /lib/svc/manifest/system
%attr (0555, root, bin) /lib/svc/method/svc-consolekit
%attr (0444, root, sys) /lib/svc/manifest/system/consolekit.xml
%dir %attr (0755, root, sys) %dir %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/log
%dir %attr (0755, root, root) %{_localstatedir}/log/ConsoleKit

%files devel
%defattr (-, root, bin)
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%if %build_pam_module
%files pam
%defattr (-, root, bin)
%{_libdir}/security/pam*.so*
%dir %attr (0755, root, sys) %{_datadir}
%{_mandir}/man8/*
%endif

%changelog
* Wed Feb 08 2012 - brian.cameron@oracle.com
- Update Requires/BuildRequires.
* Fri Apr 08 2011 - brian.cameron@oracle.com
- Add a /lib/svc/method/svc-consolekit script to fix CR #7025709
* Fri Apr 23 2010 - halton.huo@sun.com
- Move manifest from /var/svc to /lib/svc
* Fri Oct 23 2009 - brian.cameron@sun.com
- Add BuildRequires: SUNWxorg-headers
* Fri Oct 23 2009 - brian.cameron@sun.com
- Add manpages.
* Tue Aug 18 2009 - halton.huo@sun.com
- Enable pam module.
* Thu Jul 30 2009 - halton.huo@sun.com
- Add %pre and %post for -root pkg.
* Mon Jul 27 2009 - halton.huo@sun.com
- Move from SFE and spilit base part to ConsoleKit.spec
* Thu Jul 23 2009 - halton.huo@sun.com
- Bump to 0.3.1
- Remove upstreamed patch: emptystruct.diff, pam.diff, solaris-getpwnamr.diff
  and reorder rest
- Add patch dev-console.diff to change owner of /dev/console for console login
* Tue Jun 23 2009 - halton.huo@sun.com
- Add copyright
* Wed Apr 08 2009 - halton.huo@sun.com
- Add patch8: solaris-getpwnamr.diff to fix bug #22361
* Wed Apr 08 2009 - halton.huo@sun.com
- Add patch5: add-sunray-type.diff to add Sunray for display-typs.conf.in
- Add patch6: dynamic-tty.diff to add --tty for ck-dynaminc
- Add patch7: solaris-vtdaemon.diff to check vtdaemon service code for Solaris
* Thu Mar 26 2009 - halton.huo@sun.com
- Add all files under etc/ConsoleKit/ to %files root
* Sat Feb 07 2009 - brian.cameron@sun.com
- Package should not install anything to  /var/run.
* Tue Dec 30 2008 - halton.huo@sun.com
- Add patch ck-dynamic.diff to fix bug #19333
* Tue Oct 21 2008 - halton.huo@sun.com
- Add standard patch comment
* Thu Aug 07 2008 - brian.cameron@sun.com
- Bump to 0.3.0.
* Tue Jun 24 2008 - simon.zheng@sun.com
- Add patch 05-getcurrentsession.diff for freedesktop bug #15866.
* Tue Mar 11 2008 - brian.cameron@sun.com
- Minor cleanup
* Tue Mar 04 2008 - simon.zheng@sun.com
- Add patch 04-ck-history.diff to fix crash.
* Sat Mar 01 2008 - simon.zheng@sun.com
- Add patch 03-pam.diff to build pam module library 
  pam-ck-connector that registers text login session into 
  ConsoleKit. And this library is packed as a separate 
  package called SFEconsolekit-pam.
* Mon Feb 25 2008 - brian.cameron@sun.com
- Bump release to 0.2.10.  Worked with the maintainer to get seven
  recent patches upstream.
* Mon Feb 25 2008 - simon.zheng@sun.com
- Rework ConsoleKit-06-fixvt.diff for better macro definition.
* Fri Feb 22 2008 - brian.cameron@sun.com
- Add the patch ConsoleKit-05-devname.diff that Simon wrote, patch
  ConsoleKit-06-fixvt.diff so that patch 4 builds properly when you
  do not have VT installed, patch ConsoleKit-07-fixactiveconsole.diff
  so that Active device is set to "/dev/console" when not using VT,
  ConsoleKit-08-fixseat.diff to correct a crash due to a NULL string
  in a printf, and ConsoleKit-09-novt.diff to fix ConsoleKit so that
  it sets x11-display-device to "/dev/console" when not using
  VT.
* Tue Feb 19 2008 - simon.zheng@sun.com
- Add patch ConsoleKit-04-vt.diff. Use sysnchronous event notification
  in STREAMS to monitor VT activation. 
* Fri Feb 15 2008 - brian.cameron@sun.com
- Rework ConsoleKit-03-paths.diff so it makes better use of #ifdefs.
* Fri Feb 15 2008 - simon.zheng@sun.com
- Bump to 0.2.9. Add ConsoleKit-03-noheaderpaths.diff because there's not
  header paths.h on Solaris.
* Thu Feb 07 2008 - Brian.Cameron@sun.com
- Add /var/log/ConsoleKit/history file to packaging.
* Thu Jan 31 2008 - Brian.Cameron@sun.com
- Bump to 0.2.7.  Remove two upstream patches added on January 25,
  2007.
* Fri Jan 25 2008 - Brian.Cameron@sun.com
- Bump to 0.2.6.  Rework patches.  Add patch ConsoleKit-02-RBAC.diff
  to make ConsoleKit use RBAC instead of PolicyKit on Solaris.
  Patch ConsoleKit-03-fixbugs.diff fixes some bugs I found.
* Tue Sep 18 2007 - Brian.Cameron@sun.com
- Bump to 0.2.3.  Remove upstream ConsoleKit-01-head.diff
  patch and add ConsoleKit-02-fixsolaris.diff to fix some
  issues building ConsoleKit when VT is not present.
* Mon Aug 16 2007 - Brian.Cameron@sun.com
- Created.


