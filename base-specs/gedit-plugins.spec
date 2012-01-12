#
# spec file for package: gedit-plugins
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:       gedit-plugins
Summary:    Plugins for gedit
Vendor:     Gnome Community
Version:    2.30.0
Release:    1
License:	GPLv2
Url: 		http://live.gnome.org/GeditPlugins
Source:     http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.30/%{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-build


%description
Plugins for gedit including: bracketcompletion charmap codecomment colorpicker
drawspaces joinlines sessionsaver showtabbar smartspaces terminal 

%prep
rm -rf %name-%version
%setup -q -n %name-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi


export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix}			\
	    --bindir=%{_bindir}			\
	    --mandir=%{_mandir}                 \
            --infodir=%{_infodir}		\
            --sysconfdir=%{_sysconfdir}		\
            --disable-scrollkeeper

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1    
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL   

rm  $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.la
rm  $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.pyo
rm  $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*/*.pyo

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Bump to 2.30.0.
* Tue Feb 23 2010 - yuntong.jin@sun.com
- Initial base spec


