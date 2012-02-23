#
# spec file for package SUNWvinagre
#
# includes module(s): vinagre
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan
#

%include Solaris.inc

%use vinagre = vinagre.spec

Name:               SUNWvinagre
License:	    GPL v2
Summary:            Vinagre - A VNC client for the GNOME Desktop
Version:            %{vinagre.version}
SUNW_Pkg:           SUNWvinagre
IPS_package_name:   desktop/remote-desktop/vinagre
Meta(info.classification): %{classification_prefix}:Applications/Internet
SUNW_Copyright:     %{name}.copyright
SUNW_BaseDir:       %{_basedir}
BuildRoot:          %{_tmppath}/%{name}-%{version}-build
Source1:            %{name}-manpages-0.1.tar.gz

%include default-depend.inc
%include desktop-incorporation.inc
Requires:           library/desktop/libgnomecanvas
Requires:           library/gnome/gnome-libs
Requires:           library/gnutls
Requires:           system/network/avahi
Requires:           library/gnome/gnome-component
Requires:           gnome/config/gconf
Requires:           gnome/gnome-panel
Requires:           library/gnome/gnome-vfs
Requires:           library/desktop/gtk-vnc
Requires:           library/popt
Requires:           system/library/fontconfig
Requires:           system/library/freetype-2
Requires:           system/library/math
Requires:           library/libxml2
BuildRequires:      x11/library/libice
Requires:           service/gnome/desktop-cache
BuildRequires:      library/desktop/libgnomecanvas
BuildRequires:      library/gnome/gnome-libs
BuildRequires:      library/gnutls
BuildRequires:      system/network/avahi
BuildRequires:      library/gnome/gnome-component
BuildRequires:      gnome/config/gconf
BuildRequires:      gnome/gnome-panel
BuildRequires:      library/gnome/gnome-vfs
BuildRequires:      library/desktop/gtk-vnc
BuildRequires:      library/libxml2
BuildRequires:      developer/gnome/gnome-doc-utils
BuildRequires:      gnome/gnome-keyring
BuildRequires:      library/gnome/gnome-keyring

%package l10n
Summary:                 %{summary} - l10n files

%package devel
Summary:        %{summary} - development files
SUNW_BaseDir:   %{_basedir}

%package root
Summary:       %{summary} - / filesystem
SUNW_BaseDir:            /

%prep
rm -rf %name-%version
mkdir -p %name-%version
%vinagre.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
%vinagre.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%vinagre.install -d %name-%version

# remove duplicated files in %{_datadir}/doc/vinagre,
# we have them in %{_datadir}/doc/SUNWvinagre
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/vinagre

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache icon-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%doc -d vinagre-%{vinagre.version} README AUTHORS
%doc(bzip2) -d vinagre-%{vinagre.version} COPYING ChangeLog po/ChangeLog help/ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/vinagre
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/vinagre-applet
%{_libdir}/vinagre-1
%dir %attr (0755, root, bin) %{_libdir}/bonobo
%dir %attr (0755, root, bin) %{_libdir}/bonobo/servers
%{_libdir}/bonobo/servers/GNOME_VinagreApplet.server
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/vinagre
%{_datadir}/vinagre-1
%{_datadir}/gnome/help/vinagre/C
%{_datadir}/omf/vinagre/vinagre-C.omf
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (-, root, root) %{_datadir}/mime
%dir %attr (-, root, root) %{_datadir}/mime/packages
%{_datadir}/mime/packages/vinagre-mime.xml
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*/apps
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*/mimetypes
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/*/status
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/icons/hicolor/*/status/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/omf/vinagre/vinagre-[a-z][a-z].omf
%{_datadir}/omf/vinagre/vinagre-[a-z][a-z]_[A-Z][A-Z].omf
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/vinagre/[a-z][a-z]
%{_datadir}/gnome/help/vinagre/[a-z][a-z]_[A-Z][A-Z]

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/vinagre.schemas

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Tue Jan 26 2010 - halton.huo@sun.com
- Update %files reflect version bumping to 2.29.6
* Fri Sep 11 2009 - jedy.wang@sun.com
- Remove SUNWmlib dependency.
* Wed Aug 12 2009 - halton.huo@sun.com
- Update %files to reflect version bumping to 2.27.90
* Wed Jul 29 2009 - halton.huo@sun.com
- Change %files to reflect version bumping to 2.27.5
- Add -devel pkg
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Tue Jan 06 2009 - halton.huo@sun.com
- Change %files to reflect version bumping
* Tue Dec 23 2008 - halton.huo@sun.com
- Update %files after bump to 2.25.3
* Mon Dec 22 2008 - halton.huo@sun.com
- update deps after run check-deps.pl
* Thu Nov 20 2008 - halton.huo@sun.com
- Add %{_datadir}/locale to %files l10n
* Thu Nov 13 2008 - halton.huo@sun.com
- Moved from SFE
* Wed Aug 20 2008 - nonsea@users.sourceforge.net
- Update %files becuase verion upgrading
* Wed Feb 20 2008 - nonsea@users.sourceforge.net
- Add -root package, add %post and %preun -root package.
- Update files according updated version.
* Fri Nov 30 2007 - nonsea@users.sourceforge.net
- Initial spec



