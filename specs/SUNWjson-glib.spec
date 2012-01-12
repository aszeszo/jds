#
# spec file for package SUNWjson-glib
#
# includes module(s): json-glib
#
# Copyright (c) 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

Name:                    SUNWjson-glib
IPS_package_name:        library/json-glib
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 JSON parser library for GLib
Version:                 0.14.0
License:                 LGPL v2.1
Source:			 http://ftp.gnome.org/pub/GNOME/sources/json-glib/0.14/json-glib-%{version}.tar.bz2
Url:                     http://live.gnome.org/JsonGlib
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc

%if %{!?_without_gtk_doc:1}%{?_without_gtk_doc:0}
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWgtk-doc
%endif
BuildRequires: SUNWglib2-devel
Requires: SUNWglib2

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name
Requires: SUNWglib2

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n json-glib-%version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

./configure --prefix=%{_prefix}		\
	    --bindir=%{_bindir}		\
            --libdir=%{_libdir}		\
            --includedir=%{_includedir}	\
	    --mandir=%{_mandir}		\
	    %{gtk_doc_option}		\
	    --disable-static

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
%doc COPYING ChangeLog NEWS README
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/girepository-1.0
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gir-1.0
%dir %attr (0755, root, other) %{_docdir}

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%if %{!?_without_gtk_doc:1}%{?_without_gtk_doc:0}
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc
%endif

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Fri Sep 30 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.14.0.
* Thu Sep 15 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.13.90.
* Thu Aug 18 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.13.4.
* Wed Jul 06 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.12.6.
* Sat Oct 23 2010 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 0.12.0.
* Wed Feb 03 2010 - Albert Lee <trisk@opensolaris.org>
- Bump to 0.10.0
* Sat Nov 14 2009 - Albert Lee <trisk@opensolaris.org>
- Bump to 0.8.2
- Drop patch1
- Update source URL, add license
- Update dependencies
* Sun Jun 21 2009 - trisk@forkgnu.org
- Initial spec
