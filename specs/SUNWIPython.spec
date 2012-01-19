#
# spec file for package SUNWIPython
#
# includes module(s): ipython
#
# Copyright (c) 2005 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan
#

%include Solaris.inc
%use ipython = ipython.spec

Name:                    SUNWIPython
License:		 BSD
IPS_package_name:        library/python-2/ipython-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 Enhanced interactive Python shell
Version:                 %{ipython.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

Requires: SUNWPython26
BuildRequires: SUNWPython26-devel
BuildRequires: SUNWpython26-setuptools

%prep
rm -rf %name-%version
mkdir %name-%version
%ipython.prep -d %name-%version

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export MSGFMT="/usr/bin/msgfmt"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%ipython.build -d %name-%version

%install
%ipython.install -d %name-%version

# install man page
find $RPM_BUILD_ROOT%{_mandir} -name "*irunner*"|xargs rm
find $RPM_BUILD_ROOT%{_mandir} -name "*.gz"|xargs gzip -d

# Delete irunner because it depends on pexpect which is not in Solaris.
rm -rf $RPM_BUILD_ROOT%{_bindir}/irunner
rm -rf $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages/IPython/irunner.*

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr(0755, root, sys) %{_datadir}
%doc -d ipython-%{ipython.version} IPython/DPyGetOpt.py
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%dir %attr (0755, root, other) %{_docdir}
%dir %attr (0755, root, other) %{_docdir}/ipython
%{_docdir}/ipython/*

%changelog
* Wed Oct 14 2009 - li.yuan@sun.com
- Update dependencies.
* Wed Oct 14 2009 - li.yuan@sun.com
- Use Python 2.6.
* Mon Sep 28 2009 - ke.wang@sun.com
- Use the manpages shipped with community package to replace the ones written by jds
* Tue Jan 06 2009 - christian.kelly@sun.com 
- Took out doc/COPYING and doc/Changelog of %doc section.
* Thu Sep 18 2008 - li.yuan@sun.com
- Added %doc to %files for copyright.
* Mon Mar 31 2008 - li.yuan@sun.com
- Add copyright file
* Mon Sep 03 2007 - li.yuan@sun.com
- Remove irunner for we do not use it.
* Sun Sep 02 2007 - li.yuan@sun.com
- Initial version.


