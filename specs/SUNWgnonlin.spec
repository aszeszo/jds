#
# spec file for package SUNWgnonlin
#
# includes module(s): gnonlin
#
# Copyright (c) 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#

%define OSR 11978:0.10.10

%define         majmin          0.10

%include Solaris.inc
Name:                    SUNWgnonlin
IPS_package_name:        library/audio/gstreamer/plugin/gnonlin
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
License:                 LGPL v2
Version:                 0.10.17
Distribution:            Java Desktop System
Summary:                 Non-linear editing elements for GStreamer
Source:                  http://gstreamer.freedesktop.org/src/gnonlin/gnonlin-%{version}.tar.bz2
SUNW_Copyright:		 %{name}.copyright
URL:                     http://gstreamer.freedesktop.org/src/gnonlin/
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir:            %{_basedir}
%include desktop-incorporation.inc
%include default-depend.inc
Requires:                SUNWglib2
Requires:                SUNWgnome-media
BuildRequires:           SUNWglib2-devel
BuildRequires:           SUNWgnome-media-devel

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc

%prep
%setup -q -n gnonlin-%version

%build
./configure --prefix=%{_prefix} --enable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majmin}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majmin}/*.a

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/gstreamer-%{majmin}
%{_libdir}/gstreamer-%{majmin}/libgnl.so
%doc AUTHORS README
%doc(bzip2) COPYING COPYING.LIB ChangeLog common/ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, sys) %{_datadir}

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%changelog
* Mon Jan 24 2011 - Brian Cameron  <brian.cameron@oracle.com>
- Bump to 0.10.17.
* Fri Jan 14 2011 - Brian Cameron  <brian.cameron@oracle.com>
- Bump to 0.10.16.
* Thu Mar 11 2010 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.15.
* Thu Feb 11 2010 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.14.
* Thu Sep 10 2009 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.13.
* Sat Aug 15 2009 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.12.
* Mon Jun 08 2009 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.11.
* Tue May 12 2009 - Brian Cameron  <brian.cameron@sun.com>
- Now install gtk-docs.
* Sun Mar 01 2009 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.10.
* Wed Aug 15 2007 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.9.
* Mon Jul 09 2007 - Brian Cameron  <brian.cameron@sun.com>
- Bump to 0.10.8.
* Fri Feb 09 2007 - irene.huang@sun.com
- Created.
