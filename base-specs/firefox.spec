#
# Copyright (c) 2005-2011, Oracle and/or its affiliates. All rights reserved.
#
%define owner ginnchen

%define OSR LFI#124386 (Mozilla Exec. summary):n/a

# bugdb: bugzilla.mozilla.org
#
#####################################
##   Package Information Section   ##
#####################################

Name:        firefox
Summary:     Mozilla Firefox Web browser
Version:     10.0.2
%define tarball_version 10.0.2
Release:     1
Copyright:   MPL
License:     MPL
Group:       Applications/Internet
Distribution:Java Desktop System
Vendor:      Mozilla Foundation
Source:      http://ftp.mozilla.org/pub/mozilla.org/%{name}/nightly/%{tarball_version}-candidates/build1/source/%{name}-%{tarball_version}.source.tar.bz2
Source1:     firefox-icon.png
Source2:     firefox.desktop
#%if %option_without_moz_nss_nspr
#Source3:     nspr-nss-config
#%endif
Source4:     %{name}-xpcom.pc.in
Source5:     %{name}-plugin.pc.in
Source6:     %{name}-js.pc.in
%ifarch i386
Source7:     http://www.tortall.net/projects/yasm/releases/yasm-1.1.0.tar.gz
%endif

%define studio_12_1 %($CC -V 2>&1 | grep -c 5\.10)
%define studio_12_2 %($CC -V 2>&1 | grep -c 5\.11)

%ifarch sparc
Source8:     firefox10-profile-sparc-ss12-2.tar.bz2
%else
Source8:     firefox10-profile-x86-ss12-2.tar.bz2
%endif

%if %option_with_indiana_branding
Source9:     ora_solaris.png
%endif

# owner:hawklu date:2007-11-28 type:branding
# change preference to support multi-language
Patch1: firefox-01-locale.diff

# owner:ginnchen date:2011-03-07 type:feature
# See CR#6962345
Patch2: firefox-02-js-ctypes-compiler-workaround.diff

# owner:fujiwara date:2008-04-10 type:bug
# bugster:6686579 bugzilla:285267
Patch3: firefox-03-g11n-nav-lang.diff

# owner:ginnchen date:2008-08-19 type:bug
# bugster:6724471 bugzilla:451007
Patch4: firefox-04-donot-delay-stopping-realplayer.diff

# owner:ginnchen date:2011-11-21 type:feature
Patch5: firefox9-05-sqlite3763.diff

# owner:ginnchen date:2008-10-15 type:feature
# bugzilla:457196
Patch6: firefox9-06-jemalloc.diff

# owner:ginnchen date:2011-03-07 type:bug
Patch7: firefox9-07-uconv_sse2.diff

#%if %option_without_moz_nss_nspr
# owner:ginnchen date:2009-05-21 type:branding
#Patch8: firefox-08-system-nss-nspr.diff
#%endif

# owner:ginnchen date:2011-03-07 type:feature
Patch9: firefox10-09-ipc.diff

# owner:ginnchen date:2011-07-18 type:bug
Patch10: firefox6-10-appname-tr.diff

# owner:ginnchen date:2011-04-18 type:feature
Patch11: firefox9-11-sqlite-unix-excl.diff

# owner:hawklu date:2008-12-16 type:branding
Patch12: firefox6-12-xpcom-glue-no-hidden.diff

# owner:hawklu date:2008-04-20 type:branding
Patch13: firefox6-13-gen-devel-files.diff

%if %option_with_indiana_branding
# owner:davelam date:2009-03-02 type:branding
Patch14: firefox8-14-getting-started.diff
%endif

# owner:hawklu date:2009-05-22 type:branding
Patch15: firefox-15-use-system-theora.diff

# owner:ginnchen date:2011-11-21 type:bug bugzilla:701273 status:upstream
Patch16: firefox10-16-nsXBLProtoImpl.diff

# owner:ginnchen date:2011-10-25 type:feature
Patch17: firefox10-17-js-compiler.diff

# owner:ginnchen date:2011-03-08 type:bug
Patch18: firefox-18-libvpx-compile.diff

# owner:ginnchen date:2011-03-08 type:feature
Patch19: firefox6-19-xpcom-sparc-compile.diff

# owner:ginnchen date:2012-1-11 type:bug bugzilla:717174 bugzilla:682625 status:upstream
Patch20: firefox10-20-xBGR-plugin.diff

# owner:ginnchen date:2011-03-08 type:feature
# See CR#7023690
Patch21: firefox-21-compiler-workaround.diff

# owner:ginnchen date:2011-03-08 type:bug
Patch22: firefox9-22-jsfunc.diff

# owner:ginnchen date:2011-03-08 type:bug
Patch23: firefox9-23-ycbcr.diff

#%if %option_without_moz_nss_nspr
# owner:ginnchen date:2010-03-04 type:branding
# we need to move -lsqlite3 ahead of -L/usr/lib/mps
#Patch24: firefox6-24-storage-test.diff
#%endif

# owner:ginnchen date:2011-06-20 type:feature
Patch25: firefox-25-json-compile.diff

# owner:ginnchen date:2010-03-14 type:feature
Patch26: firefox10-26-pgo-ss12_2.diff

# owner:ginnchen date:2011-04-06 type:feature bugzilla:610323
Patch27: firefox9-27-methodjit-sparc.diff

# owner:ginnchen date:2010-03-14 type:feature
Patch28: firefox6-28-patch-for-debugging.diff

# owner:ginnchen date:2011-12-29 type:feature
Patch29: firefox9-29-selectAddons-app-scope.diff

# owner:ginnchen date:2010-03-14 type:bug
Patch30: firefox10-30-gfxAlphaRecovery.diff

