#
# spec file for package SUNWdbus-python26
#
# includes module(s): dbus-python
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: bugzilla.freedesktop.org
#
%include Solaris.inc

%define pythonver 2.6

%include base.inc
%use dbus_python = dbus-python.spec

Name:                    SUNWdbus-python26
IPS_package_name:        library/python-2/python-dbus-26
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                 D-Bus Python %{pythonver} bindings
Version:                 %{dbus_python.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWdbus-python24.copyright
License:                 %{dbus_python.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:	SUNWdbus
Requires:	SUNWlxml
Requires:       SUNWlexpt
Requires:       SUNWPython26-extra
Requires:       SUNWdbus-glib
BuildRequires:	SUNWdbus-devel
BuildRequires:	SUNWlxml
BuildRequires:  SUNWPython26-extra
BuildRequires:  SUNWpython26-setuptools
BuildRequires:  SUNWdbus-glib-devel
BuildRequires:  consolidation/desktop/gnome-incorporation

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version
%dbus_python.prep -d %name-%version

%build
PKG_CONFIG_DISABLE_UNINSTALLED=
unset PKG_CONFIG_DISABLE_UNINSTALLED
export PYTHON=/usr/bin/python%{pythonver}
%dbus_python.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%dbus_python.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages
%dir %attr (0755, root, sys) %{_datadir}
%doc -d dbus-python-%{dbus_python.version} AUTHORS
%doc -d dbus-python-%{dbus_python.version} README
%doc(bzip2) -d dbus-python-%{dbus_python.version} COPYING
%doc(bzip2) -d dbus-python-%{dbus_python.version} ChangeLog
%doc(bzip2) -d dbus-python-%{dbus_python.version} NEWS
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/dbus-python
%{_datadir}/doc/dbus-python/*

%changelog
* Tue Mar 10 2009 - brian.cameron@sun.com
- Cleanup based on code review.
* Thu Mar 05 2009 - brian.cameron@sun.com
- Split from SUNWdbus-bindings.spec.  Remove 64 bit support as it is not
  needed for the python bindings.
* Wed Mar 04 2009 - dave.lin@sun.com
- Add /usr/share/man/man1 in %files
* Sun Sep 14 2008 - brian.cameron@sun.com
- Add new copyright files.
* Thu Mar 27 2008 - brian.cameron@sun.com
- Add SUNW_Copyright
* Tue Nov 20 2007 - brian.cameron@sun.com
- Add libdbus-glib-1.3 manpage.
* Fri Sep 28 2007 - laca@sun.com
- convert to new style multi-ISA build
- delete SUNWxwrtl dep
* Sat Feb 25 2007 - dougs@truemail.co.th
- updated to include 64-bit build RFE: #6480511
* Fri Jan 26 2007 - damien.carbery@sun.com
- Set PKG_CONFIG vars in %build because dbus-python use autofoo/configure/make
  process rather than setup.py.
* Thu Jan 25 2007 - damien.carbery@sun.com
- Add %{_datadir}/doc to devel pkg, because of new dbus-python tarball.
* Thu Dec 21 2006 - brian.cameron@sun.com
- Remove references to SUNWdbus-bindings-root since we do not
  build this package.
* Thu Sep 21 2006 - brian.cameron@sun.com
- Created.



