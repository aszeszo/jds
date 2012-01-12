#
# spec file for package uperf
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai
#

Name:         uperf
License:      GPL v3
Version:      1.0.3-beta
Release:      1
Distribution: Java Desktop System
Vendor:	      Gnome Community
Summary:      uperf
Source:       http://sourceforge.net/projects/uperf/files/uperf/uperf-1.0.3-beta/uperf-1.0.3-beta.tar.gz

URL:          http://sourceforge.net/projects/uperf
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%description
uperf is a network performance tool that supports modelling and replay of 
various networking patterns.


%prep
%setup -q

%build
export CFLAGS="%optflags"
./configure --prefix=%{_prefix}		\
            --datarootdir=%{_prefix}/share/uperf	\
            --bindir=%{_bindir} 

%install
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Jul 07 2011 - jeff.cai@oracle.com
Inital spec
