#
# spec file for package SUNWbrltty
#
# includes module(s): brltty
#
# Copyright 2007 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan 
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use brltty_64 = brltty.spec
%endif

%include base.inc
%use brltty = brltty.spec

Name:              SUNWbrltty
License:	   GPLv2 LGPLv2.1
IPS_package_name:  library/accessibility/brltty
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
Summary:           Braille support
Version:           %{brltty.version}
SUNW_BaseDir:      %{_basedir}
SUNW_Copyright:    %{name}.copyright
BuildRoot:         %{_tmppath}/%{name}-%{version}-build
Requires: SUNWugen
Requires: SUNWcslr
Requires: SUNWPython26
Requires: SUNWPython26-extra
Requires: SUNWgnome-a11y-libs
BuildRequires: SUNWxwrtl
BuildRequires: SUNWxwplt
BuildRequires: SUNWugenu
BuildRequires: SUNWcslr
BuildRequires: SUNWPython26-devel
BuildRequires: SUNWPython26-extra
BuildRequires: SUNWgnome-a11y-libs-devel
BuildRequires: SUNWgnome-media
BuildRequires: SUNWaudh
# Add BuildConfli to workaround the build issue: 
# "wrong ELF class: ELFCLASS64"
BuildConflicts: SUNWocaml

%include default-depend.inc
%include desktop-incorporation.inc

%package -n SUNWbrltty-root
Summary:           %{summary} - / filesystem
IPS_package_name:  library/accessibility/brltty
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package -n SUNWbrltty-devel
Summary:           %{summary} - development files
IPS_package_name:  library/accessibility/brltty
SUNW_BaseDir:      %{_basedir}
%include default-depend.inc

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%brltty_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%brltty.prep -d %name-%version/%base_arch

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="%optflags -I%{_includedir}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"

%ifarch amd64 sparcv9
%brltty_64.build -d %name-%version/%_arch64
%endif

%brltty.build -d %name-%version/%base_arch

%install

%ifarch amd64 sparcv9
%brltty_64.install -d %name-%version/%_arch64
%endif

%brltty.install -d %name-%version/%base_arch

rm -rf $RPM_BUILD_ROOT%{_mandir}/man3

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc(bzip2) -d %{base_arch}/brltty-%{brltty.version} README
%doc(bzip2) -d %{base_arch}/brltty-%{brltty.version} LICENSE-LGPL
%doc(bzip2) -d %{base_arch}/brltty-%{brltty.version} LICENSE-GPL
%doc -d %{base_arch}/brltty-%{brltty.version}/Documents CONTRIBUTORS
%doc -d %{base_arch}/brltty-%{brltty.version}/Documents HISTORY
%doc(bzip2) -d %{base_arch}/brltty-%{brltty.version}/Documents ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/brltty*
%{_bindir}/vstp
%{_bindir}/xbrlapi
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libbrlapi.so.*
%{_libdir}/libbrlapi.so
%{_libdir}/brltty/libbrltty*.so
%{_libdir}/brltty/rw
%{_libdir}/python?.?/vendor-packages
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/man1/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/brltty*
%{_bindir}/%{_arch64}/vstp
%{_bindir}/%{_arch64}/xbrlapi
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/libbrlapi.so.*
%{_libdir}/%{_arch64}/libbrlapi.so
%{_libdir}/%{_arch64}/brltty/libbrltty*.so
%{_libdir}/%{_arch64}/brltty/rw
%endif

%files root
%defattr(-, root, sys)
%dir %attr (0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/brltty/*

%files devel
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/brlapi*.h
%{_includedir}/brltty/*.h
%dir %attr(0755, root, sys) %{_datadir}

%changelog
* Fri Aug 21 2009 - li.yuan@sun.com
- Change owner to liyuan.
* Tue Jun 30 2009 - christian.kelly@sun.com
- Correct typo.
* Tue Jun 16 2009 - brian.cameron@sun.com
- Remove empty mandir from devel package.
* Wed Jun 03 2009 - dave.lin@sun.com
- add 'BuildConflicts: SUNWocaml'.
* Fri Sep 19 2008 - halton.huo@sun.com
- Add %doc part to %files
* Mon Jul 07 2008 - li.yuan@sun.com
- Fix 6697334. Add 64 bit libraries support.
* Thu Apr 03 2008 - damien.carbery@sun.com
- Add SUNW_Copyright.
* Mon Nov 12 2007 - li.yuan@sun.com
- Remove brlapi manpages.
* Thu Oct 11 2007 - damien.carbery@sun.com
- Add 'Build/Requires: SUNWcslr' to fix 6615512.
* Wed Oct 10 2007 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Sep 28 2007 - laca@sun.com
- add option to build with FOX instead of Nevada X
* Wed Jul 25 2007 - damien.carbery@sun.com
- Update %files for new tarball. Add Build/Requires SUNWPython-extra and
  SUNWPython/-devel to ensure python bindings are built (for use with orca).
* Thu Oct 05 2006 - damien.carbery@sun.com
- Add Requires SUNWxwplt to partially fix 6454451.
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Thu May 04 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue Apr 04 2006 - glynn.foster@sun.com
- Fix installation of devel vs non-devel libraries.
* Thu Feb 23 2006 - william.walker@sun.com
- Anal-rententive version name change to match ../brltty.spec (3.7.2)
* Fri Feb 17 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Fri Oct 28 2005 - damien.carbery@sun.com
- Update packaging for new source tarball. Add prerequisite packages.
* Fri Sep 09 2005 - <laca@sun.com>
- add unpackaged files to %files
* Thu Aug 25 2005
- Removed the 'export CC="/opt/SUNWspro/bin/cc"' line. No longer needed.
* Mon Aug 22 2005
- Adjustments needed to make the package proto maps equivalent to what gets
  installed via "make install"
* Tue Aug 16 2005 - rich.burridge@sun.com
- initial version
