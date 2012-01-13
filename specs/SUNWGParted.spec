#
# spec file for package SUNWGParted
#
# Copyright (c) 2009, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: ml40262
#
%include Solaris.inc

%define owner ml40262
%define OSR 11229:0.4.1

Name:                    SUNWGParted
IPS_package_name:        desktop/administration/gparted
Meta(info.classification): %{classification_prefix}:System/Administration and Configuration
Summary:                 GNOME Partition Editor
Version:                 0.4.5
License:                 GPL v2
SUNW_BaseDir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Source:                  %{sf_download}/gparted/gparted-%{version}.tar.bz2
Source1:                 %{name}-exec_attr
Patch1:                  GParted-01-solaris.diff

# these packages are only available on i386/x64
%ifnarch sparc

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWparted
Requires: SUNWgtkmm
Requires: SUNWglibmm
Requires: SUNWpangomm
Requires: SUNWcairomm
Requires: SUNWsigcpp
Requires: SUNWfontconfig
Requires: SUNWntfsprogs
Requires: SUNWdesktop-cache
Requires: SUNWgnome-libs
Requires: SUNWgksu
Requires: SUNWlibms
BuildRequires: SUNWxwplt
BuildRequires: SUNWmlib
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWgksu

%prep
%setup -q -c -n %name-%version
cd gparted-%{version}
%patch1 -p1
cd ..

%build
cd gparted-%{version}
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"
./configure --prefix=/usr
make AM_CFLAGS="%optflags" AM_CXXFLAGS="%cxx_optflags"
cd ..

%install
[ "$RPM_BUILD_ROOT" != "" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
cd gparted-%{version}
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/security/exec_attr.d
install --mode=0644 %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/security/exec_attr.d/desktop-administration-gparted

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%post
%restart_fmri icon-cache

%postun
%restart_fmri icon-cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d gparted-%{version} COPYING AUTHORS NEWS ChangeLog README
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_sbindir}
%{_sbindir}/gparted
%{_sbindir}/gpartedbin
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man8
%{_mandir}/man8/gparted.8
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications/
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/gnome/
%dir %attr (0755, root, bin) %{_datadir}/gnome/help/
%dir %attr (0755, root, bin) %{_datadir}/gnome/help/gparted/
%dir %attr (0755, root, bin) %{_datadir}/gnome/help/gparted/[Ca-z]*/
%{_datadir}/gnome/help/gparted/[Ca-z]*/gparted.xml
%dir %attr (0755, root, bin) %{_datadir}/gnome/help/gparted/[Ca-z]*/figures/
%{_datadir}/gnome/help/gparted/[Ca-z]*/figures/gparted_window.png
%dir %attr (0755, root, bin) %{_datadir}/omf/
%dir %attr (0755, root, bin) %{_datadir}/omf/gparted/
%{_datadir}/omf/gparted/*
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/16x16/apps/
%{_datadir}/icons/hicolor/16x16/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/22x22/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/22x22/apps/
%{_datadir}/icons/hicolor/22x22/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/apps/
%{_datadir}/icons/hicolor/24x24/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/apps/
%{_datadir}/icons/hicolor/32x32/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/apps/
%{_datadir}/icons/hicolor/48x48/apps/*
%defattr (-, root, other)
%{_datadir}/locale/[a-z][a-z]
%{_datadir}/locale/[a-z][a-z]_[A-Z][A-Z]
%attr(0755, root, sys) %dir %{_sysconfdir}
%dir %attr(0755, root, sys) /etc/security
%dir %attr(0755, root, sys) /etc/security/exec_attr.d
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %attr (0444, root, sys) /etc/security/exec_attr.d/*

#endif for "ifnarch sparc"
%endif

%changelog
* Mon May 02 2011 - brian.cameron@oracle.com
- Add root package and install the RBAC configuration file
  /etc/security/exec_attr.d/desktop-administration-gparted to associate gparted
  with the "System Administrator" profile.
* Tue Oct 19 2010 - Mark.Logan@oracle.com
- Add Requires and BuildRequires gksu
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Wed Apr 21 2010 - christian.kelly@oracle.com
- Add SUNWgnome-libs as dependency.
* Sat Oct 03 2009 - dave.lin@sun.com
- Fixed post script issue.
* Tue Jun 09 2009 - Mark.Logan@sun.com
- initial version added to SVN


