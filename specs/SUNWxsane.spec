#
# spec file for package SUNWxsane
#
# includes module(s): xsane
#
# Copyright (c) 2009, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc

%define OSR 5667:1.x

Name:                    SUNWxsane
Summary:                 Graphical scanning frontend for the SANE scanner interface.
License:                 GPL v2
Version:                 0.997
URL:                     http://www.xsane.org/
Source:                  http://www.xsane.org/download/xsane-%{version}.tar.gz
# date:2007-02-25 owner:jefftsai type:feature
Patch1:                  xsane-01-gettext.diff
# date:2007-07-01 owner:jefftsai type:feature
Patch2:                  xsane-02-doc.diff
# date:2008-12-30 owner:jefftsai type:bug bugster:6765509
Patch3:                  xsane-03-keyboard.diff
# date:2007-08-04 owner:jefftsai type:feature
Patch4:                  xsane-04-manpage.diff
# date:2007-08-15 owner:jefftsai type:feature
Patch5:                  xsane-05-tiff-jpegcompress.diff
SUNW_Pkg:                SUNWxsane
IPS_package_name:        image/scanner/xsane
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include desktop-incorporation.inc
%include default-depend.inc
Requires: SUNWgtk2
Requires: SUNWfontconfig
Requires: SUNWfreetype2
Requires: library/lcms
Requires: SUNWlexpt
Requires: SUNWlibexif
Requires: SUNWlibms
Requires: SUNWlibusb
BuildRequires: library/libtool/libltdl
BuildRequires: SUNWmlib
Requires: SUNWzlib
Requires: SUNWTiff
Requires: SUNWjpg
Requires: SUNWpng
Requires: SUNWgnome-camera
Requires: SUNWgnome-img-editor
Requires: image/scanner/xsane/sane-backends
BuildRequires: SUNWxwplt
BuildRequires: SUNWxwrtl
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWTiff-devel
BuildRequires: SUNWjpg-devel
BuildRequires: SUNWpng-devel
BuildRequires: SUNWgnome-camera-devel
BuildRequires: SUNWgnome-img-editor-devel
BuildRequires: image/scanner/xsane/sane-backends

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n xsane-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
# /usr/sfw needed for libusb
export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib"
	    		
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

aclocal -I m4
libtoolize --force
glib-gettextize --force
autoconf -f
cp /usr/share/automake-1.11/config.{guess,sub} .
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}
make -j$CPUS RANLIB=/usr/ccs/bin/ranlib

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT MKINSTALLDIRS=`pwd`/mkinstalldirs
rmdir $RPM_BUILD_ROOT%{_sbindir}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

#Create a link to xsane binary for gimp plugin
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins
chmod -R 755 $RPM_BUILD_ROOT%{_libdir}/gimp
cd $RPM_BUILD_ROOT%{_libdir}/gimp/2.0/plug-ins
ln -s ../../../../bin/xsane

# Rename zh dir to zh_TW dir as the contents of zh.po is in fact for zh_TW
# and zh is a symlink to zh_CN.
cd $RPM_BUILD_ROOT%{_datadir}/locale
mv zh zh_TW

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%doc xsane.AUTHOR
%doc(bzip2) xsane.COPYING xsane.NEWS xsane.CHANGES intl/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (-, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (-, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%{_datadir}/sane
%{_libdir}/gimp/2.0/plug-ins/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Thu Sep 10 2009 - halton.huo@sun.com
- Bump to Bump to 0.997
* Tue Dec 30 2008 - halton.huo@sun.com
- Add patch keyboard.diff to fix CR #6765509
* Tue Sep 23 2008 - simon.zheng@sun.com
- Bump to 0.996. Remove upstream patch 03-desktopfile.diff.
* Fri Aug 15 2008 - simon.zheng@sun.com
- Add 05-tiff-jpegcompress.diff to fix bugster bug #6728809. 
* Mon Aug 11 2008 - harry.fu@sun.com
- Change zh dir to zh_TW dir for #6735224
* Mon Aug 04 2008 - simon.zheng@sun.com
- Add patch 04-manpage.diff
* Tue Jul 01 2008 - simon.zheng@sun.com
- Add patch 02-doc.diff, 03-desktopfile.diff.
* Mon Jun 23 2008 - damien.carbery@sun.com
- Update Build/Requires after 'ldd xsane'. Make gimp symlink a relative one
  because absolute symlinks are not permitted in Solaris.
* Sun Jun 22 2008 - simon.zheng@sun.com
- Clean up and move spec file from 
  spec-files-extra to spec-files-other/core.
* Sun Mar 02 2008 - simon.zheng@sun.com
- Correct package version numbers.
* Wed Oct 17 2007 - laca@sun.com
- add /usr/gnu to CFLAGS/LDFLAGS
* Mon Apr 02 2007 - daymobrew@users.sourceforge.net
- Rename zh dir to zh_CN in %install as zh a symlink to zh_CN and causing
  installation problems as a dir.
* Tue Mar 20 2007 - simon.zheng@sun.com
- Split into 2 files, SFExsane.spec and 
  linux-specs/xsane.spec.
* Wed Mar  7 2007 - simon.zheng@sun.com
- Bump to version 0.994
- Modify %file to enable gimp-plugin
* Sun Nov  5 2006 - laca@sun.com
- Create



