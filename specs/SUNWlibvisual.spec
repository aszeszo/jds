#
# spec file for package SUNWlibvisual.spec
#
# include module(s): libvisual, libvisual-plugins
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use libvisual64 = libvisual.spec
%use libvisual_plugins64 = libvisual-plugins.spec
%endif

%include base.inc
%use libvisual = libvisual.spec
%use libvisual_plugins = libvisual-plugins.spec

Name:                   SUNWlibvisual
License:                GPL v2, LGPL v2.1
IPS_package_name:       library/desktop/libvisual
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                Libvisual provides a convenient API for writing visualization plugins
Version:                %{libvisual.version}
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:		%{name}.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWlibmsr
BuildRequires: SUNWxorg-mesa
Requires: SUNWgtk2
Requires: SUNWlibmsr

%package l10n
Summary:       %{summary} - l10n files
Requires:       %{name}

%package devel
Summary:        %{summary} - development files
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name
Requires: SUNWgnome-common-devel

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libvisual64.prep -d %name-%version/%_arch64
%libvisual_plugins64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%libvisual.prep -d %name-%version/%{base_arch}
%libvisual_plugins.prep -d %name-%version/%{base_arch}

%build

%ifarch amd64 sparcv9
export CFLAGS="%optflags64 -features=extensions -D__volatile=__volatile__"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="$FLAG64 -Wl,-Mmap.remove_all"
export PKG_CONFIG_PATH="%{_pkg_config_path64}"
%libvisual64.build -d %name-%version/%_arch64

export CFLAGS="$CFLAGS -I%{_builddir}/%name-%version/%{_arch64}/libvisual-%{libvisual.version}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="$FLAG64 -L%{_builddir}/%name-%version/%{_arch64}/libvisual-%{libvisual.version}/libvisual/.libs"
export PKG_CONFIG_PATH="%{_builddir}/%name-%version/%{_arch64}/libvisual-%{libvisual.version}:%{_pkg_config_path64}"
%libvisual_plugins64.build -d %name-%version/%_arch64
%endif

export CFLAGS="-features=extensions -D__volatile=__volatile__"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%{_ldflags} -Wl,-Mmap.remove_all"
export PKG_CONFIG_PATH="%{_pkg_config_path}"
%libvisual.build -d %name-%version/%{base_arch}

export CFLAGS="$CFLAGS -I%{_builddir}/%name-%version/%{base_arch}/libvisual-%{libvisual.version}"
export LDFLAGS="%_ldflags -L%{_builddir}/%name-%version/%{base_arch}/libvisual-%{libvisual.version}/libvisual/.libs"
export PKG_CONFIG_PATH="%{_builddir}/%name-%version/%{base_arch}/libvisual-%{libvisual.version}:%{_pkg_config_path}"
%libvisual_plugins.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libvisual64.install -d %name-%version/%_arch64
%libvisual_plugins64.install -d %name-%version/%_arch64
%endif

%libvisual.install -d %name-%version/%{base_arch}
%libvisual_plugins.install -d %name-%version/%{base_arch}

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755,root,bin) %{_libdir}
%{_libdir}/libvisual*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libvisual*
%endif
%defattr (-, root, other)
%dir %attr(0755, root, sys) %{_datadir}
%ifnarch sparc
%{_datadir}/libvisual*
%endif
%doc %{base_arch}/libvisual-%{libvisual.version}/AUTHORS
%doc %{base_arch}/libvisual-%{libvisual.version}/README
%doc(bzip2) %{base_arch}/libvisual-%{libvisual.version}/COPYING
%doc(bzip2) %{base_arch}/libvisual-%{libvisual.version}/NEWS
%doc(bzip2) %{base_arch}/libvisual-%{libvisual.version}/ChangeLog
%doc(bzip2) %{base_arch}/libvisual-%{libvisual.version}/po/ChangeLog
%doc %{base_arch}/libvisual-plugins-%{libvisual_plugins.version}/AUTHORS
%doc %{base_arch}/libvisual-plugins-%{libvisual_plugins.version}/NEWS
%doc %{base_arch}/libvisual-plugins-%{libvisual_plugins.version}/README
%doc %{base_arch}/libvisual-plugins-%{libvisual_plugins.version}/po/ChangeLog
%doc(bzip2) %{base_arch}/libvisual-plugins-%{libvisual_plugins.version}/COPYING
%doc(bzip2) %{base_arch}/libvisual-plugins-%{libvisual_plugins.version}/ChangeLog

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other)	%{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*.pc
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%changelog
* Mon Oct 18 2010 - brian.cameron@oracle.com
- Correct setting of LDFLAGS to not include /usr/X11/lib/amd64.
  Fixes CR #6964559.
* Fri Apr 09 2010 - brian.cameron@sun.com
- Fix building of libvisual-plugins and add amd64 build.
* Fri Feb  5 2010 - christian.kelly@sun.com
- Disable build of plugins, getting a build error.
* Thu Feb 19 2009 - brian.cameron@sun.com
- Remove -xarch=sse2 since it was not being implemented properly.  When
  building with sse2 specific flags you have to install to a directory
  specific to the architecture.
* Fri Jan 16 2009 - christian.kelly@sun.com
- Fixed %files.
* Fri Jan 09 2009 - brian.cameron@sun.com
- Add SUNWlibmsr and SUNWgnome-base-libs as dependencies.  Fixes bug 
  #6791253.
* Fri Jan 09 2009 - christian.kelly@sun.com
- Fix up %files section.
* Mon Dec 22 2008 - takao.fujiwara@sun.com
- add l10n package.
* Tue Nov 25 2008 - jim.li@sun.com
- add copyright file
- add license tag
- combine SFElibvisual and SFElibvisual-plugin to SUNWlibvisual
- use sun compiler 12 instead of gcc
* Sun Jun 29 2008 - river@wikimedia.org
- force /usr/sfw/bin/gcc, use gcc cflags instead of studio
* Thu Jan 24 2008 - moinak.ghosh@sun.com
- Initial spec.



