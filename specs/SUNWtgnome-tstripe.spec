#
# spec file for package SUNWtgnome-tstripe
#Copyright (c) 2010, 2012 Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner stephen

%define OSR 6160:n/a

%include Solaris.inc

# NOTE: If the version is bumped the new tarball must be uploaded to the
#       Sun Download Center. Contact GNOME RE for assistance.
%define tstripe_version 0.6.8

Name:                    SUNWtgnome-tstripe
IPS_package_name:        gnome/trusted/trusted-stripe
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Trusted Extensions
Summary:                 GNOME Trusted Stripe
License:                 cr_Oracle
Version:                 %{tstripe_version}
Source:			 http://dlc.sun.com/osol/jds/downloads/extras/tjds/tsoljds-tstripe-%{tstripe_version}.tar.bz2
Patch1:			 tsoljds-tstripe-01-dont-set-DISPLAY.diff
Patch2:			 tsoljds-tstripe-02-TPEXEC.diff
Patch3:                  tsoljds-tstripe-03-pfexec.diff
Patch4:                  tsoljds-tstripe-04-l10n-updates.diff
Patch5:                  tsoljds-tstripe-05-primary-zone.diff
Source1:                 l10n-configure.sh
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:		 %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: library/desktop/libgnomecanvas
BuildRequires: gnome/gnome-panel
BuildRequires: gnome/trusted/libgnometsol
BuildRequires: library/gnome/gnome-keyring
BuildRequires: x11/trusted/libxtsol

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n tsoljds-tstripe-%{tstripe_version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1

%build
export ACLOCAL_FLAGS="-I /usr/share/aclocal"

libtoolize -f
intltoolize -c -f --automake

bash -x %SOURCE1 --enable-copyright

aclocal $ACLOCAL_FLAGS
autoconf
autoheader
automake -acf

CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS" \
./configure --with-gnome-prefix=%{_prefix} \
            --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
	    --mandir=%{_mandir}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT/%{_datadir}/gnome
mkdir -p trusted/applications
cd trusted/applications
ln -sf ../../../applications/at-properties.desktop .
ln -sf ../../../applications/display-properties.desktop .
ln -sf ../../../applications/window-properties.desktop .
ln -sf ../../../applications/keyboard.desktop .
ln -sf ../../../applications/keybinding.desktop .
ln -sf ../../../applications/gnome-settings-mouse.desktop .
ln -sf ../../../applications/gnome-appearance-properties.desktop .
ln -sf ../../../applications/alacarte.desktop .
ln -sf ../../../applications/iiim-properties.desktop .
ln -sf ../../../applications/gnome-power-preferences.desktop .
ln -sf ../../../applications/gnome-power-statistics.desktop .
ln -sf ../../../applications/time-slider.desktop .
ln -sf ../../../applications/at-properties.desktop .
ln -sf ../../../applications/imf-selector.desktop .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, other)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/tsoljds-tstripe
%{_bindir}/tsoljds-setssheight
%{_bindir}/tsoljds-xagent-proxy
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/TrustedPathExecutables
%{_datadir}/gnome/gtkrc.tjds
%dir %attr (0755, root, other) %{_datadir}/gnome/trusted
%dir %attr (0755, root, other) %{_datadir}/gnome/trusted/applications
%{_datadir}/gnome/trusted/applications/*

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale

%changelog
* Thu Apr 19 2012 - stephen.browne@oracle.com
- Add patch  tsoljds-tstripe-05-primary-zone.diff to make sure we only try
  to lazy boot primary zones

* Wed Mar 09 2011 - brian.cameron@oracle.com
- Add patch tsoljds-tstripe-03-pfexec.diff so that the proxy always calls
  tsoljds-xagent with pfexec.

* Wed Mar 09 2011 - brian.cameron@oracle.com
- Add code to remove l10n if %build_l10n is not true.

* Tue Mar 01 2011 - stephen.browne@oracle.com
- add TPEXEC desktop symlinks and update TPEXECS 

* Wed Jul 28 2010 - stephen.browne@oracle.com
- uprev version, update copyright, remove upstream patches

* Thu Jul 07 2008 - stephen.browne@sun.com
- Uprev version, remove updtream patch

* Fri May 16 2008 - stephen.browne@sun.com
- Uprev version, remove upstream patches, remove conditional build

* Thu May 08 2008 - takao.fujiwara@sun.com
- Add SUNWtgnome-tstripe-02-po.diff for cs.po
  Contributed l10n from Hana Zalska <Hana.Zalska@sun.com>

* Tue Mar 25 2008 - takao.fujiwara@sun.com
- Removed upstreamed scripts.
- Removed upstreamed tsoljds-tstripe-01-pwd-fns.diff

* Tue Mar 25 2008 - damien.carbery@sun.com
- Revert to 0.1.5 because 0.6 tarball missing po dir and breaking build.

* Fri Mar 14 2008 - stephen.browne@sun.com
- update version. point source at dlc.sun.com

* Wed Sep 19 2007 - stephen.browne@sun.com
- Add two new binaries to match the new tarball

* Wed Sep 19 2007 - damien.carbery@sun.com
- Remove getpwuid_r patch, tsoljds-tstripe-01-pwd-fns.diff, as they it is not
  needed from snv_73 on.

* Tue Aug 14 2007 - damien.carbery@sun.com
- Add patch tsoljds-tstripe-01-pwd-fns.diff to use the correct versions of the
  password functions. The issue only

* Tue Mar 27 2007 - damien.carbery@sun.com
- Remove instances of mkinstalldirs as it is not needed and the mkinstalldirs
  file has been removed from the svn repository.

* Tue Jan 20 2007 - stephen.browne@sun.com
- Added new configuration file to %files section

* Tue Oct 17 2006 - damien.carbery@sun.com
- Add '-lnsl' to LDFLAGS to fix build.

* Tue Oct 17 2006 - damien.carbery@sun.com
- Add 'make' to the %build section as only having 'make install' was populating
  $RPM_BUILD_ROOT even when the package failed.

* Fri Sep 15 2006 - takao.fujiwara@sun.com
- Add *-10n package.

* Sun Jul 30 2006 - damien.carbery@sun.com
- Always use nightly tarballs as source.

* Tue Jul 11 2006 - damien.carbery@sun.com
- Add autogen.sh commands to %prep to permit building from 'cvs co' tarballs.

* Wed May 24 2006 - stephen.browne@sun.com
- remove man page from files and shorten summary

* Wed Mar  8 2006 - damien.carbery@sun.com
- Add %dir %attr for %{_datadir} as %defattr is wrong for this dir.

* Mon Mar  6 2006 - Damien Carbery <damien.carbery@sun.com>
- Added Build/BuildRequires for SUNWtgnome-tsol-libs/-devel.

* Thu Mar  2 2006 - Damien Carbery <damien.carbery@sun.com>
- Added Build/BuildRequires for SUNWgnome-panel/-devel.

* Tue Feb 14 2006 - <ghee.teo@sun.com>
- Added Build/BuildRequires for SUNWgnome-base-libs/-devel.

* Fri Jan 27 2006 - <stephen.browne@sun.com>
- Erwann moved tsolmetacity changes back to base metacity so renamed this file
- and make it only build the stripe now

* Mon Oct 03 2005 - <stephen.browne@sun.com>
- added trusted stripe

* Fri Aug 19 2005 - <stephen.browne@sun.com>
- moved patch to base metacity spec file
- edited references to not pass in build dir - must be used with Laca's relative
- path pkgbuild patch

* Wed Aug 17 2005 - <stephen.browne@sun.com>
- created 



