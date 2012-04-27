#
# spec file for package SUNWsexy-python.spec
#
# Copyright 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#

%define OSR 10058:0.11.1

####################################################################
# sexy-python is a set of Python bindings around libsexy
####################################################################

%include Solaris.inc

Name:                    SUNWsexy-python
IPS_package_name:        library/python-2/python-sexy-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                 Python bindings around libsexy
License:                 LGPL v2.1
Version:                 0.1.9
Source:			 http://releases.chipx86.com/libsexy/sexy-python/sexy-python-%{version}.tar.gz
Patch1:			 sexy-python-01-solaris-port.diff
URL:			 http://www.chipx86.com/wiki/Libsexy
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright

%ifnarch sparc
# these packages are only avavilable on x86
# =========================================

BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgtk2
Requires: SUNWlibsexy
Requires: SUNWpygtk2-26
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWpygtk2-26-devel
BuildRequires: SUNWlibsexy
BuildRequires: library/python-2/setuptools-26
BuildRequires: SUNWbtool
BuildRequires: SUNWgnome-common-devel

%package -n SUNWsexy-python24
IPS_Package_Name: library/python-2/python-sexy-24
IPS_component_version: 0.1.9
IPS_build_version: 5.11
IPS_vendor_version: 0.175.0.0.0.1.0
IPS_legacy: false
Meta(pkg.renamed): true
Meta(org.opensolaris.consolidation): desktop
Meta(variant.opensolaris.zone): global, nonglobal
Obsoleted_By: library/python-2/python-sexy-26 >= 0.1.9-0.151
Obsoleted_By: consolidation/desktop/desktop-incorporation = *
PkgBuild_Make_Empty_Package: true

%define pythonver 2.6

%prep
%setup -q -n sexy-python-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%{_ldflags}"
export MSGFMT="/usr/bin/msgfmt"

./configure --prefix=%{_prefix}			\
	    --bindir=%{_bindir}			\
	    --sysconfdir=%{_sysconfdir}		\
	    --includedir=%{_includedir}		\
	    --mandir=%{_mandir}			\
            --libdir=%{_libdir}

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/*.la

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/pygtk/*
%doc AUTHORS NEWS README
%doc(bzip2) COPYING ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

# endif for "ifnarch sparc"
%endif

%changelog
* Wed Sep 17 2008 - matt.keenn@sun.com
- Update copyright
* Wed Mar 26 2008 - dave.lin@sun.com
- change to not build this component on SPARC
* Tue Mar 18 2008 - damien.carbery@sun.com
- Add Build/Requires for SUNWgnome-python-libs.
* Wed Feb 13 2008 - erwann@sun.com
- Moved to SFO
* Sat Sep 08 2007 - trisk@acm.jhu.edu
- Fix rules, update Python library dir
* Fri Aug  24 2007 - erwann@sun.com
- Initial spec



