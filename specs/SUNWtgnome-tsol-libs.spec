#
# spec file for package SUNWtgnome-tsol-libs
#
# includes module(s): libgnometsol
#
# Copyright (c) 2005 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner stephen

%define OSR 6160:n/a

# NOTE: If the version is bumped the new tarball must be uploaded to the
#       Sun Download Center. Contact GNOME RE for assistance.
%define libgnometsol_version 0.6.2

%include Solaris.inc

Name:                    SUNWtgnome-tsol-libs
IPS_package_name:        gnome/trusted/libgnometsol
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Trusted Extensions
Summary:                 GNOME Trusted Extensions Libraries - platform dependent
License:                 cr_Oracle
Version:                 %{libgnometsol_version}
Source:			 http://dlc.sun.com/osol/jds/downloads/extras/tjds/libgnometsol-%{libgnometsol_version}.tar.bz2
Source1:                 l10n-configure.sh
Patch1:			 libgnometsol-01-LB_CLI.diff
Patch2:			 libgnometsol-02-invalid-sl.diff
Patch3:			 libgnometsol-03-perzoneauth.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:	  	 %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWgtk2
Requires: SUNWgnome-libs
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWlibgnome-keyring
BuildRequires: x11/trusted/libxtsol
BuildRequires: consolidation/desktop/desktop-incorporation

%package l10n
Summary:                 %{summary} - l10n files
Requires: %{name}

%package devel
Summary:                 GNOME Trusted Extensions Libraries - platform independent
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWtgnome-tsol-libs

%prep
%setup -q -n libgnometsol-%{libgnometsol_version}
%patch1 
%patch2 
%patch3 -p1

%build
export ACLOCAL_FLAGS="-I /usr/share/aclocal"
export LDFLAGS="%_ldflags"

libtoolize -f
intltoolize --copy --force --automake

bash -x %SOURCE1 --enable-copyright

aclocal $ACLOCAL_FLAGS
autoconf
autoheader
automake -acf

./configure --with-gnome-prefix=%{_prefix} \
            --prefix=%{_prefix}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libgnometsol.la
rm $RPM_BUILD_ROOT%{_libdir}/libgnometsol.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, other)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libgnometsol.so*
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/tgnome-selectlabel

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale

%files devel
%defattr (-, root, other)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/pkgconfig

%changelog
* Tue Apr 20 2010 - christian.kelly@oracle.com
- Set LDFLAGS.
* Fri May 16 2008 - stephen.browne@sun.com
- Uprev version, remove upstream patch, remove conditional build

* Thu May 08 2008 - takao.fujiwara@sun.com
- Add SUNWtgnome-tsol-libs-01-po.diff for cs.po
  Contributed l10n from Hana Zalska <Hana.Zalska@sun.com>

* Tue Mar 25 2008 - takao.fujiwara@sun.com
- remove upstreamed scripts.

* Fri Mar 14 2008 - stephen.browne@sun.com
- update version. point source at dlc.sun.com

* Fri Sep 15 2006 - takao.fujiwara@sun.com
- Add *-10n package.

* Sun Jul 30 2006 - damien.carbery@sun.com
- Always use nightly tarballs as source.

* Wed Jul 19 2006 - damien.carbery@sun.com
- Update Build/BuildRequires after check-deps.pl run.

* Tue Jul 11 2006 - damien.carbery@sun.com
- Add autogen.sh commands to %prep to permit building from 'cvs co' tarballs.

* Fri Jun 30 2006 - <stephen.browne@sun.com>
- changed version to default for port to vermillion

* Tue Feb 14 2006 - <ghee.teo@sun.com>
- Added Build/BuildRequires for SUNWgnome-base-libs/-devel.

* Mon Feb 13 2006 - <ghee.teo@sun.com>
- Added Build/BuildRequires for SUNWxwts

* Thu Aug 25 2005 - <stephen.browne@sun.com>
- created 



