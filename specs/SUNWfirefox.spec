#
# spec file for package SUNWfirefox
#
# includes module(s): firefox
#
# Copyright (c) 2005, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner ginnchen
#
# DO NOT REMOVE NEXT LINE
# PACKAGE NOT INCLUDED IN GNOME UMBRELLA ARC
#
%include Solaris.inc
%use firefox = firefox.spec

#####################################
##   Package Information Section   ##
#####################################

%define lang_list ar be bg ca cs da de el es-AR es-CL es-ES et fi fr he hi-IN hr hu id is it ja kk ko lt lv mk nb-NO nl nn-NO pl pt-BR pt-PT ro ru sk sl sq sr sv-SE th tr uk vi zh-CN zh-HK zh-TW 
%define l10n_version 10.0.2

Name:          SUNWfirefox
IPS_package_name: web/browser/firefox
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       Mozilla Firefox Web browser
Version:       %{firefox.version}
Source:        %{name}-manpages-0.1.tar.gz
Source1:       firefoxl10n-%{l10n_version}.tar.gz
SUNW_BaseDir:  %{_basedir}
SUNW_Category: FIREFOX,application,%{jds_version}
SUNW_Copyright:%{name}.copyright
License:       MOZILLA PUBLIC LICENSE V1.1
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

#####################################
##  Package Requirements Section   ##
#####################################

%include default-depend.inc
%include desktop-incorporation.inc
#Requires: system/library/c++-runtime
Requires: system/library/c++/sunpro
Requires: system/library/math
Requires: shell/bash
Requires: library/desktop/gtk2
BuildRequires: library/desktop/gtk2
BuildRequires: library/gnome/gnome-component
BuildRequires: system/header
Requires: system/library/fontconfig
Requires: system/library/freetype-2
Requires: gnome/config/gconf
BuildRequires: gnome/config/gconf
Requires: library/gnome/gnome-libs
BuildRequires: library/gnome/gnome-libs
Requires: library/gnome/gnome-vfs
BuildRequires: library/gnome/gnome-vfs
Requires: library/zlib
BuildRequires: library/zlib
Requires: codec/libtheora
BuildRequires: codec/libtheora
Requires: codec/ogg-vorbis
BuildRequires: codec/ogg-vorbis
Requires: database/sqlite-3
BuildRequires: database/sqlite-3
Requires: library/libnotify
BuildRequires: library/libnotify
Requires: system/library/libdbus-glib
BuildRequires: system/library/libdbus-glib
Requires: system/library/libdbus
BuildRequires: system/library/libdbus
Requires: library/libffi
BuildRequires: library/libffi
Requires: system/library/dbus
BuildRequires: system/library/dbus
BuildRequires: compress/zip
BuildRequires: archiver/gnu-tar
BuildRequires: compress/bzip2
#%if %option_with_indiana_branding
# comment this out until I can find where to get it 
# to install it on the build machines
#Requires: SUNWgetting-started-guide
#%endif
# %if %option_without_moz_nss_nspr
# Requires: library/nspr
# Requires: library/security/nss
# %endif
BuildRequires: x11/library/mesa
BuildRequires: x11/library/libxscrnsaver
Requires: system/font/truetype/dejavu

#####################################
##   Package Description Section   ##
#####################################

%package devel
Summary:       %{summary} - development files
SUNW_BaseDir:  %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:      %{name}

#####################################
##   Package Preparation Section   ##
#####################################

%prep
rm -rf %name-%version
mkdir -p %name-%version
%firefox.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

mkdir -p l10n
cd l10n
gzip -dc %{SOURCE1} | tar -xvf -
cd ..

#####################################
##      Package Build Section      ##
#####################################

%build
export PKG_CONFIG_PATH=${_libdir}/pkgconfig:%{_pkg_config_path}
export LDFLAGS="-B direct -z ignore"
export CFLAGS="-xlibmopt"
export OS_DEFINES="-D__USE_LEGACY_PROTOTYPES__"
export CXXFLAGS="-xlibmil -xlibmopt -D_XOPEN_SOURCE=500 -D__EXTENSIONS__"

%firefox.build -d %name-%version

