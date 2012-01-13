#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner ginnchen
# bugdb: bugzilla.freedesktop.org
#

%define OSR 12578:1.0.2
%define doc_version 3070600
%define tarball_version 3070603

Name:         sqlite 
License:      public domain 
Group:        System/Libraries
Version:      3.7.6.3
Release:      1
Distribution: Java Desktop System
Vendor:	      www.sqlite.org
Summary:      SQL database engine 
Source:       http://www.sqlite.org/%{name}-autoconf-%{tarball_version}.tar.gz
Source1:      mapfile-libsqlite3
Source2:      http://www.sqlite.org/%{name}-doc-%{doc_version}.zip
Source3:      pkgIndex.tcl 
# This is specified here since unzip is used in this spec file.
BuildRequires: compress/unzip

# owner:hawklu date:2008-10-10 type:bug bugster:?? 
Patch1: sqlite3-01-using-mapfile.diff

# owner:ginnchen date:2011-03-29 type:bug d.o.o 15412 bugster:7031954
Patch2: sqlite3-02-using-libcurses.diff

# owner:ginnchen date:2011-06-08
Patch3: sqlite3-03-posix_fallocate64.diff

URL:          http://www.sqlite.org
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}
Autoreqprov:  on

%description
SQLite is a software library that implements a self-contained, 
serverless, zero-configuration, transactional SQL database engine. 
SQLite is the most widely deployed SQL database engine in the world. 

%package devel
Summary:      SQL database engine library
Group:        Development/Libraries
Requires:     %{name} = %{version}

%description devel
SQLite is a software library that implements a self-contained, 
serverless, zero-configuration, transactional SQL database engine. 
SQLite is the most widely deployed SQL database engine in the world. 

%prep
%setup -q -n %{name}-autoconf-%{tarball_version}

%patch1 -p1
%patch2 -p1
%patch3 -p1

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

cp %{SOURCE1} .

%if %option_with_debug
 export CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS -DSQLITE_SECURE_DELETE -DSQLITE_ENABLE_FTS3 -DUSE_PREAD -DHAVE_USLEEP -DHAVE_FDATASYNC -DHAVE_STATVFS -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_ENABLE_STAT2 -I. "
%else
 export CFLAGS="%optflags -D_POSIX_PTHREAD_SEMANTICS -DNDEBUG -DSQLITE_SECURE_DELETE -DSQLITE_ENABLE_FTS3 -DUSE_PREAD -DHAVE_USLEEP -DHAVE_FDATASYNC -DHAVE_STATVFS -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_ENABLE_STAT2 -I. "
%endif

export LD=/usr/bin/ld
export LDFLAGS="%_ldflags -Bdirect"
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --bindir=%{_bindir} \
    --mandir=%{_mandir} \
    --enable-threadsafe \
    --enable-cross-thread-connections \
    --enable-load-extension \
    --enable-shared  \
    --disable-static \
    --with-tcl="/usr/lib"

make -j $CPUS


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

# install docs
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc
cd $RPM_BUILD_ROOT%{_datadir}/doc
unzip %{SOURCE2}
mv %{name}-doc-%{doc_version} sqlite3 


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Wed Jul 13 2011 - ginn.chen@oracle.com
- Fix manpage.
* Wed Jun 08 2011 - ginn.chen@oracle.com
- Add sqlite3-03-posix_fallocate64.diff, fix 32bit library building on snv_166.
* Tue May 31 2011 - ginn.chen@oracle.com
- Bump to 3.7.6.3.
* Mon Apr 18 2011 - ginn.chen@oracle.com
- Enable SQLITE_ENABLE_STAT2.
* Fri Apr 15 2011 - ginn.chen@oracle.com
- Bump to 3.7.6.1.
* Tue Mar 29 2011 - ginn.chen@oracle.com
- Update sqlite3-02-using-libcurses.diff to fix CR #7031954.
* Fri Mar 18 2011 - brian.lu@oracle.com
- Fix bug CR #7026620
* Thu Oct 21 2010 - brian.lu@sun.com
- Bump to 3.7.3
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Wed Jun 02 2010 - brian.cameron@oracle.com
- Bump to 3.6.23.
* Mon Apr 06 2010 - brian.lu@sun.com
- Fix bug d.o.o 15412.
* Tue Mar 02 2010 - brian.lu@sun.com
- Change license to public domain.
* Fri Jan 15 2010 - brian.lu@sun.com
- initial version of the spec file.
