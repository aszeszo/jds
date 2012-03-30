#
# spec file for package SUNWtsclient
#
# includes module(s): tsclient
#
# Copyright (c) 2010, 2012 Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%include Solaris.inc

%use tsclient = tsclient.spec

Name:               SUNWtsclient
Summary:            tsclient - A frontend for rdesktop and other remote desktop tools
Version:            %{tsclient.version}
SUNW_Pkg:           SUNWtsclient
IPS_package_name:   desktop/remote-desktop/tsclient
Meta(info.classification): %{classification_prefix}:Applications/Internet
SUNW_Copyright:     %{name}.copyright
License:            %{tsclient.license}
SUNW_BaseDir:       %{_basedir}
BuildRoot:          %{_tmppath}/%{name}-%{version}-build
Source1:            %{name}-manpages-0.1.tar.gz

%include default-depend.inc
%include desktop-incorporation.inc
Requires:           library/desktop/libgnomecanvas
Requires:           gnome/gnome-panel
Requires:           library/gnome/gnome-libs
Requires:           library/gnome/gnome-vfs
Requires:           gnome/config/gconf
Requires:           library/popt
Requires:           system/library/math
Requires:           system/library/fontconfig
Requires:           library/gnome/gnome-component
Requires:           library/libxml2
Requires:           system/library/libdbus-glib
Requires:           system/library/dbus
Requires:           library/security/openssl
Requires:           gnome/gnome-audio
Requires:           system/library/freetype-2
Requires:           library/expat
Requires:           library/zlib
Requires:           image/library/libpng
Requires:           desktop/remote-desktop/rdesktop
Requires:           desktop/remote-desktop/tigervnc
Requires:           x11/server/xorg
Requires:           gnome/gnome-keyring
Requires:           library/gnome/gnome-keyring
BuildRequires:      SUNWxwplt
BuildRequires:      x11/library/libice
BuildRequires:      system/library/math/header-math
BuildRequires:      library/medialib
BuildRequires:      library/desktop/libgnomecanvas
BuildRequires:      gnome/gnome-panel
BuildRequires:      library/gnome/gnome-libs
BuildRequires:      library/gnome/gnome-vfs
BuildRequires:      system/library/libdbus-glib
BuildRequires:      system/library/dbus
BuildRequires:      library/libxml2
BuildRequires:      image/library/libpng

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%tsclient.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
%tsclient.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%tsclient.install -d %name-%version

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_datadir}/locale
# Rename dirs that are symlinks on the installed system.
mv nl_NL nl
mv pl_PL pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d tsclient-%{tsclient.version} README AUTHORS
%doc(bzip2) -d tsclient-%{tsclient.version} COPYING ChangeLog po/ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/tsclient
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/tsclient-applet
%dir %attr (0755, root, bin) %{_libdir}/bonobo
%dir %attr (0755, root, bin) %{_libdir}/bonobo/servers
%{_libdir}/bonobo/servers/GNOME_TSClientApplet.server
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (-, root, other) %{_datadir}/application-registry
%{_datadir}/application-registry/tsclient.applications
%dir %attr (-, root, other) %{_datadir}/applications
%{_datadir}/applications/tsclient.desktop
%dir %attr (-, root, other) %{_datadir}/mime-info
%{_datadir}/mime-info/*
%dir %attr (-, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Thu Mar 29 2012 - jeff.cai@oracle.com
- Change to ips package names
* Thu Mar 05 2009 - brian.cameron@sun.com
- Change SUNWdbus-bindings to SUNWdbus-glib.
* Wed Nov 05 2008 - halton.huo@sun.com
- Add po/ChangeLog to %files
* Wed Sep 17 2008 - halton.huo@sun.com
- Change Requires: SUNWlibm to SUNWlibms to fix bugster #6748982
* Wed Sep 10 2008 - halton.huo@sun.com
- Add %doc to %files for new copyright
* Thu Aug 07 2008 - halton.huo@sun.com
- Use sgml format man pages.
* Wed Jul 01 2008 - halton.huo@sun.com
- s/SUNWxwsrv/SUNWxorg-server since we use Xephyr instead of Xnest
* Tue Jun 01 2008 - damien.carbery@sun.com
- Rename 2 locale dirs because they are symlinks on the installed system (nl_NL
  to nl and pl_PL to pl).
* Fri Jun 27 2008 - nonsea@users.sourceforge.net
- Add Requires to SUNWrdesktop, SUNWvncviewer and SUNWxwsrv
* Thu Jun 19 2008 - nonsea@users.sourceforge.net
- Initial spec



