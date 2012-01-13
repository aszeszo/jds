#
# spec file for package SUNWtgnome-xagent
#
# includes module(s): gnome-session
#
# Copyright (c) 2004 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet

%include Solaris.inc

%define with_hal %(pkginfo -q SUNWhal && echo 1 || echo 0)

%use gsession = gnome-session.spec

Name:                    SUNWtgnome-xagent
IPS_package_name:        gnome/trusted/xagent
License:                 GPLv2
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Trusted Extensions
Summary:                 GNOME Trusted Xagent
# keep the version as the same as tstripe
Version:                 0.6.8
Source1:                 tsoljds-migration
#owner:gheet date:2006-11-03 type:feature
Patch1:			 SUNWtgnome-xagent-01-trusted-extensions.diff
Patch2:			 SUNWtgnome-xagent-02-URI-support.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWxorg-headers
BuildRequires: x11/trusted/libxtsol
Requires: SUNWlibglade
Requires: SUNWgnome-vfs-root
Requires: SUNWgnome-libs
Requires: SUNWgnome-config
Requires: SUNWgnome-panel
# Requires: SUNWgnome-component
BuildRequires: runtime/perl-512
Requires: SUNWbzip
Requires: SUNWzlib
Requires: SUNWlxml
Requires: SUNWgnome-desktop-prefs
BuildRequires: SUNWxwrtl
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWgnome-desktop-prefs-devel
BuildRequires: consolidation/desktop/desktop-incorporation

%prep
rm -rf %name-%version
mkdir %name-%version
%gsession.prep -d %name-%version
# This line works for cbe 0.18 only
cd %{name}-%{version}/gnome-session-%{gsession.version} 
%patch1 -p1
%patch2 -p1
%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export MSGFMT="/usr/bin/msgfmt"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export LDFLAGS="-L/usr/X11/lib -R/usr/X11/lib -L/usr/sfw/lib -R/usr/sfw/lib"
export CFLAGS="%optflags -I/usr/X11/include"
export RPM_OPT_FLAGS="$CFLAGS"

%gsession.build -d %name-%version

%install
%gsession.install -d %name-%version
install -d $RPM_BUILD_ROOT/usr/dt/config
install --mode=0755 %SOURCE1 $RPM_BUILD_ROOT/usr/dt/config
rm -Rf $RPM_BUILD_ROOT%{_sysconfdir}
rm -Rf $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_datadir}/gnome/mandatory.tsolsession
rm -Rf $RPM_BUILD_ROOT%{_datadir}/gnome/default.session
rm -Rf $RPM_BUILD_ROOT%{_datadir}/gnome/default.wm
rm -Rf $RPM_BUILD_ROOT%{_datadir}/locale
rm -Rf $RPM_BUILD_ROOT%{_datadir}/pixmaps
rm -Rf $RPM_BUILD_ROOT%{_datadir}/control-center-2.0
rm -Rf $RPM_BUILD_ROOT%{_bindir}/gnome-session
rm -Rf $RPM_BUILD_ROOT%{_bindir}/gnome-session-save
rm -Rf $RPM_BUILD_ROOT%{_bindir}/gnome-session-remove
rm -Rf $RPM_BUILD_ROOT%{_bindir}/gnome-session-properties
rm -Rf $RPM_BUILD_ROOT%{_bindir}/gnome-wm
rm -Rf $RPM_BUILD_ROOT%{_bindir}/gnome-smproxy
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash/flash.gif
rm -Rf $RPM_BUILD_ROOT%{_datadir}
rm -Rf $RPM_BUILD_ROOT%{_libdir}
rm -Rf $RPM_BUILD_ROOT/helpers

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):supported" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d gnome-session-%{gsession.version} README AUTHORS
%doc(bzip2) -d gnome-session-%{gsession.version} COPYING NEWS ChangeLog
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, other)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/tsoljds-xagent
%dir %attr (0755, root, bin) /usr/dt
%dir %attr (0755, root, bin) /usr/dt/config
/usr/dt/config/tsoljds-migration

%changelog
* Mon Sep 2008 - ghee.teo@sun.com
- Added new copyright format changes.
* Fri May 16 2008 - stephen.browne@sun.com
- remove conditional build

* Wed May 07 2008 - damien.carbery@sun.com
- Remove PERL5LIB setting as it is not necessary.

* Wed Jun 06 2007 - damien.carbery@sun.com
- %define with_hal to fix build.

* Fri Nov 03 2006 - ghee.teo@sun.com
- Updated SUNWtgnome-xagent-01-trusted-extensions.diff to work for 2.16

* Wed Jul 26 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-desktop-prefs/-devel for gnome-settings-daemon.

* Wed Jul 26 2006 - damien.carbery@sun.com
- Use 'version' number from gnome-session.spec instead of hard coding here.

* Thu Jul 13 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-panel/-devel for gnome-desktop.

* Mon Jun 26 2006 - takao.fujiwara@sun.com
- Add tsoljds-migration
- Update SUNWtgnome-xagent-01-trusted-extensions.diff to add tsoljds-migration
  Fixes 6439165.

* Wed May 24 2006 - stephen.browne@sun.com
- shorten summary

* Thu 16 Mar 2006 - ghee.teo@sun.com
- Move mandatory.tsolsession to SUNWgnome-session spec file.

*Fri 03 Mar 2006 - ghee.teo@sun.com
- Make this build for cbe 0.18.

* Wed 22 feb 2006  - ghee.teo@sun.com
- Version which is based on SUNWgnome-session.spec.
  Remove all files which are not required by this module.