# owner:ginnchen date:2010-05-12 type:bug
Patch31: firefox-31-async-channel-crash.diff

# owner:ginnchen date:2010-06-20 type:branding
Patch32: firefox7-32-yasm.diff

# owner:ginnchen date:2012-01-12 type:bug bugzilla:717863 status:upstream
Patch33: firefox10-33-jsgc-pagesize.diff

# owner:ginnchen date:2011-10-08 type:branding
Patch34: firefox7-34-js-numeric-limits.diff

# owner:ginnchen date:2010-06-20 type:branding
Patch35: firefox10-35-static-assert.diff

# owner:ginnchen date:2010-10-26 type:branding
Patch36: firefox10-36-gtkembed.diff

# owner:ginnchen date:2012-01-18 type:bug bugzilla:669556
Patch37: firefox10-37-sunaudio-buffer.diff

# owner:ginnchen date:2011-10-25 type:branding
Patch38: firefox9-38-libffi-3-0-9.diff

# owner:ginnchen date:2010-07-04 type:branding
# for snv_168 or later
Patch39: firefox-39-nss-compile.diff

# owner:ginnchen date:2011-10-10 type:bug bugzilla:675585
Patch40: firefox8-40-gthread-dlopen.diff

# owner:ginnchen date:2012-1-10 type:bug buzilla:716462
Patch41: firefox10-41-xBGR-performance.diff

# owner:ginnchen date:2011-11-04 type:bug bugzilla:702529
Patch42: firefox10-42-about-memory.diff

# owner:ginnchen date:2011-11-08 type:bug bugzilla:700615
Patch43: firefox10-43-donot-disable-locale-addon.diff

# owner:ginnchen date:2011-11-15 type:bug bugzilla:702179
Patch44: firefox10-44-dtrace-probe.diff

# owner:ginnchen date:2011-11-15 type:feature
Patch45: firefox8-45-libnspr_flt4.diff

URL:         http://www.mozilla.com/firefox

BuildRoot:   %{_tmppath}/%{name}-%{tarball_version}-build
Prefix:      /usr
Provides:    webclient
Autoreqprov: on

#####################################
##     Package Defines Section     ##
#####################################

%define _unpackaged_files_terminate_build 0
%define _ffdir %{_libdir}/%{name}
#%if %option_without_moz_nss_nspr
#%define nss_nspr_dir %{_libdir}/mps
#%else
%define nss_nspr_dir %{_libdir}/%{name}
#%endif

#####################################
##   Package Description Section   ##
#####################################

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

#####################################
##   Package Preparation Section   ##
#####################################

%prep
%setup -q -c -n %{name}

cd mozilla-release
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
#%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1

%if %option_with_debug
%patch28 -p1
%endif

%if %option_with_indiana_branding
%patch14 -p1
%endif

#%if %option_without_moz_nss_nspr
#%patch8 -p1
#%patch24 -p1
#%else
%patch45 -p1
#%endif

#####################################
##      Package Build Section      ##
#####################################

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

cat << "EOF" > .mozconfig
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
. $topsrcdir/browser/config/mozconfig
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --mandir=%{_mandir}
%if %option_with_debug
ac_add_options --enable-debug
ac_add_options --disable-optimize
ac_add_options --enable-tests
%else
ac_add_options --disable-debug
ac_add_options --enable-optimize
ac_add_options --disable-tests
ac_add_options --enable-system-sqlite
%endif
ac_add_options --enable-libxul
ac_add_options --enable-jemalloc
ac_add_options --enable-official-branding
ac_add_options --disable-updater
ac_add_options --enable-ipc
ac_add_options --enable-dtrace
ac_add_options --with-system-zlib
ac_add_options --with-system-bz2
ac_add_options --enable-system-pixman
ac_add_options --enable-system-ffi
ac_add_options --disable-crashreporter
ac_add_options --enable-debug-symbols=no
#%if %option_without_moz_nss_nspr
# ac_add_options --with-system-nspr
# ac_add_options --with-system-nss
#%endif
ac_add_options --enable-startup-notification
EOF

BUILD_OFFICIAL=1
MOZILLA_OFFICIAL=1
MOZ_PKG_FORMAT=BZ2
PKG_SKIP_STRIP=1
export BUILD_OFFICIAL MOZILLA_OFFICIAL MOZ_PKG_FORMAT PKG_SKIP_STRIP CFLAGS CXXFLAGS

#Build in a separated directory
SRCDIR=$PWD
export MOZCONFIG=$PWD/.mozconfig

%if %option_with_indiana_branding
cp %{SOURCE9} ${SRCDIR}/mozilla-release/browser/branding/official/content
%endif

mkdir -p ../obj
cd ../obj

#%if %option_without_moz_nss_nspr
#cp %{SOURCE3} ${SRCDIR}/../obj
#chmod +x ${SRCDIR}/../obj/nspr-nss-config
#export NSPR_CONFIG=${SRCDIR}/../obj/nspr-nss-config\ nspr
#export NSS_CONFIG=${SRCDIR}/../obj/nspr-nss-config\ nss
#%endif

# PGO build
%if %option_with_debug
%else
# to generate PGO profile
# export MOZ_PROFILE_GENERATE=1
# Notes:
# cd ~/packages/BUILD/SUNWfirefox-10.0/obj
# export OBJDIR=`pwd`
# mkdir -p jarlog/en-US
# export JARLOG_DIR=$OBJDIR/jarlog/en-US
# rm -rf browser.profile/*
# rm toolkit/library/libxul.so
# python _profile/pgo/profileserver.py 
# gtar cvf profile.tar browser.profile jarlog
# bzip2 profile.tar
# 
# to use PGO profile
#export MOZ_PROFILE_USE=1
#gtar jxf %{SOURCE8}
%endif

