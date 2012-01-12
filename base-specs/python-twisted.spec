#
# base spec file for package python-twisted
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#

%define name Twisted

%define OSR 8094:2.5.0

Name:                    python-twisted
Summary:                 Event-based framework for internet applications
Vendor:                  twistedmatrix.org
URL:                     http://twistedmatrix.com/trac/
Version:                 10.1.0
Source:                  http://tmrc.mit.edu/mirror/twisted/Twisted/10.1/Twisted-%{version}.tar.bz2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                Python

%{?!pythonver:%define pythonver 2.6}

%prep
%setup -q -n Twisted-%version

%build
python%{pythonver} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{pythonver} setup.py install --root=$RPM_BUILD_ROOT --prefix=%_prefix

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

mkdir -p ${RPM_BUILD_ROOT}%{_basedir}/demo/twisted-python%{pythonver}
mv ${RPM_BUILD_ROOT}%{_bindir}/* \
   ${RPM_BUILD_ROOT}%{_basedir}/demo/twisted-python%{pythonver}
rmdir ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 27 2010 - brian.cameorn@oracle.com
- Bump to 10.1.0.
* Fri Mar 12 2010 - brian.cameron@sun.com
- Bump to 10.0.0 since it has been determined OSR is not needed.
* Fri Feb 19 2010 - brian.cameron@sun.com
- Revert to 8.2 until OSR can be completed.
* Wed Jan 27 2010 - brian.cameron@sun.com
- Bump to 9.0.
* Thu Oct 27 2009 - yuntong.jin@sun.com
- Change the owner to jouby
* Fri Jan 23 2009 - brian.cameron@sun.com
- Updated to 8.2.
* Thu Nov 27 2008 - darren.kenny@sun.com
- Split from SUNWpython-twisted.spec
* Wed Jul 23 2008 - brian.cameron@sun.com
- Bump to 8.1.
* Tue Feb 19 2008 - darren.kenny@sun.com
- Move demo scripts from /usr/bin to /usr/demo/twisted
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version
