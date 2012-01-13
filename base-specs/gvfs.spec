#
# spec file for package gvfs
#
# Copyright (c) 2007, 2011 Oracle and/or its affiliates. All Rights Reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         gvfs
License:      LGPLv2
Group:        System/Libraries/GNOME
Version:      1.6.7
Release:      1
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      Virtual File System Library for GNOME
Source:       http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.6/%{name}-%{version}.tar.bz2
URL:          http://www.gnome.org/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:	      %{_defaultdocdir}/doc
Autoreqprov:  on
#owner:yippi date:2008-04-28 type:branding 
# Note this patch is needed until HAL 0.5.10 is available on Solaris.
Patch1:       gvfs-01-hal-version.diff
#owner:padraig date:2008-04-28 type:feature bugster:6664678 bugzilla:526902
Patch2:       gvfs-02-enable-cdda-without-cdio.diff
#owner:jefftsai date:2009-08-07 type:bug doo:4915 bugzilla:567664
Patch3:       gvfs-03-unmount-webdav.diff
#owner:gheet date:2009-04-16 type:bug doo:7996
Patch4:	      gvfs-04-smb-browse-anon.diff
#owner:gheet date:2009-05-12 type:bug bugzilla:581711
Patch5:       gvfs-05-tmp-dir.diff
#owner:gheet date:2009-07-23 type:bug doo:10235
Patch6:       gvfs-06-void-return.diff
#owner:gheet date:2010-02-11 type:bug doo:13755
Patch7:       gvfs-07-init-dbus-error.diff
#owner:padraig date:2010-03-26 type:feature doo:15345
Patch8:       gvfs-08-trash-no-mounts-monitor.diff
#owner:padraig date:2011-11-24 type:bug bugster:6859847 bugzilla:551339
Patch9:       gvfs-09-dav-copy-dir.diff
#owner:padraig date:2011-12-05 type:bug bugster:6982200 bugzilla:579276
Patch10:      gvfs-10-dav-rename.diff

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

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

#autoreconf --force --install
libtoolize --force 
aclocal $ACLOCAL_FLAGS
autoconf
CFLAGS="$RPM_OPT_FLAGS -DDBUS_API_SUBJECT_TO_CHANGE=1"	\
./configure --prefix=%{_prefix}		\
            --sysconfdir=%{_sysconfdir} \
            --libexecdir=%{_libexecdir} \
            %{gtk_doc_option}
make -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Dec 05 2011 - padraig.obriain@oracle.com
- Add patch gvfs-10-dav-rename.diff to fix CR 6982200
* Thu Nov 24 2011 - padraig.obriain@oracle.com
- Add patch gvfs-09-dav-copy-dir.diff to fix CR 6859847
* Wed Jun 02 2010 - brian.cameron@oracle.com
- Bump to 1.6.2.
* Mon Apr 26 2010 - christian.kellt@oracle.com
- Bump to 1.6.1.
* Tue Mar 30 2010 - christian.kelly@sun.com
- Bump to 1.6.0.
* Fri Mar 26 2009 - padraig.obriain@sun.com
- Add patch 08-trash-no-mounts-monitor for d.o.o. 15345
* Thu Mar 11 2010 - christian.kelly@sun.com
- Bump to 1.5.5.
* Sun Feb 14 2010 - christian.kelly@sun.com
- Bump to 1.5.3.
* Mon Feb  1 2010 - christian.kelly@sun.com
- Bump to 1.5.2.
* Tue Oct 20 2009 - dave.lin@sun.com
- Bump to 1.4.1
* Wed Sep 23 2009 - dave.lin@sun.com
- Bump to 1.4.0
* Tue Sep 08 2009 - dave.lin@sun.com
- Bump to 1.3.6
* Tue Aug 25 2009 - jeff.cai@sun.com
- Bump to 1.3.5.
- Remove patch -08-webdav-mount-failure since community has a new fix
* Tue Aug 11 2009 - christian.kelly@sun.com
- Bump to 1.3.4.
* Mon Aug 10 2009 - jeff.cai@sun.com
- Add patch -08-webdav-mount-failture to fix #589221
* Fri Aug 07 2009 - jeff.cai@sun.com
- Add patch -07-webdav-unmount to fix doo #4915 and bugzilla
  #567664
  Change the webdav backend to solve hang of Nautilus when unmounting
  the mount location.
