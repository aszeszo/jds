#
# spec file for package SUNWpython26-notify
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jedy
# includes module(s): notify-python
#

%include Solaris.inc

%define pythonver 2.6
%use notify_python = notify-python.spec

Name:                    SUNWpython26-notify
IPS_package_name:        library/python-2/python-notify-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 Python %{pythonver} bindings for libnotify
URL:                     http://www.galago-project.org/
Version:                 %{notify_python.version}
License:                 LGPL v2.1
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          SUNWpython-notify.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                library/desktop/gtk2
Requires:                runtime/python-26
Requires:                gnome/gnome-panel
Requires:                library/python-2/pygtk2-26
BuildRequires:           library/desktop/gtk2
BuildRequires:           runtime/python-26
BuildRequires:           gnome/gnome-panel
BuildRequires:           library/python-2/pygtk2-26
BuildRequires:           library/python-2/setuptools-26
BuildRequires:           developer/macro/gnu-m4

%package devel
Summary:                %{summary} - development files
SUNW_BaseDir:           %{_basedir}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%notify_python.prep -d %name-%version

%build
%notify_python.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%notify_python.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d %{notify_python.name}-%{notify_python.version} AUTHORS
%doc(bzip2) -d %{notify_python.name}-%{notify_python.version} ChangeLog COPYING
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/gtk-2.0/pynotify
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/pygtk

%files devel
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Thu Feb 12 2009 - brian.cameron@sunc.om
- created 2.6 version based on SUNWpython-notify.spec.
* Wed Onv 05 2008 - jedy.wang@sun.com
- Update license.
* Tue Sep 16 2008 - jedy.wang@sun.com
- Add copyright files.
* Thu Jul 17 2008 - dave.lin@sun.com
- Add default file attribute for devel pkg to fix the incorrect attribute issue
* Mon Jun 30 2008 - jedy.wang@sun.com
- Rename to SUNWpython-notify
* Wed Jun 25 2008 - jedy.wang@sun.com
- Moved from spec-files-extra
* Sat Apr 12 2008 - brian.cameron@sun.com
- created



