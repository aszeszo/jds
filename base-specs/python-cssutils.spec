#
# spec file for package python-cssutils
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%{?!pythonver:%define pythonver 2.6}

%define OSR 10175:0.9.x


%define tarball_version 0.9.6

Name:                    python-cssutils
License:  		 LGPL v3
Vendor:                  Google Code
Summary:                 A Python package to parse and build CSS Cascading Style Sheets.
URL:                     http://code.google.com/p/cssutils/
Version:                 0.9.6
Source:                  http://cssutils.googlecode.com/files/cssutils-%{tarball_version}.zip
BuildRoot:               %{_tmppath}/%{name}-%{tarball_version}-build
Docdir:			 %{_defaultdocdir}/python-cssutils

%description
A Python package to parse and build CSS Cascading Style Sheets. It supports DOM only, and not any rendering facilities.

%prep
%setup -q -n cssutils-%{tarball_version}
unzip -d cssutils-%{tarball_version}.zip %{SOURCE}

%install
python%{pythonver} setup.py install --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.pyo" -exec rm -f {} ';'

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages
rm -r $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/cssutils-%{tarball_version}-py%{pythonver}.egg-info
%{_libdir}/python%{pythonver}/vendor-packages/cssutils
%{_libdir}/python%{pythonver}/vendor-packages/encutils
%{_libdir}/python%{pythonver}/vendor-packages/tests

%changelog
* Sat Oct 17 2009 - brian.cameron@sunc.om
- Bump to 0.9.6.
* Wed Jul 22 2009 - brian.cameron@sun.com
- Bump to 0.9.6b1.
* Mon Mar 02 2009 - dave.lin@sun.com
- Change the svr4 pkg version number to digit only.
  to fix the integration issue.
* Fri Jan 23 2009 - jijun.yu@sun.com
- Bump to 0.9.6a0.
* Thu Nov 13 2008 - jijun.yu@sun.com
- Initial base spec
