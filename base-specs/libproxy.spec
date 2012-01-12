#
# spec file for package libproxy
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
# bugdb: http://code.google.com/p/libproxy/issues/detail?id=
#

%define OSR 10998:0.x

%if %opt_arch64
%define _demodir %{_prefix}/demo/jds/bin/%{_arch64}
%else
%define _demodir %{_prefix}/demo/jds/bin
%endif

Name:         libproxy
License:      LGPL v2.1
Group:        System/Libraries/GNOME
Version:      0.3.1
Release:      1
URL:          http://code.google.com/p/libproxy/
Distribution: Java Desktop System
Vendor:       Google Code
Summary:      Libproxy is a library that provides automatic proxy configuration management
Source:       http://libproxy.googlecode.com/files/libproxy-%{version}.tar.bz2
#owner:wangke date:2009-09-11 type:branding
Patch1:       libproxy-01-build.diff
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%package devel
Summary:      %{summary} - development files	
Requires:     %{name} = %{version}

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%build
libtoolize --force
aclocal
autoconf
automake -a -c -f
export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"
export MOZJS_CFLAGS="%optflags"
export MOZJS_LIBS="%{_ldflags}"

./configure --prefix=%{_prefix}			 \
	    --libdir=%{_libdir}			 \
	    --bindir=%{_bindir}			 \
            --includedir=%{_includedir}/libproxy \
            --sysconfdir=%{_sysconfdir}		 \
	    --mandir=%{_mandir}			 \
	    --libexecdir=%{_libexecdir}		 \
            --without-kde	                 \
%if %build_module_gnome
            --with-gnome                         \
            --without-mozjs                      \
            --without-dotnet                     \
            --without-direct                     \
            --without-envvar                     \
            --without-file                       \
            --without-wpad                       \
            --without-networkmanager             \
            --without-webkit                     \
            --without-python
%else
%if %build_module_mozjs
            --without-gnome                      \
            --without-dotnet                     \
            --without-direct                     \
            --without-envvar                     \
            --without-file                       \
            --without-wpad                       \
            --without-networkmanager             \
            --without-webkit                     \
            --without-python
%else
            --without-dotnet                     \
            --without-gnome                      \
            --without-mozjs
%endif
%endif

make \
    pyexecdir=%{_libdir}/python%{pythonver}/vendor-packages \
    pythondir=%{_libdir}/python%{pythonver}/vendor-packages

%install
make install DESTDIR=$RPM_BUILD_ROOT \
    pyexecdir=%{_libdir}/python%{pythonver}/vendor-packages \
    pythondir=%{_libdir}/python%{pythonver}/vendor-packages

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%if %build_module_gnome
%else
%if %build_module_mozjs
%else
install -d $RPM_BUILD_ROOT%{_demodir}
mv $RPM_BUILD_ROOT%{_bindir}/* $RPM_BUILD_ROOT%{_demodir}
%endif
%endif
rm -r $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Dec 17 2009 - ke.wang@sun.com
- Separated into three packages: SUNWlibproxy, SUNWlibproxy-gnome
  and SUNWlibproxy-mozjs
* Fri Oct 16 2009 - ke.wang@sun.com
- Bump to 0.3.1
* Fri Sep 11 2009 - ke.wang@sun.com
- Bump to 0.3.0
- Remove patch libproxy-01-orig-build.diff
- Remove patch libproxy-02-wpad-fallback.diff
- Remove patch libproxy-03-proxy-readline.diff
- Remove patch libproxy-05-config-posix.diff
- Add patch libproxy-01-build.diff
* Wed Mar 11 2009 - ke.wang@sun.com
- Mended bugdb
- Remove patch4 because the problem is fixed in Python26
* Tue Mar 10 2009 - ke.wang@sun.com
- Add patch5 to replace _GUN_SOURCE with _POSIX_C_SOURCE
* Mon Feb 23 2009 - ke.wang@sun.com
- make wpad-fallback be built by default, but not be check against
  user can use PX_CONFIG_ORDER to enable it
* Mon Feb 16 2009 - ke.wang@sun.com
- Add patch libproxy-04-py-find-lib.diff for python binding
* Fri Feb 13 2009 - takao.fujiwara@sun.com
- Add patch proxy-readline.diff to work proxy demo correctly.
* Mon Feb 2, 2009 - ke.wang@sun.com
- Initial spec.
