#
# spec file for package libvisual-plugins.spec
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke

%define OSR 10429:0.x

Name:                   libvisual-plugins
License:                GPL v2
Summary:                Visualization plugins for the Libvisual library
Version:                0.4.0
Vendor:                 Other
URL:                    http://localhost.nl/~synap/libvisual-wiki/index.php/Main_Page
Source:                 http://downloads.sourceforge.net/libvisual/libvisual-plugins-%{version}.tar.bz2
# date:2009-09-24 owner:wangke type:branding
Patch1:                 libvisual-plugins-01-opengl.diff

Requires: libvisual

%prep
%setup -q -n libvisual-plugins-%{version}
%patch1 -p1

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

autoconf
# the following ifarch-endif contains plugins
# which depend on OpenGL 
./configure --prefix=%{_prefix}		\
            --bindir=%{_bindir}		\
            --libdir=%{_libdir}		\
            --mandir=%{_mandir}		\
            --datadir=%{_datadir}	\
            --sysconfdir=%{_sysconfdir}	\
            --enable-shared=yes		\
            --enable-static=no		\
%ifarch sparc
            --disable-opengl		\
%endif
            --disable-corona		\
            --disable-gforce 


make -j$CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755,root,bin) %{_libdir}
%{_libdir}/*

%defattr (-, root, other)
%dir %attr(0755, root, sys) %{_datadir}
%{_datadir}/*

%changelog
* Thu Sep 24 2009 - jedy.wang@sun.com
- Add 02-opengl.diff and disable OpenGL plugins on SPARC.
* Tue Mar 10 2009 - harry.lu@sun.com
- Change owner to Jerry Tan
* Tue Nov 25 2008 - jim.li@sun.com
- add license tag
- rename SFElibvisual-plugins to libvisual-plugins
- use sun compiler 12 instead of gcc
* Tue Jan 29 2008 - moinak.ghosh@sun.com
- Initial spec.
