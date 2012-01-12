#
# spec file for package SUNWnautilus-sendto
#
# includes module(s): nautilus-sendto
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: padraig
#

%include Solaris.inc

%use nst = nautilus-sendto.spec

Name:               SUNWnautilus-sendto
Summary:            nautiluse-sendto - Nautilus context menu for sending files
Version:            %{nst.version}
SUNW_Pkg:           SUNWnautilus-sendto
IPS_package_name:   gnome/file-manager/nautilus/extension/nautilus-sendto
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/File Managers
SUNW_BaseDir:       %{_basedir}
SUNW_Copyright:     %{name}.copyright
License:            %{nst.license}
BuildRoot:          %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:      SUNWglib2
Requires:      SUNWgtk2
Requires:      SUNWdbus-glib
Requires:      SUNWgnome-config
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWdbus-glib-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-file-mgr-devel
Requires:      %{name}-root

%package l10n
Summary:       %{summary} - l10n files
Requires:      %{name}

%package root
Summary:       %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:        %{summary} - development files
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:       %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%nst.prep -d %name-%version

%build
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
%nst.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%nst.install -d %name-%version

# remove unused plugins
cd $RPM_BUILD_ROOT%{_libdir}/nautilus-sendto/plugins
rm libnstbluetooth.so
rm libnstburn.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d nautilus-sendto-%{nst.version} AUTHORS README
%doc(bzip2) -d nautilus-sendto-%{nst.version} COPYING NEWS
%doc(bzip2) -d nautilus-sendto-%{nst.version} ChangeLog ChangeLog.pre-1.1.4.1
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/nautilus-sendto
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/nautilus
%{_libdir}/nautilus-sendto
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/nautilus-sendto
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/nst.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %dir %{_datadir}
%{_datadir}/gtk-doc

%changelog
* Mon Feb 22 2010 - halton.huo@sun.com
- Unremove Gajim plugin according ARC review.
* Thu Feb 04 2010 - halton.huo@sun.com
- Remove unused plugins according ARC review.
* Wed Nov 18 2009 - halton.huo@sun.com
- Add -devel pkg
* Wed Aug 05 2009 - halton.huo@sun.com
- Initial spec


