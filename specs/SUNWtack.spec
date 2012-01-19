#
# spec file for package SUNWtack
#
# includes module(s): tack 
#
# Copyright (c) 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#

%include Solaris.inc

%define _basedir    /usr 
%define _subdir     gnu
%define _prefix     %{_basedir}/%{_subdir}

%ifarch amd64 sparcv9
%include arch64.inc
%use tack_64 = tack.spec
%endif

%include base.inc
%use tack = tack.spec 

Name:                    SUNWtack
IPS_package_name:        terminal/tack
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:                 A CRT screen handling and optimization package.
# note: 1.06 is not a valid IPS version number so changed it to 1.0.6
Version:                 1.0.6
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          %{name}.copyright
License:                 GPLv2
Requires: SUNWncurses
BuildRequires: SUNWncurses-devel
%include desktop-incorporation.inc
%include default-depend.inc

%prep

rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
rm -rf %name-%version/%{_arch64}
mkdir %name-%version/%{_arch64}
%tack_64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%tack.prep -d %name-%version/%{base_arch}

%build

export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="-I/usr/include/ncurses %optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags -L/usr/gnu/lib -R/usr/gnu/lib -lncurses"
%tack.build -d %name-%version/%{base_arch}

%ifarch amd64 sparcv9
if [ "x`basename $CC`" != xgcc ]
then
  FLAG64="-xarch=generic64"
else
  FLAG64="-m64"
fi
export LDFLAGS="$FLAG64 -L/usr/gnu/lib/%{_arch64} -R/usr/gnu/lib/%{_arch64} -lncurses "
export CFLAGS="-I/usr/include/ncurses %optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
%tack_64.build -d %name-%version/%{_arch64}
%endif

%install

rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%tack_64.install -d %name-%version/%{_arch64}
rm -rf $RPM_BUILD_ROOT/usr/gnu/bin/%{_arch64}
%endif

cd $RPM_BUILD_DIR
%tack.install -d %name-%version/%{base_arch}

mkdir -p $RPM_BUILD_ROOT%{_basedir}/bin
cd $RPM_BUILD_ROOT%{_basedir}/bin
ln -s ../%{_subdir}/bin/tack gtack
 
%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%{_bindir}/tack
%{_basedir}/bin/gtack
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr(0755, root, sys) %{_basedir}/gnu/share

%doc -d %{base_arch}/tack-%{tack.version} CHANGES HISTORY README
%doc(bzip2) -d %{base_arch}/tack-%{tack.version} COPYING
%dir %attr (0755, root, other) %{_datadir}/doc

%ifarch amd64 sparcv9
%endif

%changelog
* Wen Jul 13 2011 - yanjing.guo@oracle.com	
- fix bug 7031695
* Wen Jun 24 2010 - Thomas.Wangner@sun.com
- add missing directory permissions root:bin -> root:other for
 /usr/gnu/share/doc
* Wed Aug 05 2009 - christian.kelly@sun.com
- Fix %files section.
* Mon Jul 27 2009 - yuntong.jin@sun.com
- Initial spec file created.