cd %{_builddir}/%{name}-%{version}/l10n
for lang in %{lang_list}
do
  mv $lang.xpi langpack-$lang@firefox.mozilla.org.xpi
done

%install
%firefox.install -d %name-%version

# create file list for SUNWfirefox to separate xpidl|xpt_dump|xpt_link
cd $RPM_BUILD_ROOT%{_libdir}
find %{firefox.name} ! -type d | egrep -v "(xpidl|xpt_dump|xpt_link|libsoftokn3\.so|libnssdbm3\.so|libfreebl3\.so|libfreebl_32int_3\.so|libfreebl_32fpu_3\.so|libfreebl_32int64_3\.so)" | \
  sed -e 's#{#\\{#g' -e 's#}#\\}#g' -e 's#^.*$#%{_libdir}/&#' \
    >  %{_builddir}/%name-%version/%{name}.list

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

# re-sign these libraries after post process
mcs -d $RPM_BUILD_ROOT/usr/lib/firefox/libsoftokn3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/firefox %{_builddir}/%name-%version/obj/nss/shlibsign -v -i $RPM_BUILD_ROOT/usr/lib/firefox/libsoftokn3.so
mcs -d $RPM_BUILD_ROOT/usr/lib/firefox/libnssdbm3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/firefox %{_builddir}/%name-%version/obj/nss/shlibsign -v -i $RPM_BUILD_ROOT/usr/lib/firefox/libnssdbm3.so

%ifarch sparc
mcs -d $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl_32int_3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/firefox %{_builddir}/%name-%version/obj/nss/shlibsign -v -i $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl_32int_3.so
mcs -d $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl_32fpu_3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/firefox %{_builddir}/%name-%version/obj/nss/shlibsign -v -i $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl_32fpu_3.so
mcs -d $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl_32int64_3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/firefox %{_builddir}/%name-%version/obj/nss/shlibsign -v -i $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl_32int64_3.so
%else
mcs -d $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/firefox %{_builddir}/%name-%version/obj/nss/shlibsign -v -i $RPM_BUILD_ROOT/usr/lib/firefox/libfreebl3.so
%endif

cd %{_builddir}/%{name}-%{version}/l10n
chmod 0644 *.xpi
mkdir -p $RPM_BUILD_ROOT/usr/lib/firefox/extensions
cp *.xpi $RPM_BUILD_ROOT/usr/lib/firefox/extensions/

%clean
rm -rf $RPM_BUILD_ROOT

#########################################
##  Package Post[Un] Install Section   ##
#########################################

%post
%restart_fmri desktop-mime-cache || exit 1
exit 0

%postun
%restart_fmri desktop-mime-cache || exit 1
exit 0

%files -f SUNWfirefox.list

%doc -d firefox/mozilla-release README.txt LICENSE 
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/firefox
%dir %attr (0755, root, bin) %{_libdir}

%dir %attr (0755, root, bin) %{_libdir}/firefox/jsloader
%dir %attr (0755, root, bin) %{_libdir}/firefox/jsloader/resource

%ips_tag(com.oracle.elfsign=false) %{_libdir}/firefox/libsoftokn3.so
%ips_tag(com.oracle.elfsign=false) %{_libdir}/firefox/libnssdbm3.so
%ifarch sparc
%ips_tag(com.oracle.elfsign=false) %{_libdir}/firefox/libfreebl_32int_3.so
%ips_tag(com.oracle.elfsign=false) %{_libdir}/firefox/libfreebl_32fpu_3.so
%ips_tag(com.oracle.elfsign=false) %{_libdir}/firefox/libfreebl_32int64_3.so
%else
%ips_tag(com.oracle.elfsign=false) %{_libdir}/firefox/libfreebl3.so
%endif

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/firefox.desktop
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/firefox-icon.png
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%{_libdir}/firefox/extensions/langpack-*

