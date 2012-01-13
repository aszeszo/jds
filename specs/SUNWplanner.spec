#
# spec file for package SUNWplanner
#
# includes module(s): planner 
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jat
#
%include Solaris.inc
%use planner = planner.spec

Name:                    SUNWplanner
IPS_package_name:        desktop/project-management/planner
Meta(info.classification): %{classification_prefix}:Applications/Office
Summary:                 Planner is a project managment tool for the GNOME desktop
Version:                 %{planner.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{planner.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                SUNWlibgnomecanvas
Requires:                SUNWdesktop-cache
Requires:                %{name}-root
BuildRequires:           SUNWgnome-common-devel
                                                                                
# GLIB GTK LIBGNOMECANVAS LIBGLADE
BuildRequires: SUNWlibgnomecanvas-devel
# LIBGNOMEUI LIBGNOMEUI
BuildRequires: SUNWgnome-libs-devel
# GNOME_VFS
BuildRequires: SUNWgnome-vfs-devel
# GCONF
BuildRequires: SUNWgnome-config-devel
# LIBXML
BuildRequires: SUNWlxml-devel
# LIBXSLT
BuildRequires: SUNWlxsl-devel
# PYGTK
BuildRequires: SUNWpygtk2-26-devel
BuildRequires: SUNWpython26-setuptools

# GLIB GTK LIBGNOMECANVAS LIBGLADE
# LIBGNOMEUI LIBGNOMEUI
Requires: SUNWgnome-libs
# GNOME_VFS
Requires: SUNWgnome-vfs
# GCONF
Requires: SUNWgnome-config
# LIBXML
Requires: SUNWlxml
# LIBXSLT
Requires: SUNWlxsl
# PYGTK
Requires: SUNWpygtk2-26

Requires: SUNWlibgnome-keyring


%package devel
Summary:      %{summary} - development files
SUNW_BaseDir: %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:     %{name}

%package root
Summary:      %{summary} - / filesystem
SUNW_BaseDir: /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:      %{summary} - l10n files
Requires:     %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%planner.prep -d %name-%version

%build
export LDFLAGS="%_ldflags"
export CFLAGS="%optflags"
export PYTHON="/usr/bin/python%{default_python_version}"
%planner.build -d %name-%version
                                                                                
%install
%planner.install -d %name-%version
rm -rf $RPM_BUILD_ROOT%{_libdir}/python2.6/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages \
	$RPM_BUILD_ROOT%{_libdir}/python2.6/vendor-packages

# generated in the postinstall scripts (update-mime-database)
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/aliases
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/globs
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/magic
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/mime.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/subclasses
rm -f $RPM_BUILD_ROOT%{_datadir}/mime/XMLnamespaces

# Clean up unpackaged files
rm -fr $RPM_BUILD_ROOT%{_datadir}/gtk-doc
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'
                                                                                
%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache mime-types-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache mime-types-cache

%files
#	%dir %attr (0755, root, other) %{_datadir}/doc
#	%defattr (-, root, bin)
#	%doc -d planner-%{planner.version} README AUTHORS
#	%doc(bzip2) -d planner-%{planner.version} COPYING NEWS ChangeLog
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libplanner*.so*
%dir %attr (0755, root, bin) %{_libdir}/planner
%dir %attr (0755, root, bin) %{_libdir}/planner/file-modules
%attr(755,root,root) %{_libdir}/planner/file-modules/*
%dir %attr (0755, root, bin) %{_libdir}/planner/plugins
%attr(755,root,root) %{_libdir}/planner/plugins/*
%dir %attr (0755, root, bin) %{_libdir}/planner/storage-modules
%attr(755,root,root) %{_libdir}/planner/storage-modules/*
%dir %attr (0755, root, bin) %{_libdir}/python2.6
%dir %attr (0755, root, bin) %{_libdir}/python2.6/vendor-packages
%{_libdir}/python2.6/vendor-packages/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/planner.desktop
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/planner/C
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/mimetypes
%attr (0644, root, bin) %{_datadir}/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-planner.png
%dir %attr (0755, root, root) %{_datadir}/mime
%dir %attr (0755, root, root) %{_datadir}/mime/packages
%attr(644,root,bin) %{_datadir}/mime/packages/planner.xml
%{_datadir}/omf/planner/*-C.omf
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%attr(644,root,root) %{_datadir}/pixmaps/gnome-planner.png
%dir %attr (0755, root, bin) %{_datadir}/planner
%dir %attr (0755, root, bin) %{_datadir}/planner/dtd
%{_datadir}/planner/dtd/*
%dir %attr (0755, root, bin) %{_datadir}/planner/glade
%{_datadir}/planner/glade/*
%dir %attr (0755, root, bin) %{_datadir}/planner/images
%{_datadir}/planner/images/*
%dir %attr (0755, root, bin) %{_datadir}/planner/stylesheets
%{_datadir}/planner/stylesheets/*
%dir %attr (0755, root, bin) %{_datadir}/planner/sql
%{_datadir}/planner/sql/*
%dir %attr (0755, root, bin) %{_datadir}/planner/ui
%{_datadir}/planner/ui/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/planner.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z]*.omf

%changelog
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Tue Mar 03 2009 - brian.cameron@sun.com
- Use find command to remove .la files.
* Tue Sep 23 2008 - takao.fujiwara@sun.com
- Fixed wrong files and permissions.
* Monday, June 30, 2008 - joseph.townsend@sun.com
- Initial spec-file created



