#
# spec file for package SUNWgtkperf
#
# includes module(s): gtkperf
#
# Copyright (c) 2005 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner dermot
#
%include Solaris.inc
%
%ifarch amd64 sparcv9
%include arch64.inc
%use gtkperf64 = gtkperf.spec
%endif

%include base.inc
%use gtkperf = gtkperf.spec

Name:                    SUNWgtkperf
IPS_package_name:        benchmark/gtkperf
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:                 Gtk+ performance testing application
Version:                 %{gtkperf.version}
SUNW_Copyright:          %{name}.copyright
License:                 %{gtkperf.license}
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWgtk2
Requires: SUNWlibms
BuildRequires: SUNWgtk2-devel

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%{_arch64}
%gtkperf64.prep -d %name-%version/%{_arch64}
%endif

mkdir %name-%version/%{base_arch}
%gtkperf.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
export CFLAGS="%optflags64"
export LDFLAGS="%_ldflags"
%gtkperf64.build -d %name-%version/%{_arch64}
%endif

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
%gtkperf.build -d %name-%version/%{base_arch}

%install
%ifarch amd64 sparcv9
%gtkperf64.install -d %name-%version/%{_arch64}
%endif

%gtkperf.install -d %name-%version/%{base_arch}
# Delete the unneeded README/COPYING etc files.
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gtkperf
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/gtkperf
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*

%changelog
* Thu Jan 07 2010 - jedy.wang@sun.com
- Add 64-bit support.
* Fri Sep 11 2009 - jedy.wang@sun.com
- Remove SUNWmlib dependency.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Mon Feb 20 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Mon Oct 21 2005 - damien.carbery@sun.com
- Initial spec file created.



