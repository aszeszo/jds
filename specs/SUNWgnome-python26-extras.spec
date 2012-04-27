#
# spec file for package SUNWgnome-python-extras
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#
%include Solaris.inc

%define pythonver 2.6

%use gpe = gnome-python-extras.spec

Name:                    SUNWgnome-python26-extras
IPS_package_name:        library/python-2/python-gnome-extras-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 Supplemental Python %{pythonver} bindings for GNOME
URL:                     %{gpe.url}
Version:                 %{gpe.version}
License:                 %{gpe.license}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWgnome-python-extras.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                SUNWgtk2
Requires:                runtime/python-26
Requires:                SUNWgnome-python26
Requires:                SUNWpygtk2-26
Requires:                SUNWpygobject26
Requires:                SUNWfirefox
Requires:                SUNWgksu
Requires:                SUNWgtkspell
BuildRequires:           SUNWgtk2-devel
BuildRequires:           SUNWgnome-python26-devel
BuildRequires:           SUNWpygtk2-26-devel
BuildRequires:           SUNWpygobject26-devel
BuildRequires:           SUNWfirefox-devel
BuildRequires:           SUNWgksu-devel
BuildRequires:           SUNWgtkspell-devel
BuildRequires:           library/python-2/setuptools-26

%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%gpe.prep -d %name-%version

%build
export CXX="$CXX -norunpath -compat=5"
export PYTHON=/usr/bin/python%{pythonver}
export PKG_CONFIG_PATH=/usr/lib/python%{pythonver}/pkgconfig
%gpe.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gpe.install -d %name-%version

echo deleting pyo files
find $RPM_BUILD_ROOT -type f -name "*.pyo" -exec rm -f {} ';'

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/gtk-2.0/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/pygtk/*
%doc -d gnome-python-extras-%{gpe.version} AUTHORS COPYING README
%doc(bzip2) -d gnome-python-extras-%{gpe.version} COPYING.GPL COPYING.LGPL ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Wed Oct 14 2009 - darren.kenny@sun.com
- Remove .pyo files from package.
* Wed Jul 08 2009 - dave.lin@sun.com
- Remove the compiler option -xregs=no%frameptr as it's set as default.
* Fri May 22 2009 - darren.kenny@sun.com
- Add -norunpath and other flags for CXX builds, to fix bug#6842284
* Thu Feb 26 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWgnome-python26-extras.spec.
* Tue Feb 24 2009 - laca@sun.com
- set PYTHON and PKG_CONFIG_PATH so the correct python version and
  dependencies are picked up
* Tue Feb 10 2009 - halton.huo@sun.com
- Add Requires: SUNWgtkspell to fix issue #3 for CR6753371
* Tue Nov 25 2008 - brian.lu@sun.com
- Remove "with-ff3" option, not needed any more
* Fri Sep 12 2008 - matt.keenn@sun.com
- Update copyright
* Fri May 30 2008 - evan.yan@sun.com
- Add option "--with-ff3" to enable building with Firefox3
- Add patch gnome-python-extras-02-using-firefox3.diff
* Wed May 21 2008 - damien.carbery@sun.com
- Add Build/Requires: SUNWfirefox/-devel and SUNWgksu/-devel after
  check-deps.pl run.
* Wed Feb 20 2007 - Darren Kenny <darren.kenny@sun.com>
- Move from spec-files-other since it's GNOME related.
* Mon Feb 18 2007 - Darren Kenny <darren.kenny@sun.com>
- Import into svn.opensolaris.org/spec-files-other
* Tue Jul 10 2007 - Brian Cameron <brian.cameron@sun.com>
- Bump to 2.19.1
* Fri Feb 9 2007 - Irene Huang <irene.huang@sun.com>
- created



