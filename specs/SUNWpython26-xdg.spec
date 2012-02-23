#
# spec file for package SUNWpython-xdg
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%include Solaris.inc

%define pythonver 2.6
%use pyxdg = python-xdg.spec

Name:            SUNWpython26-xdg
IPS_package_name: library/python-2/python-xdg-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:         %{pyxdg.summary}
URL:             %{pyxdg.url}
Version:         %{pyxdg.version}
License:         %{pyxdg.license}
SUNW_BaseDir:    %{_basedir}
SUNW_Copyright:  SUNWpython-xdg.copyright
BuildRoot:       %{_tmppath}/%{name}-%{version}-build
BuildRequires:   runtime/python-26
BuildRequires:   library/python-2/setuptools-26
Requires:        runtime/python-26

%include default-depend.inc
%include gnome-incorporation.inc

%description
Extensions to python-distutils for large or complex distributions.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
%pyxdg.prep -d  %{name}-%{version}

%build
%pyxdg.build -d  %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%pyxdg.install -d  %{name}-%{version}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/*
%doc -d  pyxdg-%version AUTHORS README PKG-INFO
%doc(bzip2) -d  pyxdg-%version COPYING ChangeLog
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWpython-xdg.spec.
* Tue Nov 18 2008 - jedy.wang@sun.com
- Fix installation directory problem.
* Wed Oct 29 2008 - brian.cameron@sun.com
- Add patch xdg-01-indentation.diff to fix runtime bugzilla bug #18289.
* Mon Oct 27 2008 - brian.cameron@sun.com
- Bump to 0.16.
* Fri Sep 12 2008 - matt.keenn@sun.com
- Update copyright
* Wed May 14 2008 - darren.kenny@sun.com
- Add dependency for SUNWPython
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version


