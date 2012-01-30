#
# spec file for package numpy
#
# includes module(s): numpy
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
# bugdb: http://projects.scipy.org/scipy/numpy/report
#
%{!?pythonver:%define pythonver 2.6}

%define OSR 8466:1.0.4

Name:         numpy
License:      BSD
Group:        Development/Languages/Python
Version:      1.4.1
Release:      1
Distribution: Java Desktop System
Vendor:       SciPy
Summary:      Python XML module
Source:       %{sf_download}/numpy/numpy-%{version}.tar.gz
URL:          http://numpy.scipy.org/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/doc
Autoreqprov:  off
Prereq:       /sbin/ldconfig
Requires:     python >= %{pythonver}
BuildRequires: python-devel >= %{pythonver}

%description
Numerical processing extensions to the python programming language.

%prep
%setup -q -n numpy-%{version}

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
%defattr(-, root, root)
%{_bindir}
%{_libdir}/python?.?/vendor-packages

%changelog
* Mon May 03 2010 - brian.cameron@oracle.com
- Bump to 1.4.1.
* Thu Jan 28 2010 - brian.cameron@sun.com
- Bump to 1.4.0.
* Mon Nov 02 2009 - brian.cameron@sun.com
- Add patch numpy-01-f77compat.diff to fix doo bug #11709.  This fix allows
  SciPy to be compiled with NumPy.
* Tue Apr 14 2009 - brian.cameron@sun.com
- Bump to 1.3.0.
* Tue Feb 03 2009 - brian.cameron@sun.com
- Bump to 1.2.1.
* Mon Nov 24 2008 - laca@sun.com
- use %{pythonver} macro to select which version of Python to build with
* Mon Nov 17 2007 - jedy.wang@sun.com
- Fix installation directory bug.
* Thu Oct 25 2007 - brian.cameron@sun.com
- Initial version.  Based on the spec-files-extra SFEpython-numpy.spec
  file written by Ananth Shrinivas <ananth@sun.com> on Sep 02 2007.

