#
# spec file for package java-atk-wrapper
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:         java-atk-wrapper
License:      LGPL v2.1
Group:        System/Libraries/GNOME
Version:      0.30.4
Release:      1
URL:          http://live.gnome.org/Accessibility/JavaATKWrapper
Distribution: Java Desktop System
Vendor:       Gnome Community
Summary:      A wrapper of ATK Bridge for Java Swing apps.
Source:       http://ftp.gnome.org/pub/GNOME/sources/java-atk-wrapper/0.30/%{name}-%{version}.tar.bz2
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
# date:2010-05-28 owner:wangke type:bug doo:15964
Patch1:       java-atk-wrapper-01-custom-g-main-context.diff

%define glib2_version 2.5.7
%define atk_version 1.4.0
%define at_spi_version 1.1.8
%define at_spi_release 1

BuildRequires: atk-devel >= %{atk_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: at-spi-devel >= %{at_spi_version}-%{at_spi_release}
Requires:      atk >= %{atk_version}
Requires:      glib2 >= %{glib2_version}
Requires:      at-spi >= %{at_spi_version}

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%build
#aclocal
#autoconf
#automake -a -c -f
autoreconf --install --force
CFLAGS="%optflags"
LDFLAGS="%{_ldflags}"
%define java_home /usr/java
./configure --prefix=%{_prefix} \
	    --libdir=%{_libdir} \
            JAVA_HOME=%{java_home}

cd jni
make
%if %build_java
cd ../wrapper
make
%endif

%install
cd jni
make install DESTDIR=$RPM_BUILD_ROOT
%if %build_java
cd ../wrapper
make install DESTDIR=$RPM_BUILD_ROOT
%endif
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Nov 10 2010 - kerr.wang@oracle.com
- Bump to 0.30.4.
* Mon Nov  8 2010 - kerr.wang@oracle.com
- Bump to 0.30.3.
* Tue Oct 20 2010 - kerr.wang@oracle.com
- Bump to 0.30.2.
* Fri May 28 2010 - ke.wang@sun.com
- Bump to 0.30.1.
* Fri May 28 2010 - ke.wang@sun.com
- Add java-atk-wrapper-01-custom-g-main-context.diff to fix doo 15964.
* Mon Apr 26 2010 - christian.kelly@oracle.com
- Bump to 0.30.0.
* Thu Mar 11 2010 - christian.kelly@sun.com
- Bump to 0.29.5.
* Mon Mar  1 2010 - christian.kelly@sun.com
- Bump to 0.29.4.
* Mon Feb  1 2010 - christian.kelly@sun.com
- Bump to 0.29.3.
* Mon Jan 18 2010 - christian.kelly@sun.com
- Bump to 0.29.2.
* Fri Nov 27, 2009 - ke.wang@sun.com
- Bump to 0.29.1
* Thu Sep 24, 2009 - ke.wang@sun.com
- Bump to 0.28.0
* Sun Aug 16, 2009 - ke.wang@sun.com
- Bump to 0.27.7
* Thu Aug 06, 2009 - ke.wang@sun.com
- Bump to 0.27.6
* Wed Jul 29, 2009 - ke.wang@sun.com
- Bump to 0.27.5
* Thu Jul 16, 2009 - ke.wang@sun.com
- Bump to 0.27.4
* Mon Jul 06, 2009 - ke.wang@sun.com
- Remove dependency on gtk2
* Mon Jul 06, 2009 - ke.wang@sun.com
- Initial spec.
