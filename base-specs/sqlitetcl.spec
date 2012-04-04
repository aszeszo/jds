#
# Copyright (c) 2010, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner ginnchen
# bugdb: bugzilla.freedesktop.org
#

%define OSR 12578:1.0.2
%define tarball_version 3071100

Name:         sqlite-tea 
License:      public domain 
Group:        System/Libraries
Version:      3.7.11
Release:      1
Distribution: Java Desktop System
Vendor:	      www.sqlite.org
Summary:      SQL database engine Tcl extension 

# This is specified here since unzip is used in this spec file.
BuildRequires: compress/unzip

# owner:hawklu date:2011-01-30 type:bug bugster:7015869
Patch1:  sqlite3tcl-01-using-LD.diff

URL:          http://www.sqlite.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}
Autoreqprov:  on

%description
SQLite is a software library that implements a self-contained, 
serverless, zero-configuration, transactional SQL database engine. 
SQLite is the most widely deployed SQL database engine in the world. 

%prep
cp -r sqlite-autoconf-%{tarball_version} %{name}-%{tarball_version}
cd %{name}-%{tarball_version}/tea

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

export PATH=`pwd`:$PATH

%if %option_with_debug
 export CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS -DSQLITE_SECURE_DELETE -DSQLITE_ENABLE_FTS3 -DUSE_PREAD -DHAVE_USLEEP -DHAVE_FDATASYNC -DHAVE_STATVFS -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_ENABLE_STAT2 -DSQLITE_MAX_SCHEMA_RETRY=25 -DSQLITE_DEFAULT_PAGE_SIZE=32768 -DSQLITE_MAX_DEFAULT_PAGE_SIZE=32768 -I. "
%else
 export CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS -DNDEBUG -DSQLITE_SECURE_DELETE -DSQLITE_ENABLE_FTS3 -DUSE_PREAD -DHAVE_USLEEP -DHAVE_FDATASYNC -DHAVE_STATVFS -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_ENABLE_STAT2 -DSQLITE_MAX_SCHEMA_RETRY=25 -DSQLITE_DEFAULT_PAGE_SIZE=32768 -DSQLITE_MAX_DEFAULT_PAGE_SIZE=32768 -I. "
%endif

export LDFLAGS="%_ldflags -Bdirect"
cd %{name}-%{tarball_version}/tea
./configure \
    --prefix=%{_prefix} \
    --exec_prefix=%{_prefix} \
    --libdir=%{_libdir}/tcl8.4/ \
    --bindir=%{_bindir} \
    --enable-shared  \
    --with-tcl="/usr/lib"

make -j $CPUS

%install
cd %{name}-%{tarball_version}/tea
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_mandir}/mann

%clean
rm -rf $RPM_BUILD_ROOT

%files

%changelog
* Fri Mar 23 2012 - ginn.chen@oracle.com
- Bump to 3.7.11. Add -DSQLITE_MAX_SCHEMA_RETRY=25 -DSQLITE_DEFAULT_PAGE_SIZE=32768 -DSQLITE_MAX_DEFAULT_PAGE_SIZE=32768
* Tue May 31 2011 - ginn.chen@oracle.com
- Bump to 3.7.6.3.
* Mon Apr 18 2011 - ginn.chen@oracle.com
- Enable SQLITE_ENABLE_STAT2.
* Fri Apr 15 2011 - ginn.chen@oracle.com
- Bump to 3.7.6.1
* Mon Jan 31 2011 - brian.lu@oracle.com
- initial version of the spec file.
