#
# spec file for package SUNWpython26-notify
#
# Copyright 2009 Sun Microsystems, Inc.
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
Requires:                SUNWgtk2
Requires:                SUNWPython26
Requires:                SUNWgnome-panel
Requires:                SUNWpygtk2-26
BuildRequires:           SUNWgtk2-devel
BuildRequires:           SUNWPython26-devel
BuildRequires:           SUNWgnome-panel-devel
BuildRequires:           SUNWpygtk2-26-devel
BuildRequires:           SUNWpython26-setuptools
BuildRequires:           SUNWgm4

%package devel
Summary:                %{summary} - development files
SUNW_BaseDir:           %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

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



