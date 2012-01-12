#
# spec file for package pkg-config
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#

%define OSR delivered in s10:n/a

Name:			pkg-config
License:		GPLv2
Group:			System/Libraries
Version:		0.26
Release:		1
Distribution:		Java Desktop System
Vendor:			Gnome Community
Summary:		Helper tool used when compiling applications and libraries.
Source:			http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
URL:			http://pkgconfig.freedesktop.org
BuildRoot:		%{_tmppath}/%{name}-%{version}-build
Docdir:			%{_defaultdocdir}/%{name}
Autoreqprov:		on

%description
pkg-config is a helper tool used when compiling applications and libraries. It helps you insert the correct compiler options on the command line

%prep
%setup -q

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

CFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files

%changelog
* Thu Oct 20 2011 - brian.cameron@oracle.com
- Bump to 0.26.
* Thu Jun 03 2010 - dave.lin@sun.com
- Rolled back to 0.23. Because 0.25 escapes characters '$', '(' and ')', and 
  returns the string like this "\$\(top_builddir\)/../...", which could not be
  substituted correctly in Makefile and cause many gnome modules build failed.
* Fri May 28 2010 - brian.cameron@oracle.com
- Bump to 0.25.  I previously unbumped back to 0.23 because 0.24 had a COPYING
  file that said GPLv3.  However, this was an error and has been corrected in
  0.25.  So now it is okay to bump.
* Mon May 24 2010 - brian.cameron@oracle.com
- Bump to 0.24.
* Tue Jul 15 2008 - damien.carbery@sun.com
- Separate out from SUNWgnome-common-devel.spec.
