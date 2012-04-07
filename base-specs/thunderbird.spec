#
# Copyright (c) Sun Microsystems, Inc.
#
%define owner lin
# bugdb: bugzilla.mozilla.org
#

%define OSR LFI#124386 (Mozilla Exec. summary):n/a

#####################################
##   Package Information Section   ##
#####################################

Name:        thunderbird
Summary:     Mozilla Thunderbird Standalone E-mail and Newsgroup Client
Version:     10.0.2
%define tarball_version 10.0.2
Release:     1
Copyright:   MPL
License:     MPL
Group:       Applications/Internet
Distribution:Java Desktop System
Vendor:      Mozilla Foundation
Source:      http://ftp.mozilla.org/pub/mozilla.org/%{name}/releases/%{tarball_version}/source/%{name}-%{tarball_version}.source.tar.bz2
Source1:     thunderbird-icon.png
Source2:     thunderbird.desktop

%if %option_with_lightning
%define lightning_version 1.2.1
%define lightning_tarball_version 1.2.1
%define lightningl10n_tarball_version 1.2.1

Source3:     http://ftp.mozilla.org/pub/mozilla.org/calendar/lightning/releases/%{lightning_tarball_version}/source/lightning-%{lightning_tarball_version}.source.tar.bz2
Source4:     lightning-l10n-%{lightningl10n_tarball_version}.tar.bz2
%endif

%ifarch i386
Source7:     http://www.tortall.net/projects/yasm/releases/yasm-1.1.0.tar.gz
%endif

%if %option_without_moz_nss_nspr
Source8:     nspr-nss-config
%endif

#####################################
##     Package Defines Section     ##
#####################################

%define _unpackaged_files_terminate_build 0
%define lightning_dir "{e2fda1a4-762b-4020-b5ad-a41df1933103}"
%define moz_srcdir comm-release
%define moz_objdir obj-tb
%define moz_l10n_srcdir l10n-release
%define lightning_lang_list bg ca cs da de es-AR es-ES et eu fi fr gl hu id is it ja ko lt nb-NO nl nn-NO pa-IN pl pt-PT ro ru sk sl sq sv-SE tr uk zh-CN zh-HK zh-TW

#####################################
##      Thunderbird patches        ##
#####################################

# owner:lin date:2012-01-17 type:bug
Patch500: thunderbird10-00-bin-libs.diff

# owner:lin date:2011-11-09 type:bug
Patch501: thunderbird8-01-enable-extensions.diff

# owner:hawklu date:2009-09-03 type:bug doo:1114 
Patch526: thunderbird3-26-no-offline-download.diff

# owner:hawklu date:2009-12-31 type:bug bugzilla:537210 
Patch528: thunderbird3-28-sync-toolbar.diff

# owner:migi date:2011-02-14 type:bug d.o.o 14555
Patch538: thunderbird3-38-fade-animations.diff

#####################################
##     Reuse firefox patches       ##
#####################################

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

URL:         http://www.mozilla.com/thunderbird

BuildRoot:   %{_tmppath}/%{name}-%{tarball_version}-build
Prefix:      /usr
Provides:    webclient
Autoreqprov: on

#####################################
##   Package Description Section   ##
#####################################

%description
Mozilla Thunderbird is a standalone e-mail and newsgroup client 
that can be used as a companion to Mozilla Firefox or by itself. 

#####################################
##   Package Preparation Section   ##
#####################################

%prep

%setup -q -c -n %{name}

#
# Prepare toolchains under dir %{name}
#
%ifarch i386
gtar zxf %{SOURCE7}
%endif

