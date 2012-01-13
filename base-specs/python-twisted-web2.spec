#
# base spec file for package python-twisted-web2
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#

%define OSR 10182:8.1.0

Name:                    Twisted-Web2
Summary:                 A HTTP/1.1 Server Framework
URL:                     http://twistedmatrix.com/trac/
Version:                 8.1.0
Vendor:                  twistedmatrix.org
Source:                  http://tmrc.mit.edu/mirror/twisted/Web2/8.1/TwistedWeb2-%{version}.tar.bz2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                Python

%{?!pythonver:%define pythonver 2.6}

%prep
%setup -q -n TwistedWeb2-%{version}

%build
python%{pythonver} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{pythonver} setup.py install --prefix=$RPM_BUILD_ROOT/%_prefix

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Oct 27 2009 - yuntong.jin@sun.com
- Change the owner to jouby
* Thu Nov 27 2008 - darren.kenny@sun.com
- Split from SUNWpython-twisted-web2.spec
* Tue Sep 30 2008 - brian.cameron@sun.com
- Bump to 8.1.0.
* Fri Jul 25 2008 - brian.cameron@sun.com
- Initial version.
