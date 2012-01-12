#
# base spec file for package python-zope-interface
#
%define owner jouby 
#

%define OSR 8094:3.3.0

Name:                    python-zope-interface
Summary:                 A separate distribution of the zope.interface package used in Zope 3
Vendor:                  zope.org
License:                 ZPL
URL:                     http://zope.org/Wikis/Interfaces/FrontPage
Version:                 3.3.0
Source:                  http://www.zope.org/Products/ZopeInterface/%{version}/zope.interface-%{version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
Requires:                Python

%{?!pythonver:%define pythonver 2.6}

%prep
%setup -q -n zope.interface-%version

%build
python%{pythonver} ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{pythonver} ./setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix} --no-compile

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Oct 27 2009 - yuntong.jin@sun.com
- Change the owner to jouby
* Thu Nov 27 2008 - darren.kenny@sun.com
- Split from SUNWpython-zope-interface.spec
* Tue Sep 16 2008 - matt.keenn@sun.com
- Update copyright
* Mon May 26 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWPython/-devel.
* Wed Feb 19 2008 - darren.kenny@sun.com
- Revert to 3.3.0 since 3.4.x series seems to be too unstable (and version
  number keeps changing). Wait until 3.4.x stabilises before returning to it.
* Tue Feb 19 2008 - ghee.teo@sun.com
- Updated version to 3.4.1
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- Initial version
