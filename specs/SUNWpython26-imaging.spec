#
# spec file for package SUNWpython-imaging
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan
#

%include Solaris.inc

%define pythonver 2.6
%use pil = python-imaging.spec

Name:                    SUNWpython26-imaging
License:		 Historical Permission Notice and Disclaimer
IPS_package_name:        library/python-2/python-imaging-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 %{pil.summary}
URL:                     %{pil.url}
Version:                 %{pil.version}
Release:                 1
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWpython-imaging.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
BuildRequires:           SUNWPython26-devel
BuildRequires:           SUNWzlib
BuildRequires:           SUNWjpg-devel
BuildRequires:           SUNWpng-devel
BuildRequires:           SUNWfreetype2
BuildRequires:           SUNWpython26-setuptools
BuildRequires:           SUNWxwinc
Requires:                SUNWzlibr
Requires:                SUNWfreetype2
Requires:                SUNWPython26
BuildRequires:           SUNWjpg

%include default-depend.inc
%include desktop-incorporation.inc

%description
The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
%pil.prep -d %{name}-%{version}

%build
%pil.build -d %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%pil.install -d %{name}-%{version}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/PIL
%{_libdir}/python%{pythonver}/vendor-packages/PIL.pth
%doc -d Imaging-%{version} Sane/README
%doc(bzip2) -d Imaging-%{version} CHANGES README Sane/CHANGES Scripts/README
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Mon Nov 16 2009 - li.yuan@sun.com
- Change owner to liyuan.
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWpython-imaging.spec
* Tue Sep 16 2008 - matt.keenn@sun.com
- Update copyright
* Wed May 14 2008 - darren.kenny@sun.com
- Add SUWNjpg dependency.
* Fri Feb 15 2008 - dermot.mccluskey@sun.com
- remove *.pyo
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version



