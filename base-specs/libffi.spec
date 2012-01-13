#
# spec file for package libffi
#
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#

%define OSR 9803:3.0.5

Name:         libffi
License:      MIT
Vendor:       sourceware.org
Group:        Development/Libraries/C and C++
Summary:      Foreign Function Interface Library
Version:      3.0.9
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Source0:      ftp://sources.redhat.com/pub/libffi/libffi-%{version}.tar.gz
# owner:laca date:2008-03-23 type:bug
Patch1:       libffi-01-__i386__.diff
# owner:ginnchen date:2010-04-28 type:bug
# patch by Rainer Orth
Patch2:       libffi-02-SHT_AMD64_UNWIND.diff
# owner:ginnchen date:2011-03-22 type:bug bugster:7029370
Patch3:       libffi-03-sparcv8-struct-return.diff

URL:          http://sourceware.org/libffi/

%prep 
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CC="/usr/sfw/bin/gcc -static-libgcc"
export LD="$CC"
export CFLAGS="%gcc_optflags"
export LDFLAGS="%_ldflags"

libtoolize -f
aclocal-1.9 $ACLOCAL_FLAGS
automake-1.9 -a -c -f
autoheader configure.ac
autoconf
./configure 			\
		--prefix=%{_prefix}	\
		--libdir=%{_libdir}	\
		--disable-static

echo '#define FFI_NO_RAW_API 1' >> fficonfig.h
echo '#define FFI_MMAP_EXEC_WRIT 1' >> fficonfig.h

make

%install
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%changelog -n libffi
* Mon Mar 28 2010 - ginn.chen@oracle.com
- Add libffi-03-sparcv8-struct-return.diff
- Add FFI_MMAP_EXEC_WRIT to make sure closure is executable
* Wed Apr 28 2010 - ginn.chen@sun.com
- bump to 3.0.9, add libffi-02-SHT_AMD64_UNWIND.diff
* Mon Mar 30 2009 - laca@sun.com
- bump to 3.0.8
* Fri Mar 23 2008 - laca@sun.com
- initial spec
