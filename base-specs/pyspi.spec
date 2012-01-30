#
# spec file for package pyspi
#
# includes module(s): pyspi
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%{!?pythonver:%define pythonver 2.6}

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         pyspi
License:      LGPL
Group:        Development/Languages/Python
Version:      0.6.1
Release:      2
Distribution: Java Desktop System
Vendor:       Sun Microsystems, Inc.
Summary:      Python bindings for CSPI
Source:       http://people.redhat.com/zcerza/dogtail/releases/%{name}-%{version}.tar.gz
URL:          http://gnome.org/projects/pyspi
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/doc
Autoreqprov:  off
Prereq:       /sbin/ldconfig
Requires:      python >= %{pythonver}
Requires:      at-spi
Requires:      Pyrex
BuildRequires: python-devel >= %{pythonver}
BuildRequires: at-spi-devel

%description
Python bindings for CSPI

%prep
%setup -q

%install
python%{pythonver} setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_libdir}/python?.?/vendor-packages

%changelog
* Wed Apr 15 2009 - dave.lin@sun.com
- Remove %build section which would be covered in %install section.
* Wed Mar 25 2009 - li.yuan@sun.com
- Move pyspi from SUNWgnome-python-libs to SUNWgnome-a11y-libs. Move files
  from site-packages to vendor-packages.
* Mon Nov 24 2008 - laca@sun.com
- use %{pythonver} macro to select with version of Python to build which
* Mon Nov 17 2007 - jedy.wang@sun.com
- Fix installation directory bug.
* Wed Aug 20 2008 - brian.cameron@sun.com
- Remove patch pyspi-01-solaris.diff since it is no longer needed now that the
  x11.pc file is in our builds.
* Mon Aug 11 2008 - damien.carbery@sun.com
- Remove the site-packages to vendor-packages as it is done in the top level
  spec file now.
* Wed Nov 07 2007 - damien.carbery@sun.com
- Update fix for 6615442 - vendor-packages dir already existed so the mv
  created a site-packages dir under vendor-packages. mv command corrected.
* Wed Oct 10 2007 - damien.carbery@sun.com
- Move files from site-packages to vendor-packages. Fixes 6615442.
* Thu Nov 09 2006 - damien.carbery@sun.com
- Bump to 0.6.1.
* Sat Oct 07 2006 - brian.cameron@sun.com
- Bump to 0.6.0.  Add patch to allow building on Solaris.
* Fri Aug 25 2006 - damien.carbery@sun.com
- Bump to 0.5.5.
* Thu May 04 2006 - laca@sun.com
- Bump to 0.5.4
* Tue Jan 17 2006 - damien.carbery@sun.com
- Bump to 0.5.3.
* Thu Oct 27 2005 - laca@sun.com
- move from site-packages to vendor-packages
* Mon Oct 24 2005 - damien.carbery@sun.com
- Include .pyc files. A Google search indicates that most people include them.
* Thu Oct 20 2005 - damien.carbery@sun.com
- Remove 'make' call from %install. Already in '%build'.
- Delete .pyc files so they are not included in the package.
* Wed Oct 19 2005 - damien.carbery@sun.com
- Initial version.
