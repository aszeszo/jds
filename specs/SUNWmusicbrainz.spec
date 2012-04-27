#
# spec file for package SUNWmusicbrainz
#
# includes module(s): libmusicbrainz
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc
%use musicbrainz = libmusicbrainz3.spec

Name:                    SUNWmusicbrainz
IPS_package_name:        library/musicbrainz/libmusicbrainz
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 Library for accessing MusicBrainz servers
Version:                 %{musicbrainz.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{musicbrainz.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: library/neon
BuildRequires: developer/build/cmake
BuildRequires: SUNWlibdiscid-devel

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version
%musicbrainz.prep -d %name-%version

%build
%musicbrainz.build -d %name-%version

%install
%musicbrainz.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libmusicbrainz*.so*
%doc -d libmusicbrainz-%{musicbrainz.version} AUTHORS README
#%doc -d libmusicbrainz-%{musicbrainz.version} perl/Bundle/README
#%doc -d libmusicbrainz-%{musicbrainz.version} perl/Client/README
#%doc -d libmusicbrainz-%{musicbrainz.version} perl/TRM/README
#%doc -d libmusicbrainz-%{musicbrainz.version} perl/Queries/README
#%doc -d libmusicbrainz-%{musicbrainz.version} python/README
%doc(bzip2) -d libmusicbrainz-%{musicbrainz.version} COPYING
#%doc(bzip2) -d libmusicbrainz-%{musicbrainz.version} ChangeLog 
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/musicbrainz3

%changelog
* Wed Nov 18 2009 - ke.wang@sun.com
- Bump to 3.0.2
* Mon Sep 15 2008 - brian.cameron@sun.com
- Add new copyright files.
* Mon Mar 31 2008 - brian.cameron@sun.com
- Add SUNW_Copyright
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Wed Jan 04 2006 - damien.carbery@sun.com
- Set LDFLAGS/CFLAGS to find expat files under /usr/sfw.
* Tue Sep 27 2005 - brian.cameron@sun.com
- Fix libmusicbrainz so it links against the Forte STL library
  since it was building with unresolved symbols before.
* Mon Jul 25 2005 - balamurali.viswanathan@wipro.com
- Create a separate devel package
* Fri Jul 08 2005 - balamurali.viswanathan@wipro.com
- Modify patch not to include -lstdc++
* Thu Jul 07 2005 - balamurali.viswanathan@wipro.com
- Initial spec-file created


