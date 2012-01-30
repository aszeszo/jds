#
# spec file for xscreensaver packages
#
# SVR4 names:                    pkg(5)/IPS names:
#  SUNWxscreensaver              desktop/xscreensaver
#  SUNWxscreensaver-hacks        desktop/xscreensaver/hacks
#  SUNWxscreensaver-hacks-gl     desktop/xscreensaver/hacks/hacks-gl
#  SUNWrss-glx                   desktop/xscreensaver/hacks/rss-glx
#
# includes module(s): xscreensaver, rss-glx
#
# Copyright (c) 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# packages are under the same license as the packages themselves.
#
%define owner alanc
#
%include Solaris.inc
%include l10n.inc

%define OSR 12732:5.0.1

%define src_name xscreensaver
%define src_version 5.12
%define src_url http://www.jwz.org/xscreensaver
%define src_dir %{src_name}-%{src_version}

%define pkg5_name_base          desktop/xscreensaver
%define pkg5_name_hacks         desktop/xscreensaver/hacks
%define pkg5_name_hacks_gl      desktop/xscreensaver/hacks/hacks-gl
%define pkg5_name_hacks_rss     desktop/xscreensaver/hacks/rss-glx

# Publisher name used in .p5i files to install hack packages
%{?pkg5_publisher:#}%define pkg5_publisher solaris

%{?sf_download:#}%define sf_download http://downloads.sourceforge.net
%define rss_name rss-glx
%define rss_version 0.9.0
%define rss_url %{sf_download}/rss-glx
%define rss_dir %{rss_name}_%{rss_version}

%define rss_OSR 4342:0.8.1

%define app_defaults_dir %{_datadir}/X11/app-defaults
%define xss_libdir %{_libdir}/xscreensaver

Name:                    SUNWxscreensaver
IPS_package_name:        %{pkg5_name_base}
Meta(info.classification): %{classification_prefix}:System/X11
Summary:                 XScreenSaver - Screen Saver/Locker for the X Window System
SUNW_Desc:               XScreenSaver is two things: it is both a large collection of screen savers (distributed in the 'hacks' packages) and it is also the framework for blanking and locking the screen (this package).
Version:                 %{src_version}
SUNW_BaseDir:            /
SUNW_Copyright:          %{name}.copyright
License:                 MIT
BuildRoot:               %{_tmppath}/%{name}-%{src_version}-build
Source:                  %{src_url}/%{src_dir}.tar.gz
Source1:                 %{rss_url}/%{rss_dir}.tar.bz2
Source2:                 xscreensaver-opensolaris-logo.png
%if %option_with_sun_branding
Source3:                 solaris-lockscreen-logos-1.0.tar.bz2
%endif
Source4:                 suntouch-manpages.pl
Source5:         %{src_name}-po-sun-%{po_sun_version}.tar.bz2
# .p5i files are used to offer links to install the hack packages in
# the xscreensaver-demo program when they're not installed (which they're
# not after a LiveCD install, since they don't fit) - bugzilla:10681
Source6:                 xscreensaver-hacks.p5i.in
Source7:                 xscreensaver-hacks-gl.p5i.in
Source8:                 rss-glx.p5i.in
Source9:                 xscreensaver.desktop

# date:2008-12-15 owner:alanc type:bug bugster:6785377
Patch1: xscreensaver-01-intltool.diff
# date:2006-05-10 owner:alanc type:branding bugster:6526791
# bugster:4871833,6368607,6652454
Patch2: xscreensaver-02-Solaris.app-defaults.diff
# date:2006-05-10 owner:alanc type:branding
Patch3: xscreensaver-03-GNOME-desktop.diff
# date:2006-05-10 owner:alanc type:branding bugster:6770336 bugzilla:10681
Patch4: xscreensaver-04-solaris-paths.diff
# date:2010-11-12 owner:alanc type:feature
Patch5: xscreensaver-05-atoms.diff
# date:2006-05-10 owner:alanc type:feature
# bugster:6735203,6673036,6484604,6673036,6670025,6611183,6478362,6417168
# bugster:6346056,6308859,6269444,6182506,6237901,5039878,6178584,5039876
# bugster:5077993,5077989,5079870,4931584,5039876,5059445,4782515,4783832
# bugster:6845751,5083155,6176524,6541240,6839026,6825374,6769901,6857559
# bugster:6475285,6670659,6461887,6395649,6520014,6736157,6573182,6203951
Patch6: xscreensaver-06-gtk-lock.diff
# date:2006-05-10 owner:ma54148 type:feature bugster:4849641
Patch7: xscreensaver-07-allow-root.diff
# date:2006-05-10 owner:alanc type:feature bugster:5077981,6176524
Patch8: xscreensaver-08-passwdTimeout-pref.diff
# date:2006-05-10 owner:alanc type:feature
Patch9: xscreensaver-09-dpms.diff
# date:2006-05-10 owner:johnfisc type:feature
# bugster:6673036,6451477,6698996,6845488,6845488
Patch10: xscreensaver-10-trusted.diff
# date:2006-06-07 owner:ma54148 type:feature
# bugster:5015296,6417168,6654320,7008058
Patch11: xscreensaver-11-pam_audit.diff
# date:2006-08-09 owner:alanc type:branding
Patch12: xscreensaver-12-barcode-hack.diff
# date:2006-08-09 owner:alanc type:branding
Patch13: xscreensaver-13-glsnake.diff
# date:2008-01-03 owner:samlau type:bug bugster:6610282
Patch14: xscreensaver-14-bug-6610282.diff
# date:2008-02-11 owner:uejio type:bug bugster:6583181
Patch15: xscreensaver-15-bug-6583181.diff
# date:2008-02-27 owner:ma54148 type:bug bugster:6585644
Patch16: xscreensaver-16-notice_events.diff
# date:2008-06-03 owner:uejio type:bug bugster:6583247
Patch17: xscreensaver-17-bug-6583247.diff
# date:2009-02-05 owner:alanc type:bug bugster:4802301
Patch18: xscreensaver-18-bug-4802301.diff
# date:2009-07-31 owner:bp230705 type:bug bugster:6859039
Patch19: xscreensaver-19-bug-6859039.diff
# date:2010-06-30 owner:arvind type:bug bugster:6964562
Patch20: xscreensaver-20-bug-6964562.diff
# date:2010-11-09 owner:alanc type:bug bugzilla:16559
Patch21: xscreensaver-21-verbose.diff
# date:2011-05-10 owner:arvind type:bug bugster:7033508
Patch22: xscreensaver-22-bug-7033508.diff

# date:2008-03-07 owner:alanc type:branding
Patch101: rss-glx-101-matrixview.diff
# date:2008-03-07 owner:alanc type:branding
Patch102: rss-glx-102-install-util.diff

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWcslr
Requires: SUNWglib2
Requires: SUNWgnome-a11y-libs
Requires: SUNWgnome-component
Requires: SUNWgnome-config
Requires: SUNWgtk2
Requires: SUNWlibatk
Requires: SUNWlibglade
Requires: SUNWlibmsr
Requires: SUNWlxmlr
Requires: SUNWpango
BuildRequires: runtime/perl-512
BuildRequires: SUNWxwplt
BuildRequires: SUNWarc
BuildRequires: SUNWbtool
BuildRequires: SUNWhea
BuildRequires: SUNWggrp
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWgnome-a11y-libs-devel
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWlibatk-devel
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWlxml-devel
BuildRequires: SUNWpango-devel
BuildRequires: SUNWtoo
BuildRequires: SUNWxwinc
BuildRequires: system/library/libdbus
BuildRequires: consolidation/desktop/gnome-incorporation

%package hacks
IPS_package_name:        %{pkg5_name_hacks}
Meta(info.classification): %{classification_prefix}:System/X11
Summary:                 XScreenSaver - display mode modules
SUNW_Desc:               Modules that provide different display modes (hacks) for XScreenSaver
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}-hacks.copyright
Version:                 %{src_version}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %{name}
Requires: SUNWcslr
Requires: SUNWglib2
Requires: SUNWgtk2
Requires: SUNWlibmsr
BuildRequires: SUNWxwplt

%package hacks-gl
IPS_package_name:        %{pkg5_name_hacks_gl}
Meta(info.classification): %{classification_prefix}:System/X11
Summary:                 XScreenSaver - OpenGL display mode modules
SUNW_Desc:               Modules that provide different OpenGL-based display modes (hacks) for the screen saver
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}-hacks-gl.copyright
License:                 MIT, GPL v2
Version:                 %{src_version}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %{name}
Requires: SUNWcslr
Requires: SUNWglib2
Requires: SUNWgtk2
Requires: SUNWlibmsr
Requires: SUNWxorg-mesa
BuildRequires: SUNWxwplr
BuildRequires: SUNWxwplt
%define opengl_dir /usr

