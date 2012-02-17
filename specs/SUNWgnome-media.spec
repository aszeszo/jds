#
# spec file for packages SUNWgnome-media
#
# includes module(s): gst, gst-plugins-base, gst-plugins-good
#
# Copyright 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%define with_hal %(pkginfo -q SUNWhal && echo 1 || echo 0)

%ifarch amd64 sparcv9
%include arch64.inc
%use gst64 = gst.spec
%use gst_plugins_base64 = gst-plugins-base.spec
%use gst_plugins_good64 = gst-plugins-good.spec
%endif

%include base.inc
%use gst = gst.spec
%use gst_plugins_base = gst-plugins-base.spec
%use gst_plugins_good = gst-plugins-good.spec

%define gst_minmaj %(echo %{gst.version} | cut -f1,2 -d.)

Name:                    SUNWgnome-media
IPS_package_name:        library/audio/gstreamer
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 GNOME streaming media framework
Version:                 %{gst.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 LGPL v2, LGPL v2.1, GPL v2, BSD, MIT, Public Domain
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc

Requires: codec/flac
Requires: codec/libtheora
Requires: codec/ogg-vorbis
Requires: codec/speex
Requires: gnome/config/gconf
Requires: gnome/gnome-audio
Requires: image/library/libjpeg
Requires: image/library/libpng
Requires: library/aalib
Requires: library/desktop/gobject/gobject-introspection
Requires: library/desktop/gtk2
Requires: library/desktop/pango
Requires: library/gnome/gnome-keyring
Requires: library/gnome/gnome-libs
Requires: library/gnome/gnome-vfs
Requires: library/liboil
Requires: library/libsoup
Requires: library/libxml2
Requires: library/musicbrainz/libdiscid
Requires: library/musicbrainz/libmusicbrainz
Requires: library/python-2/python-extra-26
Requires: library/zlib
Requires: media/cdrtools
Requires: runtime/python-26
Requires: service/gnome/desktop-cache
Requires: system/hal
Requires: system/library/math
Requires: x11/library/libx11
Requires: x11/library/libxext
Requires: x11/library/libxv

BuildRequires: developer/parser/bison
BuildRequires: library/desktop/libvisual
BuildRequires: media/cdrtools
BuildRequires: runtime/perl-512
BuildRequires: system/header
BuildRequires: text/gawk
BuildRequires: text/gnu-grep
BuildRequires: text/gnu-sed
BuildRequires: x11/server/xorg

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%gst64.prep -d %name-%version/%_arch64
%gst_plugins_base64.prep -d %name-%version/%_arch64
%gst_plugins_good64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%gst.prep -d %name-%version/%{base_arch}
%gst_plugins_base.prep -d %name-%version/%{base_arch}
%gst_plugins_good.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
# There seems to be an issue with the version of libtool that GStreamer is
# now using.  The libtool script uses the echo and RM variables but does not
# define them, so setting them here addresses this.
export echo="/usr/bin/echo"
export RM="/usr/bin/rm"

export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

# The taglib gst-plugins-good plugin does not build without setting this since
# AC_PROG_PATH does not work with CXX set to the full-path of the C++ compiler.
# So, overriding the setting fixes this.
#
export HAVE_CXX=yes

%ifarch amd64 sparcv9
export CXXFLAGS="%cxx_optflags64"

export CFLAGS="%optflags64 -I/usr/sfw/include -DANSICPP"
export RPM_OPT_FLAGS="$CFLAGS"
export PKG_CONFIG_PATH="%{_pkg_config_path64}"

%gst64.build -d %name-%version/%_arch64

export CFLAGS="%optflags64 -I/usr/sfw/include -I/usr/X11/include -DANSICPP"
export LDFLAGS="%{_ldflags} -lresolv"
export PKG_CONFIG_PATH="%{_builddir}/%name-%version/%{_arch64}/gstreamer-%{gst.version}/pkgconfig:%{_pkg_config_path64}"

%gst_plugins_base64.build -d %name-%version/%_arch64

unset LDFLAGS

export CFLAGS="%optflags64 -I/usr/sfw/include -DANSICPP"
export PKG_CONFIG_PATH="%{_builddir}/%name-%version/%{_arch64}/gstreamer-%{gst.version}/pkgconfig:%{_builddir}/%name-%version/%{_arch64}/gst-plugins-base-%{gst_plugins_base.version}/pkgconfig:%{_pkg_config_path64}"

# The taglib library is not in Solaris, but the spec-file in SFE does not
# provide 64-bit libraries, so avoid building it with 64-bit to avoid build
# failing if it is installed.
#
export GST_EXTRA_CONFIG="--disable-taglib"

%gst_plugins_good64.build -d %name-%version/%_arch64

export GST_EXTRA_CONFIG=""
%endif

export CXXFLAGS="%cxx_optflags"

export CFLAGS="%optflags -I/usr/sfw/include -DANSICPP"
export RPM_OPT_FLAGS="$CFLAGS"
export PKG_CONFIG_PATH="%{_pkg_config_path}"

%gst.build -d %name-%version/%{base_arch}

export CFLAGS="%optflags -I/usr/sfw/include -I/usr/X11/include -DANSICPP"
export LDFLAGS="%_ldflags -lresolv"
export PKG_CONFIG_PATH="%{_builddir}/%name-%version/%{base_arch}/gstreamer-%{gst.version}/pkgconfig:%{_pkg_config_path}"

%gst_plugins_base.build -d %name-%version/%{base_arch}

unset LDFLAGS

export CFLAGS="%optflags -I/usr/sfw/include -DANSICPP"
export PKG_CONFIG_PATH="%{_builddir}/%name-%version/%{base_arch}/gstreamer-%{gst.version}/pkgconfig:%{_builddir}/%name-%version/%{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/pkgconfig:%{_pkg_config_path}"

%gst_plugins_good.build -d %name-%version/%{base_arch}

%install
# There seems to be an issue with the version of libtool that GStreamer is
# now using.  The libtool script uses the echo and RM variables but does not
# define them, so setting them here addresses this.
export echo="/usr/bin/echo"
export RM="/usr/bin/rm"

rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
# Rebuilding the gobject-introspection files requires resetting.
export PKG_CONFIG_PATH="%{_pkg_config_path64}"
export CFLAGS="%optflags64 -DANSICPP"

%gst64.install -d %name-%version/%_arch64
%gst_plugins_base64.install -d %name-%version/%_arch64
%gst_plugins_good64.install -d %name-%version/%_arch64

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/gstreamer-%{gst_minmaj}/tools
cd $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
for prog in gst-feedback gst-inspect gst-launch gst-typefind \
            gst-xmlinspect gst-xmllaunch; do
  mv $prog-%{gst_minmaj} ../../lib/%{_arch64}/gstreamer-%{gst_minmaj}/tools
  rm -f $prog
  ln -s ../../lib/%{_arch64}/gstreamer-%{gst_minmaj}/tools/$prog-%{gst_minmaj} $prog
done

perl -pi -e 's,^toolsdir=.*,toolsdir=\${exec_prefix}/%{_arch64}/lib/gstreamer-%{gst_minmaj}/tools,' $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/pkgconfig/gstreamer-%{gst_minmaj}.pc
%endif

cd %{_builddir}

# Rebuilding the gobject-introspection files requires resetting.
export PKG_CONFIG_PATH="%{_pkg_config_path}"
export CFLAGS="%optflags -DANSICPP"

%gst.install -d %name-%version/%{base_arch}
%gst_plugins_base.install -d %name-%version/%{base_arch}
%gst_plugins_good.install -d %name-%version/%{base_arch}

mkdir -p $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_minmaj}/tools
cd $RPM_BUILD_ROOT%{_bindir}
for prog in gst-feedback gst-inspect gst-launch gst-typefind \
            gst-xmlinspect gst-xmllaunch; do
  mv $prog-%{gst_minmaj} ../lib/gstreamer-%{gst_minmaj}/tools
  rm -f $prog
  ln -s ../lib/gstreamer-%{gst_minmaj}/tools/$prog-%{gst_minmaj} $prog
