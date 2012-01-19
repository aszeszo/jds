#
# spec file for package SUNWtgnome-tsoljdsselmgr
#
# Copyright (c) 2005 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner stephen

%define OSR 6160:n/a

# NOTE: If the version is bumped the new tarball must be uploaded to the
#       Sun Download Center. Contact GNOME RE for assistance.
%define tsoljdsselmgr_version 0.6.2

%include Solaris.inc

Name:                    SUNWtgnome-tsoljdsselmgr
IPS_package_name:        gnome/trusted/selection-manager
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Trusted Extensions
Summary:                 GNOME Trusted Extensions Selection Manager
License:                 cr_Oracle
Version:                 %{tsoljdsselmgr_version}
Source:			 http://dlc.sun.com/osol/jds/downloads/extras/tjds/tsoljdsselmgr-%{tsoljdsselmgr_version}.tar.bz2
# date:2008-07-10 owner:dcarbery type:bug
Patch1:                  tsoljdsselmgr-01-gtk-disable-deprecated.diff
# date:2011-07-19 owner:stephen type:bug
Patch2:                  tsoljdsselmgr-02-au_close.diff
Source1:                 l10n-configure.sh
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWlibgnomecanvas-devel
BuildRequires: SUNWtsu
BuildRequires: SUNWtgnome-tsol-libs-devel
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWgnome-keyring
BuildRequires: SUNWlibgnome-keyring
BuildRequires: x11/trusted/libxtsol
Requires: SUNWlibgnomecanvas
Requires: SUNWtsu
Requires: SUNWtgnome-tsol-libs
Requires: SUNWgnome-component
Requires: SUNWgnome-config
Requires: SUNWgnome-libs
Requires: SUNWgnome-vfs

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n tsoljdsselmgr-%{tsoljdsselmgr_version}
%patch1 -p1
%patch2 -p1

%build
export ACLOCAL_FLAGS="-I /usr/share/aclocal"

libtoolize -f
intltoolize --copy --force --automake

bash -x %SOURCE1 --enable-copyright

aclocal $ACLOCAL_FLAGS
autoconf
autoheader
automake -acf

./configure --with-gnome-prefix=%{_prefix} \
            --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
	    --mandir=%{_mandir}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, other)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/tsoljdsselmgr
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/sel_config

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale

%changelog
* Thu Jul 10 2008 - damien.carbery@sun.com
- Add 01-gtk-disable-deprecated to get module to build with new gtk+ tarball.

* Fri May 16 2008 - stephen.browne@sun.com
- Uprev version, remove upstream patch, remove conditional build

* Thu May 08 2008 - takao.fujiwara@sun.com
- Add SUNWtgnome-tsoljdsselmgr-01-po.diff for cs.po
  Contributed l10n from Hana Zalska <Hana.Zalska@sun.com>

* Tue Mar 25 2008 - takao.fujiwara@sun.com
- Remove upstreamed scripts.

* Fri Mar 14 2008 - stephen.browne@sun.com
- update version point source at dlc.sun.com

* Wed Oct 17 2007 - stephen.browne@sun.com
- remove damiens patch.  Fix is now in source

* Wed Jul 25 2007 - damien.carbery@sun.com
- Add patch, 01-gtk-tooltips, to build with latest gtk+.

* Fri Sep 15 2006 - takao.fujiwara@sun.com
- Add *-10n package.

* Sun Jul 30 2006 - damien.carbery@sun.com
- Always use nightly tarballs as source.

* Wed Jul 19 2006 - damien.carbery@sun.com
- Update Build/BuildRequires after check-deps.pl run.

* Thu Jul 13 2006 - damien.carbery@sun.com
- Add %{_datadir}/locale to %files, a byproduct of intltool up-rev.

* Tue Jul 11 2006 - damien.carbery@sun.com
- Add autogen.sh commands to %prep to permit building from 'cvs co' tarballs.

* Wed May 24 2006 - stephen.browne@sun.com
- remove man page from files and shorten summary

* Wed Mar 29 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWtsu.

* Tue Jan 31 2006 - <stephen.browne@sun.com>
- created 



