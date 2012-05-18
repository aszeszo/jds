#
# spec file for package SUNWgnome-themes-standard
#
# includes module(s): gnome-themes-standard
#
# Copyright (c) 2011,2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi

%include Solaris.inc

Name:                    SUNWgnome-themes-standard
IPS_package_name:        gnome/theme/gnome-icon-theme-standard
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 Standard GNOME themes
Version:                 3.4.2
License:                 LGPL v2.1
Source:			 http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-standard/3.4/gnome-themes-standard-%{version}.tar.xz
# date:2011-07-14 owner:yippi type:bug bugzilla:654714
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

%if %build_l10n
%package l10n
IPS_package_name:        gnome/theme/gnome-icon-theme-standard/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                %{name}
%endif

%prep
%setup -q -n gnome-themes-standard-%version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

./configure --prefix=%{_prefix}		\
	    --bindir=%{_bindir}		\
            --libdir=%{_libdir}		\
            --includedir=%{_includedir}	\
	    --mandir=%{_mandir}		\
	    %{gtk_doc_option}		\
	    --disable-static

gmake -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT
gmake install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%if %{!?_without_gtk_doc:0}%{?_without_gtk_doc:1}
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc
%endif

# Do not install generated files.
rm -fr $RPM_BUILD_ROOT{%_datadir}/hicolor

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc COPYING ChangeLog NEWS README
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/gtk-3.0
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gnome-background-properties
%dir %attr (-, root, other) %{_datadir}/icons
%{_datadir}/icons/Adwaita
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrast/*/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/HighContrastInverse/*/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/LowContrast
%dir %attr (0755, root, other) %{_datadir}/icons/LowContrast/*
%dir %attr (0755, root, other) %{_datadir}/icons/LowContrast/*/*
%dir %attr (0755, root, other) %{_datadir}/icons/LowContrast/*/*/*
%{_datadir}/themes
%dir %attr (0755, root, other) %{_docdir}

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Thu May 17 2012 - brian.cameron@oracle.com
- Bump to 3.4.2.
* Fri May 04 2012 - brian.cameron@oracle.com
- Bump to 3.4.1.
* Wed Oct 19 2011 - brian.cameron@oracle.com
- Bump to 3.2.1.
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 3.2.0.
* Tue Sep 13 2011 - brian.cameron@oracle.com
- Bump to 3.1.91.
* Thu Aug 18 2011 - brian.cameorn@oracle.com
- Bump to 3.1.5.
* Sat Aug 06 2011 - brian.cameron@oracle.com
- Bump to 3.1.4.
* Thu Jul 07 2011 - brian.cameron@oracle.com
- Created with 3.1.3.
