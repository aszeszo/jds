#
# spec file for package clutter-gst
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%define OSR 12686:0.8.0

Summary:      clutter-gst - gstreamer integration library for clutter
Name:         clutter-gst
Version:      1.2.0
Release:      1
License:      LGPLv2.1
Group:        System/Libraries
Distribution: Java Desktop System
Vendor:       clutter-project.org
Source:	      http://www.clutter-project.org/sources/clutter-gst/1.2/clutter-gst-%{version}.tar.bz2
URL:          http://www.clutter-project.org/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n clutter-gst-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

./configure --prefix=%{_prefix}         \
            --libexecdir=%{_libexecdir} \
            --sysconfdir=%{_sysconfdir} \
            %{gtk_doc_option}           \
%if %debug_build
            --enable-debug=yes          \
%else
            --enable-debug=no           \
%endif


make -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
#Clean up unpackaged files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*

%changelog
* Fri Oct 22 2010 - brian.cameron@oracle.com
- bump to 1.2.0.
* Fri Mar 26 2010 lin.ma@sun.com
- Revert to 1.0.0
* Mon Mar 08 2010 halton.huo@sun.com
- Revert to 0.10.0, hold bumping until new OSR filed.
* Wed Mar 03 2010  halton.huo@sun.com
- Bump to 1.0.0
- Remove clutter-gst-01-build.diff, not needed.
- Remove uncompatible m4 files
* Tue Feb 23 2010  christian.kelly@sun.com
- Add clutter-gst-01-build.diff, fix build issue.
* Tue Aug 25 2009  lin.ma@sun.com
- Bump to 0.10.0
* Fri Jun 26 2009  chris.wang@sun.com
- Change owner to lin
* Tue Jul  1 2008  chris.wang@sun.com
- Initial build.
