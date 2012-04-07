#
# spec file for package brasero
#
# Copyright 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

%include l10n.inc
%include Solaris.inc

Name:           SUNWgnome-cd-burner
IPS_package_name: desktop/cd-burning/brasero
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
License:        GPL v2
Version:        2.30.3
Summary:        Gnome CD/DVD burner
Source:         http://ftp.gnome.org/pub/GNOME/sources/brasero/2.30/brasero-%{version}.tar.bz2
Source1:        l10n-configure.sh 
Source2:        brasero-po-sun-%{po_sun_version}.tar.bz2
#Source3:        %{name}-manpages-0.1.tar.gz
URL:            http://www.gnome.org/projects/brasero
SUNW_Basedir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# date:2009-05-27 owner:lin type:branding
Patch1:         brasero-01-libtool.diff
# date:2011-03-16 type:bug owner:davelam
# bugzilla:639732
Patch2:         brasero-02-require-ice.diff
# date:2011-04-15 type:branding owner:gheet bugster:7028711
Patch3:		brasero-03-fix-menu.diff
# date:2011-04-15 type:branding owner:lin bugster:6988688,7042121
Patch4:		brasero-04-tmpdir.diff

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: library/desktop/gtk2
BuildRequires: library/audio/gstreamer
BuildRequires: library/media-player/totem-pl-parser
BuildRequires: library/libxml2
BuildRequires: system/library/dbus
#BuildRequires: system/hal
BuildRequires: service/hal
BuildRequires: developer/gnome/gnome-doc-utils
BuildRequires: library/desktop/xdg/libcanberra
BuildRequires: crypto/gnupg
Requires: library/desktop/gtk2
Requires: service/gnome/desktop-cache
Requires: system/library/dbus
Requires: library/audio/gstreamer
Requires: library/media-player/totem-pl-parser
Requires: library/libxml2
#Requires: system/hal
Requires: service/hal
Requires: desktop/gksu
Requires: gnome/file-manager/nautilus

%description
Brasero is a application to burn CD/DVD for the Gnome Desktop. It is designed to be as simple as possible and has some unique features to enable users to create their discs easily and quickly.

%package devel
Summary:                 %summary - developer files
SUNW_BaseDir:            %{_basedir}

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%package l10n
Summary: %{summary} - l10n files

%prep
%setup -q -n brasero-%{version}

#gzcat %SOURCE3 | tar -xf -

bzcat %SOURCE2 | tar xf -
cd po-sun; make; cd ..

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

find . -name "*.[ch]" -exec dos2unix -ascii {} {} \;

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

intltoolize --copy --force --automake
sh %SOURCE1 --enable-copyright
libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f 
autoconf

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
    --libdir=%{_libdir}		\
    --libexecdir=%{_libexecdir}	\
    --sysconfdir=%{_sysconfdir}	\
    --disable-inotify		\
    --enable-shared		\
    --disable-static		\
    --disable-scrollkeeper	\
    --disable-gtk-doc		\
    --disable-cdrkit

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_libdir}/nautilus
#cd sun-manpages
#make install DESTDIR=$RPM_BUILD_ROOT

# RBAC related
mkdir -p $RPM_BUILD_ROOT/etc/security/exec_attr.d

