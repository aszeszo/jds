#
# spec file for package SUNWpyyaml
#
# includes module(s): pyyaml
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#

%include Solaris.inc
%define pythonver 2.6
%use pyyaml = pyyaml.spec

Name:                    SUNWpyyaml26
IPS_package_name:        library/python-2/pyyaml-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 A YAML parser and emitter for the Python language
URL:                     http://pyyaml.org/
Version:                 %{pyyaml.version}
License:		 MIT
Distribution:		 Java Desktop System
SUNW_BaseDir:		 %{_basedir}
SUNW_Copyright:		 SUNWpyyaml.copyright
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                runtime/python-26
BuildRequires:           runtime/python-26
BuildRequires:           library/python-2/setuptools-26

%prep
rm -rf %name-%version
mkdir -p %name-%version
%pyyaml.prep -d %name-%version

%build
%pyyaml.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%pyyaml.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/PyYAML-%{pyyaml.tarball_version}-py%{pythonver}.egg-info
%{_libdir}/python%{pythonver}/vendor-packages/yaml/*
%doc -d PyYAML-%{pyyaml.tarball_version} LICENSE README
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Fri Mar 06 2009 - li.yuan@sun.com
- Change owner name to liyuan.
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWpyyaml.spec.
* Fri Jan 09 2009 - jim.li@sun.com
- Bump to 3.08
* Mon Nov 21 2008 - jim.li@sun.com
- add copyright
- add license tag
- rename SFEpyyaml to SUNWpyyaml
* Fri Oct 31 2008 - brian.cameron@sun.com
- Bump to 3.06.
* Sat Apr 12 2008 - brian.cameron@sun.com
- created with 3.05.