#
# Replace lightning source code.
#
%if %option_with_lightning
rm -rf %{moz_srcdir}/calendar
mkdir -p lightning
cd lightning
bzcat %SOURCE3 | tar xf -
cd ..
cp -r lightning/*/calendar %{moz_srcdir}/calendar
rm -rf lightning

# Lightning l10n
bzcat %SOURCE4 | tar xf -
cd %{moz_l10n_srcdir}
# Prepare zh-HK based on zh-TW
cp -rf zh-TW zh-HK
cd ..
%endif

#####################################
##     Adding firefox patches      ##
#####################################
# Ginn: should comment out 12, 13, 14, 26, 36

cd %{moz_srcdir}/mozilla
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
#%patch12 -p1
#%patch13 -p1
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
#%patch26 -p1
%patch27 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
#%patch36 -p1
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

#%if %option_without_moz_nss_nspr
#%patch8 -p1
#%patch24 -p1
#%else
%patch45 -p1
#%endif

#####################################
##     Original adding patches     ##
#####################################

# go back to the thunderbird directory
cd ..  
%patch500 -p1
%patch501 -p1
%patch526 -p1
# %patch528 -p1
%patch538 -p1


#####################################
##      Package Build Section      ##
#####################################

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export PKG_CONFIG_PATH=${_libdir}/pkgconfig:%{_pkg_config_path}
export LDFLAGS="-B direct -z ignore"
export CFLAGS="-xlibmopt"
export OS_DEFINES="-D__USE_LEGACY_PROTOTYPES__"
export CXXFLAGS="-xlibmil -xlibmopt -D_XOPEN_SOURCE=500 -D__EXTENSIONS__"
SRCDIR=$PWD

#
# Build toolchains
#
%ifarch i386
cd yasm*
./configure --prefix=${SRCDIR}/sol_toolchain
gmake
gmake install
export PATH=${SRCDIR}/sol_toolchain/bin:$PATH
#export YASM=${SRCDIR}/sol_toolchain/bin/yasm
#export LIBJPEG_TURBO_AS=${SRCDIR}/sol_toolchain/bin/yasm
cd ${SRCDIR}
%endif

cat << "EOF" > mozconfig.release
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../%{moz_objdir}
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --mandir=%{_mandir}
%if %option_with_debug
ac_add_options --enable-debug
ac_add_options --disable-optimize
#ac_add_options --enable-tests
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
%if %option_without_moz_nss_nspr
# ac_add_options --with-system-nspr
# ac_add_options --with-system-nss
%endif
ac_add_options --enable-startup-notification
EOF

#
# Thunderbird specific
#
cat << "EOF" >> mozconfig.release
ac_add_options --enable-application=mail
# ac_add_options --enable-system-cairo
%if %option_with_lightning
ac_add_options --enable-calendar
ac_add_options --with-l10n-base=../%{moz_l10n_srcdir}
%endif
EOF

export DISABLE_LIGHTNING_INSTALL=1
export BUILD_OFFICIAL=1 
export MOZILLA_OFFICIAL=1
export MOZ_PKG_FORMAT=BZ2
export PKG_SKIP_STRIP=1
export MOZCONFIG=$PWD/mozconfig.release

mkdir -p ${SRCDIR}/%{moz_objdir}

%if %option_without_moz_nss_nspr
cp %{SOURCE8} ${SRCDIR}/%{moz_objdir}
chmod +x ${SRCDIR}/%{moz_objdir}/nspr-nss-config
export NSPR_CONFIG=${SRCDIR}/%{moz_objdir}/nspr-nss-config\ nspr
export NSS_CONFIG=${SRCDIR}/%{moz_objdir}/nspr-nss-config\ nss
%endif

# Build src
cd ${SRCDIR}/%{moz_objdir}
${SRCDIR}/%{moz_srcdir}/configure
make -j $CPUS
# Build package
cd ${SRCDIR}/%{moz_objdir}/mail/installer
make

%install
/bin/rm -rf $RPM_BUILD_ROOT

SRCDIR=$PWD
# Build lightning l10n
%if %option_with_lightning
mv ${SRCDIR}/%{moz_srcdir}/calendar/locales/shipped-locales /tmp/lightning-shipped-locales
for lang in %{lightning_lang_list}
do
    echo $lang >> ${SRCDIR}/%{moz_srcdir}/calendar/locales/shipped-locales
done
cd ${SRCDIR}/%{moz_objdir}/calendar/lightning
make repack-l10n-all
cd ${SRCDIR}
%endif

BUILDDIR=${SRCDIR}/%{moz_objdir}
/bin/mkdir -p $RPM_BUILD_ROOT%{_libdir}
cd $RPM_BUILD_ROOT%{_libdir}
/usr/bin/bzip2 -dc $BUILDDIR/mozilla/dist/thunderbird-*.tar.bz2 | gtar -xf -

/bin/mkdir -p $RPM_BUILD_ROOT%{_bindir}
/bin/ln -s ../lib/thunderbird/thunderbird $RPM_BUILD_ROOT%{_bindir}/thunderbird

%if %option_with_lightning
cd thunderbird/extensions
mkdir %{lightning_dir}
cd %{lightning_dir}
unzip $BUILDDIR/mozilla/dist/xpi-stage/lightning-all.xpi
%endif

/bin/mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
/bin/mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -c -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/thunderbird-icon.png
install -c -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/thunderbird.desktop

# remove local dictionary and share the one that delivered 
# by myspell-dictionary
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries/en-US.dic
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries/en-US.aff
rmdir $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries

%clean
/bin/rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Feb 17 2012 - lin.ma@oracle.com
- Bump to Thunderbird 10.0.2
- Bump to Lightning 1.2.1
* Tue Jan 10 2012 - lin.ma@oracle.com
- Bump to Thunderbird 9.0.1
- Bump to Lightning 1.1.1
- Update l10n list
- Remove thunderbird3-11-jemalloc-shared-library.diff and thunderbird3-22-use-system-theora-and-sqlite.diff
* Tus Nov 23 2011 - lin.ma@oracle.com
- Bump to Thunderbird 8.0.
* Fri Sep 16 2011 - lin.ma@oracle.com
- Fix CR#7090043 and CR#7090554
* Wed Sep 07 2011 - lin.ma@oracle.com
- Bump to 6.0.2. Uses explict lightning lang list.
- Remove zh-HK lang hack
* Fri July 18 2011 - lin.ma@oracle.com
- Bump to 6.0
* Fri July 8 2011 - lin.ma@oracle.com
- Bump to 5.0
* Fri Jun 24 2011 - lin.ma@oracle.com
- Bump to 3.1.11
* Wen May 04 2011 - yun-tong.jin@oracle.com
- Bump to 3.1.10
* Tue Mar 09 2011 - brian.lu@oracle.com
- Bump to 3.1.9
* Mon Feb 14 2011 - Michal.Pryc@Oracle.Com
- Add thunderbird3-38-fade-animations.diff to fix d.o.o. 14555.
* Fri Dec 10 2010 - brian.lu@oracle.com
- Bump to 3.1.7
* Fri Nov 19 2010 - ginn.chen@oracle.com
- Add thunderbird3-36-gtk-dialog_a11y.diff to fix d.o.o. 17425.
* Tue Sep 28 2010 - brian.lu@sun.com
- Bump to 3.1.4
* Fri Sep 10 2010 - brian.lu@sun.com
- Bump to 3.1.2 CR6983039
* Thu Sep 02 2010 - brian.lu@sun.com
- Fix d.o.o 16060
* Mon Aug 02 2010 - brian.lu@sun.com
- Bump to 3.1.1
* Thu Jul 15 2010 - brian.lu@sun.com
- Fix d.o.o 16490
* Tue Jul 13 2010 - brian.lu@sun.com
- Fix bug d.o.o 16285
* Wed Jun 30 2010 - brian.lu@sun.com
- Bump to 3.1
* Fri Jun 18 2010 - brian.lu@sun.com
- Bump to 3.0.5
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Sat May 08 2010 - brian.lu@sun.com
- Fix d.o.o 15616
* Sat Apr 17 2010 - brian.lu@sun.com
- Bump to 3.0.4
* Wed Mar 10 2010 - brian.lu@sun.com
- Add $ORIGIN to --with-rpath
* Tue Mar 09 2010 - brian.lu@sun.com
- Add --with-rpath to fix bug d.o.o 14849
  Remove patch thunderbird3-30-using-sqlite-3-6-17.diff
* Tus Mar 02 2010 - ginn.chen@sun.com
- Bump to Thunderbird 3.0.3.
* Thu Feb 04 2010 - ginn.chen@sun.com
- Add thunderbird3-12-nspr_use_zone_allocator.diff.
* Tue Feb 02 2010 - brian.lu@sun.com
- Using chrome.manifest that supports mutli languages
* Mon Jan 25 2010 - brian.lu@sun.com
- Bump to 3.0.1
* Wed Jan 13 2010 - brian.lu@sun.com
- bug d.o.o 13561 is fixed in 1.0b1 
  Remove the patch thunderbird3-30-timezone.diff
* Thu Dec 31 2009 - brian.lu@sun.com
- Add two patches:
  thunderbird3-28-sync-toolbar.diff
  thunderbird3-29-account-setup.diff
* Fri Dec 18 2009 - ginn.chen@sun.com
- Bump lighting to 1.0b1rc1.
* Wed Dec 16 2009 - ginn.chen@sun.com
- Add thunderbird3-27-startup-notification.diff
* Mon Dec 14 2009 - brian.lu@sun.com
- Define lightning_version
* Thu Dec 08 2009 - brian.lu@sun.com
- Bump to 3.0
* Wed Dec 02 2009 - ginn.chen@sun.com
- Bump to Thunderbird 3.0rc2.
* Wed Nov 25 2009 - ginn.chen@sun.com
- Bump to Thunderbird 3.0rc1.
* Fri Nov 13 2009 - ginn.chen@sun.com
- Remove thunderbird.cfg, thunderbird3-02-disable-online-update.diff
  disable-updater should be enough.
- Update thunderbird3-11-jemalloc-shared-library.diff
* Web Sep 23 2009 - ginn.chen@sun.com
- Remove configure files.
* Wed Sep 23 2009 - brian.lu@sun.com
- Remove the upstreamed patch thunderbird3-23-bug504043.diff
  and thunderbird3-25-downloadable-font.diff
- Update patch thunderbird3-26-no-offline-download.diff
- Bump to beta4
* Tue Sep 22 2009 - brian.lu@sun.com
- Update patch thunderbird3-26-no-offline-download.diff
* Fri Sep 18 2009 - ginn.chen@sun.com
- Add patch thunderbird3-17-compiler-workaround-2.diff
* Thu Sep 03 2009 - brian.lu@sun.com
- Add patch thunderbird3-26-no-offline-download.diff
* Wed Jul 29 2009 - ginn.chen@sun.com
- Add patch thunderbird3-25-downloadable-font.diff
* Thu Jul 23 2009 - ginn.chen@sun.com
- Update thunderbird3-22-use-system-theora-and-sqlite.diff
  Fix build issue with system sqlite library.
* Thu Jul 23 2009 - brian.lu@sun.com
- Bump to 3.0b3
  Remove following upstreamed patches:
  thunderbird3-03-js.diff
  thunderbird3-06-font-config.diff
  thunderbird3-07-pango-1-23.diff
  thunderbird3-08-im-context-not-match.diff
  thunderbird3-09-rename-nsSelectionBatcher.diff
  thunderbird3-10-bigendian.diff
  thunderbird3-13-js-dtrace.diff
  thunderbird3-14-xinerama.diff
  thunderbird3-17-runmozilla.diff
  thunderbird3-19-small-migration-wizard-window.diff

  Update following patches:
  thunderbird3-16-delay-stopping-realplayer.diff
  thunderbird3-20-system-nss-nspr.diff
* Wed Jun 17 2009 - brian.lu@sun.com
- Enable debug mode when "--with-debug" is specified
* Wed Jun 02 2009 - brian.lu@sun.com
- Change bugzilla:9112 to doo:9112 and bugzilla:8471 to doo:8471
* Mon May 25 2009 - ginn.chen@sun.com
- Add thunderbird3-20-system-nss-nspr.diff
      thunderbird3-21-sunaudio-sparc.diff
      thunderbird3-22-use-system-theora.diff
* Tue Mar 31 2009 - brian.lu@sun.com
- Fix bug 7723
* Mon Mar 30 2009 - ginn.chen@sun.com
- Remove thunderbird3-12-ldap-crash.diff, this bug is gone.
* Fri Mar 06 2009 - ginn.chen@sun.com
- Copy firefox3-25-pango-1-23.diff to thunderbird3-07-pango-1-23.diff
* Fri Mar 06 2009 - brian.lu@sun.com
- Replace the patch thunderbird3-07-pango-1-23.diff with 
  the  patch firefox3-25-pango-1-23.diff 
* Thu Mar 05 2009 - ginn.chen@sun.com
- add option to use system cairo and jpeg
* Wed Mar 04 2009 - ginn.chen@sun.com
- copy firefox3-*.diff to thunderbird3-*.diff
- use configure in ext-sources
* Mon Mar 02 2009 - alfred.peng@sun.com
- Patch updates for Thunderbird 3.0b2.
* Fri Feb 27 2009 - brian.lu@sun.com
- bump to Thunderbird 3.0b2
* Thu Feb 19 2009 - brian.lu@sun.com
- Fix the issue caused by pango upgrade
* Fri Jan 23 2009 - brian.lu@sun.com
- Fix the bug 6187
* Fri Jan 16 2009 - brian.lu@sun.com
-  Change the bugzilla ID of thunderbird-13-ldap-crash.diff to 374731
* Wed Dec 31 2008 - brian.lu@sun.com
- Replace the patch thunderbird-24-rename-selectionBacher.diff
  with thunderbird-25-allow-muldefs.diff
* Mon Dec 22 2008 - brian.lu@sun.com
- Upgrade to 3.0b1
* Tue Dec 02 2008 - brian.lu@sun.com
- Fix the bug CR677345
* Mon Oct 13 2008 - ginn.chen@sun.com
- Change /bin/tar to tar.
* Oct 10 2008 - alfred.peng@sun.com
- Add thunderbird-21-ksh.diff for indiana only to fix bugster CR6750518.
* Man 06 2008 - brian.lu@sun.com
- Bump lightning to 0.9 
* Sat Sep 27 2008 - ginn.chen@sun.com
- Bump to 2.0.0.17
* Fri Sep 26 2008 - brian.lu@sun.com
- Fix the bug CR6752288
* Tue Jul 29 2008 - brian.lu@sun.com
- bump to 2.0.0.16
* Mon Jul 21 2008 - ginn.chen@sun.com
- Add bugdb info.
* Mon Jun 02 2008 - ginn.chen@sun.com
- Add indiana branding patch: thunderbird-18-remove-hardcoded-fontname.diff
* Mon May 05 2008 - dave.lin@sun.com
- bump to 2.0.0.14
* Thu April 24 2008 - brian.lu@sun.com
- bump lightning to 0.8
* Wed Mar 26 2008 - brian.lu@sun.com
- Fix bug CR6640830
* Thu Feb 28 2008 - dave.lin@sun.com
- bump to TB 2.0.0.12
* Fir Nov 28 2007 - evan.yan@sun.com
- replace thunderbird-08-locale.diff with mozilla-09-locale.diff, to correct our
  way of supporting multi-language
* Mon Nov 19 2007 - dave.lin@sun.com
- bump to TB 2.0.0.9
- remove patch thunderbird-16-crash-with-some-themes.diff since it has been upstreamed
* Tue Nov 13 2007 - brian.lu@sun.com
- Add patch, thunderbird-16-crash-with-some-themes.diff 
  to fix 'thunderbird crashing under some themes' bug CR6586103 
* Fri Nov 02 2007 - dave.lin@sun.com
- bump lightning to 0.7
* Fri Aug 03 2007 - dave.lin@sun.com
- bump to 2.0.0.6
* Mon Jun 23 2007 - dave.lin@sun.com
- bump to 2.0.0.5
* Thu Jun 21 2007 - damien.carbery@sun.com
- Add patch, mozilla-08-cairo-update.diff, to update the private copy of
  cairo.h used in the build.
* Tue June 05 2007 - brian.lu@sun.com
- Fix the bug CR6284006: GConf Error: Bad key or directory name: "desktop/gnome/url-handlers/GMT+00/command": `+' messages 
* Mon Apr 30 2007 - dave.lin@sun.com
- remove local dictionary and use the one delivered by myspell-dictionary(CR6218511)
* Thu Apr 27 2007 - brian.lu@sun.com
- add patch to grey out "Check for Updates" in Thunderbird menu since it's not supported
* Sat Apr 21 2007 - dave.lin@sun.com
- Bump to 2.0.0.0
* Thu Apr 12 2007 - dave.lin@sun.com
- bump to 2.0.0.0rc1, removed the patches thunderbird-11-drag-and-drop.diff,
  thunderbird-12-defaultAccount.diff which are upstreamed in this release
* Thu Apr 12 2007 - dave.lin@sun.com
- disable update feature in Thunderbird menu since it's not supported
  on Solaris so far(CR#6542910)
* Wed Mar 23 2007 - brian.lu@sun.com 
- Fix the bug CR6535724:Thunderbird crashes with LDAP in snv 60 
* Mon Mar 12 2007 - brian.lu@sun.com 
- Fix the bug CR6530327
* Sat Mar 10 2007 - dougs@truemail.co.th
- Fixed URL for lightning
* Sat Mar 03 2007 - dave.lin@sun.com
- bump lightning version to 0.3.1
* Thu Feb 01 2007 - brian.lu@sun.com
- fix drag and drop crashing bug CR6519257 
- bugzilla id 367203. The patch has been put into upstream
* Sun Jan 28 2007 - laca@sun.com
- add full download url for lightning
* Fri Jan 26 2007 - dave.lin@sun.com
- enable lightning extension(0.3) in Thunderbird
* Wed Jan 24 2007 - dave.lin@sun.com
- bump version to 2.0b2
* Thu Dec 28 2006 - dave.lin@sun.com
- change the patch type to branding for some patches in patch comments
- bump version to 2.0b1 and remove mozilla-03-s11s-smkfl.diff, 
  mozilla-04-s11x-smkfl.diff since they're upstreamed in that branch
* Fri Nov 17 2006 - dave.lin@sun.com
- add patch comments
* Mon Nov 13 2006 - dave.lin@sun.com
- change the version to 1.5.0.8 since 2.0a1 could not be able to integrated 
  into SNV, and add patches mozilla-03-s11s-smkfl.diff, mozilla-04-s11x-smkfl.diff 
  back because they're not upstreamed in the branch that for Thunderbird 1.5.x
* Thu Sep 07 2006 - dave.lin@sun.com
- add patch thunderbird-10-no-pkg-files.diff to remove patch checker scripts
  since it's unnecessary to deliver them with the bundled version
- change the version 2.0a1 to 2.0 to comply WOS integration rules
- re-organize the patch list
* Mon Aug 28 2006 - dave.lin@sun.com
- create symbol link libnssckbi.so -> /usr/lib/mps/libnssckbi.so
  to fix bug CR#6459752
* Tue Aug 08 2006 - dave.lin@sun.com
- bump version to 2.0a1
- remove the patch mozilla-03-s11s-smkfl.diff, mozilla-04-s11x-smkfl.diff
  which have been fixed in 2.0a1
- change to xpinstall/packager to run the make to generate the binary tarball
* Mon Jul 31 2006 - dave.lin@sun.com
- bump to 1.5.0.5
* Fri Jul 07 2006 - dave.lin@sun.com
- add patch mozilla-07-no-ldlibpath.diff to remove the LD_LIBRARY_PATH in
- change to "disable-static, enable-shared" per Brian Lu
* Wed Jun 21 2006 - dave.lin@sun.com
- remove patch thunderbird-07-ldap-prefs.diff to fix bug CR#6344861
* Fri Jun 02 2006 - dave.lin@sun.com
- bump src version to 1.5.0.4
* Sat Apr 29 2006 - halton.huo@sun.com
- Add patch thunderbird-09-no-nss-nspr.diff to not deliver the nss,nspr
* Fri Apr 27 2006 - damien.carbery@sun.com
- Remove patch 9 as it is not in svn and breaks build.
* Fri Apr 27 2006 - dave.lin@sun.com
- change to not deliver the devel pkg
- add patch thunderbird-09-no-nss-nspr.diff to not deliver the nss,nspr
  libraries, and use firefox's instead 
- remove patch mozilla-06-skip-strip.diff, use another simple way to skip
  strip instead, setting PKG_SKIP_STRIP=1 
* Fri Apr 21 2006 - dave.lin@sun.com
- bump to 1.5.0.2, remove patch 06 thunderbird-06-save-all-attach.diff,
  which is already upstreamed
* Fri Apr 14 2006 - dave.lin@sun.com
- add patch mozilla-06-skip-strip.diff to make no stripped libraries 
- add patch firefox-13-locale.diff to make firefox automatically
  pick up locale setting from user environment and start up in
  that locale
* Thu Apr 13 2006 - dave.lin@sun.com
- Changed the installation location from "/usr/sfw/lib" to "/usr/lib"
  on Solaris

* Fri Mar 10 2006 -halton.huo@sun.com
- Add patch thunderbird-06-save-all-attach.diff to fix 6373061.
- Add patch thunderbird-07-ldap-prefs.diff to fix CR6344861.

* Tue Jan 17 2006 - dave.lin@sun.com
- Bump tarball version to 1.5
- add two configure options --enable-static, --disable-shared
- to get rid of intermedia shared libraries  
- disable parallel build option 

* Tue Nov 08 2005 - dave.lin@sun.com
- Bump tarball version to 1.5rc1
- Remove the patch mozilla-07-bz307041.diff since it's upstreamed in 1.5rc1 already

* Thu Nov  1 2005 - laca@sun.com
- change version to numeric and introduce %tarball_version

* Fri Oct 21 2005 - <halton.huo@sun.com>
- Bump to 1.5b2.
- Add patch 307041 from bugzilla.

* Mon Sep 26 2005 - <halton.huo@sun.com>
- Bump to 1.5b1.
- Move dir mozilla to thunderbird after tarball unpacking.

* Thu Sep 08 2005 - damien.carbery@sun.com
- Change BuildPrereq to BuildRequires, a format that build-gnome2 understands.

* Mon Sep 05 2005 - Dave Lin <dave.lin@sun.com>
- Add patches to remove the specific gtar options
- Set MOZ_PKG_FORMAT=BZ2 to keep consistent of tarball
  format between linux and solaris

* Fri Sep 02 2005 - damien.carbery@sun.com
- Change gtar to tar and rework tar command.

* Mon Aug 22 2005 - Dave Lin <dave.lin@sun.com>
- initial version of the spec file created

