#
# spec file for package SUNWdrivel
#
# includes module(s): drivel
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner ydzhang
#

%include Solaris.inc

%use drivel = drivel.spec

Name:               SUNWdrivel
IPS_package_name:   editor/blog/drivel
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:            Drivel - Blog Editor
Version:            %{drivel.version}
SUNW_Copyright:     %{name}.copyright
License:            %{drivel.license}
SUNW_BaseDir:       %{_basedir}
BuildRoot:          %{_tmppath}/%{name}-%{version}-build
Source1:            %{name}-manpages-0.1.tar.gz

# these packages are only available on i386/x64
%ifnarch sparc

%include default-depend.inc
%include desktop-incorporation.inc
Requires:           SUNWlibgnomecanvas
Requires:           SUNWgnome-libs
Requires:           SUNWgnome-gtksourceview
Requires:           SUNWgtkspell
Requires:           SUNWgnu-idn
Requires:           SUNWcurl
Requires:           %{name}-root
Requires:           SUNWdesktop-cache
Requires:           SUNWlibsoup
BuildRequires:      SUNWlibgnomecanvas-devel
BuildRequires:      SUNWgnome-libs-devel
BuildRequires:      SUNWgnome-gtksourceview-devel
BuildRequires:      SUNWgtkspell-devel
BuildRequires:      SUNWgnome-doc-utils

%package l10n
Summary:            %{summary} - l10n files
Requires:           %{name}

%package root
Summary:            %{summary} - / filesystem
SUNW_BaseDir:       /
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir -p %name-%version
%drivel.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build
export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"
%drivel.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%drivel.install -d %name-%version

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
%doc -d drivel-%{drivel.version} README AUTHORS
%doc(bzip2) -d drivel-%{drivel.version} COPYING ChangeLog po/ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/drivel
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/drivel
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, bin) %{_datadir}/omf
%dir %attr (0755, root, bin) %{_datadir}/omf/drivel
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*.png
%dir %attr (0755, root, other) %{_datadir}/mime-info
%{_datadir}/mime-info/*
%dir %attr (0755, root, root) %{_datadir}/mime
%dir %attr (0755, root, root) %{_datadir}/mime/packages
%{_datadir}/mime/packages/*
%dir %attr (0755, root, other) %{_datadir}/application-registry
%{_datadir}/application-registry/*
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/gnome
%dir %attr (0755, root, other) %{_datadir}/icons/gnome/*
%{_datadir}/icons/gnome/*/mimetypes/*
%dir %attr (0755, root, other) %{_datadir}/gnome
%dir %attr (0755, root, bin) %{_datadir}/gnome/help
%dir %attr (0755, root, bin) %{_datadir}/gnome/help/drivel
%{_datadir}/gnome/help/drivel/*/drivel.xml
%{_datadir}/gnome/help/drivel/C/legal.xml
%{_datadir}/omf/drivel/drivel-C.omf
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%dir %attr (0755, root, bin) %{_datadir}/omf/drivel
%{_datadir}/omf/drivel/drivel-[a-z][a-z].omf
%attr (-, root, other) %{_datadir}/locale

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/drivel.schemas

#endif for "ifnarch sparc"
%endif

%changelog
* Mon Aug 02 2010 - christian.kelly@oracle.com
- Fix %files.
* Mon Jul 05 2010 - christian.kelly@oracle.com
- Fix %files.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 9 2009 - david.zhang@sun.com
- Add ifnarch sparc so that it only build at i386/x64 platform
* Wed Feb 11 2009 - david.zhang@sun.com
- Initial spec



