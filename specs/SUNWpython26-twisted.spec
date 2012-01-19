#
# spec file for package SUNWpython-twisted
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%define pythonver 2.6
%use pt = python-twisted.spec

Name:                    SUNWpython26-twisted
IPS_package_name:        library/python-2/python-twisted-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 %{pt.summary}
URL:                     %{pt.url}
Version:                 %{pt.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWpython-twisted.copyright
License:                 MIT
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:                SUNWPython26
Requires:                library/python-2/python-zope-interface-26
BuildRequires:           SUNWPython26-devel
BuildRequires:           SUNWpython26-zope-interface
BuildRequires:           SUNWpython26-setuptools

%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
%pt.prep -d %{name}-%{version}

%build
%pt.build -d %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
%pt.install -d %{name}-%{version}

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_basedir}/demo/twisted-python%{pythonver}
%{_basedir}/demo/twisted-python%{pythonver}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/Twisted-%{version}-py%{pythonver}.egg-info
%{_libdir}/python%{pythonver}/vendor-packages/twisted
%doc -d Twisted-%{version} README twisted/topfiles/README twisted/conch/topfiles/README
%doc -d Twisted-%{version} twisted/mail/topfiles/README twisted/names/topfiles/README
%doc -d Twisted-%{version} twisted/news/topfiles/README twisted/pair/topfiles/README
%doc -d Twisted-%{version} twisted/python/zsh/README twisted/runner/topfiles/README
%doc -d Twisted-%{version} twisted/web/topfiles/README twisted/words/topfiles/README
%doc -d Twisted-%{version} doc/conch/benchmarks/README doc/core/examples/threadedselect/README
%doc -d Twisted-%{version} twisted/topfiles/CREDITS
%doc(bzip2) -d Twisted-%{version} LICENSE twisted/copyright.py NEWS
%doc(bzip2) -d Twisted-%{version} twisted/topfiles/NEWS twisted/conch/topfiles/NEWS
%doc(bzip2) -d Twisted-%{version} twisted/lore/topfiles/NEWS twisted/mail/topfiles/NEWS
%doc(bzip2) -d Twisted-%{version} twisted/names/topfiles/NEWS twisted/news/topfiles/NEWS
%doc(bzip2) -d Twisted-%{version} twisted/pair/topfiles/NEWS
%doc(bzip2) -d Twisted-%{version} twisted/runner/topfiles/NEWS twisted/web/topfiles/NEWS
%doc(bzip2) -d Twisted-%{version} twisted/words/topfiles/NEWS
%doc(bzip2) -d Twisted-%{version} twisted/topfiles/ChangeLog.Old
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Thu Oct 27 2009 - yuntong.jin@sun.com
- Change the owner to jouby
* Thu Feb 12 2009 - brian.cameron@sun.com
- created 2.6 version based on SUNWpython-twisted.spec.
* Tue Dec 02 2008 - brian.cameron@sun.com
- Add missing build dependency SUNWpython-setuptools
* Wed Jul 23 2008 - brian.cameron@sun.com
- Bump to 8.1.
* Tue Feb 19 2008 - darren.kenny@sun.com
- Move demo scripts from /usr/bin to /usr/demo/twisted
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version