%package -n SUNWrss-glx
IPS_package_name:        %{pkg5_name_hacks_rss}
Meta(info.classification): %{classification_prefix}:System/X11
Summary:                 XScreenSaver - Really Slick ScreenSaver OpenGL display modules
SUNW_Desc:               Modules that provide additional OpenGL-based display modes (hacks) for XScreenSaver
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWrss-glx.copyright
License:                 GPL v2
Version:                 %{rss_version}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %{name}
Requires: SUNWbzip
Requires: SUNWcslr
Requires: SUNWimagick
Requires: SUNWlibC
Requires: SUNWlibmsr
Requires: SUNWxorg-mesa
BuildRequires: SUNWxwplr
BuildRequires: SUNWxwplt

%package l10n
Summary:                 XScreenSaver - l10n content
Requires: %{name}

%prep
%setup -q -n %{src_dir}
bzcat %SOURCE5 | tar xf -
cd po-sun; make; cd ..
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
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

chmod a+x install-sh configure

cp %SOURCE2 driver/opensolaris-logo.png
%if %option_with_sun_branding
bzcat %SOURCE3 | tar xf -
mv solaris-lockscreen-logos/unlock-logo.png driver/unlock-logo.png
mv solaris-lockscreen-logos/trusted-logo.png driver/trusted-logo.png
%else
ln -s opensolaris-logo.png driver/unlock-logo.png
ln -s opensolaris-logo.png driver/trusted-logo.png
%endif

