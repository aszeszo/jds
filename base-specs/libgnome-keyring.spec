#
# spec file for package gnome-keyring
#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         libgnome-keyring
License:      LGPL v2
Group:        System/GUI/GNOME
Version:      2.30.1
Release:      4
Distribution: Java Desktop System
Vendor:	      Gnome Community
URL:          http://www.gnome.org
Summary:      GNOME Keyring
Source:       http://download.gnome.org/sources/%{name}/2.30/%{name}-%{version}.tar.bz2
%if %build_l10n
Source1:      l10n-configure.sh
%endif
# date:2010-01-26 owner:jefftsai type:branding
Patch1:       libgnome-keyring-01-disable-eggdbus.diff

BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%define gtk2_version 2.4.0
%define pkgconfig_version 0.15.0
%define gtk_doc_version 1.1

Requires: gtk2 >= %{gtk2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: gtk-doc >= %{gtk_doc_version}
BuildRequires: pkgconfig >= %{pkgconfig_version}

%description

The library libgnome-keyring is used by applications to integrate with
the gnome keyring system.

%package devel
Summary:      GNOME Keyring Library
Group:        Development/Libraries/GNOME
Requires:     %{name} = %{version}
Requires:     gtk2-devel >= %{gtk2_version}

%description devel
The library libgnome-keyring is used by applications to integrate with
the gnome keyring system.

%prep
%setup -q
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

libtoolize --force
intltoolize -f -c --automake

%if %build_l10n
bash -x %SOURCE1 --enable-copyright
%endif

aclocal $ACLOCAL_FLAGS -I .
autoconf
autoheader
automake -a -c -f

export CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include"	\
export LDFLAGS="%_ldflags"

./configure --prefix=%{_prefix}			\
	    --libdir=%{_libdir}			\
	    --sysconfdir=%{_sysconfdir}		\
	    --mandir=%{_mandir}			\
	    --disable-pam			\
            --libexecdir=%{_libexecdir}

# FIXME: hack: stop the build from looping
touch po/stamp-it

make -j $CPUS

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make -i install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

#%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_datadir}/locale/*/LC_MESSAGES/*
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libexecdir}/gnome-keyring-ask

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gnome-keyring-1/*
%{_libdir}/lib*.so

%changelog
* Fri Feb 17 2012 - brian.cameron@oracle.com
- Changes needed to build 64-bit version.
* Mon Apr 26 2010 - christian.kelly@oracle.com
- Bump to 2.30.1.
* Jan 26 2010 - jeff.cai@sun.com
- Split libgnome-keyring from SUNWgnome-keyring
