#
# spec file for package SUNWlibcanberra
#
# includes module(s): libcanberra
#
# Copyright (c) 2008, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: bugzilla.freedesktop.org
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libcanberra_64 = libcanberra.spec
%endif

%include base.inc
%use libcanberra = libcanberra.spec

Name:                    SUNWlibcanberra
IPS_package_name:        library/desktop/xdg/libcanberra
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 Event Sound API Using XDG Sound Theming Specification
Version:                 %{libcanberra.version}
Source1:                 %{name}-manpages-0.1.tar.gz
SUNW_Copyright:          %{name}.copyright
License:                 %{libcanberra.license}
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWgtk2
Requires: SUNWgtk3
Requires: SUNWlibcanberra-root
Requires: SUNWxdg-sound-theme
Requires: SUNWgnome-media
Requires: SUNWogg-vorbis
Requires: SUNWlibltdl
Requires: SUNWdesktop-cache
Requires: SUNWpulseaudio
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWgtk3-devel
BuildRequires: SUNWgnome-media-devel
BuildRequires: SUNWogg-vorbis-devel
BuildRequires: SUNWpulseaudio-devel

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
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libcanberra_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%libcanberra.prep -d %name-%version/%base_arch

cd %{_builddir}/%{name}-%{version}
gzcat %SOURCE1 | tar xf -

%build
# There seems to be an issue with the version of libtool that GStreamer is
# now using.  The libtool script uses the echo and RM variables but does not
# define them, so setting them here addresses this.
export echo="/usr/bin/echo"
export RM="/usr/bin/rm"

%ifarch amd64 sparcv9
export PKG_CONFIG_LIBDIR="%{_pkg_config_path64}"
export CFLAGS="%optflags64"
%libcanberra_64.build -d %name-%version/%_arch64
%endif

export PKG_CONFIG_LIBDIR="%{_pkg_config_path}"
export CFLAGS="%optflags"
%libcanberra.build -d %name-%version/%base_arch

%install
# There seems to be an issue with the version of libtool that GStreamer is
# now using.  The libtool script uses the echo and RM variables but does not
# define them, so setting them here addresses this.
export echo="/usr/bin/echo"
export RM="/usr/bin/rm"

%ifarch amd64 sparcv9
%libcanberra_64.install -d %name-%version/%_arch64
%endif

%libcanberra.install -d %name-%version/%base_arch

cd %{_builddir}/%{name}-%{version}/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libcanberra-%{version}
%{_libdir}/lib*.so*
%{_libdir}/gtk-2.0/modules/libcanberra-gtk-module.so
%{_libdir}/gtk-3.0/modules/libcanberra-gtk-module.so
%{_libdir}/gtk-3.0/modules/libcanberra-gtk3-module.so
%{_libdir}/gnome-settings-daemon-3.0/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libcanberra-%{version}
%{_libdir}/%{_arch64}/lib*.so*
%{_libdir}/%{_arch64}/gtk-2.0/modules/libcanberra-gtk-module.so
%{_libdir}/%{_arch64}/gtk-3.0/modules/libcanberra-gtk-module.so
%{_libdir}/%{_arch64}/gtk-3.0/modules/libcanberra-gtk3-module.so
%{_libdir}/%{_arch64}/gnome-settings-daemon-3.0/*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%doc -d %{base_arch} %{libcanberra.name}-%{libcanberra.version}/README
%doc -d %{base_arch} %{libcanberra.name}-%{libcanberra.version}/doc/README
%doc(bzip2) -d %{base_arch} %{libcanberra.name}-%{libcanberra.version}/LGPL
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_datadir}/gdm
%dir %attr (0755, root, bin) %{_datadir}/gdm/autostart
%{_datadir}/gdm/autostart/*
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/*
%{_datadir}/gtk-doc
%{_datadir}/vala/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/*
%{_mandir}/man3/*


%files root
%defattr(-, root, sys)
%attr(0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/libcanberra.schemas

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
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/libcanberra
%{_datadir}/doc/libcanberra/*
%dir %attr (0755, root, other) %{_datadir}/gnome

%changelog
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Fix packaging for libcanberra 0.28 release.
* Thu Jul 01 2010 - brian.cameron@oracle.com
- Add CFLAGS to %build so that the 64-bit libraries get built with the correct
  ELFCLASS.
* Tue Apr 27 2010 - brian.cameron@sun.com
- Build i386 after amd64.  Fixes doo bug #15773.
* Wed Jan 13 2010 - christian.kelly@sun.com
- Fix %files.
* Mon Sep 14 2009 - brian.cameron@sun.com
- Update packaging for new 0.17 version.
* Fri Jul 29 2009 - ke.wang@sun.com
- Add 64-bit support
* Wed Jul 01 2009 - brian.cameron@sun.com
- Bump to 0.14.
* Wed Jun 24 2009 - brian.cameron@sun.com
- Bump to 0.13.  Remove upstream patch libcanberra-02-close-file.diff.
* Mon Apr 13 2009 - brian.cameron@sun.com
- Bump to 0.12.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Tue Feb 10 2009 - halton.huo@sun.com
- Add Requires: SUNWltdl to fix issue #5 for CR6753371
* Wed Jan 21 2009 - brian.cameron@sun.com
- Bump to 0.11.  Remove upstream patches.
* Thu Jan 15 2008 - brian.cameron@sun.com
- Add a patch to fix the OSS backend so it works.
* Thu Oct 30 2008 - brian.cameron@sun.com
- Add patch libcanberra-02-gstreamer.diff to fix bug where libcanberra core
  dumps when it tries to play a second sound.  Fixes bugster bug #6761078.
* Mon Oct 13 2008 - brian.cameron@sun.com
- Bump to 0.10.  Add root package and %post and %preun sections for the
  new GConf schemas.
* Tue Sep 09 2008 - brian.cameron@sun.com
- Bump to 0.9.  Remove upstream patches libcanberra-02-gstreamer.diff and
  libcanberra-03-fix-gst-play.diff.
* Fri Aug 29 2008 - brian.cameron@sun.com
- Add patch libcanberra-03-fix-gst-play so it actually plays the sound.
* Fri Aug 29 2008 - brian.cameron@sun.com
- Add patch libcanberra-02-gstreamer.diff to add audioconvert and audioresample
  plugins to the output pipeline, so it works on Solaris.
* Thu Aug 28 2008 - brian.cameron@sun.com
- Bump to 0.8.  Now has its own GStreamer support, so removed our patch.
* Wed Aug 20 2008 - brian.cameron@sun.com
- Add Requires/BuildRequires and patch libcanberra-02-gstreamer.diff to support
  a GStreamer backend.
* Thu Aug 14 2008 - brian.cameron@sun.com
- Created with version 0.6.

