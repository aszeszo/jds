#
# spec file for package SUNWpygtksourceview26 aka 
#                       library/python-2/pygtksourceview-26
#
# includes module(s): pygtksourceview
#
# Copyright (c) 2005, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc
%define pythonver 2.6
%define python_version %{pythonver}

%use pygtksourceview = pygtksourceview.spec

Name:              SUNWpygtksourceview26
IPS_package_name:  library/python-2/pygtksourceview2-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:           Python 2.6 bindings for the gtksourceview library
Version:           %{pygtksourceview.version}
SUNW_BaseDir:      %{_basedir}
SUNW_Copyright:    %{name}.copyright
License:           %{pygtksourceview.license}
BuildRoot:         %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: runtime/python-26
Requires: library/python-2/pygobject-26
Requires: library/desktop/gtksourceview
BuildRequires: runtime/python-26
BuildRequires: library/python-2/pygobject-26
BuildRequires: library/python-2/pygtk2-26
BuildRequires: library/desktop/gtksourceview
BuildRequires: library/python-2/setuptools-26
BuildRequires: text/gnu-sed

%package devel
Summary:           %{summary} - development files
SUNW_BaseDir:      %{_basedir}

%prep
rm -rf %name-%version
mkdir %name-%version
%pygtksourceview.prep -d %name-%version

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED

export PYTHON="/usr/bin/python2.6"
export CPPFLAGS="-I/usr/xpg4/include -I/usr/include/python%{pythonver}"
export CFLAGS="%optflags -I/usr/xpg4/include -I%{_includedir} -I/usr/include/python%{pythonver}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export PYCC_CC="$CC"
export PYCC_CXX="$CXX"

%pygtksourceview.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%pygtksourceview.install -d %name-%version

# move to vendor-packages
if [ -x $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages ]; then
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python?.?/vendor-packages

%files devel
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/*

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Fri Feb  4 2010 - laszlo.peter@oracle.com
- created, based on SUNWgnome-python26-libs.spec
* Wed Sep 23 2009 - brian.cameron@sun.com
- Use PKG_CONFIG_TOP_BUILD_DIR environment variable when building pygtk and
  pygtksourceview, so that pkg-config expands $(top_builddir), otherwise
  pygobject pkg-config variables do not expand nicely and the build fails.
* Sat Jun 20 2009 - christian.kelly@sun.com
- Minor pkg'ing fix.
* Wed Mar 25 2009 - li.yuan@sun.com
- Move pyspi from SUNWgnome-python-libs to SUNWgnome-a11y-libs.
* Mon Feb  2 2009 - laca@sun.com
- created, based on SUNWgnome-python25-libs.spec
* Tue Nov 25 2008 - laca@sun.com
- get rid of SUNWgnome-python-libs-common because there are no files
  that we can share between 2.4 and 2.5.
* Mon Nov 24 2008 - laca@sun.com
- created, based on SUNWPython-extra.spec
* Wed Sep 17 2008 - laca@sun.com
- set PYTHON to python2.4 (instead of just python) to make sure the
  right version is used for the build
* Tue Aug 12 2008 - damien.carbery@sun.com
- Add %{_libdir}/libpyglib-2.0.so* to %files.
* Mon Aug 11 2008 - damien.carbery@sun.com
- Move site-packages to vendor-packages here because pygobject 2.15.2 borked
  when vendor-packages was specified by pyexecdir and pythondir in make
  install.
* Tue Oct 16 2007 - damien.carbery@sun.com
- Remove unnecessary environment variable settings.
* Mon Oct  8 2007 - damien.carbery@sun.com
- Add SUNWgnome-gtksourceview dependency as it is required to by
  pygtksourceview.
* Sun Oct  7 2007 - damien.carbery@sun.com
- Add pygtksourceview as it is required to build python bindings in gedit.
* Fri Sep 28 2007 - laca@sun.com
- delete some unnecessary env vars
* Fri Aug 31 2007 - damien.carbery@sun.com
- Remove pygtksourceview.spec. It is still not building and isn't required.
* Thu Jul 05 2007 - damien.carbery@sun.com
- Add pygtksourceview.spec, but disable it because it is not building yet.
* Tue Jan  9 2007 - laca@sun.com
- define PYCC_CC and PYCC_CXX to override what the configure script sets
  in CC/CXX
* Mon Aug 28 2006 - damien.carbery@sun.com
- Fix typo in PKG_CONFIG_PATH data (s/=/-/).
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Fri May 12 2006 - damien.carbery@sun.com
- Small update to dependency list after check-deps.pl run.
* Thu May 11 2006 - brian.cameron@sun.com
- Move pygtk-demo to demo directory.
* Wed Apr  5 2006 - damien.carbery@sun.com
- Add pygobject. It has been moved from pygtk2.
* Mon Feb 20 2006 - damien.carbery@sun.com
- Complete update of Build/Requires after running check-deps.pl script.
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Mon Jan 09 2006 - damien.carbery@sun.com
- Add gnome-vfs module.
* Thu Oct 27 2005 - laca@sun.com
- add pygtk2
* Tue Sep 20 2005 - laca@sun.com
- move to /usr as Python was also moved there
* Thu Sep 01 2005 - damien.carbery@sun.com
- Remove unused pygtk2 references.
* Wed Aug 30 2005 - damien.carbery@sun.com
- Add Build/Requires for SUNWgnome-file-mgr (nautilus) and SUNWgnome-print
  (libgnomeprint/libgnomeprintui) so that those submodules will be built.
* Mon Aug 29 2005 - rich.burridge@sun.com
- Adjusted to put files under /usr/sfw
* Thu Aug 25 2005 - rich.burridge@sun.com
- Removed the 'export CC="/opt/SUNWspro/bin/cc"' line. No longer needed.
* Mon Aug 22 2005 - rich.burridge@sun.com
- Adjustments needed to make the package proto maps equivalent to what gets
  installed via "make install"
* Thu Aug 11 2005 - rich.burridge@sun.com
- initial version



