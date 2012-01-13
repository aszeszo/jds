#
# spec file for package SUNWlibnotify
#
# includes module(s): libnotify
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libnotify64 = libnotify.spec
%endif

%include base.inc
%use libnotify = libnotify.spec

Name:                    SUNWlibnotify
IPS_package_name:        library/libnotify
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 Library for desktop notifications
Version:                 %{libnotify.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 LGPLv2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc

BuildRequires:           SUNWgtk2
BuildRequires:           SUNWdbus
BuildRequires:           SUNWdbus-glib
Requires:                SUNWgtk2
Requires:                SUNWdbus

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%{_arch64}
%libnotify64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%libnotify.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
export PKG_CONFIG_PATH=%{_libdir}/%{_arch64}/pkgconfig
export CFLAGS="%optflags64"
export LDFLAGS="%_ldflags"
%libnotify64.build -d %name-%version/%{_arch64}
%endif

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
%libnotify.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libnotify64.install -d %name-%version/%{_arch64}
%endif

%libnotify.install -d %name-%version/%{base_arch}

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/notify-send
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/libnotify.so*
%{_libdir}/pkgconfig/libnotify.pc
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/notify-send
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/libnotify.so*
%{_libdir}/%{_arch64}/pkgconfig/libnotify.pc
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc/html/libnotify/*
%{_includedir}/libnotify/*.h

%changelog
* Wen Apl 27 2011 - yun-tong.jin@oracle.com
- Add required SUNWgtk2 and SUNWdbus to fix CR 7037733
* Thu Jan 21 2010 - jedy.wang@sun.com
- Updates cflags to fix 64-bit build problem.
* Sun Jan  3 2009 - christian.kelly@sun.com
- Add dep on SUNWgtk2.
* Tue Dec 29 2009 - jedy.wang@sun.com
- Add 64-bit support.
* Thu Dec  3 2009 - christian.kelly@sun.com
- Separate into own spec (from gnome-panel).