# Adjust man pages to Solaris standards:
#  - add paths to synopsis
#  - add attributes section to end with package info & stability
%define suntouch_manpages_cmd /usr/perl5/bin/perl %SOURCE4
%{suntouch_manpages_cmd} \
    -a '{Availability, %{pkg5_name_base}}' \
    -a '{Interface Stability, Volatile}' \
    -p %{_prefix}/bin/ \
    driver/xscreensaver.man \
    driver/xscreensaver-command.man \
    driver/xscreensaver-demo.man
%{suntouch_manpages_cmd} \
    -a '{Availability, %{pkg5_name_base}}' \
    -a '{Interface Stability, Private}' \
    -p %{xss_libdir}/bin/ \
    driver/xscreensaver-get*.man \
    driver/xscreensaver-text.man
%{suntouch_manpages_cmd} \
    -a '{Availability, %{pkg5_name_hacks}}' \
    -a '{Interface Stability, Private}' \
    -p %{xss_libdir}/hacks/ \
    hacks/*.man
%{suntouch_manpages_cmd} \
    -a '{Availability, %{pkg5_name_hacks_gl}}' \
    -a '{Interface Stability, Private}' \
    -p %{xss_libdir}/hacks/ \
    hacks/glx/*.man

cp %{SOURCE6} driver/
cp %{SOURCE7} driver/
cp %{SOURCE8} driver/

%setup1 -q -n %{rss_name}_%{rss_version}

%patch101 -p1
%patch102 -p1

%{suntouch_manpages_cmd} \
    -a '{Availability, %{pkg5_name_hacks_rss}}' \
    -a '{Interface Stability, Private}' \
    -p %{xss_libdir}/hacks/ \
    src/*.1


# Clear pictures we don't want in build
rm -f src/matrixview_textures/cpics
touch src/matrixview_textures/cpics

%build

CPUS=$(/usr/sbin/psrinfo | grep -c on-line)
if test "x${CPUS}" = "x" -o ${CPUS} = 0; then
     CPUS=1
fi
MAKEFLAGS=-j${CPUS}

# Mapfile flags copied from X - these are generically good for all libraries
# and applications and should probably move to Solaris.inc in the future.
# See the comments in each mapfile for a description of what it does.

# Mark the stack and as much of heap/data as possible non-executable,
# so that it's harder for attackers to exploit buffer overflows
# SPARC architecture requires PLT section in .data be executable, so
# we can only make .bss, not all of .data no-exec on SPARC

%define mapfile_noexbss         -Wl,-M,/usr/lib/ld/map.noexbss
%ifarch sparc
%define mapfile_noexdata        %{mapfile_noexbss}
%else
%define mapfile_noexdata        -Wl,-M,/usr/lib/ld/map.noexdata
%endif
%define mapfile_noexstack       -Wl,-M,/usr/lib/ld/map.noexstk
# Alignment directives for more efficient memory/page mappings
%define mapfile_pagealign       -Wl,-M,/usr/lib/ld/map.pagealign
%define mapfile_heapalign       -Wl,-M,/usr/lib/ld/map.bssalign

# Flags useful for libraries, shared objects, and programs
%define mapfiles_for_all        %{mapfile_pagealign} %{mapfile_noexdata}
# Flags only useful for programs, not libraries/shared objects
%define mapfiles_for_progs      %{mapfile_heapalign} %{mapfile_noexstack} %{mapfile_noexbss}

# XScreenSaver

PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

export PATH=/usr/perl5/bin:${PATH}
export PERL=/usr/perl5/bin/perl
export XGETTEXT=/usr/gnu/bin/xgettext
export GNOME_DATADIR='%{xss_libdir}/config'
export GLADE_DATADIR='%{xss_libdir}/config'

cd %{_builddir}/%{src_dir}

# Force building with mesa headers & libraries to make sure we build the
# same on all systems, whether or not proprietary GL from Sun or nVidia is
# also installed and don't end up accidentally depending on those.
# Unfortunately, xscreensaver is hardcoded to use <GL/gl.h> style paths,
# so we create local install path to work around that.
mkdir -p mesa/GL
ln -s /usr/include/mesa/*.h mesa/GL
%define mesa_includes -I%{_builddir}/%{src_dir}/mesa
%define mesa_libpath -L/usr/lib/mesa

# Additional optimization flags, to make the hacks show off the hardware
# better and because for just a screensaver display we can get away with
# using optimizations that may change strict correctness of floating point ops.
%if %cc_is_gcc
%define extra_opt_flags -funsafe-math-optimizations
%define c_warning_flags -Wall
%define cxx_warning_flags -Wall
%else
%define extra_opt_flags -fsimple=2 -nofstore -xlibmil -xprefetch
%define c_warning_flags -v
%define cxx_warning_flags +w2
%endif

export CFLAGS="%c_warning_flags %optflags %extra_opt_flags %mesa_includes"
export CXXFLAGS="%cxx_warning_flags %cxx_optflags %extra_opt_flags %mesa_includes"
export LDFLAGS="%mesa_libpath %_ldflags %mapfiles_for_all %mapfiles_for_progs"

# Several patches change configure.in & Makefile.in files, so autoreconf
autoreconf -v --install --force

./configure --enable-maintainer-mode \
 --with-gnome --enable-gtk-doc --with-gtk2=/usr --with-pixbuf=/usr \
 --enable-locking --with-pam=/usr --without-shadow --without-kerberos \
 --with-dpms --with-xinput-ext --with-randr-ext --enable-root-passwd \
 --with-gl=%{opengl_dir}  --without-motif --with-jpeg=/usr \
 --prefix=%{_prefix} \
 --datadir=%{_datadir} \
 --mandir=%{_mandir} \
 --localstatedir=%{_localstatedir} \
 --libexecdir=%{xss_libdir}/bin \
 --with-hackdir=%{xss_libdir}/hacks \
 --with-configdir=%{xss_libdir}/config/control-center-2.0 \
 --with-image-directory=%{_datadir}/pixmaps/backgrounds \
 --with-text-file=/etc/motd \
 --with-x-app-defaults=%{app_defaults_dir}

# Update potfiles.in to pick up our added sources like lock-Gtk.c
cd po
make generate_potfiles_in -o Makefile
make POTFILES -o Makefile
# FIXME: hack, add "-o Makefile" to avoid looping.
make generate_potfiles_in POTFILES xscreensaver.pot -o Makefile

cd %{_builddir}/%{src_dir}

# FIXME: hack: stop the build from looping
touch po/stamp-it

make ${MAKEFLAGS}

cd %{_builddir}/%{src_dir}/driver
for f in *.p5i.in ; do
    sed 's/@PUBLISHER@/%{pkg5_publisher}/' $f > $(basename $f .in)
done

# RSS-GLX hacks
cd %{_builddir}/%{rss_dir}
./configure \
 --disable-sound \
 --prefix=%{xss_libdir} \
 --bindir='$(prefix)/hacks' \
 --localstatedir=%{_localstatedir} \
 --mandir=%{_mandir} \
 --with-configdir=%{xss_libdir}/config/control-center-2.0 \
 CPPFLAGS="-D_FILE_OFFSET_BITS=64"

make ${MAKEFLAGS}

%install

rm -rf ${RPM_BUILD_ROOT}

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart
cp -p %{SOURCE9} ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart
chmod 444 ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart/xscreensaver.desktop

cd %{_builddir}/%{src_dir}
chmod a+x install-sh intltool-*
make -e install_prefix=${RPM_BUILD_ROOT} SHELL=/bin/bash install
cp -pf driver/*-logo.png ${RPM_BUILD_ROOT}%{xss_libdir}/config/
cp -pf utils/images/logo-180.gif ${RPM_BUILD_ROOT}%{xss_libdir}/config/
cp -pf driver/*.p5i ${RPM_BUILD_ROOT}%{xss_libdir}/config/

mv ${RPM_BUILD_ROOT}%{_bindir}/xscreensaver-get* \
   ${RPM_BUILD_ROOT}%{_bindir}/xscreensaver-text \
   ${RPM_BUILD_ROOT}%{xss_libdir}/bin

# Remove hacks we've chosen not to ship at all for various reasons
REMOVED_HACKS="extrusion flyingtoasters ljlatest sonar webcollage"
for h in ${REMOVED_HACKS} ; do
    rm -f ${RPM_BUILD_ROOT}%{xss_libdir}/hacks/${h} \
          ${RPM_BUILD_ROOT}%{_mandir}/man6/${h}.6 \
          ${RPM_BUILD_ROOT}%{xss_libdir}/config/control-center-2.0/${h}.xml
done
rm -f ${RPM_BUILD_ROOT}%{xss_libdir}/hacks/webcollage-helper

cd %{_builddir}/%{rss_dir}
make install DESTDIR=${RPM_BUILD_ROOT}
# Move rss-glx man pages to section 6 (games/amusements) to match xscreensaver
for m in */*.1 ; do
    mv ${RPM_BUILD_ROOT}%{_mandir}/man1/$(basename $m) \
       ${RPM_BUILD_ROOT}%{_mandir}/man6/$(basename $m .1).6 ; \
