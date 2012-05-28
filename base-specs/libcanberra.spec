#
# spec file for package libcanberra
#
# includes module(s): libcanberra
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: bugzilla.freedesktop.org
#

%define OSR 9780:0.6

Name:                    libcanberra
License:                 LGPL v2.1
Group:                   Libraries/Multimedia
Version:                 0.26
Distribution:            Java Desktop System
Vendor:                  0pointer.de
Summary:                 Event Sound API Using XDG Sound Theming Specification
Source:                  http://0pointer.de/lennart/projects/libcanberra/libcanberra-%{version}.tar.gz
# This patch is needed until autoconf is updated to 2.63 and libtool to 2.2.
#owner:yippi date:2008-09-02 type:branding 
Patch1:                  libcanberra-01-solaris.diff
#owner:yippi date:2010-09-24 type:bug doo:16974 
Patch2:                  libcanberra-02-device.diff
URL:                     http://0pointer.de/blog/projects/sixfold-announcement.html
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

Requires:                SUNWgnome-config
BuildRequires:           SUNWgnome-config-devel

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
Requires: %name

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 
%patch2 -p1 

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export LDFLAGS="%{_ldflags}"

glib-gettextize -f
autoreconf --force --install

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir} --bindir=%{_bindir} \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --enable-gtk \
            --disable-static

make -j$CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Feb 09 2011 - brian.cameron@oracle.com
- Now call autoreconf.
* Mon Oct 04 2010 - brian.cameron@oracle.com
- Bump to 0.26.
* Tue Sep 14 2010 - brian.cameron@oracle.com
- Add patch libcanberra-02-device.diff so that libcanberra respects the
  device setting from gnome-volume-control.  This adds a dependency on
  GConf (SUNWgnome-config).
* Mon Jun 14 2010 - brian.cameron@oracle.com
- Bump to 0.25.
* Tue Apr 02 2010 - christian.kelly@oracle.com
- Set LDFLAGS, otherwise libs in /usr/lib are 64bit versions.
* Mon Apr 19 2010 - brian.cameron@oracle.com
- Bump to 0.24.
* Mon Mar 01 2010 - brian.cameron@sun.com
- Bump to 0.23.
* Mon Oct 19 2009 - brian.cameron@sun.com
- Bump to 0.22.
* Thu Oct 15 2009 - brian.cameron@sun.com
- Bump to 0.21.
* Wed Oct 14 2009 - brian.cameron@sun.com
- Bump to 0.20.
* Wed Oct 14 2009 - brian.cameron@sun.com
- Bump to 0.19.
* Mon Sep 21 2009 - brian.cameron@sun.com
- Bump to 0.18.
* Sun Sep 13 2009 - brian.cameron@sun.com
- Bump to 0.17.
* Thu Aug 27 2009 - brian.cameron@sun.com
- Bump to 0.16.
* Wed Aug 05 2009 - brian.cameron@sun.com
- Bump to 0.15.
* Fri Jul 24 2009 - ke.wang@sun.com
- Split from SUNWlibcanberra.spec to add 64-bit support