%files devel
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/%{firefox.name}
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/idl/%{firefox.name}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Tue Dec 27 2011 - ginn.chen@oracle.com
- Update to Firefox 9.0.1.
* Tue Nov 15 2011 - ginn.chen@oracle.com
- Update to Firefox 8.0.
* Thu Oct 13 2011 - ginn.chen@oracle.com
- Update to Firefox 7.0.1.
* Fri Sep 09 2011 - ginn.chen@oralce.com
- Fix lang pack permissions.
* Thu Sep 08 2011 - ginn.chen@oracle.com
- Update to Firefox 6.0.2.
* Fri Aug 26 2011 - laszlo.peter@oracle.com
- merge l10n content into main package
* Fri Aug 12 2011 - ginn.chen@oracle.com
- Update to Firefox 6.0.
* Tue Jul 26 2011 - ginn.chen@oracle.com
- Fix CR 7071032.
* Tue Jul 12 2011 - ginn.chen@oracle.com
- Update to Firefox 5.0.
* Thu Jun 09 2011 - ginn.chen@oracle.com
- Add -D__USE_LEGACY_PROTOTYPES__ to make it compile on snv_166.
* Fri Apr 29 2011 - ginn.chen@oracle.com
- Update to Firefox 4.0.1.
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add "License" tag
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Thu Mar 04 2010 - brian.lu@sun.com
- Add Requires: SUNWdbus-glib
      BuildRequires: SUNWdbus-glib
      Requires: SUNWdbus-libs
      BuildRequires: SUNWdbus-libs
* Sun Dec  7 2009 - christian.kelly@sun.com
- Add BuildRequires SUNWlibxml2-python26.
* Wed Nov 26 2009 - ginn.chen@sun.com
- Update for Firefox 3.6.
* Thu Jun 11 2009 - brian.lu@sun.com
- Add '-B direct' option 
* Mon May 25 2009 - ginn.chen@sun.com
- Add SUNWlibtheora and SUNWogg-vorbis to dependency.
- Comment out dependency of SUNWsqlite3 until we use that.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 30 2009 - ginn.chen@sun.com
- Correction for build dependency of nss, nspr.
* Mon Mar 23 2009 - jeff.cai@sun.com
- Since /usr/lib/firefox/firefox (SUNWfirefox) requires /usr/bin/bash which is
  found in SUNWbash, add the dependency
* Tue Feb 10 2009 - dave.lin@sun.com
- Enable apoc adapter as default.
* Wed Sep 17 2008 - ginn.chen@sun.com
- Remove /usr/lib/firefox/components/compreg.dat and /usr/lib/firefox/components/xpti.dat in postinstall and postremove
- Touch /usr/lib/firefox/.autoreg in postinstall
- Remove staroffice-mime.types.in, staroffice-mailcap.in
* Tue Aug 19 2008 - ginn.chen@sun.com
- Remove -xldscope=symbolic in CFLAGS, CXXFLAGS, use -xldscope=hidden in libpixman Makefile.in instead
* Mon Aug 18 2008 - dave.lin@sun.com
- Rename SUNWfirefox3.spec to SUNWfirefox.spec since FF2 has been replaced by FF3 in Nevada and OS for several builds
* Fri Aug 15 2008 - dave.lin@sun.com
- add -xldscope=symbolic in CFLAGS, CXXFLAGS to fix the cairo crash issue per Brian's request
* Thu Jul 17 2008 - dave.lin@sun.com
- Removed the unnecessary dependency SUNWsolaris-devel-docs(CR6700877),
  SUNWfirefox.
* Thu May 22 2008 - dave.lin@sun.com
- Change to build pkg only if "--with-ff3" is specified, otherwise build nothing
- change to build as "SUNWfirefox" and as default browser
* Fri May 16 2008 - damien.carbery@sun.com
- Disable creation of symlink for firefox 3. This means that ff2 is left as
  default browser.
