#
# spec file for package tack 
#
# Copyright (c) 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
# bugdb :
#

%define OSR 12493:1.06

Name:	        tack	
# remember to update the Version in SUNWtack.spec as well!
Version:        1.06	
Release:        1
License:        GPLv2	
Vendor:         gnu.org
Group:    System/Libraries
Distribution:	Java Desktop System
Vendor:		Sun Microsystems, Inc.
Summary: Tack is a diagnostic that is designed to create and verify the correctness of terminfo's
Source:   http://ftp.gnu.org/pub/gnu/ncurses/%{name}-%{version}.tar.gz
URL:		 http://www.gnu.org/software/ncurses/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Docdir:		%{_defaultdocdir}/ncurses
Autoreqprov:	on

%description
This program is a diagnostic that is designed to create and
verify the correctness of terminfo's.  This program can be used to
create new terminal descriptions that are not included in the standard
release.

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

CFLAGS="$RPM_OPT_FLAGS"                  \
./configure  --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=%{_sysconfdir} --includedir=%{_preincludedir} --datadir=%{_datadir} --bindir=%{_bindir} --libdir=%{_libdir} --enable-widec         

make -j $CPUS
 
%install
make DESTDIR=$RPM_BUILD_ROOT install 

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%files
%defattr(-, root, root)
%{_bindir}/*


%clean
rm -r $RPM_BUILD_ROOT

%changelog
* Tue Jul 26 2009 - yuntong.jin@sun.com
- Initial spec file created.
