#
# spec file for package SUNWthunderbird
#
# includes module(s): thunderbird
#
# Copyright (c) 2005, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#
# DO NOT REMOVE NEXT LINE
# PACKAGE NOT INCLUDED IN GNOME UMBRELLA ARC
#
%include Solaris.inc
%use thunderbird = thunderbird.spec

#####################################
##   Package Information Section   ##
#####################################

%define lang_list ar bg ca cs da de el es-AR es-ES et eu fi fr gl he hu id is it ja ko lt nb-NO nl nn-NO pa-IN pl pt-BR pt-PT ro ru sk sl sq sv-SE tr uk zh-CN zh-HK zh-TW
%define l10n_version 10.0.2

Name:          SUNWthunderbird
IPS_package_name: mail/thunderbird
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       Mozilla Thunderbird Email/Newsgroup Client
Version:       %{thunderbird.version}
Source:        %{name}-manpages-0.1.tar.gz
Source1:       thunderbirdl10n-%{l10n_version}.tar.gz 
SUNW_BaseDir:  %{_basedir}
SUNW_Category: THUNDERBIRD,application,%{jds_version}
SUNW_Copyright:%{name}.copyright
License:        MOZILLA PUBLIC LICENSE V1.1
BuildRoot:     %{_tmppath}/%{name}-%{version}-build

#####################################
##  Package Requirements Section   ##
#####################################

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: archiver/gnu-tar
BuildRequires: codec/libtheora
BuildRequires: codec/ogg-vorbis
BuildRequires: compress/zip
BuildRequires: compress/bzip2
BuildRequires: database/sqlite-3
BuildRequires: gnome/config/gconf
BuildRequires: library/desktop/gtk2
BuildRequires: library/gnome/gnome-component
BuildRequires: library/gnome/gnome-libs
BuildRequires: library/gnome/gnome-vfs
BuildRequires: library/zlib
BuildRequires: library/libnotify
BuildRequires: library/libffi
BuildRequires: text/gnu-sed
BuildRequires: system/header
BuildRequires: system/library/libdbus-glib
BuildRequires: system/library/libdbus
BuildRequires: system/library/dbus
BuildRequires: system/library/freetype-2
BuildRequires: system/library/fontconfig
BuildRequires: system/library/math
BuildRequires: x11/library/mesa
BuildRequires: x11/library/libxscrnsaver
%if %option_without_moz_nss_nspr
#BuildRequires: library/nspr
#BuildRequires: library/security/nss
%endif
Requires: system/font/truetype/dejavu

#####################################
##   Package Description Section   ##
#####################################

%if %option_with_lightning
%package calendar
IPS_package_name: mail/thunderbird/plugin/thunderbird-lightning
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:       %{summary} - Calendar
Version:       %{thunderbird.lightning_version}
SUNW_BaseDir:  %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWthunderbird
%endif

#####################################
##   Package Preparation Section   ##
#####################################

%prep
rm -rf %name-%version
mkdir -p %name-%version
%thunderbird.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

#####################################
##      Package Build Section      ##
#####################################

%build

%thunderbird.build -d %name-%version

%install

%thunderbird.install -d %name-%version

# Lightning extension ID
# rm -rf $RPM_BUILD_ROOT/usr/lib/thunderbird/extensions/calendar-timezones@mozilla.org
# rm $RPM_BUILD_ROOT/usr/lib/thunderbird/distribution/extensions/tbtestpilot@labs.mozilla.com.xpi
# rmdir $RPM_BUILD_ROOT/usr/lib/thunderbird/distribution/extensions/
# rmdir $RPM_BUILD_ROOT/usr/lib/thunderbird/distribution

# create file list for SUNWthunderbird, SUNWthunderbird-calendar(ie. Lightning)
cd $RPM_BUILD_ROOT%{_libdir}
find %{thunderbird.name} ! -type d | egrep -v "(%{thunderbird.lightning_dir}|xpidl|xpt_dump|xpt_link|libsoftokn3\.so|libnssdbm3\.so|libfreebl3\.so|libfreebl_32int_3\.so|libfreebl_32fpu_3\.so|libfreebl_32int64_3\.so)" | \
  sed -e 's#{#\\{#g' -e 's#}#\\}#g' -e 's#^.*$#%{_libdir}/&#' \
  > %{_builddir}/%name-%version/%{name}.list