done
# Don't need to ship static libraries in the package
rm ${RPM_BUILD_ROOT}%{xss_libdir}/lib/lib*.a \
   ${RPM_BUILD_ROOT}%{xss_libdir}/lib/lib*.la
rmdir ${RPM_BUILD_ROOT}%{xss_libdir}/lib

# Run script to add rss-glx hacks to XScreenSaver app-defaults, then delete it
${RPM_BUILD_ROOT}%{xss_libdir}/hacks/rss-glx_install.pl \
  ${RPM_BUILD_ROOT}%{app_defaults_dir}/XScreenSaver
chmod 0444 ${RPM_BUILD_ROOT}%{app_defaults_dir}/XScreenSaver
rm ${RPM_BUILD_ROOT}%{xss_libdir}/hacks/rss-glx_install.pl

cd ${RPM_BUILD_ROOT}

# Make compatibility links for SUNWxscreensaver
install -m 755 -d usr/X11

install -m 755 -d usr/X11/bin
ln -s ../../bin/xscreensaver \
      ../../bin/xscreensaver-command \
      ../../bin/xscreensaver-demo \
      usr/X11/bin

install -m 755 -d usr/X11/lib
ln -s ../../lib/xscreensaver usr/X11/lib

install -m 755 -d usr/X11/lib/X11/app-defaults
ln -s ../../../../share/X11/app-defaults/XScreenSaver \
      usr/X11/lib/X11/app-defaults

