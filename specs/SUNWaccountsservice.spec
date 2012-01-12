#
# spec file for package SUNWaccountsservice
#
# includes module(s): accountsservice
#
# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

Name:                    SUNWaccountsservice
IPS_package_name:        library/xdg/accountsservice
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Sessions
Summary:                 Accounts Service
Version:                 0.6.12
License:                 LGPL v2.1
Source:			 http://www.freedesktop.org/software/accountsservice/accountsservice-%version.tar.bz2
Source1:                 accountsservice.xml
Source2:                 svc-accountsservice
Patch1:                  accountsservice-01-polkit.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc

BuildRequires: SUNWglib2-devel
Requires: SUNWglib2

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %name
Requires: SUNWglib2-devel

%if %build_l10n
%package l10n
IPS_package_name:        library/xdg/accountsservice/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}
%endif

%prep
%setup -q -n accountsservice-%version
%patch1 -p1

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags -DFALLBACK_MINIMAL_UID=100"
export LDFLAGS="%{_ldflags}"

libtoolize --force
aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf
./configure --prefix=%{_prefix}		\
            --sysconfdir=%{_sysconfdir} \
            --localstatedir=%{_localstatedir} \
	    --bindir=%{_bindir}		\
            --libdir=%{_libdir}		\
            --libexecdir=%{_libexecdir} \
            --includedir=%{_includedir}	\
	    --mandir=%{_mandir}		\
	    --disable-static

gmake -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

install -d $RPM_BUILD_ROOT/lib/svc/manifest/system
install --mode=0444 %SOURCE1 $RPM_BUILD_ROOT/lib/svc/manifest/system
install -d $RPM_BUILD_ROOT/lib/svc/method
cp %SOURCE2 $RPM_BUILD_ROOT/lib/svc/method/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc AUTHORS COPYING NEWS README
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/girepository-1.0
%{_libdir}/accounts-daemon
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/dbus-1
%{_datadir}/gir-1.0
%{_datadir}/polkit-1
%dir %attr (0755, root, other) %{_docdir}

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1
%dir %attr (0755, root, bin) %{_sysconfdir}/dbus-1/system.d
%{_sysconfdir}/dbus-1/system.d/*

%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, other) %{_localstatedir}/lib
%{_localstatedir}/lib/AccountsService
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%dir %attr (0755, root, sys) /lib/svc/manifest
%dir %attr (0755, root, sys) /lib/svc/manifest/system
%attr (0555, root, bin) /lib/svc/method/svc-accountsservice
%attr (0444, root, sys) /lib/svc/manifest/system/accountsservice.xml

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Sat Jul 09 2011 - Brian Cameron <brian.cameron@oracle.com>
- Created with 0.6.12.
