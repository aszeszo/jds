#
# spec file for package SUNWpython-twisted-web2
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%define pythonver 2.6
%use ptw = python-twisted-web2.spec

Name:                    SUNWpython26-twisted-web2
IPS_package_name:        library/python-2/python-twisted-web2-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 %{ptw.summary}
URL:                     %{ptw.url}
Version:                 %{ptw.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWpython-twisted-web2.copyright
License:                 MIT
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
BuildRequires:           library/python-2/python-twisted-26
BuildRequires:           SUNWpython26-setuptools
Requires:                SUNWPython26
Requires:                library/python-2/python-twisted-26

%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
%ptw.prep -d %{name}-%{version}

%build
%ptw.build -d %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%ptw.install -d %{name}-%{version}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/*
%doc -d TwistedWeb2-%{version} README
%doc(bzip2) -d TwistedWeb2-%{version} LICENSE NEWS
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Thu Oct 27 2009 - yuntong.jin@sun.com
- Change the owner to jouby
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWpython-twisted-web2.spec.
* Tue Sep 30 2008 - brian.cameron@sun.com
- Bump to 8.1.0.
* Fri Jul 25 2008 - brian.cameron@sun.com
- Initial version.


