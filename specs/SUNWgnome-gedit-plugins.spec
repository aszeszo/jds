#
# spec file for package: SUNWgnome-gedit-plugins
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#

%include Solaris.inc

%{?!pythonver:%define pythonver 2.6}

%use gedit_plugins = gedit-plugins.spec

Name:       SUNWgnome-gedit-plugins
IPS_package_name: editor/gedit/gedit-plugins
Meta(info.classification): %{classification_prefix}:Applications/Accessories,%{classification_prefix}:Development/Editors
Summary:    A collection of plugins for gedit
Version:    %{gedit_plugins.version}
SUNW_Copyright: %{name}.copyright
License:	GPLv2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir:            %{_basedir}

%include default-depend.inc
%include desktop-incorporation.inc

Requires:       SUNWgnome-text-editor
Requires:       SUNWgnome-python26-desktop
Requires:       SUNWgnome-gtksourceview
Requires:       runtime/python-26 

BuildRequires:  SUNWgnome-text-editor-devel
BuildRequires:  SUNWgnome-doc-utils
BuildRequires:  SUNWgnome-base-libs
BuildRequires:  SUNWgnome-common-devel 
BuildRequires:  SUNWxwinc
BuildRequires:  SUNWxorg-headers
BuildRequires:  SUNWperl-xml-parser
BuildRequires:  SUNWgmake
BuildRequires:  developer/build/automake-110
BuildRequires:  SUNWgnome-doc-utils
BuildRequires:  SUNWgnome-base-libs
BuildRequires:  SUNWgnome-common-devel
BuildRequires:  text/gnu-gettext
BuildRequires:  SUNWgnome-character-map

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc


%description
Plugins for gedit including: bracketcompletion, charmap, codecomment, colorpicker
drawspaces, joinlines, sessionsaver, showtabbar, smartspaces, terminal 
%prep
rm -rf %name-%version
mkdir %name-%version
%gedit_plugins.prep -d %name-%version
cd %{_builddir}/%name-%version

%build
export CPPFLAGS="-I/usr/include/gucharmap-2 -I/usr/include/python%{pythonver}"
export CFLAGS="%optflags -I/usr/include/gucharmap-2 -I%{_includedir} -I/usr/include/python%{pythonver}"
export RPM_OPT_FLAGS="$CFLAGS"
export PYTHON=/usr/bin/python%{pythonver} 
%gedit_plugins.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gedit_plugins.install -d %name-%version

find $RPM_BUILD_ROOT -name "*.pyc" -exec rm {} \;

%post
%restart_fmri gconf-cache desktop-mime-cache

%postun
%restart_fmri desktop-mime-cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, sys)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/gedit-2
%dir %attr (0755, root, bin) %{_libdir}/gedit-2/plugins
%{_libdir}/gedit-2/plugins/sessionsaver/*.py
%{_libdir}/gedit-2/plugins/lib*.so
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_libdir}/gedit-2/plugins/*.py

%dir %attr (0755, root, bin) %{_datadir}/gedit-2
%dir %attr (0755, root, bin) %{_datadir}/gedit-2/plugins
%{_datadir}/gedit-2/plugins/sessionsaver/sessionsaver.ui
%{_datadir}/gedit-2/plugins/drawspaces/drawspaces.ui
%{_datadir}/gedit-2/plugins/bookmarks/bookmark.png
%{_datadir}/gedit-2/plugins/commander/modules/*.py
%{_datadir}/gedit-2/plugins/commander/modules/*.pyo
%{_datadir}/gedit-2/plugins/commander/modules/find/*.py
%{_datadir}/gedit-2/plugins/commander/modules/find/*.pyo

%dir %attr (0755, root, sys) %{_datadir}
%doc  -d gedit-plugins-%{gedit_plugins.version}  AUTHORS  NEWS README 
%doc(bzip2)  -d gedit-plugins-%{gedit_plugins.version} ChangeLog COPYING 
%dir %attr (0755, root, other) %{_datadir}/doc

%{_libdir}/gedit-2/plugins/commander/*.py
%{_libdir}/gedit-2/plugins/commander/commands/*.py
%{_libdir}/gedit-2/plugins/commander/commands/*.pyo
%{_libdir}/gedit-2/plugins/multiedit/*.py

%files root
%defattr (-, root, sys)
%dir %attr (0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/gedit-show-tabbar-plugin.schemas
%{_sysconfdir}/gconf/schemas/gedit-drawspaces.schemas

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/locale/*
%dir %attr (0755, root, other) %{_datadir}/locale/*/LC_MESSAGES
%{_datadir}/locale/*/LC_MESSAGES/*.mo


%changelog
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Bump to 2.30.0.
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Missing SUNW_BaseDir.
- Add sub-packages for -l10n and -root.
- Major re-working of %files.
* Wen Mar 31 2010 - yuntong.jin@sun.com
- Fix files attr 
* Tue Feb 23 2010 - yuntong.jin@sun.com
- Initial spec




