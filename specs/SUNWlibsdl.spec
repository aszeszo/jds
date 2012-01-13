#
# spec file for package SUNWlibsdl
#
# includes module(s): libsdl
#
# Copyright 2007 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner davelam
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use sdl_64 = libsdl.spec
%endif

%include base.inc
%use sdl = libsdl.spec

Name:        SUNWlibsdl
IPS_package_name: library/sdl
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:     %{sdl.summary}
Version:     %{sdl.version}
SUNW_BaseDir:%{_basedir}
SUNW_Copyright:%{name}.copyright
License:      LGPL v2.1
BuildRoot:   %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlibms
Requires: SUNWgnome-audio
BuildRequires: SUNWxwplt
BuildRequires: SUNWxwrtl
BuildRequires: SUNWgnome-audio-devel
BuildRequires: SUNWxorg-mesa
BuildRequires: SUNWaudh

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
%sdl_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%sdl.prep -d %name-%version/%base_arch

%build
%ifarch amd64 sparcv9
export LDFLAGS="%_ldflags -m64"
%sdl_64.build -d %name-%version/%_arch64
%endif

export LDFLAGS="%_ldflags"
%sdl.build -d %name-%version/%base_arch

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%sdl_64.install -d %name-%version/%_arch64
%endif

%sdl.install -d %name-%version/%base_arch

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%doc -d %{base_arch}/SDL-%{sdl.version} README CREDITS
%doc(bzip2) -d %{base_arch}/SDL-%{sdl.version} COPYING WhatsNew
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libSDL*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
 
%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/sdl-config
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/*
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*.pc
%endif

%changelog
* Wed Nov 10 2010 - dave.lin@oracle.com
- Added license tag.
* Tue Jan 12 2010 - dave.lin@sun.com
- Remove OpenGL check, use 'BuildRequires: SUNWxorg-mesa' instread.
* Mon Feb 23 2009 - elaine.xiong@sun.com
- Remove SSE2 support to fix CR6808201.
* Thu Sep 19 2008 - dave.lin@sun.com
- Update the license file and add %doc lines to include licensing/copyright files
* Wed Apr  4 2007 - laca@sun.com
- Create



