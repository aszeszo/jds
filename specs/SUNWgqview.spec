#
#
# spec file for package SUNWgqview
#
# includes module(s): gqview
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby

%include Solaris.inc
%use gqview = gqview.spec
Name:                    SUNWgqview
IPS_package_name:        image/viewer/gqview
Meta(info.classification): %{classification_prefix}:Applications/Graphics and Imaging
Summary:                 GQview - Image browser
URL:                     http://gqview.sourceforge.net/
Version:                 %{gqview.version}
Source:                  http://prdownloads.sourceforge.net/gqview/gqview-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:		 SUNWgqview.copyright
License:  		 GPL v2, Public Domain
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWuiu8
Requires: SUNWgtk2
Requires: SUNWlcms
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWgnome-common-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%gqview.prep -d %name-%version

%build
export CFLAGS="%optflags -DEDITOR_GIMP"
export LDFLAGS="-lX11 -lsocket"
%gqview.build -d %name-%version

%install
%gqview.install -d %name-%version
if [ -d $RPM_BUILD_ROOT/%{_libdir}/locale ]; then
  mv $RPM_BUILD_ROOT/%{_libdir}/locale $RPM_BUILD_ROOT/%{_datadir}/
  rm -r  $RPM_BUILD_ROOT/%{_libdir}
fi
mv $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN.GB2312 $RPM_BUILD_ROOT%{_datadir}/locale/zh_CN 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d gqview-%{gqview.version} README AUTHORS
%doc(bzip2) -d gqview-%{gqview.version} COPYING ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/doc/gqview-%{gqview.version}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man*/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wen Oct 14 2009 - yuntong.jin@sun.com
- add dependence SUNWlcms to fix CR 6886498 
* Fri Jun 26 2009 - chris.wang@sun.com
- Change owner jouby
* Tue Jun 02 2009 - dave.lin@sun.com
- fixed dependency issue(CR6843581).
- removed the obsoleted option %option_with_gnu_iconv.
* Mon Sep 16 2008 - chris.wang@sun.com
- Revised copyright file
* Wed Aug 21 2008 - chris.wang@sun.com
- Move #6734879's fix to Solaris spec from base spec
* Wed Jul 23 2008 - damien.carbery@sun.com
- Check that installed dirs exist before removing or moving them.

* Wed Jul 23 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-base-libs/-devel because gtk+ is required. Also
  add BuildRequires SUNWgnome-common-devel because pkg-config is used by
  configure.

* Tue Jul  7 2008 - chris.wang@sun.com 
- Initial build.