done

perl -pi -e 's,^toolsdir=.*,toolsdir=\${exec_prefix}/lib/gstreamer-%{gst_minmaj}/tools,' $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gstreamer-%{gst_minmaj}.pc

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_mandir}/man1/*.1
chmod 755 $RPM_BUILD_ROOT%{_mandir}/man3/*.3
chmod 755 $RPM_BUILD_ROOT%{_mandir}/man5/*.5

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# RBAC related
mkdir -p $RPM_BUILD_ROOT/etc/security/prof_attr.d

# prof_attr(4)
cat >> $RPM_BUILD_ROOT/etc/security/prof_attr.d/library-audio-gstreamer <<EOF
Desktop Removable Media User:RO::Access removable media for desktop user:
Console User:RO:::profiles=Desktop Removable Media User
EOF

%if %{!?_without_gtk_doc:0}%{?_without_gtk_doc:1}
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gst*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libgst*.so*
%{_libdir}/gstreamer-%{gst_minmaj}/lib*.so*
%{_libdir}/gstreamer-%{gst_minmaj}/tools
%{_libdir}/gstreamer-%{gst_minmaj}/gst-plugin-scanner
%{_libdir}/girepository-1.0/*
%ifarch amd64 sparcv9
%dir %attr(0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/gst*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libgst*.so*
%{_libdir}/%{_arch64}/gstreamer-%{gst_minmaj}/lib*.so*
%{_libdir}/%{_arch64}/gstreamer-%{gst_minmaj}/tools
%{_libdir}/%{_arch64}/gstreamer-%{gst_minmaj}/gst-plugin-scanner
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}/girepository-1.0
%{_libdir}/%{_arch64}/girepository-1.0/*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%doc %{base_arch}/gstreamer-%{gst.version}/AUTHORS
%doc %{base_arch}/gstreamer-%{gst.version}/README
%doc(bzip2) %{base_arch}/gstreamer-%{gst.version}/COPYING
%doc(bzip2) %{base_arch}/gstreamer-%{gst.version}/NEWS
%doc(bzip2) %{base_arch}/gstreamer-%{gst.version}/ChangeLog
%doc(bzip2) %{base_arch}/gstreamer-%{gst.version}/common/ChangeLog
%doc %{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/AUTHORS
%doc %{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/README
%doc(bzip2) %{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/COPYING
%doc(bzip2) %{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/COPYING.LIB
%doc(bzip2) %{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/NEWS
%doc(bzip2) %{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/ChangeLog 
%doc(bzip2) %{base_arch}/gst-plugins-base-%{gst_plugins_base.version}/common/ChangeLog
%doc %{base_arch}/gst-plugins-good-%{gst_plugins_good.version}/AUTHORS
%doc %{base_arch}/gst-plugins-good-%{gst_plugins_good.version}/README
%doc(bzip2) %{base_arch}/gst-plugins-good-%{gst_plugins_good.version}/COPYING
%doc(bzip2) %{base_arch}/gst-plugins-good-%{gst_plugins_good.version}/NEWS
%doc(bzip2) %{base_arch}/gst-plugins-good-%{gst_plugins_good.version}/ChangeLog 
%doc(bzip2) %{base_arch}/gst-plugins-good-%{gst_plugins_good.version}/common/ChangeLog
%doc(bzip2) %{base_arch}/gst-plugins-good-%{gst_plugins_good.version}/docs/random/ChangeLog-0.8
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/gir-1.0/*.gir
%dir %attr (0755, root, other) %{_datadir}/gstreamer-0.10
%{_datadir}/gstreamer-0.10/*
%dir %attr (0755, root, other)
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man5
%{_mandir}/man1/gst*
%{_mandir}/man5/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/gstreamer-%{gst_minmaj}.schemas
%attr (0755, root, sys) %dir /etc/security
%attr (0755, root, sys) %dir /etc/security/prof_attr.d
%ips_tag(restart_fmri=svc:/system/rbac:default) %attr (0444, root, sys) /etc/security/prof_attr.d/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/gstreamer-%{gst_minmaj}/gst
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%if %{!?_without_gtk_doc:1}%{?_without_gtk_doc:0}
%{_datadir}/gtk-doc
%endif
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Fri Feb 17 2012 - brian.cameron@oracle.com
- Now build with vfs and soup 64-bit plug-ins.
* Wed Apr 06 2011 - brian.cameron@oracle.com
- Add "RO" to prof_attr config.
* Thu Apr 15 2010 - christian.kelly@oracle.com
- Re-enable dependency on liboil.
* Thu Feb 11 2010 - brian.cameron@sun.com
- Fix packaging after bumping GStreamer to 0.10.26.
* Fri Jan 15 2009 - lin.ma@sun.com
- Move the definition of 'Desktop Removable Media User' from
  SUNWgnome-cd-burner to here - doo 13911.
* Mon May 18 2009 - dave.lin@sun.com
- Comment out the line 'Requires: SUNWmkcd' until we work out the bug CR6840919.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Fri Feb 20 2009 - brian.cameron@sun.com
- Update packaging as needed for gst-plugins-good 0.10.14.
* Fri Sep 12 2008 - brian.cameron@sun.com
- Add new copyright files.
* Wed Jun 18 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWlibsoup/-devel after check-deps.pl run.
* Wed May 07 2008 - damien.carbery@sun.com
- Remove PERL5LIB setting as it is not necessary.
* Tue Apr 01 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Fri Sep 28 2007 - laca@sun.com
- delete SUNWxwrtl dep
* Thu Aug 02 2007 - damien.carbery@sun.com
- Add -lresolv to LDFLAGS for gst-plugins-base for hstrerror function.
* Thu Aug 02 2007 - damien.carbery@sun.com
- Delete gtk-doc files in %install when built using --without-gtk-doc. The root
  cause is in the gst/gst-plugins modules but this fix works for now.
* Tue Jun 26 2007 - irene.huang@sun.com
- remove libcdio as dependency
* Fri Oct 20 2006 - damien.carbery@sun.com
- Remove SUNWhalh BuildRequires because header files are in SUNWhea in snv_51.
* Mon Sep 18 2006 - Brian.Cameron@sun.com
- Add SUNWhalh BuildRequires.
* Mon Sep 04 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Thu Aug 24 2006 - brian.cameron@sun.com
- Remove pointless libgstgetbits.3, libgstdataprotocol.3 manpage and move
  libgstreamer-0.8.3 manpage to libgstreamer-0.10.3.
* Tue Aug 22 2006 - brian.cameron@sun.com
- Remove gst-md5sum man page since this is no longer a part of GStreamer.
* Mon Aug 14 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWhal after check-deps.pl run.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Fri Jun 23 2006 - christopher.hanna@sun.com
- Removed all of the 0.8 version manpages and the following
  manpages which are no longer needed:
  gst-complete, gst-compprep, gst-launch-ext, gst-register
* Wed Jun 14 2006 - brian.cameron@sun.com
- Changes from bumping to new versions of modules.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu Jun  1 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
- add the versioned binaries back in %{_libdir}/gstreamer-0.10/tools
  otherwise gnome-media (SUNWgnome-media-apps) fails
* Tue Mar 28 2006 - brian.cameron@sun.com
- Added libcdio dependency.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Jan 24 2006 - damien.carbery@sun.com
- Add Build/Requires SUNWliboil/-devel as required by liboil.
* Fri Jan 19 2006 - brian.cameron@sun.com
- Bump to GStreamer 0.10.
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Mon Nov 07 2005 - brian.cameron@sun.com
- Fix spec file so it builds xvimagesink.  This requires adding 
  /usr/X11/lib to LDFLAGS and /usr/X11/include to CFLAGS when building
  gst-plugins.  xvimagesink is faster than ximagesink since it uses
  the XVideo Xserver extension, so its nice to have.  This only works
  when using the Xorg Xserver, so users who are using Xsun will need
  to continue using the ximagesink plugin for video output.
* Tue Sep 27 2005 - laca@sun.com
- add python build dep for gstreamer-plugins gtk docs (mangle-tmpl.py)
* Mon Sep 12 2005 - laca@sun.com
- remove unpackaged files
* Fri Aug 12 2005 - balamurali.viswanathan@wipro.com
- Add dependency of SUNWflac
* Tue Jul 26 2005 - balamurali.viswanathan@wipro.com
- Add dependency of SUNWspeex and SUNWlibtheora
* Mon Jul 11 2005 - balamurali.viswanathan@wipro.com
- Add BuildRequires: SUNWmusicbrainz
* Wed Jun 01 2005 - brian.cameron@sun.com
- remove nautilus-media since it no longer works with nautilus.  Nautilus
  no longer supports extensions like nautilus-media.  Remove gnome-media
  since it needs to be split into a separate package.  This is because
  gnome-panel requires gstreamer and gnome-media requires gnome-panel.
* Tue Feb 22 2005 - brian.cameron@sun.com
- moved l10n package to last built since it tends to fail on re-install.
* Fri Jan 28 2005 - matt.keenan@sun.com
- #6222302 : Remove gstreamer properties from yelp TOC
* Tue Nov 23 2004 - damien.carbery@sun.com
- Fix 6197917: Restore files 'lost' when SUNWgnome-media packages reorganised
  to restore 'lost' Gnome 2.0 packages. Reviewed by Laca.
* Fri Nov 12 2004 - laca@sun.com
- Use the original GNOME 2.0 packaging structure: add SUNWgnome-cd*
  SUNWgnome-freedb-libs* and SUNWgnome-sound-recorder*
* Thu Oct 21 2004 - laca@sun.com
- change registry.xml to volatile, fixes 6180895
* Thu Oct 14 2004 - brian.cameron@sun.com
- Added gst-launch-ext* man pages.
* Wed Oct 06 2004 - vinay.mandyakoppal@wipro.com
- Added code to install javahelp documents.
  Fixes  bugs #5096655,5096658.
* Mon Oct 04 2004 - matt.keenan@sun.com
- Added javahelp files for share package #5108690
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Sep 27 2004 - arvind.samptur@wipro.com
- Get GNOME_Media_CDDBSlave2.server to be installed
* Fri Sep 24 2004 - brian.cameron
- Added %post section so that programs that use GStreamer will work
  properly.  The timestamp of the registry file must be later than
  the libraries for programs to work.
* Thu Sep 09 2004 - matt.keenan@sun.com
- Added a heap of manpages
* Thu Aug 26 2004 - Brian.Cameron@sun.com
- Now package gtk-docs.
* Wed Aug 25 2004 - Kazuhiko.Maekawa@sun.com
- Added l10n javahelp entry in l10n pkg files
* Tue Aug 24 2004 - laca@sun.com
- move l10n files to the l10n package
* Fri Aug 20 2004  brian.cameron@sun.com
- No longer package Nautilus_View server files since they aren't being 
  installed by the nautilus-media.spec file.
* Mon Aug 16 2004  shirley.woo@sun.com
- change .../sman1/*.1 permissions to 0755 for Solaris integration error
* Thu Jul 29 2004  brian.cameron@sun.com
- Fixed setting of PKG_CONFIG_PATH and CPPFLAGS so that they work when
  gstreamer and gst-plugins have different version #'s.
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Mon Jun 07 2004 - brian.cameron@sun.com
- Added ogg/vorbis dependancy.  Now including registry.xml.
* Wed Jun 02 2004 - brian.cameron@sun.com
- Removed SUNWgnome-pilot-link dependancy which was wrong.
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Wed May 26 2004 - brian.cameron@sun.com
- Fixed CFLAGS so that Kpic flag gets properly recognized, allowing
  gstreamer to actually work in addition to just compiling.
* Tue May 25 2004 - brian.cameron@sun.com
- Updated dependencies to include SUNWgnome-file-mgr.
* Wed May 12 2004 - brian.cameron@sun.com
- Add nautilus-media.  Made changes so that this works with 
  gstreamer and gst-plugins 0.8.1.
* Sun Mar 28 2004 - brian.cameron@sun.com
- Corrected PKG_CONFIG_PATH so it will find gst-plugins properly.
* Fri Mar 26 2004 - laca@sun.com
- buildrequires CBEbison instead of SUNWbison
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Thu Feb 26 2004 - niall.power@sun.com
- Initial spec-file created

