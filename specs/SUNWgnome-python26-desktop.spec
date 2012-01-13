#
# spec file for package SUNWgnome-python-desktop26
#
# includes module(s): gnome-python-desktop
#
# Copyright (c) 2005 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc

%define pythonver 2.6
%use gnome_python_desktop = gnome-python-desktop.spec

Name:              SUNWgnome-python26-desktop
IPS_package_name:  library/python-2/python-gnome-desktop-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:           Python %{pythonver} support desktop libraries for GNOME
Version:           %{gnome_python_desktop.version}
SUNW_BaseDir:      %{_basedir}
SUNW_Copyright:    SUNWgnome-python-desktop.copyright
License:           %{gnome_python_desktop.license}
BuildRoot:         %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWlibgnomecanvas
Requires: SUNWgnome-python26
Requires: SUNWpygtk2-26
Requires: SUNWpygobject26
Requires: SUNWpycairo26
Requires: SUNWpyorbit26
Requires: SUNWgnome-file-mgr
Requires: SUNWgnome-a11y-libs
Requires: SUNWgnome-libs
Requires: SUNWPython26-extra
Requires: SUNWgnome-config
Requires: SUNWPython26
Requires: SUNWgnome-vfs
Requires: SUNWlibms
Requires: SUNWlibpopt
BuildRequires: SUNWmlib
Requires: SUNWgnome-gtksourceview
Requires: SUNWgnome-cd-burner
Requires: SUNWgnome-component
Requires: SUNWgnome-media-apps
Requires: SUNWgnome-media-player
Requires: SUNWgnome-panel
Requires: SUNWgnome-wm
Requires: SUNWlibgtop
BuildRequires: SUNWlibgnomecanvas-devel
BuildRequires: SUNWPython26-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-python26-devel
BuildRequires: SUNWpygtk2-26-devel
BuildRequires: SUNWpygobject26-devel
BuildRequires: SUNWpycairo26-devel
BuildRequires: SUNWpyorbit26-devel
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWlibpopt-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWgnome-file-mgr-devel
BuildRequires: SUNWgnome-a11y-libs-devel
BuildRequires: SUNWPython26-extra
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-cd-burner-devel
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWgnome-media-apps-devel
BuildRequires: SUNWgnome-media-player
BuildRequires: SUNWgnome-panel-devel
BuildRequires: SUNWgnome-wm-devel
BuildRequires: SUNWgnome-gtksourceview-devel
BuildRequires: SUNWlibgtop-devel
BuildRequires: SUNWpython26-setuptools
BuildRequires: SUNWgnome-pdf-viewer

%package devel
Summary:           %{summary} - development files
SUNW_BaseDir:      %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version
%gnome_python_desktop.prep -d %name-%version

%build
export MSGFMT="/usr/bin/msgfmt"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export PYTHON="/usr/bin/python%{pythonver}"
export CPPFLAGS="-I/usr/xpg4/include -I/usr/include/python%{pythonver}"
export CFLAGS="%optflags -I/usr/xpg4/include -I%{_includedir} -I/usr/include/python%{pythonver}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%gnome_python_desktop.build -d %name-%version

%install
%gnome_python_desktop.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages

%files devel
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/pygtk/*
#%if %option_with_gtk_doc
#%{_datadir}/gtk-doc/html/*
#%endif

%changelog
* Tue Jul 07 2009 - brian.cameron@sun.com
- Split out into Python 2.4 and 2.6 spec-files
* Tue Apr 07 2009 - dave.lin@sun.com
- Change to depend on SUNWgnome-media-player instread of obsoleted devel pkg.
* Wed Jul 23 2008 - damien.carbery@sun.com
- Wrap gtk-doc in %files with %if %option_with_gtk_doc.
* Wed May 07 2008 - damien.carbery@sun.com
- Remove PERL5LIB setting as it is not necessary.
* Tue Aug 08 2006 - damien.carbery@sun.com
- Add to Build/Requires after running check-deps.pl.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Wed Mar 15 2006 - damien.carbery@sun.com
- Add to Build/Requires after running check-deps.pl.
* Tue Mar 14 2006 - damien.carbery@sun.com
- Set perms for %{_datadir} in devel package.
* Tue Mar 14 2006 - glynn.foster@sun.com
- Initial version because I'm too much of a wuss to merge it into
  SUNWgnome-python-libs.spec



