#
# base spec file for package coherence
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# bugdb: http://coherence.beebits.net/ticket/$bugid
%define owner jouby

%define OSR 11375:0.7

%{?!pythonver:%define pythonver 2.6}

%define src_url         http://coherence.beebits.net/download
%define src_name        Coherence

Name:                    Coherence
Summary:                 DLNA/UPnP framework for the digital living
URL:                     http://coherence.beebits.net
Version:                 0.6.6.2
Vendor:                  coherence.beebits.net
Source:                  %{src_url}/%{src_name}-%{version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                python

%prep
%setup -q -n %name-%version

%build
python%{default_python_version} setup.py build

%install
python%{default_python_version} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix} 

mkdir -p $RPM_BUILD_ROOT%{_datadir}/dbus-1/services
cp misc/org.Coherence.service $RPM_BUILD_ROOT%{_datadir}/dbus-1/services

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

# remove the log test code with GPL license
# https://code.fluendo.com/flumotion/trac/ticket/1259
rm $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/coherence/extern/log/test_log*

# remove applet-coherence which depends on python-qt
rm $RPM_BUILD_ROOT%{_bindir}/applet-coherence

# remove misc
rm -r $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/misc

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Oct 16 2009 - brian.lu@sun.com
- Move to python 2.6
* Fri Sep 17 2009 -brian.lu@sun.com
- Ship org.Coherence.service file
* Thu Jun 04 2009 - alfred.peng@sun.com
- Remove misc directory from the package for now.
* Thu Jun 04 2009 - alfred.peng@sun.com
- Bump to 0.6.4 and remove upstreamed patch solaris.diff.
* Fri Mar 06 2009 - alfred.peng@sun.com
- initial version 0.6.2.
