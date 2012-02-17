#
# spec file for package SUNWlibgnome-keyring
#
# includes module(s): libgnome-keyring
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libgnomekeyring64 = libgnome-keyring.spec
%endif

%include base.inc
%use libgnomekeyring = libgnome-keyring.spec

Name:                    SUNWlibgnome-keyring
License: LGPL v2
IPS_package_name:        library/gnome/gnome-keyring 
Meta(info.classification): %{classification_prefix}:System/Security
Summary:                 GNOME keyring libraries
Version:                 %{libgnomekeyring.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWlibgcrypt
Requires: SUNWglib2
Requires: SUNWgnome-keyring
BuildRequires: SUNWlibgcrypt-devel
BuildRequires: SUNWglib2

%package devel		
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libgnomekeyring.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%libgnomekeyring.prep -d %name-%version/%{base_arch}
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"
export RPM_OPT_FLAGS="$CFLAGS"

%ifarch amd64 sparcv9
%libgnomekeyring64.build -d %name-%version/%_arch64
%endif

%libgnomekeyring.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libgnomekeyring64.install -d %name-%version/%_arch64
%endif

%libgnomekeyring.install -d %name-%version/%{base_arch}

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache


%files
%doc(bzip2) %{base_arch}/libgnome-keyring-%{libgnomekeyring.version}/COPYING
%doc(bzip2) %{base_arch}/libgnome-keyring-%{libgnomekeyring.version}/NEWS
%doc(bzip2) %{base_arch}/libgnome-keyring-%{libgnomekeyring.version}/ChangeLog
%doc %{base_arch}/libgnome-keyring-%{libgnomekeyring.version}/AUTHORS
%doc %{base_arch}/libgnome-keyring-%{libgnomekeyring.version}/README
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Fri Feb 17 2012 - brian.cameron@oracle.com
- Now build 64-bit.
* Thu May 27 2010 - jeff.cai@sun.com
- Add dependency on SUNWgnome-keyring
* Wed Feb 24 2010 - jeff.cai@sun.com
- Not ship gtk-doc files in the base package since they
  already be shipped in the develpment package.
* Wed Jan 27 2010 - christian.kelly@sun.com
- Fix %files.
* Tue Jan 26 2010 - jeff.cai@sun.com
- Split SUNWgnome-keyring from SUNWgnome-libs


