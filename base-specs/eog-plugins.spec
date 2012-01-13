#
# base spec file for package eog-plugins
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 

%define OSR LFI#105446 (gnome Exec. summary):n/a

#

Name:         eog-plugins
License:      GPLv2
Group:        System/GUI/GNOME
Version:      2.30.1
Release:      1
Vendor:       Gnome Community
Summary:      Eog plugins 
Source:       http://ftp.gnome.org/pub/GNOME/sources/eog-plugins/2.30/eog-plugins-%{version}.tar.bz2

URL:          http://live.gnome.org/EyeOfGnome/Plugins
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/doc
Autoreqprov:  on


%description
plugins of  package eog ("Eye of GNOME")

%prep
%setup -q
#%if %build_l10n
#bzcat %SOURCE1 | tar xf -
#cd po-sun; make; cd ..
#%endif

#for po in po/*.po; do
#  dos2unix -ascii $po $po
#done

%build
%ifos linux
if [ -3 /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

gnome-doc-common
libtoolize --force
glib-gettextize -f
intltoolize --force --copy


aclocal $ACLOCAL_FLAGS
automake -a -c -f
autoconf

CFLAGS="$RPM_OPT_FLAGS -g"			\
./configure --prefix=%{_prefix}		\
	    --sysconfdir=%{_sysconfdir} \
	    --libexecdir=%{_libexecdir} \
	    --disable-scrollkeeper	\
            --without-lcms              \
            --with-plugins=exif-display,fit-to-width,pythonconsole,slideshowshuffle,send-by-mail

make -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=$RPM_BUILD_ROOT install
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL  


%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 20 2010 - brian.cameron@oracle.com
- Bump to 2.30.1.
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Bump to 2.30.0.
- Disable building of champlain module, doesn't seem to exist anymore.
* Thu Apr 22 2010 - christian.kelly@oracle.com
- Comment out l10n stuff.  Seems to be missing.
* Wen Api 07 2010 - yuntong.jin@sun.com
- Add send-by-mail plugin 
* Tue Jan 19 2010 - yuntong.jin@sun.com
- Init 
