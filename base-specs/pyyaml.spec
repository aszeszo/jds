#
# spec file for package pyyaml
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#

%{?!pythonver:%define pythonver 2.6}

%define OSR 10185:3.05

Name:		pyyaml
License:	MIT
Vendor:         http://pyyaml.org/
Group:		Development/Libraries
%define         tarball_version 3.09
Version:	3.9
URL:		http://pyyaml.org/
Release:	1
Distribution:	Java Desktop System
Vendor:		Sun Microsystems, Inc.
Summary:	A YAML parser and emitter for the Python languag
Source:		http://pyyaml.org/download/pyyaml/PyYAML-%{tarball_version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{tarball_version}-build
Requires:	python

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that allow
to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%prep
%setup -q -n PyYAML-%tarball_version

%build
python%{pythonver} setup.py build

%install
python%{pythonver} setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/yaml/*

%changelog
* Mon Aug 31 2009 - brian.cameron@sun.com
- Bump to 3.0.9.
* Mon Jul 06 2009 - harry.lu@sun.com
- Change owner to yippi.
* Fri Mar 06 2009 - li.yuan@sun.com
- Change owner to liyuan.
* Fri Jan 09 2009 - jim.li@sun.com
- Bump to 3.08.
* Mon Nov 10 2008 - jim.li@sun.com
- add copyright.
- add license tag.
- rename SFEpyyaml to SUNWpyyaml.
* Fri Oct 31 2008 - brian.cameron@sun.com
- Bump to 3.06.
* Sat Apr 12 2008 - brian.cameron@sun.com
- created with 3.05.
