#
# spec file for package SUNWstardict
#
# includes module(s): stardict
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yongsun

%include Solaris.inc

%define src_name stardict
%define src_url http://downloads.sourceforge.net/stardict

Name:		SUNWstardict
IPS_package_name: system/desktop/stardict
Meta(info.classification): %{classification_prefix}:Applications/Accessories
Summary:	A powerful dictionary platform written in GTK+2
Version: 	3.0.1
License: 	GPLv3
SUNW_Copyright: %{name}.copyright
SUNW_BaseDir:   %{_basedir}
SUNW_LOC:       zh,zh.GBK,zh_CN.GB18030,zh.UTF-8
SUNW_PKGLIST:   SUNWgnome-libs
Source: 	%{src_url}/%{src_name}-%{version}.tar.bz2
Patch1:         stardict-01-ss12.diff
BuildRoot:      %{_tmppath}/%{src_name}-%{version}-build
%include desktop-incorporation.inc
BuildRequires: consolidation/desktop/gnome-incorporation
%include default-depend.inc
Requires: SUNWlibC
Requires: SUNWlibpopt
Requires: SUNWgnome-base-libs
Requires: SUNWgnome-panel
Requires: SUNWpostrun
Requires: SUNWstardict-root
Requires: SUNWespeak
Requires: SUNWsigcpp
BuildRequires: SUNWlibpopt-devel
BuildRequires: SUNWgnome-base-libs-devel
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWespeak-devel
BuildRequires: SUNWsigcpp-devel

%package root
Summary:        %{summary} (ROOT)
IPS_package_name: system/desktop/stardict
SUNW_BaseDir:   /
%include default-depend.inc
Requires: SUNWgnome-base-libs-root
Requires: SUNWgnome-panel-root
Requires: SUNWpostrun-root

%prep
%setup -q -n %{src_name}-%{version}
%patch1 -p1

%build
export CXX="${CXX} -norunpath"
export CFLAGS="%optflags"
#export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags -lsocket"
./autogen.sh --prefix=%{_prefix}        \
             --disable-festival         \
             --disable-advertisement    \
             --disable-gucharmap
make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall
find ${RPM_BUILD_ROOT} -name "*.a" -exec rm  {} \; -print
find ${RPM_BUILD_ROOT} -name "*.la" -exec rm {} \; -print

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-, root, bin)
%{_bindir}/*
%{_libdir}/bonobo/*
%{_libdir}/stardict/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/applications
%attr (-, root, other) %{_datadir}/pixmaps
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/omf/*
%{_datadir}/idl/*
%{_datadir}/stardict/*
%{_datadir}/gnome/*
%{_datadir}/man/*

%files root
%defattr (-, root, sys)
%attr (-, root, sys) %{_sysconfdir}

%changelog
* Tue Aug 26 2008 - yongsun@users.sourceforge.net
- Initial spec
