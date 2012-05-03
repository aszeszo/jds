#
# spec file for package SUNWcogl
#
# includes module(s): cogl
#
# Copyright (c) 2011, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

Name:                    SUNWcogl
IPS_package_name:        library/cogl
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 Drawing library for use with 3D graphics hardware.
Version:                 1.10.2
License:                 LGPL v2.1
Source:			 http://ftp.gnome.org/pub/GNOME/sources/cogl/1.10/cogl-%{version}.tar.xz
# date:2011-10-04 owner:yippi type:bug
Patch1:                  cogl-01-makefile.diff
Url:                     http://www.clutter-project.org/
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc

%if %{!?_without_gtk_doc:1}%{?_without_gtk_doc:0}
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWgtk-doc
%endif
Requires: SUNWxorg-mesa
Requires: SUNWglib2
Requires: SUNWgdk-pixbuf
Requires: SUNWcairo
Requires: SUNWpango
BuildRequires: SUNWgobject-introspection-devel
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWgdk-pixbuf-devel
BuildRequires: SUNWcairo-devel
BuildRequires: SUNWpango-devel
BuildRequires: SUNWuiu8
BuildRequires: SUNWxwinc
BuildRequires: SUNWxorg-headers
BuildRequires: SUNWxorg-mesa

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
%setup -q -n cogl-%version
%patch1 -p1

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

# This is needed for the gobject-introspection compile to find libdrm.
export LD_LIBRARY_PATH=/usr/lib/xorg

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

# This is needed for the gobject-introspection compile to find libdrm and
# libplds4.
export LD_LIBRARY_PATH="/usr/lib/xorg:/usr/lib/mps"

aclocal-1.11 $ACLOCAL_FLAGS -I ./build/autotools
autoheader
automake-1.11 -a -c -f
autoconf
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

# Remove empty directory.
rmdir $RPM_BUILD_ROOT%{_bindir}

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
%{_datadir}/cogl
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
* Wed May 02 2012 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 1.10.2.
* Wed Oct 19 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 1.8.2.
* Tue Oct 04 2011 - Brian Cameron <brian.cameron@oracle.com>
- Initial spec file with version 1.8.0.
