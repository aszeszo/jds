#
# spec file for package SUNWobby
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner kevmca
#

%include Solaris.inc

Name:           SUNWobby
IPS_package_name: library/c++/obby
Meta(info.classification): %{classification_prefix}:Development/System
License:        GPLv2.1
Summary:        Network Text Editing Library
Version:        0.4.7
Source:         http://releases.0x539.de/obby/obby-%{version}.tar.gz
# owner:trisk date:2007-8-17 type:bug
Patch1:         obby-01-cast.diff
SUNW_Basedir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
URL:            http://gobby.0x539.de/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       SUNWnet6
Requires:       SUNWavahi-bridge-dsd
BuildRequires:  SUNWnet6-devel
BuildRequires:  SUNWavahi-bridge-dsd-devel
BuildRequires:  SUNWbtool
BuildRequires:  SUNWgnome-common-devel

%package devel
Summary:        %{summary} - development files
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:       %name

%package l10n
Summary:        %{summary} - l10n files
Requires:       %{name}

%description
obby is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.

%prep
%setup -q -n obby-%{version}
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir} \
            --libexecdir=%{_libexecdir} \
            --sysconfdir=%{_sysconfdir} \
            --enable-ipv6 \
            --with-zeroconf

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS NEWS README
%doc(bzip2) COPYING ChangeLog
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Tue Mar 3 2009 - kevin.mcareavey@sun.com
- Bump to 0.4.7
* Wed Sep 24 2008 - dave.lin@sun.com
- Set attribute to %{_datadir} in l10n pkg.
* Fri Sep 19 2008 - kevin.mcareavey@sun.com
- Changed %doc files to bzip2
* Thu Sep 18 2008 - kevin.mcareavey@sun.com
- Cleanup for spec-files-other integration
* Mon Sep 17 2007 - trisk@acm.jhu.edu
- Enable IPv6 support and Zeroconf (avahi)
* Fri Aug 17 2007 - trisk@acm.jhu.edu
- Bump to 0.4.4
- Add URL
* Tue Jul 11 2006 - laca@sun.com
- rename to SFEobby
- update file attributes
- bump to 0.4.0.rc2
* Fri May 05 2006 - damien.carbery@sun.com
- Bump to 0.4.0rc1. Add SUNWsigcpp and SUNWnet6 dependencies.
* Thu Nov 17 2005 - laca@sun.com
- create


