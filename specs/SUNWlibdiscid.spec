#
# spec file for package SUNWlibdiscid
#
# includes module(s): libdiscid
#
# Copyright (c) 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%include Solaris.inc
%use libdiscid = libdiscid.spec

Name:		SUNWlibdiscid
License: LGPL v2.1, Public Domain
IPS_package_name: library/musicbrainz/libdiscid
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:	Library for creating MusicBrainz DiscIDs
Version:	%{libdiscid.version}
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%include desktop-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version
%libdiscid.prep -d %name-%version

%build
%libdiscid.build -d %name-%version

%install
%libdiscid.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%doc -d libdiscid-%{libdiscid.version} AUTHORS README
%doc(bzip2) -d libdiscid-%{libdiscid.version} COPYING
%doc(bzip2) -d libdiscid-%{libdiscid.version} ChangeLog
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Mon Nov 16 2009 - ke.wang@sun.com
- Initial spec file


