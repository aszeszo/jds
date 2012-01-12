#
# spec file for package SUNWgsettings-schemas
#
# includes module(s): gsettings-desktop-schemas
#
# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

Name:                    SUNWgsettings-schemas
IPS_package_name:        gnome/config/gsettings-schemas
Meta(info.classification): %{classification_prefix}:Applications/Configuration and Preferences
Summary:                 GSettings Desktop Schemas
Version:                 3.2.0
License:                 LGPL v2.1
Source:			 http://ftp.gnome.org/pub/GNOME/sources/gsettings-desktop-schemas/3.2/gsettings-desktop-schemas-%{version}.tar.bz2
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

Requires: SUNWglib2
BuildRequires: SUNWglib2-devel
%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name
Requires: SUNWglib2-devel

%if %build_l10n
%package l10n
IPS_package_name:        gnome/config/gsettings-schemas/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}
%endif

%prep
%setup -q -n gsettings-desktop-schemas-%version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

./configure --prefix=%{_prefix}		\
	    --bindir=%{_bindir}		\
	    --mandir=%{_mandir}		\

gmake -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a

%if %{!?_without_gtk_doc:0}%{?_without_gtk_doc:1}
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc
%endif

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/GConf
%{_datadir}/glib-2.0
%dir %attr (0755, root, other) %{_docdir}

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/pkgconfig/*
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Fri Sep 30 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 3.2.0.
* Tue Sep 13 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 3.1.91.
* Wed Jul 06 2011 - Brian Cameron <brian.cameron@oracle.com>
- Created for version 3.1.3.