# exec_attr(4)
cat >> $RPM_BUILD_ROOT/etc/security/exec_attr.d/desktop-cd-burning-brasero <<EOF
Desktop Removable Media User:solaris:cmd:RO::/usr/bin/brasero:privs=sys_devices
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri icon-cache desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%doc README AUTHORS
%doc(bzip2) ChangeLog NEWS COPYING
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%attr (0755, root, bin)%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, bin) %{_libdir}/brasero
%dir %attr (0755, root, bin) %{_libdir}/brasero/plugins
%{_libdir}/brasero/plugins/lib*.so
# %{_libdir}/nautilus/extensions-2.0/*.so
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr(0755, root, bin) %{_datadir}/brasero
%{_datadir}/brasero/*
%dir %attr(0755, root, bin) %{_datadir}/omf
%{_datadir}/omf/*
%dir %attr(0755, root, root) %{_datadir}/mime
%dir %attr(0755, root, root) %{_datadir}/mime/packages
%{_datadir}/mime/packages/*
%dir %attr(0755, root, other) %{_datadir}/icons
%attr(-, root, other) %{_datadir}/icons/*
%dir %attr(0755, root, other) %{_datadir}/gnome
%dir %attr(0755, root, bin) %{_datadir}/gnome/help
%{_datadir}/gnome/help/*
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%{_datadir}/gir-1.0/Brasero*-1.0.gir
%{_libdir}/girepository-1.0/Brasero*-1.0.typelib

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%files root
%defattr (0755, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/brasero.schemas
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %attr (0444, root, sys) /etc/security/exec_attr.d/*

%files l10n
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/locale
%attr(-, root, other) %{_datadir}/locale/*

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Tue Apr 19 2011 - lin.ma@oracle.com
- Fixed 6988688.
* Wed Apr 06 2011 - brian.cameron@oracle.com
- Add "RO" to exec_attr config.
* Tue Sep 28 2010 - lin.ma@sun.com
- Bump to 2.30.3(doo16845)
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Mon Mar  1 2010 - christian.kelly@sun.com
- Bump to 2.29.91.
* Sun Feb 14 2010 - christian.kelly@sun.com
- Bump to 2.29.90.
* Mon Feb  1 2010 - christian.kelly@sun.com
- Bump to 2.29.6.
* Sun Jan 17 2010 - christian.kelly@sun.com
- Bump to 2.29.4.
* Sun Jan 17 2010 - christian.kelly@sun.com
- Comment out manpages which are missing.
* Fri Jan 15 2009 - lin.ma@sun.com
- Move the definition of 'Desktop Removable Media User' from here
  to SUNWgnome-media - doo 13911.
* Mon Nov 16 2009 - lin.ma@sun.com
- Move manpage patch to manpages-roff
- Update patch2 for 12650
* Wed Oct 21 2009 - dave.lin@sun.com
- Bump to 2.28.2
* Wed Oct 14 2009 - dave.lin@sun.com
- Bump to 2.28.1
* Wed Sep 23 2009 - dave.lin@sun.com
- Bump to 2.28.0
* Wed Sep 16 2009 - lin.ma@sun.com
- Bump to 2.27.92 and remove upstreamed patch.
* Thu Aug 27 2009 - lin.ma@sun.com
- Bump to 2.27.91 and update patches.
* Fri Aug 21 2009 - lin.ma@sun.com
- Disable nautilus extension because normal uses cant obtain privileges.
* Fri Aug 14 2009 - lin.ma@sun.com
- Bump to 2.27.90, updated patch3 which has been upstreamed,
- could be removed in the next version.
* Mon Jun 29 2009 - lin.ma@sun.com
- Add patch for doo:9673
* Tue Jun 16 2009 - christian.kelly@sun.com
- Bump to 2.27.3.
* Tue Jun 02 2009 - dave.lin@sun.com
- fixed dependency issue(CR6843581).
* Mon Jun 01 2009 - lin.ma@sun.com
- Bump to 2.27.2
* Sat Map 30 2009 - lin.ma@sun.com
- Bump to 2.26.2
- removed patches/brasero-02-src-data.diff.
- Updated and reordered gksu related patch.
* Tue Apr 22 2009 - lin.ma@sun.com
- Updated gksu related patch, and fixed a nit of spec.
* Tue Apr 21 2009 - lin.ma@sun.com
- Added gksu related patch.
- Added dependency for gksu.
- Changed profile name.
* Tue Apr 14 2009 - brian.cameron@sun.com
- Bump to 2.26.1.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Tue Mar 17 2009 - dave.lin@sun.com
- Bump to 2.26.0.
* Wed Mar 11 2009 - lin.ma@sun.com
- Create and new profile 'Desktop CD User' and 'Console User'.
- Removed file_dac_read, because console user owns the device.
* Tue Mar 03 2009 - lin.ma@sun.com
- Removed run-time dependency SUNWgksu, renamed to SUNWgnome-cd-burner.
- Restored removed patch 02-src-data.diff, because it's partly upstreamed.
* Mon Mar 02 2009 - dave.lin@sun.com
- Bump to 2.25.92.
- Removed upstreamed patch 02-src-data.diff.
* Tue Feb 24 2009 - lin.ma@sun.com
- Bump to 2.25.91.2 Add brasero-02-src-data.diff, add RBAC stuff.
* Tue Feb 17 2009 - brian.cameron@sun.com
- Bump to 2.25.91.  Remove upstream patch brasero-04-po.diff.
* Tue Feb 10 2009 - halton.huo@sun.com
- Add dependency on SUNWgnome-media-player, CR #6755918
* Fri Jan 16 2009 - takao.fujiwara@sun.com
- Add l10n tarball.
* Fri Jan 09 2009 - takao.fujiwara@sun.com
- Add patch po.diff from community trunk.
* Wed Sep 18 2008 - lin.ma@sun.com
- Bump to 0.8.2. Update copyright.
* Mon Sep 15 2008 - takao.fujiwara@sun.com
- Add brasero-03-g11n-im-jacket.diff to enable IM for jacket editor.
* Mon Aug 18 2008 - lin.ma@sun.com
- Initial version.