# Build yasm
%ifarch i386
gtar zxf %{SOURCE7}
mv yasm* yasm
cd yasm
./configure
gmake
cd ..
export YASM=${SRCDIR}/../obj/yasm/yasm
export LIBJPEG_TURBO_AS=${SRCDIR}/../obj/yasm/yasm
%endif

${SRCDIR}/mozilla-release/configure
make -j $CPUS

cd browser/installer
make

%install
/bin/rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/idl/%{name}
mkdir -p $RPM_BUILD_ROOT/tmp
mkdir -p $RPM_BUILD_ROOT/sdktmp

LIBDIR=$RPM_BUILD_ROOT%{_libdir}/%{name}
INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}/%{name}
IDLDIR=$RPM_BUILD_ROOT%{_datadir}/idl/%{name}

BUILDDIR=$PWD/../obj

cd $RPM_BUILD_ROOT/sdktmp
bzip2 -dc $BUILDDIR/dist/firefox-*.sdk.tar.bz2 | tar -xf -
rm $BUILDDIR/dist/firefox-*.sdk.tar.bz2

cd $RPM_BUILD_ROOT/tmp
bzip2 -dc $BUILDDIR/dist/firefox-*.tar.bz2 | tar -xf -
cd firefox
find . | xargs touch
cd ..
mv firefox/*  ${LIBDIR}

cd $RPM_BUILD_ROOT/sdktmp
cd firefox*
find . | xargs touch

mv include/* ${INCLUDEDIR}
mv idl/* ${IDLDIR}

/bin/mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
/bin/mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -c -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/firefox-icon.png
install -c -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/firefox.desktop

/bin/ln -s ../lib/firefox/firefox $RPM_BUILD_ROOT%{_bindir}/firefox

# install firefox-*.pc
mkdir -p  $RPM_BUILD_ROOT%{_libdir}/pkgconfig

/usr/bin/sed -e "s,BASEDIR,%{_basedir},g" \
             -e "s,LIBDIR,%{_libdir},g" \
             -e "s,DATADIR,%{_datadir},g"\
             -e "s,IDLDIR,%{_datadir}/idl/%{name},g"\
             -e "s,INCLUDEDIR,%{_includedir},g" \
             -e "s,NAME,%{name},g" \
%if 0
#%option_without_moz_nss_nspr
             -e "s,REQUIRES_NSPR,Requires: nspr >= 4.8,g" \
             -e "s,NSPR_RUNPATH,-R/usr/lib/mps,g" \
             -e "s,NSPR_LIB,,g" \
             -e "s,NSPR_INCLUDE,,g" \
%else
             -e "s,REQUIRES_NSPR,,g" \
             -e "s,NSPR_RUNPATH,,g" \
             -e "s,NSPR_LIB,-lnspr4,g" \
             -e "s,NSPR_INCLUDE,-I\$\{includedir\}/nspr,g" \
%endif
             %{SOURCE4} > $RPM_BUILD_ROOT/sdktmp/%{name}-xpcom.pc
install -c -m 644 $RPM_BUILD_ROOT/sdktmp/%{name}-xpcom.pc \
             $RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{name}-xpcom.pc

/usr/bin/sed -e "s,BASEDIR,%{_basedir},g" \
             -e "s,LIBDIR,%{_libdir},g" \
             -e "s,DATADIR,%{_datadir},g"\
             -e "s,INCLUDEDIR,%{_includedir},g" \
             -e "s,NAME,%{name},g" \
             %{SOURCE5} > $RPM_BUILD_ROOT/sdktmp/%{name}-plugin.pc
install -c -m 644 $RPM_BUILD_ROOT/sdktmp/%{name}-plugin.pc \
$RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{name}-plugin.pc

/usr/bin/sed -e "s,BASEDIR,%{_basedir},g" \
             -e "s,LIBDIR,%{_libdir},g" \
             -e "s,DATADIR,%{_datadir},g"\
             -e "s,INCLUDEDIR,%{_includedir},g" \
             -e "s,NAME,%{name},g" \
%if 0
#%option_without_moz_nss_nspr
             -e "s,REQUIRES_NSPR,Requires: nspr >= 4.8,g" \
             -e "s,NSPR_RUNPATH,-R/usr/lib/mps,g" \
             -e "s,NSPR_LIB,,g" \
             -e "s,NSPR_INCLUDE,,g" \
%else
             -e "s,REQUIRES_NSPR,,g" \
             -e "s,NSPR_RUNPATH,,g" \
             -e "s,NSPR_LIB,-lnspr4,g" \
             -e "s,NSPR_INCLUDE,-I\$\{includedir\}/nspr,g" \
%endif
             %{SOURCE6} > $RPM_BUILD_ROOT/sdktmp/%{name}-js.pc
install -c -m 644 $RPM_BUILD_ROOT/sdktmp/%{name}-js.pc \
$RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{name}-js.pc

# get out of the tmp dir before remove it
cd $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/tmp
rm -rf $RPM_BUILD_ROOT/sdktmp

# remove local dictionary and share the one that delivered
# by myspell-dictionary
rm -rf $RPM_BUILD_ROOT%{_ffdir}/dictionaries

# move the default bookmarks file to a separated package: SUNWfirefox-bookmark
# remove this one
rm -f $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/bookmarks.html

%clean
/bin/rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Feb 21 2012 - ginn.chen@oracle.com
- Bump to Firefox 10.0.2 ESR
* Tue Dec 27 2011 - ginn.chen@oracle.com
- Bump to Firefox 9.0..1.
* Tue Nov 15 2011 - ginn.chen@oracle.com
- Bump to Firefox 8.0.
* Thu Oct 13 2011 - ginn.chen@oracle.com
- Bump to Firefox 7.0.1.
* Thu Sep 08 2011 - ginn.chen@oracle.com
- Bump to Firefox 6.0.2.
* Fri Aug 12 2011 - ginn.chen@oracle.com
- Bump to Firefox 6.0.
* Tue Jul 12 2011 - ginn.chen@oracle.com
- Bump to Firefox 5.0.
* Fri Apr 29 2011 - ginn.chen@oracle.com
- Bump to Firefox 4.0.1.
* Thu Mar 24 2011 - ginn.chen@oracle.com
- Bump to Firefox 3.6.16.
* Mon Mar 07 2011 - ginn.chen@oracle.com
- Bump to Firefox 3.6.15.
* Wed Mar 02 2011 - ginn.chen@oracle.com
- Bump to Firefox 3.6.14.
* Fri Jan 21 2011 - ginn.chen@oracle.com
- Add support for Solaris Studio 12.2.
* Fri Dec 10 2010 - ginn.chen@oracle.com
- Bump to Firefox 3.6.13, add firefox3-29-ots-makepair.diff.
* Fri Nov 19 2010 - ginn.chen@oracle.com
- Add firefox3-28-gtk-dialog_a11y.diff to fix d.o.o. 17425.
* Thu Oct 28 2010 - ginn.chen@oracle.com
- Bump to Firefox 3.6.12.
* Thu Oct 21 2010 - ginn.chen@oracle.com
- Bump to Firefox 3.6.11.
* Mon Sep 27 2010 - ginn.chen@sun.com
- Bump to Firefox 3.6.10.
* Mon Aug 02 2010 - elaine.xiong@sun.com
- Bump to Firefox 3.6.8.
* Tue Jun 29 2010 - ginn.chen@sun.com
- Bump to Firefox 3.6.6.
* Tue Apr 06 2010 - ginn.chen@sun.com
- Bump to Firefox 3.6.3.
* Thu Mar 04 2010 - ginn.chen@sun.com
- Enable PGO, enable system sqlite, enable tests.
* Mon Feb 08 2010 - ginn.chen@sun.com
- Disable system sqlite for d.o.o. 14364.
* Thu Feb 04 2010 - ginn.chen@sun.com
- Add firefox3-23-nspr_use_zone_allocator.diff.
* Tue Jan 26 2010 - ginn.chen@sun.com
- Add firefox3-22-jemalloc-linkage.diff to fix potential malloc issues.
* Mon Jan 25 2010 - ginn.chen@sun.com
- Firefox 3.6rc2 is final.
* Mon Jan 18 2010 - ginn.chen@sun.com
- Bump to Firefox 3.6rc2.
* Wed Jan 06 2010 - ginn.chen@sun.com
- Bump to Firefox 3.6rc1.
  Add firefox3-21-atspi2.diff
* Mon Dec 21 2009 - ginn.chen@sun.com
  Add --with-system-zlib --with-system-bz2.
* Mon Dec 21 2009 - ginn.chen@sun.com
- Bump to Firefox 3.6 b5.
  Add firefox3-19-enable-about-memory.diff.
  Add firefox3-20-startup-notification.diff.
* Wed Nov 25 2009 - ginn.chen@sun.com
- Upgrade to Firefox 3.6 b4.
* Fri Nov 6 2009 - ginn.chen@sun.com
- Bump to 3.5.5.
* Thu Oct 29 2009 - ginn.chen@sun.com
- Remove patch firefox3-28-ss-privacy-level.diff, the bug was fixed in 3.5.3
* Wed Oct 28 2009 - ginn.chen@sun.com
- Bump to 3.5.4. Minor change to nspr-nss-config.
* Wed Oct 7 2009 - ginn.chen@sun.com
- Remove patch 35-check-nspr-ver.diff, it won't work for 4.8 vs 4.8.0.
- Add a workaround in nspr-nss-config. instead.
* Sat Sep 26 2009 - dave.lin@sun.com
- Add patch 35-check-nspr-ver.diff to check nspr version correctly.
* Fri Sep 18 2009 - ginn.chen@sun.com
- Bump to Firefox 3.5.3.
- Remove patch firefox3-35-downloadable-font.diff.
- Add patch firefox3-15-compiler-workaround-2.diff.
* Tue Aug 04 2009 - brian.lu@sun.com
- Use new apoc adapter source tarball
  firefox-3.5-apoc-adapter.tar.bz2
  which uses mozilla public string APIs
- Remove patch firefox3-33-apoc-failed-to-shutdown.diff
* Tue Aug 04 2009 - ginn.chen@sun.com
- Bump to Firefox 3.5.2.
- Remove patch firefox3-12-bug492720.diff firefox3-26-bug504043.diff
* Wed Jul 29 2009 - ginn.chen@sun.com
- Add patch firefox3-35-downloadable-font.diff
* Sun Jul 19 2009 - christian.kelly@sun.com
- Add patch to fix gtk includes.
* Thu Jul 16 2009 - ginn.chen@sun.com
- Bump to Firefox 3.5.1.
- Remove patch firefox3-25-bug502584.diff
* Thu Jul 16 2009 - leon.sha@sun.com
- Add patch firefox3-26-bug504043.diff
* Mon Jul 13 2009 - brian.lu@sun.com
- Fix the bug doo 10012
* Tue Jul 07 2009 - ginn.chen@sun.com
- Add patch firefox3-25-bug502584.diff
* Wed Jul 01 2009 - ginn.chen@sun.com
- Bump to Firefox 3.5.
* Thu Jun 25 2009 - ginn.chen@sun.com
- Bump to Firefox 3.5 rc3. Add fix for bugzilla 499660.
* Sat Jun 20 2009 - ginn.chen@sun.com
- Bump to Firefox 3.5 rc2.
* Thu Jun 18 2009 - brian.lu@sun.com
- The patch firefox3-31-sunaudio-sparc.diff is upstream
* Wed Jun 17 2009 - ginn.chen@sun.com
- Bump to Firefox 3.5 rc1.
* Tue Jun 16 2009 - christian.kelly@sun.com
- Re-enable use of system sqlite, build systems have the newer version
  installed now.
* Sun Jun 14 2009 - christian.kelly@sun.com
- Disable use of system sqlite.
* Thu Jun 11 2009 - brian.lu@sun.com
- Use system libsqlite3.so
* Fri Jun 05 2009 - ginn.chen@sun.com
- Use system nspr in firefox-*.pc.
* Fri Jun 05 2009 - ginn.chen@sun.com
- Add patch firefox3-12-bug492720.diff to fix build issue of libgjs.
* Wed Jun 03 2009 - brian.lu@sun.com
- Change bugzilla:9112 to doo:9112 and bugzilla:8471 to doo:8471
* Mon May 25 2009 - ginn.chen@sun.com
- Use system NSS NSPR libraries by default
  Add patch firefox3-11-system-nss-nspr.diff
  Add source nspr-nss-config
* Mon May 25 2009 - ginn.chen@sun.com
- Update patch firefox3-32-use-system-theora.diff to use libogg, libvobis.
* Tue May 22 2009 - brian.lu@sun.com
- Add patch firefox3-32-use-system-theora.diff for d.o.o 9112
* Tue May 18 2009 - brian.lu@sun.com
- Add patch firefox3-31-sunaudio-sparc.diff for d.o.o 8471
* Tue Apr 28 2009 - ginn.chen@sun.com
- Bump to 3.5 beta 4, add patch firefox3-04-oggplay.diff
  firefox3-30-timer-execution.diff for d.o.o. 8450.
* Tue Mar 31 2009 - alfred.peng@sun.com
- Add patch firefox3-22-308-security-fixes.diff to include the security
  fixes released in Firefox 3.0.8.
* Mon Mar 30 2009 - ginn.chen@sun.com
- Add patch firefox3-27-bug484932.diff. Fix d.o.o. 7638.
- Add patch firefox3-28-ss-privacy-level.diff. Workaround for d.o.o. 7634.
* Fri Mar 20 2009 - ginn.chen@sun.com
- Add patch firefox3-26-bug468727.diff.
* Thu Mar 05 2009 - ginn.chen@sun.com
- Bump to 3.1b3 build 1.
* Wed Mar 04 2009 - ginn.chen@sun.com
- Bump to 3.1b3 pre. Update patches accordingly.
* Mon Mar 02 2009 - alfred.peng@sun.com
- Add patch for OpenSolaris getting started page.
* Thu Feb 19 2009 - brian.lu@sun.com
- Fix the issue caused by pango upgrade
* Tue Feb 10 2009 - dave.lin@sun.com
- Enable apoc adapter as default.
* Web Feb 04 2009 - brian.lu@sun.com
- Enable APOC adapter when build with --with-apoc-apdater
* Mon Feb 02 2009 - alfred.peng@sun.com
- fit and finish: add default-to-downloads.diff for bugster CR#6735323.
* Wed Jan 07 2009 - dave.lin@sun.com
- Change version number from 3.1b2 to 3.1 since
  svr4 pkg requires digit only.
* Thu Dec 18 2008 - ginn.chen@sun.com
- add firefox3-21-cache-directives.diff
- update firefox3-29-strip-gtk-module-settings.diff
* Wed Dec 17 2008 - ginn.chen@sun.com
- clean up and update some patches
* Wed Dec 17 2008 - alfred.peng@sun.com
- correct the name typo of patch36.
* Tue Dec 16 2008 - brian.lu@sun.com
- patches/firefox3-36-font-config.diff
  patches/firefox3-37-xpcom-no-hidden.diff
* Mon Dec 15 2008 - dave.lin@sun.com
- Removed upstreamed patch -24-moz-fix-link-path.diff.
* Mon Dec 15 2008 - brian.lu@sun.com
- patches/firefox3-18-gen-devel-files.diff
  patches/firefox3-21-donot-delay-stopping-realplayer.diff:
  update patch
- patches/firefox3-31-js-dtrace.diff: add patch
- patches/firefox3-32-alloca.diff: add patch

* Fri Dec 12 2008 - brian.lu@sun.com
- Bump to firefox 3.1b2

  Remove following patches (upstreamed):
  firefox3-19-no-xrender-perf.diff
  firefox3-20-remap-pixman-functions.diff
  firefox3-26-know-your-rights.diff

  Add following patches:
  firefox3-30-js.diff
  firefox3-33-libogg.diff
  firefox3-34-liboggz.diff
  firefox3-35-theora-disable-inline-asm.diff

  Update follwoing patches:
  firefox3-09-remove-core-file-check.diff
  firefox3-29-strip-gtk-module-settings.diff

* Wed Dec 03 2008 - alfred.peng@sun.com
- Move the default bookmarks file to a separated package, CR6777386.
  Remove patches: firefox3-11-getting-started-bookmark.diff and
  firefox3-22-bug-report-bookmark.diff
* Thu Nov 27 2008 - ginn.chen@sun.com
- Add firefox3-28-fix-mimetype-for-helper-app.diff
- Add firefox3-29-strip-gtk-module-settings.diff
* Mon Nov 17 2008 - brian.lu@sun.com
- bump to 3.0.4
* Wed Oct 15 2008 - ginn.chen@sun.com
- Add firefox3-27-jemalloc-interpose-flag.diff.
* Fri Oct 10 2008 - alfred.peng@sun.com
- Add %option_with_indiana_branding for firefox3-25-ksh.diff.
* Fri Oct 10 2008 - alfred.peng@sun.com
- Add firefox3-25-ksh.diff for indiana only to fix bugster CR6750518.
  Add firefox3-26-know-your-rights.diff for the EULA pop-up bugster CR6757178.
  Update firefox3-11-getting-started-bookmark.diff for the default
  bookmarks and toolbar entries on OpenSolaris 2008.11.
* Fri Oct 10 2008 - ginn.chen@sun.com
- enable system cairo: fix for #3586
* Sat Sep 27 2008 - ginn.chen@sun.com
- Bump to 3.0.3.
- Add enable-libxul for debug version.
* Fri Sep 19 2008 - ginn.chen@sun.com
- Add firefox3-23-spellchecker-default.diff
- Add firefox3-24-moz-fix-link-path.diff
* Wed Sep 17 2008 - ginn.chen@sun.com
- Remove firefox3-01-change-install-dir.diff
- Remove firefox3-03-plugins.diff
- Remove firefox3-04-common-tar-option.diff
- Remove firefox3-06-find-opt.diff
- Remove firefox3-11-developer-guide-bookmark.diff
- Put timestamp into .autoreg as a workaround for IPS for now.
* Tue Sep 09 2008 - ginn.chen@sun.com
- Do not remove nss/nspr header files for now.
* Wed Sep 03 2008 - ginn.chen@sun.com
- Fix firefox-preload.list.in and some small tweaks for specfile.
* Tue Sep 02 2008 - brian.lu@sun.com
- Add %if option_with_sun_branding around patch22
* Wed Aug 27 2008 - ginn.chen@sun.com
- Update patch firefox3-20-remap-pixman-functions.diff
* Fri Aug 22 2008 - dave.lin@sun.com
- add patch firefox3-22-bug-report-bookmark.diff
* Wed Aug 20 2008 - dave.lin@sun.com
- Rename firefox3-preload.list.in to firefox-preload.list.in.
* Tue Aug 19 2008 - ginn.chen@sun.com
- Add firefox3-21-donot-delay-stopping-realplayer.diff
- Update firefox3-20-remap-pixman-functions.diff
- Remove firefox3-16-crash-in-8-bit-mode.diff
- Remove firefox3-07-no-ldlibpath.diff
* Mon Aug 18 2008 - dave.lin@sun.com
- Rename firefox3.spec to firefox.spec since FF2 has been replaced by FF3 in Nevada and OS for several builds
* Mon Aug 18 2008 - dave.lin@sun.com
- Enable debug mode when --with-debug specified
* Mon Jul 21 2008 - dave.lin@sun.com
- Fixed another "-type f" issue of find command, which is similar as below
* Mon Jul 21 2008 - damien.carbery@sun.com
- Add another "-type f" to /usr/bin/find command because Solaris find needs it
  on both sides of -o to only find files.
* Mon Jul 21 2008 - ginn.chen@sun.com
- Add bugdb info.
* Sat Jul 19 2008 - dave.lin@sun.com
- Fixed *.h *.idl 755 attribute issue.
* Thu Jul 17 2008 - brian.lu@sun.com
- bump to 3.0.1
* Thu Jul 17 2008 - dave.lin@sun.com
- Change the patch firefox3-03-plugins as branding patch
* Fri Jul 11 2008 - brian.lu@sun.com
- Add bugId for the patch firefox3-09-remove-core-file-check.diff
- Remove patch firefox3-16-crash-in-8-bit-mode.diff: upstreamed
- Add bugId for firefox3-18-gen-devel-files.diff
* Thu Jun 26 2008 - brian.lu@sun.com
- Add patch
* Fri Jun 20 2008 - dave.lin@sun.com
- Bump to Firefox 3.0 official release
* Thu Jun 12 2008 - ginn.chen@sun.com
- Bump to Firefox 3.0 RC3
- Add with-system-jpeg (bugzilla 437041)
- Add firefox3-19-no-xrender-perf.diff to improve Firefox rendering performance
  when X Render is not available.
- Remove patch10, patch14

* Thu May 29 2008 - damien.carbery@sun.com
- Disable developer guide patch to fix 6700877 as the developer guide is not
  needed for OpenSolaris or SXCE.
* Thu May 22 2008 - dave.lin@sun.com
- change to build as default browser
* Mon Apr 21 2008 - brian.lu@sun.com
- new firefox3 devel package
  remove unnecessary comment
* Mon Apr 14 2008 - brian.lu@sun.com
- bump to beta 5
  remove patch14 which has been fixed in cario trunk (to be fixed in
  firefox3 final release) but not in firefox3 beta 5
* Thu Apr 10 2008 - takao.fujiwara@sun.com
- Add firefox3-17-g11n-nav-lang.diff to assign locales in
  general.useragent.locale so that JavaScript navigator.language works.
* Thu Feb 28 2008 - brian.lu@sun.com
- Remove the patch firefox3-10-cario-perf.diff
  which causes a regression CR6668422
* Mon Feb 25 2008 - brian.lu@sun.com
- Fix the bug CR6656460 firefox crash in 8 bit mode
* Wed Feb 20 2008 - dave.lin@sun.com
- Bump to beta3, and removed upstreamed patche firefox3-15-printing-failed.diff
* Wed Jan 24 2008 - brian.lu@sun.com
- patch fixing the bug CR6646478 status:upstream
* Wed Jan 09 2008 - dave.lin@sun.com
- renamed FF 3 spec to *firefox3 to let FF 3 coexist with FF 2
* Wed Jan 09 2008 - brian.lu@sun.com
- the patch is from bugzilla.freedesktop.org (bug 4945) Fixing CR6646456
* Sat Dec 29 2007 - dave.lin@sun.com
- changed to use "make" instead of "make export" and "make libs"
* Thu Dec 27 2007 - dave.lin@sun.com
- move to 3.0 beta2
- set not building apoc adapter as default
* Mon Dec 03 2007 - dave.lin@sun.com
- bump to 2.0.0.11 for several regressions in 2.0.0.10
* Fir Nov 28 2007 - evan.yan@sun.com
- replace firefox-06-locale.diff with mozilla-09-locale.diff, to correct our way
  of supporting multi-language
* Thu Nov 27 2007 - dave.lin@sun.com
- bump to 2.0.0.10 for several security bug fixes
* Fri Nov 11 2007 - brian.lu@sun.com
- Add firefox-15-remove-core-file-check.diff patch to remove core file checking
  code in run-mozilla.sh. Fixes CR6589754.
* Fri Nov 02 2007 - dave.lin@sun.com
- bump to 2.0.0.9 to fix several regressions in previous release
* Mon Oct 22 2007 - dave.lin@sun.com
- bump to 2.0.0.8
* Sat Oct 20 2007 - laca@sun.com
- add indiana branding patch
* Fri Sep 28 2007 - laca@sun.com
- do not add developer guide bookmark when sun branding is not requested
* Wed Sep 19 2007 - dave.lin@sun.com
- bump to 2.0.0.7
* Fri Aug 03 2007 - dave.lin@sun.com
- bump to 2.0.0.6
* Mon Jul 23 2007 - dave.lin@sun.com
- bump to 2.0.0.5 and remove patch firefox-15-infinite-recursion.diff which
  has been upstreamed in that release
* Thu Jun 21 2007 - damien.carbery@sun.com
- Add patch, mozilla-08-cairo-update.diff, to update the private copy of
  cairo.h used in the build.
* Thu May 31 2007 - dave.lin@sun.com
- bump to 2.0.0.4
* Fri May 18 2007 - brian.lu@sun.com
- Firefox dumps core due to infinite recursion
* Mon Apr 30 2007 - dave.lin@sun.com
- remove local dictionary and use the one delivered by myspell-dictionary(CR6218511)
* Thu Apr 27 2007 - brian.lu@sun.com
- add patch to grey out "Check for Updates" in Firefox menu since it's not supported
* Thu Apr 12 2007 - dave.lin@sun.com
- disable update feature in Firefox menu since it's not supported
  on Solaris so far(CR#6542910)
* Wed Apri 10 2007 - brian.lu@sun.com
- change the comments of Patch15 from type:upstream to type:bug state:upstream
* Wed Apri 04 2007 - brian.lu@sun.com
- # bugster: CR6331694 partly fixed, the patch has been upstreamed
* Wed Mar 21 2007 - dave.lin@sun.com
- bump to 2.0.0.3
* Tue Mar 20 2007 - dave.lin@sun.com
- fix bug CR#6521792
    part1: add file ".autoreg" and add postinstall/postremove scripts in
           SUNWfirefox-apoc-adapter
    part2: add patch firefox-12-regenerate-compreg-file.diff
* Sat Mar 03 2007 - dave.lin@sun.com
- removed patch firefox-12-bookmark-drag-and-drop.diff which has been
  upstreamed in 2.0.0.2
* Mon Feb 26 2007 - dave.lin@sun.com
- bump version to 2.0.0.2
* Mon Feb 12 2007 - damien.carbery@sun.com
- Add patch, 02-xpcom-mps.diff, to add '-I/usr/include/mps' to firefox-xpcom.pc
  to allow totem to find prtypes.h (as nscore.h includes this).
* Mon Feb 05 2007 - brian.lu@sun.com
- fix bug CR6519241:bookmark drag and drop crash firefox
- bugzilla id 367203. The patch has been put into upstream
* Fri Jan 26 2007 - dave.lin@sun.com
- enable xinerama support to fix bug CR6507236
* Thu Jan 18 2007 - damien.carbery@sun.com
- Fix 'patch7 -p0' - change to -p1 and change patch file too.
* Wed Jan 17 2007 - damien.carbery@sun.com
- Remove unneeded patch, firefox-02-font_Xft.diff.
* Fri Jan 05 2007 - dave.lin@sun.com
- remove firefox-rebuild-databases and %preun since it's unnecessary for
  Firefox 2.0
* Thu Dec 28 2006 - dave.lin@sun.com
- change the patch type to branding for some patches in patch comments
- bump version to 2.0.0.1
* Thu Dec 07 2006 - brian.lu@sun.com
- Add "solaris developer guide" to bookmark and default home page etc
* Wed Nov 29 2006 - damien.carbery@sun.com
- Correct path to sparcv8plus dir. Enclose code within '%ifarch sparc'.
* Tue Nov 28 2006 - dave.lin@sun.com
- add %if %with_apoc_adapter to conditinoally disable building apoc
  adapter, default: build apoc adapter, use
  --without-apoc-adapter to disable it
- remove empty firefox/cpu/sparcv8plus and firefox/cpu
* Mon Nov 27 2006 - dave.lin@sun.com
- enable apoc adapter(CR#6478680)
- move manpage related part in "%ifos linux" since SUNWfirefox.spec
  would cover that on Solaris
* Fri Nov 17 2006 - dave.lin@sun.com
- add patch comments
* Wed Oct 25 2006 - dave.lin@sun.com
- bump verion to 2.0(official release)
* Fri Oct 20 2006 - dave.lin@sun.com
- bump version to 2.0rc3
* Mon Oct 09 2006 - dave.lin@sun.com
- bump version to 2.0rc2
* Thu Sep 07 2006 - dave.lin@sun.com
- add patch firefox-09-no-pkg-files.diff to remove patch checker scripts
  since it's unnecessary to deliver them with the bundled version
- change the version 2.0bx to 2.0 to comply WOS integration rules
- re-organize the patch list
* Mon Sep 04 2006 - dave.lin@sun.com
- bump version to 2.0 beta 2
* Mon Aug 28 2006 - dave.lin@sun.com
- create symbol link libnssckbi.so -> /usr/lib/mps/libnssckbi.so
  to fix bug CR#6459752
* Tue Aug 08 2006 - dave.lin@sun.com
- bump version to 2.0b1
- remove the patch mozilla-03-s11s-smkfl.diff, mozilla-04-s11x-smkfl.diff,
  firefox-03-yelp-hang.diff which have been fixed in 2.0b1
- change to xpinstall/packager to run make to make the binary tarball
* Tue Aug 08 2006 - dave.lin@sun.com
- fixed the preload list problem
* Thu Jul 27 2006 - damien.carbery@sun.com
- Remove 'aclocal' dir from %files as it is now empty.
* Wed Jul 26 2006 - matt.keenan@sun.com
- Remove firefox-10-gecko.m4.diff : yelp uses local copy now, and re-shuffled
  the rest of the firefox-* patches to be in sequence.
* Fri Jul 07 2006 - dave.lin@sun.com
- add patch mozilla-07-no-ldlibpath.diff to remove the LD_LIBRARY_PATH in
  the startup script
* Tue Jun 13 2006 - dave.lin@sun.com
- add patch firefox-15-no-nss-nspr.diff to let firefox use nss, nspr in
  /usr/lib/mps required by ARC
- remove all nss, nspr header files in development package
* Mon Jun 12 2006 - dave.lin@sun.com
- add patch firefox-14-plugins.diff to add Mozilla plugins direcotry
  (/usr/sfw/lib/mozilla/plugins) in Firefox plugin searching path(CR#6428445)
* Fri Jun 02 2006 - dave.lin@sun.com
- bump src version to 1.5.0.4
* Mon May 08 2006 - dave.lin@sun.com
- bump src version to 1.5.0.3
* Fri Apr 28 2006 - dave.lin@sun.com
- remove patch mozilla-06-skip-strip.diff, use another simple way to skip
  strip instead, setting PKG_SKIP_STRIP=1
* Fri Apr 21 2006 - dave.lin@sun.com
- switch back to 1.5.0.2 since we're not get ARC approved yet
* Fri Apr 14 2006 - dave.lin@sun.com
- removed firefox-chrome-lang.txt per l10n team's request, firefox uses new
  strategy to register chrome entries, so this file is useless
* Thu Apr 13 2006 - davelin@sun.com
- Changed the installation location from "/usr/sfw/lib" to "/usr/lib"
  on Solaris
* Tue Apr 04 2006 - dave.lin@sun.com
- Bump version to 2.0 alpha1
- Remove Patch3,4,11 which have been upstreamed into this version
- Add patch mozilla-06-skip-strip.diff to make no stripped libraries
* Fri Mar 31 2006 - dave.lin@sun.com
- Add patch firefox-13-locale.diff to make firefox automatically
  pick up locale setting from user environment and start up in
  that locale
* Fri Feb 24 2006 - dave.lin@sun.com
- Add patch firefox-11-new-tab.diff to fix CR6368789
- Add patch firefox-12-preload.diff and extra source file
  firefox-preload.list.in to enable firefox preload mechanism
- Remove useless file firefox-rebuild-databases since it's only
  for Linux
- Remove useless sources and patch
* Thu Dec 15 2005 - dave.lin@sun.com
- Add patch firefox-09-yelp-hang.diff to fix yelp hang problem.
* Fri Dec 02 2005 - damien.carbery@sun.com
- Add Makefile.in patch to link fontconfig and Xft libraries.
- make from top directory to build nsIconChannel.o.
* Fri Dec 02 2005 - dave.lin@sun.com
- Bump tarball version to 1.5.
- Modify the configuration options
* Fri Nov 11 2005 - dave.lin@sun.com
- Bump tarball version to 1.5rc3.
* Fri Nov 11 2005 - halton.huo@sun.com
- Bump tarball version to 1.5rc2.
* Tue Nov 08 2005 - dave.lin@sun.com
- Bump tarball version to 1.5rc1
- Remove the patch mozilla-07-bz307041.diff since it's upstreamed in 1.5rc1
  already
- Enable '--enalbe-timeline' in nightly builds
* Thu Nov  1 2005 - laca@sun.com
- change version to numeric and introduce %tarball_version
* Fri Oct 21 2005 - dave.lin@sun.com
- Update version from 1.5b1 to 1.5b2 and add patch 307041 from bugzilla
- Change configure option per Leo Sha from developer team
- Add nss header file in development package
* Mon Sep 26 2005 - <halton.huo@sun.com>
- Bump to 1.5b1.
- Move dir mozilla to firefox after tarball unpacking.
* Mon Sep 12 2005 - <laca@sun.com>
- get rid of %builddir as it would be different on Solaris
* Thu Sep 08 2005 - damien.carbery@sun.com
- Change BuildPrereq to BuildRequires, a format that build-gnome2 understands.
* Mon Sep 05 2005 - Dave Lin <dave.lin@sun.com>
- Add patches to remove the specific gtar options
- Set MOZ_PKG_FORMAT=BZ2 to keep consistent of tarball
  format between linux and solaris
* Fri Sep 01 2005 - damien.carbery@sun.com
- Change gtar to tar; add two necessary mkdir's.
* Mon Aug 22 2005 Dave Lin <dave.lin@sun.com>
- initial version of the spec file created
