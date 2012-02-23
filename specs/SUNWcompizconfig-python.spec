#
# spec file for package SUNWcompizconfig-python
####################################################################
# Python bindings for the compizconfig library
####################################################################
#
# Copyright (c) 2006, 2012, Oracle and/or its affiliates. All rights reserved.`
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc


%include Solaris.inc

%define OSR 8297:1.6.2

%define src_name compizconfig-python

Name:                    SUNWcompizconfig-python
IPS_package_name:        library/python-2/python-compizconfig-26
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 compizconfig libraries - is an alternative configuration system for compiz
License:                 GPL v2
Version:                 0.8.4
Source:			 http://releases.compiz-fusion.org/%{version}/%{src_name}-%{version}.tar.bz2
Patch1:			 compizconfig-python-2.6.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright

%ifnarch sparc
# these packages are only avavilable on x86
# =========================================

BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
# add build and runtime dependencies here:
BuildRequires:  runtime/python-26
BuildRequires:  desktop/compiz/library/libcompizconfig
BuildRequires:  library/python-2/setuptools-26
BuildRequires:  desktop/compiz
BuildRequires:  library/python-2/python-extra-26
Requires:       runtime/python-26
Requires:       desktop/compiz/library/libcompizconfig
BuildRequires:  consolidation/desktop/gnome-incorporation

%package devel
Summary:		 %{summary} - development files
SUNW_BaseDir:            %{_basedir}

%define pythonver 2.6

%prep
%setup -q -n %{src_name}-%version
%patch1 -p1


%build
export PYTHON=/usr/bin/python%{pythonver}

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%{_ldflags}"
export MSGFMT="/usr/bin/msgfmt"

aclocal
autoheader
automake -a -c -f
autoconf
libtoolize --force

./configure --prefix=%{_prefix}			\
	    --bindir=%{_bindir}			\
	    --sysconfdir=%{_sysconfdir}		\
	    --includedir=%{_includedir}		\
            --libdir=%{_libdir}

make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rm -Rf $RPM_BUILD_ROOT%{_libdir}/python*.*/site-packages
#rmdir $RPM_BUILD_ROOT%{_libdir}/python2.5

rm -f $RPM_BUILD_ROOT%{_libdir}/*.*a
rm -f $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/*.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/*
%doc(bzip2) COPYING
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

# endif for "ifnarch sparc"
%endif

%changelog
* Mon Feb 13 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Wed Sep 17 2008 - matt.keenn@sun.com
- Update copyright
* Wed Mar 26 2008 - dave.lin@sun.com
- change to not build this component on SPARC
* Wed Feb 13 2008 - erwann@sun.com
- Moved to SFO
* Wed Nov 14 2007 - daymobrew@users.sourceforge.net
- Add l10n package.
* Mon Oct 29 2007 - trisk@acm.jhu.edu
- Bump to 0.6.0.1
* Fri Sep 07 2007 - trisk@acm.jhu.edu
- Update rules, fix Python library location
* Fri Aug  14 2007 - erwann@sun.com
- Initial spec


