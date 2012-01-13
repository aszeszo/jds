#
# base spec file for package simplejson
#
# Copyright (c) 2008, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: http://code.google.com/p/simplejson/issues/
#
%{?!pythonver:%define pythonver 2.6}

%define OSR 10613:2.0.4

%define src_url         http://pypi.python.org/packages/source/s/simplejson
%define src_name        simplejson

Name:                    simplejson
Summary:                 JSON (JavaScript Object Notation) encoder/decoder
Vendor:                  Python.org
License:                 MIT
URL:                     http://undefined.org/python/#simplejson
Version:                 2.1.2
Source:                  %{src_url}/%{src_name}-%{version}.tar.gz
Patch1:                  simplejson-01-sortkeys.diff
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                python

%prep
%setup -q -n %name-%version
#date:2010-11-12 owner:yippi type:feature bugid:86
%patch1 -p1

%build
export PYTHON=/usr/bin/python%{pythonver}
python%{pythonver} setup.py build

%install
python%{pythonver} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix} 

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Nov 12 2010 - Brian.Cameron@oracle.com
- Bump to 2.1.2.
* Thu Apr 15 2010 - Brian.Cameron@sun.com
- Bump to 2.1.1.
* Fri Mar 12 2010 - Brian.Cameron@sun.com
- Bump to 2.1.0.
* Mon Mar 02 2009 - Brian.Cameron@sun.com
- Bump to 2.0.9.
* Tue Jan 06 2009 - brian.cameron@sun.com
- Bump to 2.0.7.
* Mon Nov 24 2008 - brian.cameron@sun.com
- initial version 2.0.4.

