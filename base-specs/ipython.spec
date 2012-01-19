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
%define pythonver 2.6

%define OSR 6719:0.8.1

Name:                   ipython
Summary:                Enhanced interactive Python shell
Version:                0.10
Release:                1
Vendor:                 SciPy
License:                BSD
Group:                  Development/Libraries
URL:                    http://ipython.scipy.org/
Source:                 http://ipython.scipy.org/dist/%{version}/ipython-%{version}.tar.gz
#owner:wangke date:2009-09-28 type:branding
Patch1:			ipython-01-manpages.diff
#owner:liyuan date:2009-12-03 type:branding
Patch2:			ipython-02-python-version.diff
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:              noarch

%description
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

%prep
%setup
find docs/man -name "*.gz"|xargs gzip -d
%patch1 -p1
%patch2 -p1
find docs/man -name "*.1"|xargs gzip

%build
python%{pythonver} setup.py build
sed s/"\/python"/"\/python%{pythonver}"/g ipython.py > ipython.bak
mv ipython.bak ipython.py
chmod 755 ipython.py

%install
%{__rm} -rf $RPM_BUILD_ROOT
python%{pythonver} setup.py install --root="$RPM_BUILD_ROOT"

# Move to vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Thu Dec 03 2009 - li.yuan@sun.com
- Use python2.6.
* Wed Oct 14 2009 - li.yuan@sun.com
- Use Python 2.6.
* Mon Sep 28 2009 - ke.wang@sun.com
- Add patch ipython-01-manpages.diff
- Use the manpages shipped with community package to replace the ones written by jds
* Tue Aug 25 2009 - christian.kelly@sun.com
- Bump to 0.10.
* Thu Aug 13 2009 - li.yuan@sun.com
- Update vendor information.
* Sun Jul 26 2009 - christian.kelly@sun.com
- Bump to 0.9.1.
* Tue Mar 17 2009 - li.yuan@sun.com
- Downgrade to 0.8.4 because of dependency problem.
* Fri Dec 05 2008 - li.yuan@sun.com
- Bump to 0.9.1.

* Fri Jun 06 2008 - brian.cameron@sun.com
- Bump to 0.8.4.

* Fri Dec 07 2007 - brian.cameron@sun.com
- Bump to 0.8.2.

* Wed Oct 10 2007 - damien.carbery@sun.com
- Move files from site-packages to vendor-packages. Fixes 6615442.

* Mon Sep  2 2007 - li.yuan@sun.com
- Initial version.
