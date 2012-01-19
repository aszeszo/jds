#
# spec file for package SUNWgst-python
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%define pythonver 2.6
%use gstp = gst-python.spec

Name:                    SUNWgst-python26
IPS_package_name:        library/python-2/python-gst-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 Python %{pythonver} bindings for the GStreamer streaming media framework
URL:                     %{gstp.url}
Version:                 %{gstp.version}
#owner:yippi date:2009-06-02 type:bug bugzilla:584633 bugster:6843650
Patch1:                  gst-python-01-python26.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWgst-python.copyright
License:                 %{gstp.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                SUNWglib2
Requires:                SUNWPython26
Requires:                SUNWpygobject26
Requires:                SUNWgnome-media
BuildRequires:           SUNWglib2-devel
BuildRequires:           SUNWpygobject26-devel
BuildRequires:           SUNWgnome-media-devel
BuildRequires:           SUNWpython26-setuptools

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%gstp.prep -d %name-%version
cd %{name}-%{gstp.version}
cd gst-python-%version
%patch1 -p1

%build
%gstp.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gstp.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/gstreamer-0.10/libgstpython.so
%{_libdir}/python%{pythonver}/vendor-packages/gst-0.10/*
%{_libdir}/python%{pythonver}/vendor-packages/pygst.pth
%{_libdir}/python%{pythonver}/vendor-packages/pygst.py
%{_libdir}/python%{pythonver}/vendor-packages/*.so
%doc -d gst-python-%{gstp.version} AUTHORS
%doc -d gst-python-%{gstp.version} README
%doc(bzip2) -d gst-python-%{gstp.version} COPYING
%doc(bzip2) -d gst-python-%{gstp.version} ChangeLog
%doc(bzip2) -d gst-python-%{gstp.version} NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, sys) %{_datadir}

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gst-python

%changelog
* Wed Nov 04 2009 - brian.cameron@sun.com
- Fix the way the patch is applied so it does not fail when the module is
  bumped.
* Tue Jun 02 2009 - brian.cameron@sun.com
- Add patch gst-python-01-python26.diff so that when building the Python 2.6
  bindings, all files use Python 2.6 instead of "#!/usr/bin/env python".
  Otherwise this package depends on the gst-python 2.4 bindings.
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWgst-python.spec.
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



