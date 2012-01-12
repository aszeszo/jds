#
# spec file for package SUNWgnome-audio
#
# includes module(s): gnome-audio
#
# Copyright (c) 2004, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use audiofile_64 = audiofile.spec
%endif

%include base.inc
%use audiofile = audiofile.spec

Name:                    SUNWgnome-audio
IPS_package_name:        gnome/gnome-audio
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                 GNOME audio support framework
Version:                 %{default_pkg_version}
Source1:                 %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 LGPL v2, MIT, Sun Public Domain, binaries use GPL v2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWaudh
Requires: SUNWlibms

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%audiofile_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%base_arch
%audiofile.prep -d %name-%version/%base_arch

cd %name-%version
gzcat %SOURCE1 | tar xf -

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export ACLOCAL_FLAGS="-I `pwd`/%name-%version/%base_arch/audiofile-%{audiofile.version}"

%ifarch amd64 sparcv9
export REAL_AUDIOFILE_CFLAGS=" "
export REAL_AUDIOFILE_LIBS="-L%{_libdir}/%{_arch64} -R%{_libdir}/%{_arch64} -laudiofile -lm"
%audiofile_64.build -d %name-%version/%_arch64
%endif

export REAL_AUDIOFILE_CFLAGS=" "
export REAL_AUDIOFILE_LIBS="-laudiofile -lm"
%audiofile.build -d %name-%version/%base_arch

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%audiofile_64.install -d %name-%version/%_arch64
%endif

%audiofile.install -d %name-%version/%base_arch

rm $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/{sfconvert,sfinfo}
rm $RPM_BUILD_ROOT%{_bindir}/{sfconvert,sfinfo}
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

cd %name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%ifarch amd64 sparcv9
%{_libdir}/%{_arch64}/lib*.so*
%endif
%{_libexecdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%doc %{base_arch}/audiofile-%{audiofile.version}/AUTHORS
%doc %{base_arch}/audiofile-%{audiofile.version}/README
%doc(bzip2) %{base_arch}/audiofile-%{audiofile.version}/COPYING
%doc(bzip2) %{base_arch}/audiofile-%{audiofile.version}/COPYING.GPL
%doc(bzip2) %{base_arch}/audiofile-%{audiofile.version}/ChangeLog
%doc(bzip2) %{base_arch}/audiofile-%{audiofile.version}/NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/audiofile-config
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/audiofile-config
%endif
%dir %attr (0755, root, bin) %{_libdir}
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
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*

%changelog
* Thu Dec 02 2010 - brian.cameron@oracle.com
- Remove ESounD.
* Wed Jun 02 2009 - dave.lin@sun.com
- Use PKG_CONFIG_TOP_BUILD_DIR environment variable when building esound,
  so that pkg-config expands $(top_builddir), otherwise audiofile pkg-config
  variables do not expand nicely and the build fails.
* Sun Sep 14 2008 - brian.cameron@sun.com
- Add new copyright files.
* Thu Mar 27 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Wed Apr  4 2007 - laca@sun.com
- convert to new style multi-isa build
* Fri Feb 23 2007 - dougs@truemail.co.th
- PKG_CONFIG_PATH64 should use _pkg_config_path64
* Mon Feb 19 2007 - laca@sun.com
- move esound and audiofile into their own spec files
- update for 64-bit audiofile and esound libs
* Tue Nov 28 2006 - damien.carbery@sun.com
- Change defattr in root package to 0644 to fix 6497737.
* Tue Sep 12 2006 - Matt.Keenan@sun.com
- Add back "rm" of _mandir, as needed
* Fri Sep 08 2006 - Matt.Keenan@sun.com
- Remove "rm" of _mandir during %install
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Fri Jul 21 2006 - damien.carbery@sun.com
- Bump audiofile to 0.2.6.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Tue May 09 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Wed Dec 21 2005 - damien.carbery@sun.com
- Redo patch 1. Remove patch 2 (pkgconfig) as it was undoing patch 1!!
* Tue Dec 20 2005 - damien.carbery@sun.com
- Bump esound to 0.2.36.
* Fri Sep 09 2005 - <laca@sun.com>
- remove unpackaged files
* Wed Jun 15 2005 - laca@sun.com
- add patch to make esound work with recent pkgconfig
- add libtoolize so that it uses the newer libtool in the CBE
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Aug 30 2004 - shirley.woo@sun.com
- Bug 5091588 : sman3/4 files should be in a separate devel package
* Wed Aug 18 2004 - damien.carbery@sun.com
- Change manpage perms for Solaris integration.
* Tue Jun 22 2004 - shirley.woo@sun.com
- changed install location to /usr/lib and /usr/bin
* Thu May 27 2004 - brian.cameron
- added --with-esd-dir option to configure so esd gets installed
  to libexec.
* Wed May 19 2004 - brian.cameron@sun.com
- Added missing man pages.
* Fri May 07 2004 - brian.cameron@sun.com
- Add esound patch1 to fix esd-config to have correct values.
  Now call aclocal/autoconf for esound so patch takes effect.
* Thu May 06 2004 - brian.cameron@sun.com
- added missing *.m4 and *-config files to packaging.
* Thu Feb 26 2004 - niall.power@sun.com
- add missing -devel pkg
* Thu Feb 26 2004 - laca@sun.com
- fix audiofile dependency in esound
