#
# spec file for package json-c
#
# Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#

Name:		json-c
Summary:	JSON Implementation in C
Version:	0.9
License:        MIT
Source:		http://oss.metaparadigm.com/json-c/json-c-%{version}.tar.gz
Patch1:         json-c-01-compile.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n json-c-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

libtoolize --force
aclocal $ACLOCAL_FLAGS
automake -a -c -f

./configure --prefix=%{_prefix}         \
            --bindir=%{_bindir}         \
            --libdir=%{_libdir}         \
            --includedir=%{_includedir} \
            --mandir=%{_mandir}         \
            --disable-static

gmake -j $CPUS


%install
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a

%if %{!?_without_gtk_doc:0}%{?_without_gtk_doc:1}
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Feb 09 2012 - Brian Cameron
- Split from SUNWjson-c.spec and now build amd64.

