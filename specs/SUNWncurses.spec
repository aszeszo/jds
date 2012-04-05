#
# spec file for package SUNWncurses
#
# includes module(s): ncurses
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved. 
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
%use ncurses_64 = ncurses.spec
%endif

%include base.inc
%use ncurses = ncurses.spec 

Name:                    SUNWncurses
IPS_package_name:        library/ncurses
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                 A CRT screen handling and optimization package.
Version:                 %{ncurses.version}
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          %{name}.copyright
License:                 MIT

%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc

%prep

rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
rm -rf %name-%version/%{_arch64}
mkdir %name-%version/%{_arch64}
%ncurses_64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%ncurses.prep -d %name-%version/%{base_arch}

%build

export PKG_CONFIG_PATH=%{_pkg_config_path}
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
%ncurses.build -d %name-%version/%{base_arch}

%ifarch amd64 sparcv9
if [ "x`basename $CC`" != xgcc ]
then
  FLAG64="-xarch=generic64"
else
  FLAG64="-m64"
fi
export LDFLAGS="$FLAG64"
export CXXFLAGS="-g -m64"
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
%ncurses_64.build -d %name-%version/%{_arch64}
%endif

%install

rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%ncurses_64.install -d %name-%version/%{_arch64}
rm -rf $RPM_BUILD_ROOT/usr/gnu/bin/%{_arch64}
mkdir -p $RPM_BUILD_ROOT%{_basedir}/lib/%{_arch64}/
mv $RPM_BUILD_ROOT%{_basedir}/%{_subdir}/lib/%{_arch64}/libncurses* $RPM_BUILD_ROOT%{_basedir}/lib/%{_arch64}/
%endif

cd $RPM_BUILD_DIR
%ncurses.install -d %name-%version/%{base_arch}

mkdir -p $RPM_BUILD_ROOT%{_basedir}/bin
cd $RPM_BUILD_ROOT%{_basedir}/bin

ln -s ../%{_subdir}/bin/ncurses5-config gncurses5-config
ln -s ../%{_subdir}/bin/clear gclear     
ln -s ../%{_subdir}/bin/infocmp ginfocmp    
ln -s ../%{_subdir}/bin/tic gtic        
ln -s ../%{_subdir}/bin/toe gtoe        
ln -s ../%{_subdir}/bin/tput gtput       
ln -s ../%{_subdir}/bin/tset gtset       
ln -s ../%{_subdir}/bin/captoinfo gcaptoinfo
ln -s ../%{_subdir}/bin/infotocap ginfotocap
ln -s ../%{_subdir}/bin/reset greset

mkdir -p $RPM_BUILD_ROOT%{_basedir}/lib
mv $RPM_BUILD_ROOT%{_basedir}/%{_subdir}/lib/libncurses* $RPM_BUILD_ROOT%{_basedir}/lib/

#install man page
#rm -rf $RPM_BUILD_ROOT%{_mandir}
#cd %{_builddir}/%name-%version/sun-manpages
#make install DESTDIR=$RPM_BUILD_ROOT

# the sun-color terminfo included in ncurses does not work,
# copying the one shipped with Sun's curses fixes it:
cp /usr/share/lib/terminfo/s/sun-color $RPM_BUILD_ROOT%{_datadir}/terminfo/s/

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT




%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/terminfo
%dir %attr (0755, root, bin) %{_datadir}/tabset
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/captoinfo
%{_bindir}/clear
%{_bindir}/infocmp
%{_bindir}/infotocap
%{_bindir}/ncurses5-config
%{_bindir}/reset
%{_bindir}/tic
%{_bindir}/toe
%{_bindir}/tput
%{_bindir}/tset
%{_libdir}/terminfo
%{_libdir}/lib*.so
%{_libdir}/lib*.so.*
%{_basedir}/lib/libncurses*
%{_datadir}/terminfo/*
%{_datadir}/tabset/*

%{_basedir}/bin/gncurses5-config
%{_basedir}/bin/gcaptoinfo
%{_basedir}/bin/gclear
%{_basedir}/bin/ginfocmp
%{_basedir}/bin/ginfotocap
%{_basedir}/bin/greset
%{_basedir}/bin/gtic
%{_basedir}/bin/gtput
%{_basedir}/bin/gtset
%{_basedir}/bin/gtoe

%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so
%{_libdir}/%{_arch64}/lib*.so.*
%dir %attr (0755, root, bin) %{_basedir}/lib/%{_arch64}
%{_basedir}/lib/%{_arch64}/libncurses*
%endif

%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*
%dir %attr(0755, root, bin) %{_mandir}/man5
%{_mandir}/man5/*
%dir %attr(0755, root, bin) %{_mandir}/man7
%{_mandir}/man7/*

%doc -d %{base_arch}/ncurses-%version ANNOUNCE AUTHORS MANIFEST NEWS README
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel

%define _preincludedir  /usr/include/ncurses

%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_preincludedir}
%{_preincludedir}/*

%changelog
* Mon Jul 25 2011 - yanjing.guo@oracle.com
- fix bug 7031693
* Thu Jun 24 2010 - Thomas.Wagner@Sun.COM
- add missing directory permissions root:bin -> root:other for /usr/gnu/share/doc
* Tue Oct 20 2009 - yuntong.jin@sun.com
- copy the sun-color terminfo from /usr/share/lib
  because the one that comes with ncurses does not work.
* Tru Sep 15 2009 - yuntong.jin@sun.com
- fix  Bug 11335 -  Installation of <SUNWncurses> failed
* Tur Sep 03 2009 - yuntong.jin@sun.com
- fix bug 11165 move ncurses bin programs under /usr/gnu/bin need move to /usr/bin
* Mon Aug 03 2009 - yuntong.jin@sun.com
- fix 10426 SUNWncurses missed man page and docs
* Mon Jul 2002009 - yuntong.jin@sun.com
- Bump to 5.7
* Tue Jue 02 2009 - yuntong.jin@sun.com
- fix bug 8971 provide 64bit lib
* Mon Mar 30 2009 - yuntong.jin@sun.com
- change the owner to yuntong.jin
* Thu Feb 26 2009 - elaine.xiong@sun.com
- correct basedir setting to fix CR6760759.
* Mon Aug 18 2008 - rick.ju@sun.com
- use /usr/gnu as prefix
* Sat Aug 16 2008 - halton.huo@sun.com
- Add (0755, root, sys) %{_datadir} to fix conflict issue.
* Tur Jul 17 2008 - rick.ju@sun.com
- Initial spec file created.




