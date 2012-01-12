#
# spec file for package seahorse
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         seahorse
License:      GPL v2, LGPL v2, FDL v1.1
Group:        System/GUI/GNOME
Version:      2.30.1
Release:      1
Distribution: Java Desktop System
Vendor:	      Gnome Community
Summary:      Seahorse
Source:       http://download.gnome.org/sources/%{name}/2.30/%{name}-%{version}.tar.bz2
%if %build_l10n
Source1:                 l10n-configure.sh
%endif

# date:2009-10-16 owner:jefftsai type:branding
Patch1:     seahorse-01-sun-ldap.diff
Patch2:     seahorse-02-libcryptui-l10n.diff
# date:2011-06-15 owner:jefftsai type:bug bugster:6772733 bugzilla:561331
Patch3:     seahorse-03-disable-im.diff

URL:          http://www.gnome.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%define gtk2_version 2.4.0
%define pkgconfig_version 0.15.0
%define gtk_doc_version 1.1

Requires: gtk2 >= %{gtk2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: gtk-doc >= %{gtk_doc_version}
BuildRequires: pkgconfig >= %{pkgconfig_version}

%description
Seahorse is a GNOME application for managing encryption keys. It also
integrates with nautilus, gedit and other places for encryption, decrption
and other operations.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi 
%else 
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif 
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1       
fi 

libtoolize --force
intltoolize -f -c --automake

%if %build_l10n
bash -x %SOURCE1 --enable-copyright
%endif

gnome-doc-prepare --force
aclocal -I /usr/share/aclocal -I m4
autoconf
autoheader
automake 

CFLAGS="$RPM_OPT_FLAGS -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include"	\
./configure --prefix=%{_prefix}			\
	    --sysconfdir=%{_sysconfdir}		\
	    --mandir=%{_mandir}			\
            --libexecdir=%{_libexecdir} 	\
            --enable-introspection=no
make  -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Jun 15 2011 - jeff.cai@oracle.com
- Add patch -03-disable-im to fix #6772733, #561331
* May 26 2010 - jeff.cai@sun.com
- Bump to 2.30.1
* Mar 31 2010 - jeff.cai@sun.com
- Bump to 2.30.0
* Mar 18 2010 - jeff.cai@sun.com
- Disable introspection to fix #15247
* Feb 23 2010 - jeff.cai@sun.com
- Bump to 2.29.91
* Feb 09 2010 - jeff.cai@sun.com
- Bump to 2.29.90
- Removed the patch -02-autostart-desktop, the trunk also not autostart
  seahorse, the patch not needed.
* Mon 18 2010 - christian.kelly@sun.com
- Bump 2.29.4.
* Dec 07 2009 - jeff.cai@sun.com
- Bump 2.29.3
- Removed patch -03-import-ssh since upstreamed
- Removed patch -02-disable-remote since gpg is enabled,
  this patch is not needed
- Removed patch -05-check-gpg2 since upstreamed
* Dec  3 2009 - christian.kelly@sun.com
- Bumo to 2.29.1.
* Nov 06 2009 - jeff.cia@sun.com
- Add patch -01-sun-ldap, a patch for sun ldap.
- Add patch -04-autostart-desktop, move the .desktop file
- Add patch -05-check-gpg2, check gpg2
* Oct 20 2009 - jeff.cai@sun.com
- Bump to 2.28.1
* Tue Sep 22 2009 - jeff.cai@sun.com
- Bump to 2.28.0
- Upstream patch -06-return-void
* Mon Sep 14 2009 - jeff.cai@sun.com
- Bump to 2.27.92
* Tue Aug 11 2009 - jeff.cai@sun.com
- Bump to 2.27.90
* Wed Jul 29 2009 - jeff.cai@sun.com
- Bump to 2.27.5
* Sun May 31 2009 - jeff.cai@sun.com
- Bump to 2.27.1
* Tue Apr 14 2009 - halton.huo@sun.com
- Bump to 2.26.1
* Mon Mar 16 2009 - jeff.cai@sun.com 
- Bump to 2.26.0
- Remove patch -04-disable-im, upstreamed.
* Tue Mar 03 2009 - jeff.cai@sun.com 
- Bump to 2.25.92
* Mon Feb 16 2009 - jeff.cai@sun.com
- Bump to 2.25.91
* Wed Feb 04 2009 - jeff.cai@sun.com
- Bump to 2.25.90
- Remove patch -05-libtasn1, not needed since the dependency
  is removed
* Mon Feb 02 2009 - jeff.cai@sun.com
- Add patch -05-libtasn1.diff, Fix #570171.
- Remove patch -01-input-passwd.diff, this bug is not 
  reproducible on 2.25.4
* Fri Jan 09 2009 - jeff.cai@sun.com
- Bump to 2.25.4
- Remove -05-ssh-upload.diff, upstreamed
- Remove -07-gp11object-slot.diff, not needed.
* Mon Dec 29 2008 - jeff.cai@sun.com
- Bump to 2.25.3
- Remove -03-a11y-hang, upstreamed.
- Remove -04-show-error, upstreamed.
- Remove -05-dialog-markup, upstreamed.
- Remove -08-progress-pos, upstreamed.
- Remove -09-key-name, upstreamed.
- Reorder the rest patches.
- Add patch -06-return-void, upstreamed.
- Add patch -07-gpobject-slot, fix bug #566031. 
  This is only a temporary solution for the build issue.
* Thu Nov 27 2008 - jeff.cai@sun.com
- Add -10-ssh-upload.diff to defer the destroy of swidget
  Fix #562413
* Tue Nov 20 2008 - jeff.cai@sun.com
- Add -09-key-name.diff to refresh key names if it changes.
  Fix #561641
* Tue Nov 19 2008 - jeff.cai@sun.com
- Add seahorse-08-progress-pos.diff to make the progress dialog
  not cover the password dialog.
* Tue Nov 18 2008 - takao.fujiwara@sun.com
- Add seahorse-07-disable-im.diff to disable input method in password.
* Wed Nov 04 2008 - jeff.cai@sun.com
- Add patch -06-import-ssh, need a better patch.
* Fri Oct 31 2008 - jeff.cai@sun.com
- Change the license tag.
* Thu Oct 30 2008 - jeff.cai@sun.com
- Add comment " not upgrade it before it goes to nevada"
* Thu Oct 30 2008 - jeff.cai@sun.com
- Add patch -04-show-error to fix #558491
- Add patch -05-dialog-markup to fix #558494
* Thu Oct 23 2008 - jeff.cai@sun.com
- Add patch -03-a11y-hang to fix #557537
* Wed Oct 22 2008 - jeff.cai@sun.com
- Bump to 2.24.1.
- Remove upstream patch -01-build-thread
- Add patch -01-input-password
- Add patch -02-disable-remote since solaris doesn't
  have PGP support
* Mon Sep 22 2008 - jeff.cai@sun.com
- Bump to 2.24.0.
- Add patch -01-build-thread
* Thu Sep 08 2008 - jeff.cai@sun.com
- Bump to 2.23.92.
* Thu Sep 02 2008 - christian.kelly@sun.com
- Bump to 2.23.91.
* Tue Aug 19 2008 - dave.lin@sun.com
- Bump to 2.23.90
* Tue Aug 05 2008 - damien.carbery@sun.com
- Bump to 2.23.6. Remove all patches as they are upstream.

* Wed Jul 23 2008 - jeff.cai@sun.com
- Add bug no.

* Mon Jul 21 2008 - jeff.cai@sun.com
- Initial Sun release