* Thu Mar 13 2008 - damien.carbery@sun.com
- Add -I/usr/X11/include to CFLAGS after update of SUNWwinc.
* Mon Feb 25 2008 - alfred.peng@sun.com
- Add "-D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" in CXXFLAGS to fix CR#6516110
* Thu Feb 21 2008 - damien.carbery@sun.com
- Rename SUNWsqlite dependency to SUNWsqlite3 to match pkg from SFW.
* Wed Jan 09 2008 - dave.lin@sun.com
- renamed FF 3 spec to *firefox3 to let FF 3 coexist with FF 2
* Fri Dec 28 2007 - dave.lin@sun.com
- deliver .autoreg no matter apoc enabled or not
* Thu Dec 27 2007 - dave.lin@sun.com
- move to 3.0 beta2
- set not building apoc adapter as default
- remove SUNWfirefox-root pkg
- disable apoc adapter since it's not available for 3.0
* Thu Dec 27 2007 - dave.lin@sun.com
- set no apoc-adapter as default
* Sat Oct 20 2007 - laca@sun.com
- add indiana getting started guide dependency
* Fri Oct 12 2007 - laca@sun.com
- add /usr/X11/include to CFLAGS if built with FOX
* Fri Sep 28 2007 - laca@sun.com
- delete Nevada X deps
- disable developer guide dep if sun branding is not requested
* Tue Aug 21 2007 - dave.lin@sun.com
- made postremove/postinstall script more robust(CR#6594606)
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Tue Apr 10 2007 - dave.lin@sun.com
- remove dependency on SUNWstaroffice-menuintegration from SUNWfirefox-root
  since it caused CR#6530982 fixed failed(see details in bugster)
* Mon Mar 26 2007 - dave.lin@sun.com
- add new package SUNWfirefox-root to fix bug CR#6530982, the package 
  would just add staroffice entries in /etc/mime.types /etc/mailcap 
  in postinstall
* Tue Mar 20 2007 - dave.lin@sun.com
- fix bug CR#6521792
    part1: add file ".autoreg" and add postinstall/postremove scripts in
           SUNWfirefox-apoc-adapter
    part2: add patch firefox-12-regenerate-compreg-file.diff
* Thu Dec 28 2006 - dave.lin@sun.com
- remove %preun to fix bug CR#6502253
* Fri Dec  8 2006 - laca@sun.com
- add SUNWsolaris-devel-docs dependency
* Tue Nov 28 2006 - dave.lin@sun.com
- add %if %with_apoc_adapter to conditinoally disable apoc adapter,
  default: enable apoc adapter, use --without-apoc-adapter to disable it
* Mon Nov 27 - dave.lin@sun.com
- enable apoc adapter(SUNWfirefox-apoc-adapter), CR#6478680
* Tue Sep 05 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Thu Jul 27 2006 - damien.carbery@sun.com
- Remove 'aclocal' dir from %files as it is now empty.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jul 13 2006 - dave.lin@sun.com
- add "-lCrun -lCstd" in CXXFLAGS to improve the startup performance
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Tue Jun 20 2006 - damien.carbery@sun.com
- Add SUNWpr and SUNWtls dependencies after check-deps.pl run.
* Mon Jun 12 2006 - dave.lin@sun.com
- changed to let firefox use nss,nspr in /usr/lib/mps required by ARC
- remove -R%{_libdir}
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri Jun 09 2006 - damien.carbery@sun.com
- Uncomment man page lines in %files.
* Thu Jun 08 2006 - dave.lin@sun.com
- add man page prepared by Leon Sha
* Thu Apr 13 2006 - dave.lin@sun.com
- changed installation location from "/usr/sfw/lib" to "/usr/lib"
* Fri Feb 24 2006 - dave.lin@sun.com
- Changed package category to FIREFOX
- Improved preremove script, using ${BASEDIR} instead of absolute path
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Thu Jan 19 2006 - damien.carbery@sun.com
- Add BuildRequires SUNWgnome-base-libs-devel.
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Fri Dec 02 2005 - damien.carbery@sun.com
- Add .autoreg file introduced in 1.5.
* Mon Oct 31 2005 - laca@sun.com
- Merge share pkgs into base
* Mon Oct 24 2005 - damien.carbery@sun.com
- Add BuildRequires SUNWgtar because source tarball needs GNU tar.
* Mon Sep 26 2005 - halton.huo@sun.com
- Change version same with linux verion.
* Fri Sep 02 2005 - damien.carbery@sun.com
- Correct ownership of %{_libdir}/pkgconfig directory.
* Fri Aug 26 2005 - dave.lin@sun.com
- initial version of the spec file created



