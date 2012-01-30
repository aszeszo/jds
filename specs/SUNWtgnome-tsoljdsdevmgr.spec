#
# spec file for package SUNWtgnomedevmgr
#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner johnf

%include Solaris.inc

%define OSR 6160:n/a

# NOTE: If the version is bumped the new tarball must be uploaded to the
#       Sun Download Center. Contact GNOME RE for assistance.
%define devmgr_version 0.6.4

Name:                    SUNWtgnome-tsoljdsdevmgr
IPS_package_name:        gnome/trusted/device-manager
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Trusted Extensions
Summary:                 GNOME Trusted Device Manager
License:                 cr_Oracle
Version:                 %{devmgr_version}
Source:			 http://dlc.sun.com/osol/jds/downloads/extras/tjds/tsoljdsdevmgr-%{devmgr_version}.tar.bz2
Source1:                 l10n-configure.sh
# owner:johnf date:2009-03-09 type:bug
Patch1:                  tsoljdsdevmgr-01-dialog-crash.diff
Patch2:                  tsoljdsdevmgr-02-use-stock-icons.diff
Patch3:                  tsoljdsdevmgr-03-use-dev_alloc_h.diff
Patch4:                  tsoljdsdevmgr-04-wnck-api-fix.diff
Patch5:                  tsoljdsdevmgr-05-l10n-updates.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:		 %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include gnome-incorporation.inc
%include default-depend.inc
Requires: SUNWlibgnomecanvas
Requires: SUNWtsu
Requires: SUNWgnome-panel
Requires: SUNWtgnome-tsol-libs
BuildRequires: SUNWlibgnomecanvas-devel
BuildRequires: SUNWtsu
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWtgnome-tsol-libs-devel
BuildRequires: x11/trusted/libxtsol
BuildRequires: consolidation/desktop/desktop-incorporation

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n tsoljdsdevmgr-%{devmgr_version}

%patch1 -p1
%patch2
%patch3
%patch4 -p1
%patch5 -p1

%build
export ACLOCAL_FLAGS="-I /usr/share/aclocal"

libtoolize -f
intltoolize --copy --force --automake

aclocal $ACLOCAL_FLAGS
autoconf
autoheader
automake -acf

CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS" \
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
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_datadir}/locale
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/tsoljdsdevmgr

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale

%changelog
* Fri Aug 22 2008 - stephen.browne@sun.com
- Uprev version, remove upstream patches

* Tue Aug  5 2008 - takao.fujiwara@sun.com
- Add tsoljdsdevmgr-02-no-gettext.diff to avoid segv. Fixes 6727185.

* Thu Jul 10 2008 - damien.carbery@sun.com
- Add 01-gtk-disable-deprecated to get module to build with new gtk+ tarball.

* Fri May 16 2008 - stephen.browne@sun.com
- Uprev version, remove upstream patch, remove conditional build

* Thu May 08 2008 - takao.fujiwara@sun.com
- Add SUNWtgnome-tsoljdsdevmgr-01-po.diff for cs.po
  Contributed l10n from Hana Zalska <Hana.Zalska@sun.com>

* Tue Mar 25 2008 - takao.fujiwara@sun.com
- Remove upstreamed scripts.
- Remove upstreamed tsoljdsdevmgr-01-pwd-fns.diff

* Fri Mar 14 2008 - stephen.browne@sun.com
- update version. point source at dlc.sun.com

* Wed Sep 19 2007 - damien.carbery@sun.com
- Remove getpwuid_r patch, tsoljdsdevmgr-01-pwd-fns.diff, as they it is not
  needed from snv_73 on.

* Wed Aug 19 2007 - damien.carbery@sun.com
- Only apply the patch to sparc as x86 builds use the 4 param versions.

* Tue Aug 18 2007 - damien.carbery@sun.com
- Add patch tsoljdsdevmgr-01-pwd-fns.diff to use 5 param versions of some 
  password functions.

* Fri Sep 15 2006 - takao.fujiwara@sun.com
- Add *-10n package.

* Sun Jul 30 2006 - damien.carbery@sun.com
- Always use nightly tarballs as source.

* Thu Jul 13 2006 - damien.carbery@sun.com
- Add %{_datadir}/locale to %files, a byproduct of intltool up-rev.

* Tue Jul 11 2006 - damien.carbery@sun.com
- Add autogen.sh commands to %prep to permit building from 'cvs co' tarballs.

* Wed May 24 2006 - stephen.browne@sun.com
- remove man page from files and shorten summary

* Wed Mar 29 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWtgnome-tsol-libs/-devel.
- Add Build/Requires SUNWtsu.

* Wed Mar  8 2006 - damien.carbery@sun.com
- Add %dir %attr for %{_datadir} as %defattr is wrong for this dir.

* Tue Mar  7 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-panel/-devel, for libwnck.

* Sat Feb 25 2006 - <john.fischer@sun.com>
- created 



