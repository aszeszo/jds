#
# spec file for package seahorse-plugins
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         seahorse-plugins
License:      GPL v2, FDL v1.1
Group:        System/GUI/GNOME
Version:      2.30.1
Release:      1
Distribution: Java Desktop System
Vendor:	      Gnome Community
Summary:      Seahorse-Plugins
Source:       http://download.gnome.org/sources/%{name}/2.30/%{name}-%{version}.tar.bz2
%if %build_l10n
Source1:                 l10n-configure.sh
%endif
#date:2011-05-07 owner:ginnchen type:bug
Patch1:       seahorse-plugins-01-gecko20.diff

URL:          http://www.gnome.org
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
Seahorse plugins integrates with nautilus, gedit and other places for
encryption/decryption operations.

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

gnome-doc-prepare --force
aclocal -I /usr/share/aclocal -I m4
autoconf
autoheader
automake 

CFLAGS="$RPM_OPT_FLAGS" 	\
./configure --prefix=%{_prefix}			\
	    --sysconfdir=%{_sysconfdir}		\
	    --mandir=%{_mandir}			\
            --libexecdir=%{_libexecdir}         \
            --enable-pgp \
			--disable-update-mime-database
make  -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT install

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat May 07 2011 - ginn.chen@oracle.com
- Fix building with gecko 2.0
- Add seahorse-plugins-01-gecko20.diff
* Wed May 26 2010 - jeff.cai@sun.com
- Bump to 2.30.1
* Wed Mar 31 2010 - jeff.cai@sun.com
- Bump to 2.30.0
* Tue Feb 23 2010 - jeff.cai@sun.com
- Bump to 2.29.91
* Tue Feb 09 2010 - jeff.cai@sun.com
- Bump to 2.29.90
* Mon Dec 07 2009 - jeff.cai@sun.com
- Bump to 2.29.3
- Upstream patch -01-check-gpg2
* Fri Oct 16 2009 - jeff.cai@sun.com
- Initial Sun release