%if %option_with_lightning
find %{thunderbird.name}/extensions/%{thunderbird.lightning_dir} ! -type d |
  sed -e 's#{#\\{#g' -e 's#}#\\}#g' -e 's#^.*$#%{_libdir}/&#' \
  > %{_builddir}/%name-%version/%{name}-calendar.list
%endif

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

# CR 7071032 re-sign these libraries after post process
SHLIBSIGN=%{_builddir}/%name-%version/%{thunderbird.name}/%{thunderbird.moz_objdir}/mozilla/nss/shlibsign

mcs -d $RPM_BUILD_ROOT/usr/lib/thunderbird/libsoftokn3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/thunderbird $SHLIBSIGN -v -i $RPM_BUILD_ROOT/usr/lib/thunderbird/libsoftokn3.so
mcs -d $RPM_BUILD_ROOT/usr/lib/thunderbird/libnssdbm3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/thunderbird $SHLIBSIGN -v -i $RPM_BUILD_ROOT/usr/lib/thunderbird/libnssdbm3.so

%ifarch sparc
mcs -d $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl_32int_3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/thunderbird $SHLIBSIGN -v -i $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl_32int_3.so
mcs -d $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl_32fpu_3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/thunderbird $SHLIBSIGN -v -i $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl_32fpu_3.so
mcs -d $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl_32int64_3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/thunderbird $SHLIBSIGN -v -i $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl_32int64_3.so
%else
mcs -d $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl3.so
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib/thunderbird $SHLIBSIGN -v -i $RPM_BUILD_ROOT/usr/lib/thunderbird/libfreebl3.so
%endif

# L10n stuff
mkdir -p l10n
cd l10n
gzip -dc %{SOURCE1} | tar -xvf -
chmod 0644 *.xpi
for lang in %{lang_list} 
do
    cp $lang.xpi $RPM_BUILD_ROOT/usr/lib/thunderbird/extensions/langpack-$lang@thunderbird.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

#########################################
##  Package Post[Un] Install Section   ##
#########################################

%post
%restart_fmri desktop-mime-cache || exit 1

%postun
%restart_fmri desktop-mime-cache || exit 1

#####################################
##      Package Files Section      ##
#####################################

%files -f SUNWthunderbird.list

%doc -d %{thunderbird.name}/%{thunderbird.moz_srcdir}/mozilla README.txt LICENSE
%dir %attr (0755, root, other) %{_datadir}/doc

%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/thunderbird
%dir %attr (0755, root, bin) %{_libdir}
# Empty dirs which is out of SUNWthunderbird.list
%dir %attr (0755, root, bin) %{_libdir}/%{thunderbird.name}/jsloader
%dir %attr (0755, root, bin) %{_libdir}/%{thunderbird.name}/jsloader/resource
%ips_tag(com.oracle.elfsign=false) %{_libdir}/%{thunderbird.name}/libsoftokn3.so
%ips_tag(com.oracle.elfsign=false) %{_libdir}/%{thunderbird.name}/libnssdbm3.so
%ifarch sparc
%ips_tag(com.oracle.elfsign=false) %{_libdir}/%{thunderbird.name}/libfreebl_32int_3.so
%ips_tag(com.oracle.elfsign=false) %{_libdir}/%{thunderbird.name}/libfreebl_32fpu_3.so
%ips_tag(com.oracle.elfsign=false) %{_libdir}/%{thunderbird.name}/libfreebl_32int64_3.so
%else
%ips_tag(com.oracle.elfsign=false) %{_libdir}/%{thunderbird.name}/libfreebl3.so
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/thunderbird.desktop
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/thunderbird-icon.png
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%{_libdir}/thunderbird/extensions/langpack-*

%if %option_with_lightning
%files calendar -f SUNWthunderbird-calendar.list
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%endif

