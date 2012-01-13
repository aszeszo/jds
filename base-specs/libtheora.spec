#
# spec file for package libtheora
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: https://trac.xiph.org/
#

%define OSR 4198:1.0

Name:         libtheora
License:      Xiph.org BSD-style, binaries use some LGPL v2.1
Group:        Libraries/Multimedia
Version:      1.1.1
%define tarball_version 1.1.1
Release:      2
Distribution: Java Desktop System
Vendor:       Xiph
Summary:      The Theora Video Compression Codec.
Source:       http://downloads.xiph.org/releases/theora/%{name}-%{tarball_version}.tar.gz
URL:          http://www.theora.org/
BuildRoot:    %{_tmppath}/%{name}-%{tarball_version}-build
Docdir:       %{_docdir}/%{name}
Autoreqprov:  on

BuildRequires:  libogg-devel >= 1.1
BuildRequires:  libvorbis-devel >= 1.0.1
BuildRequires:  SDL-devel
Requires:       libvorbis >= 1.0.1

%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

%package devel
Summary:        Development tools for Theora applications.
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libogg-devel >= 1.1
 
%description devel
The libtheora-devel package contains the header files and documentation
needed to develop applications with Ogg Theora.

%prep
%setup -q -n %{name}-%{tarball_version}

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
aclocal $ACLOCAL_FLAGS -I ./m4
autoconf
automake -a -c -f
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
#CFLAGS="$RPM_OPT_FLAGS" \
./configure --enable-shared     \
            --prefix=%{_prefix} \
            --libdir=%{_libdir}  \
            --bindir=%{_bindir} \
            --sysconfdir=%{_sysconfdir} \
            --mandir=%{_mandir} \
            --disable-asm \
	    --disable-examples


make -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT install

#clean up unpackaged files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Mon Oct 19 2009 - ke.wang@sun.com
- Add 64-bit support.
* Sat Oct 17 2009 - brian.cameron@sun.com
- Bump to 1.1.1.
* Sun Sep 13 2009 - dave.lin@sun.com
- Correct the version number, which is required as digit + dot only.
* Fri Nov 07 2008 - jerry.tan@sun.com
- bump to 1.0, remove upstream patches
* Fri Aug 29 2008 - jerry.tan@sun.com
- add patch libtheora-02-signed-short.diff to bump to 1.0beta3
* Tue Apr 29 2008 - brian.cameron@sun.com
- Bump to 1.0beta3.  Remove upstream patch libtheora-01-fixlink.diff.
  Add new patch libtheora-01-fixtestlink.diff.
* Mon Nov 05 2007 - brian.cameron@sun.com
- Bump to 1.0beta2.
* Fri Feb 09 2006 - brian.cameron@sun.com
- Go back to 1.0alpha7, but add --disable-asm configure flag so that
  we don't try to compile GCC-style assembler code with Sun Studio
  compiler.  Remove upstream patch 01-noversionscript.
* Wed Dec 06 2006 - damien.carbery@sun.com
- Revert to 1.0alpha5 because of compilation errors. Add patch too.
* Sun Dec 03 2006 - damien.carbery@sun.com
- Remove upstream patch, 01-noversionscript.
* Thu Nov 30 2006 - damien.carbery@sun.com
- Bump to 1.0alpha7.
* Thu Nov 10 2005 - damien.carbery@sun.com
- Change %setup to reference %{tarball_version} in order to build.
* Tue Sep 20 2005 - brian.cameron@sun.com
- Bump to 1.0alpha5
* Fri Sep 09 2005 - laca@sun.com
- Move ACLOCAL_FLAGS setting to the Solaris spec file
- libtoolize so it builds with newer libtool
* Fri Sep 02 2005 - damien.carbery@sun.com
- Set ACLOCAL_FLAGS to build on Solaris.
* Tue Aug 02 2005 - balamurali.viswanathan@wipro.com
- Change copyright to license
* Tue Jul 26 2005 - balamurali.viswanathan@wipro.com
- Add patch libtheora-1.0alpha4-01-docs-make.diff
* Wed Jul 20 2005 - balamurali.viswanathan@wipro.com
- Initial spec file checkin
