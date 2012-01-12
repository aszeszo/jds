#
# spec file for package SUNWmysql-python
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan
#

%include Solaris.inc

%define OSR 8096:1.2.2

Name:                    SUNWmysql-python26
IPS_package_name:        library/python-2/python-mysql-26
Meta(info.classification): %{classification_prefix}:Development/Databases
Summary:                 A MySQL database adapter for the Python programming language
License:                 Python/Zope/GPL
URL:                     http://sourceforge.net/projects/mysql-python
Version:                 1.2.2
Source:                  %{sf_download}/mysql-python/MySQL-python-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires:           SUNWPython26-devel
BuildRequires:           SUNWpython26-setuptools
Requires:                SUNWPython26
Requires:                SUNWmysql51u
Requires:                SUNWmysql51lib

%define python_version  2.6

%prep
%setup -q -n MySQL-python-%{version}

%build
# correct mysql_config path
export PATH=${PATH}:/usr/mysql/bin
export LDFLAGS="-L/usr/mysql/lib/mysql -R/usr/mysql/lib/mysql"
python%{python_version} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
# correct mysql_config path
export PATH=${PATH}:/usr/mysql/bin
python%{python_version} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix} --no-compile

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{python_version}/vendor-packages/
%doc PKG-INFO
%doc(bzip2) GPL ChangeLog HISTORY README
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Mon Nov 16 2009 - li.yuan@sun.com
- Change owner to liyuan.
* Mon Oct 05 2009 - darren.kenny@sun.com
- Create python2.6 bindings based on 2.4 version.
* Tue June 02 2009 - dave.lin@sun.com
- Add 'Requires: SUNWmysql51lib' to fix CR6846734.
* Tue Apr 21 2009 - dave.lin@sun.com
- Move the dependency from SUNWmysql5u to SUNWmysql51u
* Tue Sep 16 2008 - matt.keenn@sun.com
- Update copyright
* Tue Feb 19 2008 - darren.kenny@sun.com
- Rename spec-file to match ARC-ed package name (and community name) of
  mysql-python. Also ensure that it's looking at the /usr/mysql SUNWmysql5u
  packages rather than the sfw version.
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version