%changelog
* Fri Feb 17 2012 - lin.ma@oracle.com
- Bump to Thunderbird 10.0.2
- Bump to Lightning 1.2.1
* Tue Jan 10 2012 - lin.ma@oracle.com
- Bump to Thunderbird 9.0.1
- Bump to Lightning 1.1.1
- Update l10n list
* Wen Nov 23 2011 - lin.ma@oracle.com
- Bump to 8.0
* Wen Sep 07 2011 - lin.ma@oracle.com
- revise l10n language list and version based on Rebeccas feedback
- Remove zh-HK lang hack
* Fri Aug 26 2011 - laszlo.peter@oracle.com
- merge l10n content into main package
* Fri July 8 2011 - lin.ma@oracle.com
- Bump to 5.0
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add 'License' tag
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Tue Jan 12 2009 - brian.lu@sun.com
- Remove calendar-timezones extension
* Mon Jan 04 2009 - ginn.chen@sun.com
- Do not ship calendar-timezones extension, it was not used.
* Fri Dec 18 2009 - ginn.chen@sun.com
- Move calendar-timezones extensions to SUNWthunderbird-calendar.
* Mon May 25 2009 - ginn.chen@sun.com
- Move --without-lightning to options.inc.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 23 2009 - jeff.cai@sun.com
- Since /usr/lib/thunderbird/thunderbird (SUNWthunderbird) requires
  /usr/bin/bash which is found in SUNWbash, add the dependency.
* Thu Sep 19 2008 - brian.lu@sun.com
- add %doc section to generate new copyright files
* Thu Apr 24 2008 - brian.lu@sun.com
- remove wcap-enable.xpi because WCAP is already part of lightning 0.8
* Fri Oct 12 2007 - laca@sun.com
- add /usr/X11/include to CFLAGS/CXXFLAGS if built with FOX
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Sat Mar 03 2007 - dave.lin@sun.com
- enable WCAP in lightning
* Fri Jan 26 2007 - dave.lin@sun.com
- enable lightning extension(0.3) in Thunderbird
- remove BuildRequires: SUNWfirefox-devel since it's not necessary
- remove -R%{_libdir}/firefox since is not necessary
* Thu Dec 28 2006 - dave.lin@sun.com
- remove "Requires:  SUNWfirefox" since it's not necessary
* Tue Sep 05 2006 - Matt.Keenan@sun.com
- New Manpage tarball
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
- changed to let thunderbird use nss,nspr in /usr/lib/mps required by ARC
- remove -R%{_libdir}
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri Jun 09 2006 - damien.carbery@sun.com
- Uncomment man page lines in %files.
* Thu Jun 08 2006 - dave.lin@sun.com
- add man page prepared by Leon Sha
* Fri May 12 2006 - damien.carbery@sun.com
- Small update to dependency list after check-deps.pl run.
* Thu Apr 27 2006 - dave.lin@sun.com
- remove the devel pkg since the it's almost the same as firefox's devel pkg
- set -R%{_libdir}/firefox to let thunderbird use the nss,nspr libs delivered
  by firefox
* Fri Apr 14 2006 - dave.lin@sun.com
- changed pkg category to "THUNDERBIRD" to make it more clear
* Thu Apr 13 2006 - dave.lin@sun.com
- changed the installation location from "/usr/sfw/lib" to "/usr/lib"
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Thu Jan 18 2006 - dave.lin@sun.com
- add "-lXft -lfontconfig -lfreetype" to support configure opt "enable-static"
* Sat Dec  3 2005 - laca@sun.com
- add %post script that runs update-desktop-database
* Mon Oct 31 2005 - laca@sun.com
- merge -share pkgs into base
* Mon Sep 26 2005 - halton.huo@sun.com
- Change version same with linux verion.
* Thu Sep 22 2005 - laca@sun.com
- add %{_libdir} to %files so that we actually package thunderbird...
* Fri Sep 02 2005 - damien.carbery@sun.com
- Fix %files.
* Fri Aug 26 2005 - dave.lin@sun.com
- initial version of the spec file created
