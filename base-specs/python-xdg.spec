#
# base spec file for package python-xdg
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan 
#

%define oname xdg

%define version 0.19

%define OSR 8316:0.15

Name:            python-%oname
Summary:         Python library to access freedesktop.org standards
Vendor:          Freedesktop
License:         LGPL v2
URL:             http://www.freedesktop.org/wiki/Software/pyxdg
Version:         %{version}
Source0:         http://www.freedesktop.org/~lanius/py%{oname}-%{version}.tar.gz
BuildRoot:       %{_tmppath}/%{name}-%{version}-build
Requires:        Python

%{?!pythonver:%define pythonver 2.6}

%prep
%setup -q -n py%oname-%version

%build
python%{pythonver} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{pythonver} setup.py install --skip-build --prefix=%_prefix --root=$RPM_BUILD_ROOT

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jan 27 2009 - brian.cameron@sun.com
- Bump to 0.19.
* Mon Nov 23 2009 - brian.cameron@sun.com
- Bump to 0.18.
* Mon Nov 16 2009 - li.yuan@sun.com
- Change owner to liyuan.
* Thu Nov 27 2008 - darren.kenny@sun.com
- Split from SUNWpython-xdg.spec
- Bump to 0.17 and remove upstream patch
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
