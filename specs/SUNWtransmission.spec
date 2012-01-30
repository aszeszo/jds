#
# spec file for package SUNWtransmission
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 

%include Solaris.inc

%define OSR 9428:1.x

%define source_name transmission

Name:                    SUNWtransmission
IPS_package_name:        desktop/torrent/transmission
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:                 GTK and console BitTorrent client
Version:                 1.93
Source:                  http://download.m0k.org/transmission/files/transmission-%{version}.tar.bz2

URL:                     http://transmission.m0k.org/
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GPL v2, LGPL v2.1, MIT, BSD, Public Domain
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Source1:                 %{name}-manpages-0.1.tar.gz

# date:2009-06-22 owner:elaine type:branding
Patch1: transmission-01-set-noevports.diff
# date:2010-05-03 owner:yippi type:branding
Patch2: transmission-02-desktop.diff

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWopenssl-include
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWdbus-glib-devel
Requires: SUNWgtk2
Requires: SUNWopenssl-libraries
Requires: SUNWcurl
Requires: SUNWgnome-panel
Requires: SUNWdbus-glib
%if %option_with_gnu_iconv
Requires: SUNWgnu-libiconv
Requires: SUNWgnu-gettext
%else
Requires: SUNWuiu8
%endif

%package l10n
Summary:                 %{summary} - l10n files
Requires:        %{name}

%prep
%setup -q -c -n %{name}-%{version}
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -
cd %{source_name}-%{version}
%patch1 -p1
%patch2 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags -mt -xc99 -D__EXTENSIONS__"
%if %option_with_gnu_iconv
export CFLAGS="$CFLAGS -I/usr/gnu/include -L/usr/gnu/lib -R/usr/gnu/lib -lintl"
export CXXFLAGS="$CXXFLAGS -I/usr/gnu/include -L/usr/gnu/lib -R/usr/gnu/lib -lintl"
%endif

cd %{source_name}-%{version}

export LDFLAGS="%_ldflags"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

./configure --prefix=%{_prefix}   \
            --datadir=%{_datadir} \
            --mandir=%{_mandir}   \
	    --disable-wx	\
            --program-prefix=""

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
cd %{source_name}-%{version}
make DESTDIR=$RPM_BUILD_ROOT install

#install man page
rm -r $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr (-, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr (0755, root, other) %{_datadir}/%{source_name}
%{_datadir}/%{source_name}/*
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (-, root, other) %{_datadir}/icons/hicolor
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/transmission.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/transmission.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/transmission.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/transmission.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/transmission.png
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable
%dir %attr (-, root, other) %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/transmission.svg

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Mon May 03 2010 - brian.cameron@oracle.com
- Add patch transmission-02-desktop.diff to fix doo bug #6861.
* Mon May 03 2010 - brian.cameron@oracle.com
- Bump to 1.93.
* Fri Mar 26 2010 - brian.lu@sun.com
- Bump to 1.92
* Mon Feb 22 2010 - brian.lu@sun.com
- Bump to 1.91
* Thu Jan 28 2010 - brian.cameron@sun.com
- Bump to 1.83.
* Wed Jan 27 2010 - brian.cameron@sun.com
- Bump to 1.82.
* Mon Jan 19 2010 - brian.lu@sun.com
- Bump to 1.77.
* Mon Jul 27 2009 - elaine.xiong@sun.com
- Bump to 1.73.
* Mon Jun 22 2009 - elaine.xiong@sun.com
- Bump to 1.72. Add a branding patch to disable evports since libevent has
  troubles with evports that is the default poll mechanism used on Solaris).
* Fri May 22 2009 - elaine.xiong@sun.com
- Bump to 1.61. Remove upstream patch. Add -xc99 flag to CFLAGS.
* Thu Mar 05 2009 - brian.cameron@sun.com
- Change SUNWdbus-bindings to SUNWdbus-glib.
* Thu Feb 19 2009 - elaine.xiong@sun.com
- Bump to 1.50 and add a patch to fix build problems.
* Tue Feb 10 2009 - halton.huo@sun.com
- Add depend to SUNWgnome-panel and SUNWdbus-bindings to
  fix issue #7 for CR6753371
* Mon Jan 19 2009 - elaine.xiong@sun.com
- Bump to 1.4.2 and disable unsupported wxWidgets client.
* Mon Nov 17 2008 - elaine.xiong@sun.com
- Bump to 1.40.
* Mon Sep 15 2008 - elaine.xiong@sun.com
- Bump to 1.33.
* Tue Aug 12 2008 - elaine.xiong@sun.com
- Bump to 1.32 and remove upstream patches. 
* Tue Aug 05 2008 - elaine.xiong@sun.com
- Add new manpages into the package.
* Sat Aug 02 2008 - elaine.xiong@sun.com
- Temporarily disable new manpages.
* Tue Jul 29 2008 - takao.fujiwara@sun.com
- Add transmission-02-g11n-i18n-ui.diff. CR 6729782
* Mon Jul 28 2008 - elaine.xiong@sun.com
- Copy from SFEtransmission.spec and rename to SUNWtransmission.
* Wed Jun 25 2008 - darren.kenny@sun.com
- Bump to 1.2.2 and remove upstream patch for compiler. Add patch for solaris
  getgateway implementation.
* Tue May 27 2008 - trisk@acm.jhu.edu
- Add SUNWcurl dependency
* Sat May 24 2008 - trisk@acm.jhu.edu
- Bump to 1.21, drop patch2
* Sun Mar 02 2008 - trisk@acm.jhu.edu
- Bump to 1.06, add patch2 (fixed upstream)
* Tue Feb 26 2008 - markwright@internode.on.net
- Bump to 1.05, bump patch1, add icons.
* Thu Nov 22 2007 - daymobrew@users.sourceforge.net
- Enable building on Indiana systems.
* Thu Nov 01 2007 - trisk@acm.jhu.edu
- Bump to 0.91, replace patch1
* Mon Sep 10 2007 - trisk@acm.jhu.edu
- Bump to 0.82
* Thu Sep 6 2007 - Petr Sobotka sobotkap@centum.cz
- Fix typo in changelog
* Wed Aug 29 2007 - trisk@acm.jhu.edu
- Bump to 0.81, add workaround for broken tarball
* Mon Aug 20 2007 - trisk@acm.jhu.edu
- Clean up, allow building with Studio
* Sun Aug 19 2007 - Petr Sobotka sobotkap@centrum.cz
- Initial spec