# This function prints a list of things that get installed.
# It does this by parsing the output of a dummy run of "make install".
# Borrowed/modified from Fedora Project RPM for xscreensaver at
# http://cvs.fedoraproject.org/viewvc/rpms/xscreensaver/devel/xscreensaver.spec
list_files() {
   echo '%%defattr(-,root,bin)'
   echo '%%dir %%attr(0755, root, bin) %%{xss_libdir}'
   echo '%%dir %%attr(0755, root, bin) %%{xss_libdir}/hacks'
   echo '%%dir %%attr(0755, root, bin) %%{xss_libdir}/config/control-center-2.0'
   echo '%%dir %%attr(0755, root, sys) %%{_datadir}'
   echo '%%dir %%attr(0755, root, bin) %%{_mandir}'
   echo '%%dir %%attr(0755, root, bin) %%{_mandir}/man6'
   REMOVED_LIST=$(echo ${REMOVED_HACKS} | tr ' ' '\n')
   make -s INSTALL=true SHELL=/bin/bash DESTDIR=${RPM_BUILD_ROOT} "$@" \
      | tr -d "'"						\
      | grep -v -w -e "${REMOVED_LIST}"				\
      | sed -n -e 's@.* \(/[^ ]*\)$@\1@p'			\
      | sed    -e "s@^${RPM_BUILD_ROOT}@@"			\
               -e "s@/[a-z][a-z]*/\.\./@/@"			\
	       -e 's@/man1/\(.*\)\.1$@/man6/\1.6@'		\
	       -e 's@\(.*/man/.*\)@%%doc \1@'			\
      | sort -u
}

