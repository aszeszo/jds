#
# spec file for package SUNWgtkimageview.spec
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jedy
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use gtkimageview64 = gtkimageview.spec
%endif

%include base.inc
%use gtkimageview = gtkimageview.spec

Name:           SUNWgtkimageview
License:      LGPL v2
IPS_package_name: library/desktop/gtkimageview
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:        A simple image viewer widget for GTK+.
Version:        %{gtkimageview.version}
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc

BuildRequires:  SUNWgtk2
Requires:       SUNWgtk2

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%{_arch64}
%gtkimageview64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%gtkimageview.prep -d %name-%version/%{base_arch}


%build
%ifarch amd64 sparcv9
export PKG_CONFIG_PATH=%{_libdir}/%{_arch64}/pkgconfig
export CFLAGS="%optflags64"
export LDFLAGS="%_ldflags"
%gtkimageview64.build -d %name-%version/%{_arch64}
%endif

export PKG_CONFIG_PATH=%{_libdir}/pkgconfig
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
%gtkimageview.build -d %name-%version/%{base_arch}


%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%gtkimageview64.install -d %name-%version/%{_arch64}
%endif

%gtkimageview.install -d %name-%version/%{base_arch}

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc(bzip2) -d %{base_arch}/gtkimageview-%{gtkimageview.version} COPYING
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libgtkimageview.so*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/gtkimageview.pc
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %dir %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libgtkimageview.so*
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/gtkimageview.pc
%endif
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/gtkimageview/*.h
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc
%dir %attr (0755, root, other) %{_datadir}/doc


%changelog
* Tue Mar 02 2010 - jedy.wang@sun.com
- Update summary and SUNWgtk2 dependency.
* Fri Jan 22 2010 - jedy.wang@sun.com
- Add 64-bit support.
* Mon Dec 14 2009 - jedy.wang@sun.com
- Regenerate cofngiure before building.
* Sun Oct 11 2009 - Milan Jurik
- Initial spec


