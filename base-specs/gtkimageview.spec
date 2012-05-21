#
# spec file for package gtkimageview
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jedy
# bugdb: http://trac.bjourne.webfactional.com/
#

%define OSR 13397:0.x

Name:         gtkimageview
Vendor:       trac.bjourne.webfactional.com
Version:      1.6.4
Release:      1
Summary:      A simple image viewer widget for GTK+.

Group:        System/Libraries
License:      LGPL
URL:          http://trac.bjourne.webfactional.com
Source:       http://trac.bjourne.webfactional.com/chrome/common/releases//%{name}-%{version}.tar.gz
# date:2010-02-10 owner:jedy type:bug bugid:39
Patch1:       gtkimageview-01-cflags.diff 
# date:2010-02-10 owner:jedy type:bug bugid:38
Patch2:       gtkimageview-02-void.diff 

BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%description
GtkImageView is a simple image viewer widget for GTK+.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%ifos linux
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

#aclocal $ACLOCAL_FLAGS
glib-gettextize --force --copy
intltoolize --force --automake
gtkdocize

#automake -a -f -c --gnu
#autoconf
autoreconf --install --force
./configure --prefix=%{_prefix} \
            --bindir=%{_bindir} \
            --libdir=%{_libdir} \
            --mandir=%{_mandir} \
            --enable-compile-warnings=no \
            %gtk_doc_option \
            --disable-static

make -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT


%changelog
* Tue Mar 02 2010 - jedy.wang@sun.com
- Update summary and description.
* Fri Jan 22 2010 - jedy.wang@sun.com
- Initial spec
