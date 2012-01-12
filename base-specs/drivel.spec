#
# spec file for package drivel
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner hakwlu 
#

%define OSR 9332:2.0.3

Name:           drivel
License:        GPL v2
Group:          Development/Utilities
Version:        3.0.2
Release:        1
Distribution:   Java Desktop System
Vendor:         Sourceforge
URL:            http://dropline.net/past-projects/drivel-blog-editor/
Summary:        Drivel is a GNOME client for editing blog
Source:         http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

BuildRequires: gtk2-devel

%description
Drivel - Blog Editor

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} CFLAGS="-D__NetBSD__ -D__EXTENSIONS__"

make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make -i install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README COPYING.LIB
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/bonobo/servers/GNOME_RemoteDesktop.server

%changelog
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 3.0.2.
* Sat Jul 03 2010 - brian.lu@sun.com
- Bump to 3.0.1.
  Change the owner to hawklu
* Sat Aug 15 2009 - christian.kelly@sun.com
- Bump to 2.0.4.
* Wed Feb 11 2009 - david.zhang@sun.com
- Initial version.
