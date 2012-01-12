#
# spec file for package SUNWid3lib
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner christian
#

%include Solaris.inc

%define OSR 8315:3.8.3

Name:                    SUNWid3lib
IPS_package_name:        library/id3lib
Meta(info.classification): %{classification_prefix}:System/Libraries
Summary:                 id3lib  - a software library for manipulating ID3v1/v1.1 and ID3v2 tags
License:                 GPL
Version:                 3.8.3
Source:                  %{sf_download}/id3lib/id3lib-%{version}.tar.gz
# date:2008-02-15 owner:christian type:bug
Patch1:                  id3lib-01-wall.diff
# date:2008-02-15 owner:christian type:bug
Patch2:                  id3lib-02-uchar.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWzlib
Requires: SUNWlibC
Requires: SUNWlibms

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name

%prep
%setup -q -n id3lib-%version
%patch1  -p1
%patch2  -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --enable-shared		     \
	    --disable-static

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Fri Feb 15 2008 - dermot.mccluskey@sun.com
- add patch comments
- remove unnecessary defs (ACLOCAL, MSGFMT, C*FLAGS, fp_arch)
- add gcc C++ macro
- remove .la files
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version


