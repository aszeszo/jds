#
# spec file for package SUNWspeex
#
# includes module(s): speex 
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%define OSR 4201:1.1.10

%ifarch amd64 sparcv9
%include arch64.inc
%use speex_64 = speex.spec
%endif

%include base.inc
%use speex = speex.spec

Name:                    SUNWspeex
IPS_package_name:        codec/speex
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 Open Source speech codec
Version:                 %{speex.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{speex.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Autoreqprov:             on
                                                                                
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: developer/gnome/gettext
BuildRequires: codec/ogg-vorbis
Requires: codec/ogg-vorbis
Requires: system/library/math

%package devel
Summary:      %{summary} - development files
SUNW_BaseDir: %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%speex_64.prep -d %name-%version/%_arch64
%endif

%speex.prep -d %name-%version

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export echo="/usr/bin/echo"
%ifarch amd64 sparcv9
export PKG_CONFIG_LIBDIR=%{_pkg_config_path64}
%speex_64.build -d %name-%version/%_arch64
%endif

export PKG_CONFIG_LIBDIR=%{_pkg_config_path}
%speex.build -d %name-%version
                                    
%install
export echo="/usr/bin/echo"
%ifarch amd64 sparcv9
%speex_64.install -d %name-%version/%_arch64
%endif

%speex.install -d %name-%version

cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man3/*.3
                                                                                
%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libspeex*.so*
%dir %attr (0755, root, sys) %{_datadir}
%doc -d speex-%{speex.tarball_version} AUTHORS README
%doc(bzip2) -d speex-%{speex.tarball_version} COPYING NEWS
%doc(bzip2) -d speex-%{speex.tarball_version} ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libspeex*.so*
%endif
 
%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/speex
%{_datadir}/doc/speex/*
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*.pc
%endif

%files
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%changelog
* Thu Sep 10 2009 - ke.wang@sun.com
- Add 64-bit support.
* Fri Sep 12 2008 - brian.cameron@sun.com
- Add new copyright files.
* Mon Mar 31 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Thu May 04 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Sep 13 2005 - brian.cameron@sun.com
- Now use speex version number.
* Wed Jul 27 2005 - balamurali.viswanathan@wipro.com
- Add dependency of SUNWogg-vorbis
* Tue Jul 26 2005 - balamurali.viswanathan@wipro.com
- Initial spec-file created


