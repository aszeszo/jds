#
# spec file for package SUNWnet6
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner kevmca
#

%include Solaris.inc

%define OSR 9813:1.3

Name:           SUNWnet6
IPS_package_name: library/c++/net6
Meta(info.classification): %{classification_prefix}:Development/System
License:        LGPLv2.1
Version:        1.3.12
Summary:        A library which eases the development of network-based applications
Source:         http://releases.0x539.de/net6/net6-%{version}.tar.gz
Source1:        l10n-configure.sh
Patch1:         net6-01-close-prototype.diff
SUNW_Basedir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
URL:            http://gobby.0x539.de/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires:  SUNWsigcpp
BuildRequires:  SUNWgnutls
Requires:       SUNWlibgpg-error
BuildRequires:  SUNWsigcpp-devel
BuildRequires:  SUNWgnutls-devel
BuildRequires:  SUNWbtool

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
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

%prep
%setup -q -n net6-%{version}
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

sh %SOURCE1 --enable-copyright
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
libtoolize --force
aclocal $ACLOCAL_FLAGS
autoconf
automake -a -c -f
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir} --disable-python

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING AUTHORS NEWS ChangeLog README
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
* Thu Jan 28 2010 - brian.cameron@sun.com
- Bump to 1.3.12.  Remove upstream patch net6-02-gnutls.diff.
* Thu Jul 23 2009 - christian.kelly@sun.com
- Add patch to allow build with gnutls.
* Tue Apr 20 2009 - kevin.mcareavey@sun.com
- Bump to 1.3.9.
* Thu Sep 11 2008 - kevin.mcareavey@sun.com
- Add %doc to %files for copyright
* Tue Aug 26 2008 - kevin.mcareavey@sun.com
- Cleanup for spec-files-other integration
- Bump to 1.3.6.
* Fri Aug 17 2007 - trisk@acm.jhu.edu
- Bump to 1.3.5.
- Add URL.
* Fri Jul  7 2006 - laca@sun.com
- rename to SFEnet6.
- bump to 1.3.0rc2.
- fix version number.
- update file attributes.
- remove upstream patch enum_opts.diff.
* Mon May 08 2006 - damien.carbery@sun.com
- Add patch, 02-enum_opts, to fix build.
* Fri May 05 2006 - damien.carbery@sun.com
- Bump to 1.3.0rc1.
* Wed Nov 16 2005 - laca@sun.com
- create.


