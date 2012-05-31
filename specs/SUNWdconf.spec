#
# spec file for package SUNWdconf
#
# includes module(s): dconf
#
# Copyright (c) 2011,2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

Name:                    SUNWdconf
IPS_package_name:        gnome/config/dconf
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Sessions
Summary:                 DConf
Version:                 0.12.1
License:                 LGPL v2.1
Source:			 http://ftp.gnome.org/pub/GNOME/sources/dconf/0.12/dconf-%{version}.tar.xz
# date:2012-05-22 owner:yippi type:bug bugzilla:676619
Patch1:                  dconf-01-compile.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires: SUNWgtk3
Requires: SUNWglib2
Requires: SUNWvala
Requires: SUNWdbus
BuildRequires: SUNWgtk3-devel
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWvala-devel
BuildRequires: SUNWdbus-devel

%include default-depend.inc

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
Requires: SUNWgtk3-devel
Requires: SUNWglib2-devel
Requires: SUNWvala-devel
Requires: SUNWdbus-devel

%if %build_l10n
%package l10n
IPS_package_name:        gnome/config/dconf/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}
%endif

%prep
%setup -q -n dconf-%version
%patch1 -p1

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

touch README AUTHORS ChangeLog
aclocal-1.11 $ACLOCAL_FLAGS -I ./m4
automake-1.11 -a -c -f
./configure --prefix=%{_prefix}		\
            --prefix=%{_prefix} 	\
            --sysconfdir=%{_sysconfdir}	\
            --localstatedir=%{_localstatedir} \
            --mandir=%{_mandir}		\
            --libexecdir=%{_libexecdir}

gmake -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a

%if %{!?_without_gtk_doc:0}%{?_without_gtk_doc:1}
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc
%endif

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc COPYING NEWS
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/dconf-service
%{_libdir}/lib*.so*
%{_libdir}/gio/modules/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/dbus-1
%{_datadir}/dconf-editor
%{_datadir}/glib-2.0
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/apps/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/apps/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/64x64/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/64x64/apps/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/128x128/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/128x128/apps/
%{_datadir}/icons/hicolor/*/apps/*
%dir %attr (0755, root, other) %{_docdir}

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%dir %attr (0755, root, root) %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/*
%{_sysconfdir}/dconf/db

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc
%{_datadir}/vala/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Thu May 03 2012 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.12.1.
* Fri Sep 30 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.10.0.
* Thu Aug 18 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.9.0.
* Wed Jul 06 2011 - Brian Cameron <brian.cameron@oracle.com>
- Created for version 0.7.5.
