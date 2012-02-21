#
# spec file for package SUNWpython26-simplejson
#
# includes module(s): simplejson
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%define pythonver 2.6
%define src_url         http://pypi.python.org/packages/source/s/simplejson
%define src_name        simplejson

%use simplejson = simplejson.spec

Name:                   SUNWpython26-simplejson
IPS_package_name:       library/python-2/simplejson-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                JSON (Java Script Object Notation) encoder/decoder for Python %{pythonver}
License:                MIT
URL:                    %{simplejson.url}
Version:                %{simplejson.version}
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:         SUNWpython-simplejson.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:               runtime/python-26
BuildRequires:          runtime/python-26
BuildRequires:          library/python-2/setuptools-26

%prep
rm -rf %name-%version
mkdir -p %name-%version
%simplejson.prep -d %name-%version

%build
export PYTHON="/usr/bin/python%{pythonver}"
export CFLAGS="%optflags -I/usr/xpg4/include -I%{_includedir} -I/usr/include/python%{pythonver}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export PYCC_CC="$CC"
export PYCC_CXX="$CXX"
%simplejson.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%simplejson.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages
%doc(bzip2) -d simplejson-%{simplejson.version} LICENSE.txt
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWpython-simplejson.spec.
* Mon Nov 24 2008 - brian.cameron@sun.com
- Initial version 2.0.4.


