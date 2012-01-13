#
# spec file for package SUNWacroread
#
# includes module(s): acroread
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner dermot
#
# DO NOT REMOVE NEXT LINE
# PACKAGE NOT ARC REVIEWED BY SUN JDS TEAM
#
%include Solaris.inc
%define _prefix %{_basedir}
%define _bindir %{_prefix}/bin
%define _libdir %{_prefix}/lib


%ifarch sparc
%use acroread = acroread.spec
%else
%use acroread = acroread-x86.spec
%endif


Name:                    SUNWacroread
IPS_package_name:        desktop/pdf-viewer/acroread
Meta(info.classification): %{classification_prefix}:Applications/Office
Summary:                 Acrobat Reader for PDF files
Version:                 %{acroread.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Category:           MOZ17,application,%{jds_version}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          %{name}.copyright
License:                 %{acroread.license}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWmfrun
BuildRequires: SUNWxwplt
BuildRequires: SUNWlibms
Requires: SUNWdesktop-cache
Requires: SUNWglib2
Requires: SUNWgtk2
Requires: SUNWpango
Requires: SUNWcurl
Requires: SUNWlibatk
BuildRequires: SUNWgnome-component
BuildRequires: SUNWgnome-vfs


%package plugin
IPS_package_name:        desktop/pdf-viewer/acroread/plugin
Summary:                 Acrobat Reader Plugin for Firefox
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires: SUNWfirefox
Requires: SUNWfirefox
Requires: SUNWacroread


%prep
rm -rf %name-%version
mkdir %name-%version
%acroread.prep -d %name-%version


%install
%acroread.install -d %name-%version


%clean
rm -rf $RPM_BUILD_ROOT


%ifarch sparc
# ifarch for post/preun/files

%post
%restart_fmri icon-cache
# This is Yuk!  But it's needed as SVr4 pkgs cannot handle
# spaces in paths
PKGCOND=/usr/bin/pkgcond
is_srngz=99
is_ngz=99

if [ -x $PKGCOND ]; then
  $PKGCOND -v is_sparse_root_nonglobal_zone > /dev/null 2>&1
  is_srngz=$?
  $PKGCOND -v is_nonglobal_zone > /dev/null 2>&1
  is_ngz=$?
fi

## 'pkgcond' does not exist when you do live upgrade from S8/S9
## so in that case, use 'touch' instead for the testing
##
test_writable() {
  if [ $is_srngz -ne 99 ]; then
    $PKGCOND is_path_writable $1 && return $?
  else
    /usr/bin/touch $1/.test.$$ > /dev/null 2>&1
    if [ $? !=  0 ]; then
      return 1
    else
      rm -f  $1/.test.$$ > /dev/null 2>&1
      return 0
    fi
  fi
}

if test_writable ${BASEDIR}/lib/AdobeReader/Adobe/Help/en_US/; then
  if [ -h "${BASEDIR}/lib/AdobeReader/Adobe/Help/en_US/Adobe Reader" ]; then
    rm "${BASEDIR}/lib/AdobeReader/Adobe/Help/en_US/Adobe Reader"
  fi
  ln -s Adobe_Reader "${BASEDIR}/lib/AdobeReader/Adobe/Help/en_US/Adobe Reader"
fi

if test_writable ${BASEDIR}/lib/AdobeReader/Adobe/Help/ja_JP; then
  if [ -h "${BASEDIR}/lib/AdobeReader/Adobe/Help/ja_JP/Adobe Reader" ]; then
    rm "${BASEDIR}/lib/AdobeReader/Adobe/Help/ja_JP/Adobe Reader"
  fi
  ln -s Adobe_Reader "${BASEDIR}/lib/AdobeReader/Adobe/Help/ja_JP/Adobe Reader"
fi


%preun
PKGCOND=/usr/bin/pkgcond
is_srngz=99
is_ngz=99

if [ -x $PKGCOND ]; then
  $PKGCOND -v is_sparse_root_nonglobal_zone > /dev/null 2>&1
  is_srngz=$?
  $PKGCOND -v is_nonglobal_zone > /dev/null 2>&1
  is_ngz=$?
fi

## 'pkgcond' does not exist when you do live upgrade from S8/S9
## so in that case, use 'touch' instead for the testing
##
test_writable() {
  if [ $is_srngz -ne 99 ]; then
    $PKGCOND is_path_writable $1 && return $?
  else
    /usr/bin/touch $1/.test.$$ > /dev/null 2>&1
    if [ $? !=  0 ]; then
      return 1
    else
      rm -f  $1/.test.$$ > /dev/null 2>&1
      return 0
    fi
  fi
}

if [ -h "${BASEDIR}/lib/AdobeReader/Adobe/Help/en_US/Adobe Reader" ]; then
  if test_writable ${BASEDIR}/lib/AdobeReader/Adobe/Help/en_US/; then
    rm "${BASEDIR}/lib/AdobeReader/Adobe/Help/en_US/Adobe Reader"
  fi
fi

if [ -h "${BASEDIR}/lib/AdobeReader/Adobe/Help/ja_JP/Adobe Reader" ]; then
  if test_writable ${BASEDIR}/lib/AdobeReader/Adobe/Help/ja_JP; then
    rm "${BASEDIR}/lib/AdobeReader/Adobe/Help/ja_JP/Adobe Reader"
  fi
fi


%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/AdobeReader
%{_libdir}/AdobeReader/*
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_prefix}/sfw
%dir %attr (0755, root, bin) %{_prefix}/sfw/bin
%{_prefix}/sfw/bin/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*/apps
%attr (0644, root, bin) %{_datadir}/applications/acroread.desktop
%attr (-, root, other) %{_datadir}/icons/hicolor/*/apps/*


%else #ifarch else for post/preun/files

%post
%restart_fmri desktop-mime-cache icon-cache gconf-cache 


%preun
%restart_fmri desktop-mime-cache


%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/AdobeReader
%{_libdir}/AdobeReader/*
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*/apps
%{_datadir}/applications/acroread.desktop
%{_datadir}/icons/hicolor/*/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*/mimetypes
%attr (-, root, other) %{_datadir}/icons/hicolor/*/mimetypes/*
%dir %attr (0755, root, root) %{_datadir}/mime
%dir %attr (0755, root, root) %{_datadir}/mime/packages
%{_datadir}/mime/packages/acroread.xml
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

#ifarch endif for post/preun/files
%endif


%files plugin
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/firefox
%dir %attr (0755, root, bin) %{_libdir}/firefox/plugins
%{_libdir}/firefox/plugins/nppdf.so


%changelog
* Tue Jun 30 2009 - elaine.xiong@sun.com
- Add dependencies for SPARC version.
* Tue May 19 2009 - elaine.xiong@sun.com
- Add dependencies.
* Wed Apr 08 2009 - elaine.xiong@sun.com
- combine x86 pkg build into this spec-file.
  use desktop-cache instead of postrun.
* Wed May 26 2008 - dermot.mccluskey@sun.com
- fix typo in postinstall
* Mon May 26 2008 - dermot.mccluskey@sun.com
- add check for existing file in postinstall
* Fri Apr 25 2008 - dermot.mccluskey@sun.com
- re-do pre and post scripts for sparse zones
* Wed Apr 02 2008 - dermot.mccluskey@sun.com
- Updates for 8.1.2
* Wed Mar 12 2008 - dermot.mccluskey@sun.com
- modify %post and %preun to use BASEDIR
* Tue Jan 22 2008 - laca@sun.com
- use an include instead of an inline script
* Fri Jan 18 2008 - dermot.mccluskey@sun.com
- Updates for version 8.1.1
* Sun Nov 24 2006 - darren.kenny@sun.com
- Add .desktop and icons in appropriate places.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Mon May 22 2006 - laca@sun.com
- use product version number instead of "1.0"
* Wed May 10 2006 - dave.lin@sun.com
- move plugin file to /usr/lib/firefox/plugins since firefox changed the
  install location
* Thu Apr  6 2006 - damien.carbery@sun.com
- Add SUNWgnome-base-libs/-devel to Build/Requires after check-deps.pl run.
* Wed Nov 02 2005 - damien.carbery@sun.com
- Copy in v7 changes from JDS3.1 branch. Change mozilla references to firefox.
* Mon Oct 10 2005 - damien.carbery@sun.com
- Add %{_prefix}/sfw/bin to for backward compatability symlink. Fixes 6300634.
* Thu Aug 25 2005 - dermot.mccluskey@sun.com
- re-write for version 7 (new install dir, etc)
* Fri Nov 26 2004 - laca@sun.com
- Removed SUNWjds-integration dependency
* Fri Nov 19 2004 - damien.carbery@sun.com
- Partial fix for 6178971. Remove %pkgbuild_process because it was modifying
  the Adobe-tested binaries.
* Fri Nov 12 2004 - laca@sun.com
- Added SUNWjds-integration dependency
* Tue Oct 05 2004 - shirley.woo@sun.com
- CR 6174047 : Change SUNWacroread to install to /usr/sfw
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Thu Sep 30 2004 - damien.carbery@sun.com
- Add '%ifarch sparc' around SUNWbcp dependency as this is only on sparc.
* Wed Sep 29 2004 - shirley.woo@sun.com
- added additional dependencies to acroread &
  added acroread dependency to plugin subpkg
* Mon Sep 20 2004 - laca@sun.com
- added default dependencies to plugin subpkg
* Fri Aug 20 2004 - laca@sun.com
- moved to mozilla category.
* Mon Aug 16 2004 - dermot.mccluskey@sun.com
- added -plugin pkg
* Mon Aug 16 2004 - dermot.mccluskey@sun.com
- use acroread-copyright.txt instead of default
* Fri Aug 06 2004 - dermot.mccluskey@sun.com
- initial version


