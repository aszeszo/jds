#
# spec file for package SUNWgtk-vnc
#
# includes module(s): gtk-vnc
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%define with_64 1
%define with_browser_plugin 0
%define pythonver 2.6
%use gvnc_64_py26 = gtk-vnc.spec
%endif

%include base.inc
%define with_64 0
%define with_browser_plugin 1
%define pythonver 2.6
%use gvnc_py26 = gtk-vnc.spec

Name:               SUNWgtk-vnc
License:            LGPL v2.1, MIT, MPL 1.1
Summary:            gtk-vnc - A GTK widget for VNC clients
Version:            %{gvnc_py26.version}
SUNW_Pkg:           SUNWgtk-vnc
IPS_package_name:   library/desktop/gtk-vnc
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
SUNW_Copyright:     %{name}.copyright
SUNW_BaseDir:       %{_basedir}
BuildRoot:          %{_tmppath}/%{name}-%{version}-build
Source1:            %{name}-manpages-0.1.tar.gz

%include default-depend.inc
%include desktop-incorporation.inc
Requires:      SUNWgtk2
Requires:      SUNWgnutls
Requires:      SUNWzlibr
Requires:      SUNWlibsasl
BuildRequires: SUNWxwinc
BuildRequires: library/nspr
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWgnutls-devel
BuildRequires: SUNWfirefox-devel
BuildRequires: SUNWxwplt

%package devel
Summary:       %{summary} - development files
SUNW_BaseDir:  %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:      %{name}
Requires:      SUNWgtk2-devel
Requires:      SUNWgnutls-devel

%package python26
Summary:       %{summary} - Python 2.6 binding files
IPS_package_name: library/python-2/python-gtk-vnc-26
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
SUNW_BaseDir:  %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:      %{name}
Requires:      SUNWPython26
Requires:      SUNWpygtk2-26
BuildRequires: SUNWPython26-devel
BuildRequires: SUNWpython26-setuptools
BuildRequires: SUNWpygtk2-26-devel

%package l10n
Summary:       %{summary} - l10n files
Requires:      %{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%{_arch64}-py26
%gvnc_64_py26.prep -d %name-%version/%{_arch64}-py26
%endif

mkdir %name-%version/%{base_arch}-py26
%gvnc_py26.prep -d %name-%version/%{base_arch}-py26

cd %{_builddir}/%name-%version
gzcat %SOURCE1 | tar xf -

%build

%ifarch amd64 sparcv9
export LDFLAGS="$FLAG64"
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
%gvnc_64_py26.build -d %name-%version/%{_arch64}-py26
%endif

export LDFLAGS="%_ldflags"
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
%gvnc_py26.build -d %name-%version/%{base_arch}-py26

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%gvnc_64_py26.install -d %name-%version/%{_arch64}-py26
%endif

%gvnc_py26.install -d %name-%version/%{base_arch}-py26

# rename plugin dir to firefox
cd $RPM_BUILD_ROOT%{_libdir}
mv mozilla firefox

# remove empty bindir, refer to bugzilla #560112
rmdir $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
rmdir $RPM_BUILD_ROOT%{_bindir}

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d %{base_arch}-py26/gtk-vnc-%{gvnc_py26.version} README AUTHORS
%doc(bzip2) -d %{base_arch}-py26/gtk-vnc-%{gvnc_py26.version} COPYING.LIB ChangeLog NEWS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, bin) %{_libdir}/firefox
%dir %attr (0755, root, bin) %{_libdir}/firefox/plugins
%{_libdir}/firefox/plugins/gtk-vnc-plugin.so
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%files python26
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.6
%dir %attr (0755, root, bin) %{_libdir}/python2.6/vendor-packages
%{_libdir}/python2.6/vendor-packages/gtkvnc.so
%dir %attr (0755, root, bin) %{_libdir}/python2.6/vendor-packages/64
%{_libdir}/python2.6/vendor-packages/64/gtkvnc.so

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Mon Dec 06 2010 - brian.cameron@oracle.com
- Remove Python 2.4 bindings.
* Wed Jan 27 2010 - halton.huo@sun.com
- Add BuildRequires:SUNWfirefox-devel for the plugin
* Tue Nov 11 2009 - halton.huo@sun.com
- Add BuildRequires to SUNWxwinc and SUNWprd
* Thu Nov 05 2009 - halton.huo@sun.com
- Add pkg -python24 back because virt-manager still use it.
* Wed Oct 21 2009 - halton.huo@sun.com
- Add pkg -l10n
* Thu Oct 15 2009 - halton.huo@sun.com
- Add Requires: SUNWlibsasl
- Remove pkg -python24
* Tue Mar 24 2009 - jeff.cai@sun.com
- Since /usr/lib/amd64/pkgconfig/gtk-vnc-1.0.pc (SUNWgtk-vnc-devel) requires
  /usr/lib/amd64/pkgconfig/gtk+-2.0.pc which is found in
  SUNWgnome-base-libs-devel, add the dependency.
- Since /usr/lib/amd64/pkgconfig/gtk-vnc-1.0.pc (SUNWgtk-vnc-devel) requires
  /usr/lib/amd64/pkgconfig/gnutls.pc which is found in SUNWgnutls-devel,
  add the dependency.
* Wed Mar 18 2009 - halton.huo@sun.com
- Remove -python25 pkg
* Thu Feb 19 2009 - halton.huo@sun.com
- Add -python26 pkg
* Mon Dec 22 2008 - halton.huo@sun.com
- update deps after run check-deps.pl
* Wed Nov 26 2008 - halton.huo@sun.com
- Add -python25 pkg
- Add 64-bit gtkvnc python moudle
* Thu Nov 20 2008 - halton.huo@sun.com
- Remove -l10n pkg
* Thu Nov 13 2008 - halton.huo@sun.com
- Moved from SFE
- Enable 64-bit build
- Add package -python24
* Tue May 06 2008 - nonsea@users.sourceforge.net
- Remove ast stuff.
* Thu Oct 25 2007 - nonsea@users.sourceforge.net
- Initial spec

