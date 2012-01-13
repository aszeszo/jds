#
# spec file for package SUNWgnome-ps-viewer
#
# includes module(s): <none>  (backcompat pkg with a symlink to evince)
#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc

%define OSR wrapper package, no content delivered:n/a

Name:                    SUNWgnome-ps-viewer
IPS_package_name:        gnome/ggv
Meta(info.classification): %{classification_prefix}:Applications/Office
Summary:                 GNOME PostScript document viewer (Obsolete)
Version:                 2.6.0
License:                 cr_Oracle
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWgnome-pdf-viewer
BuildRequires: consolidation/desktop/gnome-incorporation

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cd $RPM_BUILD_ROOT%{_bindir}
ln -s evince ggv
# mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
# cd $RPM_BUILD_ROOT%{_mandir}/man1
# ln -s evince.1 ggv.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*

%changelog
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Tue Feb 28 2006 - laca@sun.com
- add backcompat spec file (make ggv a symlink to evince)