* Fri Jul 31 2009 - christian.kelly@sun.com
- Bump to 1.3.3.
* Thu Jul 23 2009 - christian.kelly@sun.com
- Unbump to 1.3.1.
* Fri Jul 17 2009 - christian.kelly@sun.com
- Bump to 1.3.2.
* Tue Jun 16 2009 - christian.kelly@sun.com
- Bump to 1.3.1.
* Mon Jun 15 2009 - christian.kelly@sun.com
- Bump to 1.2.3.
* Wed Jun 03 2009 - harry.lu@sun.com
- Change patch owner from Jijun to Ghee.
* Feb May 12 2009 - jijun.yu@sun.com
- Added patch5.
* Thu Apr 16 2009 - ghee.teo@sun.com
- added gvfs-04-smb-browse-anon.diff to allow anonymous login by default.
  doo#7996.
* Wed Apr 15 2009 - dave.lin@sun.com
- Bump to 1.2.2
* Mon Mar 23 2009 - ghee.teo@sun.com
- added gvfs-03-debug-crash.diff to stop crashing when default workgroup is nul.
* Tue Mar 17 2009 - dave.lin@sun.com
- Bump to 1.2.0
* Fri Mar 13 2009 - dave.lin@sun.com
- Bump to 1.1.8
* Tue Mar 03 2009 - ghee.teo@sun.com
Removed gvfs-03-trash-only-home.diff as it is not required based on the current
behaviour. Files from different file system are copied to trash directory.
* Tue Feb 17 2009 - dave.lin@sun.com
- Bump to 1.1.6
* Tue Feb 02 2009 - christian.kelly@sun.com
- Bump to 1.1.5.
* Wed Jan 07 2009 - christian.kelly@sun.com
- Bump to 1.1.3.
* Fri Jan 01 2009 - padraig.obriain@sun.com
- Comment out gvfs-03-trash-only-home.diff. Must determine whether the
  patch needs to be reworked.
* Sat Dec 27 2008 - dave.lin@sun.com
- Bump to 1.1.2.
* Wed Dec 03 2008 - dave.lin@sun.com
- Bump to 1.1.1
* Sat Sep 27 2008 - christian.kelly@sun.com
- Bump to 1.0.1.
* Sun Sep 21 2008 - christian.kelly@sun.com
- Bump to 0.99.8.
- Remove patch gvfs-03-trash-only-home.diff.
* Wed Sep 10 2008 - christian.kelly@sun.com
- Bump to 0.99.7.1.
* Tue Sep 02 2008 - christian.kelly@sun.com
- Bump to 0.99.6.
* Tue Aug 19 2008 - dave.lin@sun.com
- Bump to 0.99.5
* Thu Aug 14 2008 - padraig.obriain@sun.com
- Add patch -trash-only-home to avoid stat'ing Trash directories on Unix
  mounts.
* Wed Aug 06 2008 - christian.kelly@sun.com
- Bump to 0.99.4.
- Remove patch 03-trash-only-home, fixed upstream bugzilla:525779
- Rename patch 04 to 03
- Rework patch 02
* Thu Jul 24 2008 - damien.carbery@sun.com
- Bump to 0.99.3.
* Tue Jul 22 2008 - damien.carbery@sun.com
- Bump to 0.99.2.
* Fri Jul 04 2008 - padraig.obriain@sun.com
- Add patch 04-smb-mount to fix CR 6715607
* Wed Jun 25 2008 - padraig.obriain@sun.com
- Add patch -trash-only-home to avoid stat'ing Trash directory on mounted filesystems
* Wed Jun 04 2008 - damien.carbery@sun.com
- Bump to 0.99.1.
* Tue May 27 2008 - damien.carbery@sun.com
- Bump to 0.2.4.
* Mon Apr 28 2008 - padraig.obriain@sun.com
- Add patch -enable-cdda-without-cdio to enable cdda backend without libcdio.
* Wed Apr 08 2008 - damien.carbery@sun.com
- Bump to 0.2.3.
* Mon Mar 31 2008 - damien.carbery@sun.com
- Bump to 0.2.2.
* Thu Mar 27 2008 - damien.carbery@sun.com
- Bump to 0.2.1.
* Wed Mar 05 2008 - damien.carbery@sun.com
- Bump to 0.1.11.
* Mon Mar 03 2008 - alvaro.lopez@sun.com
- Added gvfs-01-hal-version.diff
* Thu Feb 28 2008 - damien.carbery@sun.com
- Bump to 0.1.8.
* Sat Nov 17 2007 - daymobrew@users.sourceforge.net
- Bump to 0.0.2. Remove upstream patches, 01-solaris and 02-solaris2.
* Fri Nov 09 2007 - daymobrew@users.sourceforge.net
- Add patch 02-solaris2 to include header files to fix 'implicit function
  declaration' warnings.

* Wed Nov 07 2007 - daymobrew@users.sourceforge.net
- Initial version.
