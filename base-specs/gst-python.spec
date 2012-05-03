#
# base spec file for package gst-python
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%{?!pythonver:%define pythonver 2.6}

%define OSR 8324:0.10.10

Name:                    gst-python
License:                 LGPL v2.1
Group:                   Libraries/Multimedia
Version:                 0.10.22
Distribution:            Java Desktop System
Vendor:                  freedesktop.org
Summary:                 Python bindings for the GStreamer streaming media framework
Source:                  http://gstreamer.freedesktop.org/src/%{name}/%{name}-%{version}.tar.bz2
URL:                     http://gstreamer.freedesktop.org/src/gst-python/
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                python
Requires:                gstreamer

%prep
%setup -q -n %name-%version

%build
export PYTHON=/usr/bin/python%{pythonver}
export PKG_CONFIG_PATH=/usr/lib/python%{pythonver}/pkgconfig
libtoolize --force
aclocal -I ./common/m4 $ACLOCAL_FLAGS
autoconf
automake
./configure --prefix=%{_prefix}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.pyo" -exec rm -f {} ';'

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed May 02 2012 - Brian Cameron  <brian.cameron@oracle.com>
- Bump to 0.10.22.
* Mon Jan 24 2011 - Brian Cameron  <brian.cameron@oracle.com>
- Bump to 0.10.21.
* Fri Jan 14 2011 - Brian Cameron  <brian.cameron@oracle.com>
- Bump to 0.10.20.
* Thu Jul 15 2010 - Brian Cameron  <brian.cameron@oracle.com>
- Bump to 0.10.19.
* Thu Feb 11 2010 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.18.
* Wed Nov 04 2009 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.17.
* Tue Oct 13 2009 - Brian Cameron  <brian.cameron@sun.com>
- Do not install .pyo files.
* Fri Aug 14 2009 - brian.cameron@sun.com
- Bump to 0.10.16.
* Mon May 11 2009 - brian.cameron@sun.com
- Bump to 0.10.15.
* Tue Mar 03 2009 - brian.cameron@sun.com
- Use find command to remove .la files.
* Mon Jan 19 2009 - brian.cameron@sun.com
- Bump to 0.10.14.
* Mon Nov 24 2008 - laca@sun.com
- split from SUNWgst-python.spec
* Mon Oct 13 2008 - brian.cameron@sun.com
- Bump to 0.10.13.  Remove upstream patch gst-python-01-pipelinetester.diff.
* Fri Sep 12 2008 - matt.keenn@sun.com
- Update copyright
* Wed Jul 16 2008 - damien.carbery@sun.com
- Update %files for newly delivered library.
* Thu Jun 19 2008 - brian.cameron@sun.com
- Bump to 0.10.12.
* Thu Mar 20 2008 - brian.cameron@sun.com
- Bump to 0.10.11.
* Tue Mar 18 2008 - damien.carbery@sun.com
- Add Build/Requires for SUNWgnome-python-libs and SUNWgnome-media.
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version