# Make sure that there were at least some files found
check_list() {
    grep -v -q '%%' "$@" ||  {
        echo ERROR: no hacks found in $@
        exit 1
    }
}

# Make lists of which hacks go into which addon package

cd %{_builddir}/%{src_dir}
(cd hacks ; list_files install ) > hacks.files
check_list hacks.files

(cd hacks/glx ; list_files install ) > hacks-gl.files
check_list hacks-gl.files

cd %{_builddir}/%{rss_dir}
(cd src ; list_files install-data-am install-exec-am ) > rss-glx.files
check_list rss-glx.files

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -s -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr (-, root, bin)

%dir %attr(0755, root, sys) %{_prefix}

%dir %attr(0755, root, bin) %{_bindir}
# xscreensaver must be setuid root in order to do PAM authentication
%attr (4555, root, bin) %{_bindir}/xscreensaver
%{_bindir}/xscreensaver-command
%{_bindir}/xscreensaver-demo

%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{xss_libdir}
%dir %attr(0755, root, bin) %{xss_libdir}/bin
%{xss_libdir}/bin/xscreensaver-lock
%{xss_libdir}/bin/xscreensaver-getimage*
%{xss_libdir}/bin/xscreensaver-text

%dir %attr(0755, root, bin) %{xss_libdir}/config
%{xss_libdir}/config/xscreensaver-demo.glade2
%{xss_libdir}/config/*.png
%{xss_libdir}/config/*.gif
%{xss_libdir}/config/*.p5i

%dir %attr(0755, root, bin) %{xss_libdir}/config/control-center-2.0
%doc %{xss_libdir}/config/control-center-2.0/README

%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/xscreensaver*.1

%dir %attr(0755, root, sys) %{_datadir}

%dir %attr(0755, root, bin) %{_datadir}/X11
%dir %attr(0755, root, bin) %{app_defaults_dir}
%{app_defaults_dir}/XScreenSaver

%dir %attr(0755, root, other) %{_datadir}/applications
%{_datadir}/applications/xscreensaver-properties.desktop

%dir %attr(0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/xscreensaver.xpm

%attr (0755, root, sys) %dir %{_sysconfdir}
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg
%attr (0755, root, sys) %dir %{_sysconfdir}/xdg/autostart
%{_sysconfdir}/xdg/autostart/xscreensaver.desktop

# compatibility links for old /usr/X11 paths
%define x11_dir /usr/X11
%dir %attr(0755, root, bin) %{x11_dir}
%dir %attr(0755, root, bin) %{x11_dir}/bin
%{x11_dir}/bin/*
%dir %attr(0755, root, bin) %{x11_dir}/lib
%{x11_dir}/lib/xscreensaver
%dir %attr(0755, root, bin) %{x11_dir}/lib/X11
%dir %attr(0755, root, bin) %{x11_dir}/lib/X11/app-defaults
%{x11_dir}/lib/X11/app-defaults/XScreenSaver

%files -f hacks.files hacks

%files -f hacks-gl.files hacks-gl

%files -f ../%{rss_dir}/rss-glx.files -n SUNWrss-glx

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr/share
%attr (-, root, other) /usr/share/locale

%changelog
* Wed Aug 15 2011 -arvind.umrao@oracle.com
  Updated xscreensaver-06-gtk-lock.diff for bug 7072588
* Fri Jun 10 2011 - jeff.cai@oracle.com
- Merge patch -23 with patch6
* Thu Jun 9 2011 - jeff.cai@oracle.com
- Add patch -23-bug-7007267, this bug fixes the a11y does not work with orca.
* Thu Jun 2 2011 - alan.coopersmith@oracle.com
  Remove temporary workaround for linker bug 6988300 since it was fixed
  in snv_151.
* Mon May 10 2011 -arvind.umrao@oracle.com
  Added xscreensaver-22-bug-7033508.diff
* Tue Dec 21 2010 - alan.coopersmith@oracle.com
  Update xscreensaver-11-pam_audit.diff to completely disable fallback to
  non-audited non-PAM direct getpwent authentication backend.
* Fri Nov 12 2010 - alan.coopersmith@oracle.com
  Add xscreensaver-05-atoms.diff, drop xscreensaver-11-OpenSolaris-colors.diff
  Renumber patches in between.
* Wed Nov 10 2010 - alan.coopersmith@oracle.com
- d.o.o Bug 16559 - xscreensaver shows extra messages
  Makes various messages only show up in verbose mode.
- Stop calling deprecated GDK_DISPLAY in xscreensaver-lock.
  Avoid segfault when manually running xscreensaver-lock.
* Mon Oct 25 2010 - alan.coopersmith@oracle.com
  Move xscreensaver.desktop here from SUNWgnome-screensaver.spec (it fixes
  d.o.o Bug 10771 -  [gnome2.28] xscreensaver fails to start on login )
* Wed Oct 20 2010 alan.coopersmith@oracle.com
  Backport to gnome-2-30 branch:
  - Add *.p5i files & update xscreensaver-04-solaris-paths.diff for doo #10681:
    xscreensaver-demo should offer .p5i links to install hacks packages
  - Bump to upstream 5.12, renumber remaining patches
  - Updated xscreensaver-13-trusted.diff to fix CR 6955133
* Wed Oct 20 2010 alan.coopersmith@oracle.com
- Temporarily disable mapfiles that trigger linker bug 6988300 until build
  machines are all upgraded to WOS build snv_151 or later.
* Thu Jul 22 2010 - alan.coopersmith@oracle.com
- Change SUNW_Desc to use ' instead of " to avoid bugs like 16602.
* Wed Jun 30 2010 - arvind.umrao@sun.com
- Added xscreensaver-27-bug-6964562.diff
* Tue Jun 22 2010 - alan.coopersmith@oracle.com
- Added xscreensaver-26-demo-accessibility.diff - adds ATK relationship
  metadata to xscreensaver-demo (preferences app) to fix CR 6199780 & 6232612.
* Tue Jun 22 2010 -arvind.umrao@sun.com
- Updated xscreensaver-13-trusted.diff to fix CR 6955133
- Updated xscreensaver-07-allow-root.diff to fix root login of screensaver
* Thu Jun 17 2010 - arvind.umrao@sun.com
- Updated xscreensaver-13-trusted.diff to fix CR 6955133
* Tue Jun 15 2010 - alan.coopersmith@oracle.com
- Make 'asterisks' setting in xscreensaver app-defaults file work, restore
  default to upstream value of true to preserve existing behavior.
- Capture keystrokes that arrive before the unlock dialog opens and replay
  them into the dialog once it appears.
- Remove some more unnecessary differences from upstream code.
* Wed Jun 9 2010 - alan.coopersmith@oracle.com
- Fix 16207 xscreensaver cores when a correct or incorrect password is entered
  http://defect.opensolaris.org/bz/show_bug.cgi?id=16207
  by removing incorrect addition of free(msg) from patch 6, since msg
  is now a static/constant string that isn't malloc'ed
* Thu Jun 10 2010 - arvind.umrao@sun.com
- Updated xscreensaver-06-gtk-lock.diff to fix 6957754
* Fri Jun 4 2010 - alan.coopersmith@oracle.com
- Fix issues handling LoginHelper settings for accessibility
  applications that need special handling.
- Fix startup of unlock countdown timer animation to be more reliable.
- Set correct warning flags for Sun cc vs. gcc
- Ignore errors from XRestackWindows, since there's always a race condition
  possible if the other client destroys its window before we process the 
  notify event and get through the call to XRestackWindows.
- When destroying windows (such as when changing screensaver "hacks" to one
  with a different visual), purge any queued VisibilityNotify events so we
  don't get XErrors when we process them and try to restack a destroyed window.
- Pass through some additional messages from the upstream code, like the
  "(Caps Lock?)" when authentication fails & Caps Lock was on and the counts
  of failed login attempts.
* Wed Jun 2 2010 - alan.coopersmith@oracle.com
- Use gnome-help to display man pages instead of running "man" in a terminal
* Tue Jun 1 2010 - alan.coopersmith@oracle.com
- Fix XErrors from XRestackWindow calls by major overhaul of accessibility
  and parent/child communication code.
- Merge patch 18 into patch 6, renumber patches 19-25 to fill the hole
- Remove some unnecessary changes from patches
* Thu May 27 2010 - brian.cameron@oracle.com
- Fixed prompting for new password when a users password is expired.
- Improve appearance of unlock dialog
* Wed May 26 2010 - alan.coopersmith@oracle.com
- Merge patches 18 & 19
- Move %descriptions to SUNW_Desc in spec file
- Make code more readable/maintainable by cleaning up comments, 
  making formatting & indentation consistent.
- Fix some copyright dates based on history from X gate
- Change a few more #ifdef sun to #ifdef __sun for consistency.
* Wed May 26 2010 - arvind.umrao
- Added patch xscreensaver-26-bug-xrandr.diff for bug bugster:6757448,6924996
* Tue May 25 2010 - brian.cameron@oracle.com
- Bump to 5.11.  Remove upstream patches.  Merge several patches so that
  patches do not apply on top of other patches so much.  Cleanup.
* Fri Mar 12 2010 - alan.coopersmith@sun.com
- Remove obsolete SUNWxwsvr (only had /usr/openwin->X11 symlinks that
  are not needed on IPS-installed machines)
* Mon Mar 1 2010 - alan.coopersmith@sun.com
- Use new IPS package names in man page attributes setting in .spec file 
  and in hacks packages message in xscreensaver-05-solaris-paths.diff
- Fix http://defect.opensolaris.org/bz/show_bug.cgi?id=14955 in
  xscreensaver-05-solaris-paths.diff
* Mon Feb 15 2010 - arvind.umrao@sun.com
- Add xscreensaver-53-bug-6924996.diff to fix CR#6924996  
* Thu Feb 04 2010 - harry.fu@sun.com
- Add po-sun translations.
* Tue Jan 26 2010 - dave.lin@sun.com
- Mark SUNWxwsvr as Nevada only package.
* Thu Dec 31 2009 - naveen.gundlagutta@sun.com
- 6865652: Add xscreensaver-50-bug-6865652.diff to disable restart, kill options in xscreensaver-demo in trusted solaris
- 6832923: Add xscreensaver-52-bug-6832923.diff to prevent xscreensaver from crashing in sunray.
* Wed Dec 23 2009 - alan.coopersmith@sun.com
- Move app-defaults file to /usr/share/X11/app-defaults
- Build against mesa headers/libraries on both SPARC & x86 now that
  SUNWxorg-mesa is delivered on SPARC in snv_130
- Report error if none of the GL hacks were built instead of quietly
  building empty packages for them
* Tue Dec 22 2009 - alan.coopersmith@sun.com
- Add xscreensaver-51-dpms-headers.diff to build with snv_130 X headers
- Use /usr/lib/ld/map.noexbss now that it's shipped in snv_125 & later
  builds (CR 6843010)
* Mon Oct 19 2009 - alan.coopersmith@sun.com
- Change default DPMS settings to match Xorg 1.7 defaults (10 minutes)
- Merge xscreensaver-32-XScr.ad.lockTimeout.diff 
   into xscreensaver-03-Sun.app-defaults.diff
- Fix patch 9 & 22 to apply cleanly to the new patch 3 results
* Wed Sep 23 2009 - alan.coopersmith@sun.com
- Move files from /usr/X11 to /usr (PSARC 2009/482)
* Thu Sep 10 2009 - arvind.umrao@sun.com
- Add xscreensaver-47-bug-6859039.diff to fix 6839026
* Mon Aug 24 2009 - alan.coopersmith@sun.com
- 6875124 Broken link in package SUNWxwsvr
* Mon Aug 17 2009 - alan.coopersmith@sun.com
- Add more BuildRequires
* Thu Aug 13 2009 - alan.coopersmith@sun.com
- Add Vendor & License tags
* Fri Jul 31 2009 - alan.coopersmith@sun.com
- forward port xscreensaver-47-bug-6859039.diff from new X gate putback
* Thu Jul 30 2009 - alan.coopersmith@sun.com
- move Solaris branding logos to solaris-lockscreen-logos-1.0.tar.bz2
* Fri Jul 24 2009 - alan.coopersmith@sun.com
- rename patches from *.patch to *.diff
* Fri Jul 17 2009 - alan.coopersmith@sun.com
- initial version (moved from X gate)
