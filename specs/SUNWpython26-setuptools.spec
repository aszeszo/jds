#
# spec file for package SUNWpython26-setuptools
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#

%include Solaris.inc

%define pythonver 2.6
%use pst = python-setuptools.spec

Name:            SUNWpython26-setuptools
IPS_package_name: library/python-2/setuptools-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:         Download, build, install, upgrade, and uninstall Python packages easily
URL:             %{pst.url}
Version:         %{pst.version}
SUNW_BaseDir:    %{_basedir}
SUNW_Copyright:  SUNWpython-setuptools.copyright
License:         PSF, Zope Public License
BuildRoot:       %{_tmppath}/%{name}-%{version}-build
BuildRequires:   SUNWPython26-devel
Requires:        SUNWPython26

%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir -p %name-%version
%pst.prep -d %name-%version

%build
%pst.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%pst.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/easy_install
%{_bindir}/easy_install-%{pythonver}
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/setuptools-%{pst.tarball_version}-py%{pythonver}.egg-info
%{_libdir}/python%{pythonver}/vendor-packages/setuptools/*
%{_libdir}/python%{pythonver}/vendor-packages/pkg_resources.pyc
%{_libdir}/python%{pythonver}/vendor-packages/easy_install.pyc
%{_libdir}/python%{pythonver}/vendor-packages/site.pyc
%{_libdir}/python%{pythonver}/vendor-packages/pkg_resources.py
%{_libdir}/python%{pythonver}/vendor-packages/easy_install.py
%{_libdir}/python%{pythonver}/vendor-packages/site.py
%doc -d setuptools-%{pst.tarball_version} PKG-INFO
%doc(bzip2) -d setuptools-%{pst.tarball_version} README.txt
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Fri Apr 30 2010 - yuntong.jin@sun.com
- Change the ownership to jouby 
* Mon Feb  2 2009 - laca@sun.com
- create based on SUNWpython25-setuptools.spec
* Tue Nov 25 2008 - laca@sun.com
- create based on SUNWpython-setuptools.spec
* Tue Nov 18 2008 - jedy.wang@sun.com
- Fix installation directory problem.
* Wed Oct 01 2008 - brian.cameron@sun.com
- Bump to 0.6.9.
* Tue Sep 16 2008 - matt.keenn@sun.com
- Update copyright
* Wed May 14 2008 - darren.kenny@sun.com
- Add SUWNPython dependency.
* Mon May 05 2008 - brian.cameron@sun.com
- Bump to 0.6.8
* Tue Mar 11 2008 - damien.carbery@sun.com
- Use %tarball_version as appropriate in %files and %pre and %install.
* Fri Mar 07 2008 - damien.carbery@sun.com
- Change package version to be numeric.
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version


