#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%define owner Herch

%include Solaris.inc

%define OSR 9526:3.3.2

Name:                SUNWswt
IPS_package_name:    library/java/swt
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:             Standard Widget Toolkit
License:             EPL v1.0 (Eclipse Public License)
Version:             3.3.2
Source:              http://www.mirrorservice.org/sites/download.eclipse.org/eclipseMirror/eclipse/downloads/drops/R-%{version}-200802211800/swt-%{version}-gtk-solaris-sparc.zip

SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:      %{name}.copyright
%include default-depend.inc
%include desktop-incorporation.inc

Requires: SUNWgtk2
Requires: SUNWgnome-libs
Requires: SUNWgnome-vfs 
Requires: SUNWpng
Requires: SUNWgnome-keyring
Requires: SUNWlibgnome-keyring
BuildRequires: SUNWxwrtl
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWpng-devel
BuildRequires: SUNWcairomm        
BuildRequires: SUNWxwinc
BuildRequires: SUNWgnome-common-devel
BuildRequires: SUNWunzip
BuildRequires: SUNWj6dev

%prep

%setup -q -c -n swt-%version
unzip -o src.zip

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"
export CXXFLAGS="%cxx_optflags"

make -j$CPUS -f make_solaris.mak JAVA_HOME=/usr/java make_swt make_atk make_awt  make_cairo make_gnome

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/swt
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/lib/java
cp *.so $RPM_BUILD_ROOT/%{_libdir}/swt
cp *.jar $RPM_BUILD_ROOT/%{_datadir}/lib/java

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, sys) %{_libdir}/swt
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, sys) %{_datadir}/lib
%dir %attr (0755, root, sys) %{_datadir}/lib/java
%{_libdir}/swt/*
%{_datadir}/lib/java/*
%doc(bzip2) about.html
%doc(bzip2) about_files/IJG_README
%doc(bzip2) about_files/lgpl-v21.txt
%doc(bzip2) about_files/mpl-v11.txt
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Mon Oct 06 2008 - dermot.mccluskey@sun.com
- Add copyright files
* Fri Oct 03 2008 - christian.kelly@sun.com
- Add empty copyright to allow spec to build.
* Fri Jun 25 2008 - harshal.patil@sun.com
- rename SFEswt to SUNWswt
- add BuildRequires section
- removed Dt dependacy from make 
- add Requires section
- add %{_datadir}/lib/java in %files
* Fri Jun 20 2008 - river@wikimedia.org
- Initial spec.



