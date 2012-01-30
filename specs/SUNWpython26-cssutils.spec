#
# spec file for package SUNWpython26-cssutils
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#

%include Solaris.inc 
%define pythonver 2.6
%use pycssutils = python-cssutils.spec

Name:                    SUNWpython26-cssutils
IPS_package_name:        library/python-2/cssutils-26
Meta(info.classification): %{classification_prefix}:Development/Python
License:  		 LGPL v3
Summary:                 A Python 2.6 package to parse and build CSS Cascading Style Sheets.
Version:                 %{pycssutils.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWpython-cssutils.copyright
BuildRoot:               %{_tmppath}/%{name}-%{pycssutils.tarball_version}-build
Requires:                SUNWPython26
BuildRequires:           SUNWpython26-setuptools
BuildRequires:           SUNWunzip

Patch1:                  cssutils-01-py26.diff 

%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir -p %name-%version
%pycssutils.prep -d %name-%version

cd %name-%version
cd cssutils-%version

%patch1 -p1

cd ../..

%install
export PYTHON="/usr/bin/python%{pythonver}"
export CFLAGS="%optflags -I/usr/xpg4/include -I%{_includedir} -I/usr/include/python%{pythonver}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

rm -rf $RPM_BUILD_ROOT
%pycssutils.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/cssutils-%{pycssutils.tarball_version}-py%{pythonver}.egg-info
%{_libdir}/python%{pythonver}/vendor-packages/cssutils
%{_libdir}/python%{pythonver}/vendor-packages/encutils
%{_libdir}/python%{pythonver}/vendor-packages/tests
%doc(bzip2) -d cssutils-%{pycssutils.tarball_version} COPYING COPYING.LESSER 
%doc(bzip2) -d cssutils-%{pycssutils.tarball_version} CHANGELOG.txt README.txt
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Mon Dec 07 2009 - yuntong.jin@sun.com
- explicitly use python2.6 in python scrip
* Wed Mar 04 2009 - dave.lin@sun.com
- Change the svr4 pkg version number to digit
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWpython-cssutils.spec.
* Tue Dec 02 2008 - jijun.yu@sun.com
- Change Copyright name.
* Thu Nov 27 2008 - jijun.yu@sun.com
- Correct Name
* Wed Nov 26 2008 - jijun.yu@sun.com
- Initial version for python 2.6.


