#
# spec file for package SUNWccsm
####################################################################
# compizconfig-settings-manager(ccsm): A fully featured Python/GTK 
# based settings manager for the CompizConfig system.
####################################################################
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc

%include Solaris.inc

%define OSR 8297:1.6.2

%define src_name ccsm

Name:                    SUNWccsm
IPS_package_name:        desktop/compiz/ccsm
Meta(info.classification): %{classification_prefix}:Applications/Graphics and Imaging
Summary:                 ccsm settings manager for the CompizConfig system
License:                 GPL v2
Version:                 0.8.2
Source:			 http://releases.compiz-fusion.org/%{version}/%{src_name}-%{version}.tar.bz2	 
# owner:jedy date:2008-08-11 type:branding
Patch1:			 ccsm-01-desktop.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright

%ifnarch sparc
# these packages are only avavilable on x86
# =========================================

BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
# add build and runtime dependencies here:
BuildRequires:  SUNWpygtk2-26-devel
BuildRequires:  SUNWPython26
BuildRequires:  SUNWpython26-setuptools
BuildRequires:  SUNWcompizconfig-python
BuildRequires:  SUNWlibsexy
Requires:       SUNWdbus-python26
Requires:       SUNWpygtk2-26
Requires:       SUNWPython26
Requires:       SUNWcompizconfig-python
Requires:       SUNWlibsexy
Requires:       SUNWdesktop-cache
%include default-depend.inc
%include desktop-incorporation.inc

%define pythonver 2.6

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n %{src_name}-%version
%patch1 -p1

%build
python%{pythonver} setup.py build --prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
python%{pythonver} setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages

%post
%restart_fmri desktop-mime-cache mime-types-cache

%postun
%restart_fmri desktop-mime-cache mime-types-cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/ccsm
%{_datadir}/ccsm/*
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/ccsm.desktop
%attr (0755, root, other) %{_datadir}/icons

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale/*

# endif for "ifnarch sparc"
%endif

%changelog
* Thu Aug 13 2009 - christian.kelly@sun.com
- Bump to 0.8.2.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Aug 11 2008 - jedy.wang@sun.com
- Add 02-desktop.diff to hide the menu enty form the menu because it has
  been integrated into gnome-appearance-properties.
* Tue Jun 01 2008 - damien.carbery@sun.com
- Fix perms in %files.
* Wed Mar 26 2008 - dave.lin@sun.com
- change to not build this component on SPARC
* Fri Feb 22 2008 - takao.fujiwara@sun.com
- Add ccsm-01-po.diff to add cs.po, es.po, hu.po, ja.po, ko.po from HEAD.
* Wed Feb 13 2008 - erwann@sun.com
- Moved to SFO
* Wed Nov 14 2007 - daymobrew@users.sourceforge.net
- Add l10n package.
* Mon Oct 29 2007 - trisk@acm.jhu.edu
- Bump to 0.6.0
* Sat Sep 08 2007 - trisk@acm.jhu.edu
- Correct rules, remove -root, fix Python library location
* Fri Aug  14 2007 - erwann@sun.com
- Initial spec



