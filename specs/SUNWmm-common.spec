#
# spec file for package SUNWmm-common
# - set of mm macros for building C++ binding
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
 
%define OSR LFI#105446 (gnome Exec. summary):n/a

%include Solaris.inc

Name:                SUNWmm-common
# Since this is a private package and due to pkgbuild limitation of ++ in regular expression
IPS_package_name:    library/desktop/c++/mm-common
#IPS_package_name:    SUNWmm-common
License:             GPLv2
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:             GNOME C++ bindings effort http://www.gtkmm.org support tools
Version:             0.9.2
License:             GPL v2
Source:              http://ftp.acc.umu.se/pub/GNOME/sources/mm-common/0.9/mm-common-%{version}.tar.bz2
SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWbash
BuildRequires: runtime/perl-512

%prep
%setup -q -n mm-common-%{version}

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

./configure --prefix=%{_prefix}  \
            --bindir=%{_bindir} \
            --mandir=%{_mandir} 

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.gitignore' -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_bindir}
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%dir %attr (0755, root, other) %{_datadir}/aclocal/*
%dir %attr (0755, root, bin) %{_datadir}/pkgconfig
%dir %attr (0755, root, bin) %{_datadir}/pkgconfig/*
%{_mandir}
%dir %attr (0755, root, other) %{_datadir}/mm-common
%dir %attr (0755, root, other) %{_datadir}/mm-common/*
%dir %attr (0755, root, other) %{_datadir}/mm-common/*/*
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/mm-common/README
%{_datadir}/doc/mm-common/skeletonmm.tar.gz

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Mon Feb 15 2010 - christian.kelly@sun.com
- Bump to 0.9.2.
* Thu Oct 21 2009 - ghee.teo@sun.com
- Fixed some dependencies and also installation location.
* Fri Oct 02 2009 - ghee.teo@sun.com
- initial version


