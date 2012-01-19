#
# spec file for package notify-python
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jedy
#

%{?!pythonver:%define pythonver 2.6}

%define OSR 9207:0.x

Name:                    notify-python
Summary:                 Python bindings for libnotify
Vendor:                  Galago
URL:                     http://www.galago-project.org/
Version:                 0.1.1
License:                 LGPL v2.1
Source:                  http://www.galago-project.org/files/releases/source/notify-python/notify-python-%{version}.tar.bz2
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n notify-python-%version

%build
export PYTHON=/usr/bin/python%{pythonver}
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

autoheader
aclocal $ACLOCAL_FLAGS
autoconf
automake -a -c -f
./configure --prefix=%{_prefix}

# Refer to http://trac.galago-project.org/ticket/121 for the reason to remove
# the file
rm src/pynotify.c
make

%install
rm -rf $RPM_BUILD_ROOT
# Do a make clean first as the tarball contains out dated generated code
# see last comment in http://trac.galago-project.org/ticket/121
make clean
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.pyo" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/gtk-2.0/pynotify
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/pygtk
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Mon Feb 16 2009 - jedy.wang@sun.com
- Remove src/pynotify.c before building.
* Thu Feb 12 2009 - brian.cameron@sun.com
- Split from SUNWpython-notify.spec file.
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
