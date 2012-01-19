#
# spec file for packages SUNWlibgsf
#
# includes module(s): libgsf
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner hawklu
%define pythonver %{default_python_version}

%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libgsf_64 = libgsf.spec
%endif

%include base.inc
%use libgsf = libgsf.spec

Name:                    SUNWlibgsf
IPS_package_name:        library/desktop/libgsf
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GNOME Structured File Library
Version:                 %{libgsf.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 GNU General Public License Version 2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include gnome-incorporation.inc
Requires: SUNWlxmlr
Requires: SUNWglib2
Requires: SUNWlibgsf-root
Requires: SUNWgnome-component
Requires: SUNWgnome-vfs
Requires: SUNWgnome-config
Requires: SUNWlxml
Requires: SUNWbzip
Requires: SUNWzlib
Requires: SUNWlibms
Requires: SUNWpygobject26
Requires: SUNWpygtk2-26
Requires: SUNWdesktop-cache
BuildRequires: SUNWglib2-devel
BuildRequires: SUNWlibm
BuildRequires: SUNWgnome-component-devel
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWlxml-devel
BuildRequires: SUNWpygobject26-devel
BuildRequires: SUNWpygtk2-26-devel
BuildRequires: SUNWpython26-setuptools

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include gnome-incorporation.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                %{name}
Requires:                SUNWglib2-devel
Requires:                SUNWlxml-devel
Requires:                SUNWgnome-component-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libgsf_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%libgsf.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build

export PYTHON="/usr/bin/python%{default_python_version}"

%ifarch amd64 sparcv9
if [ "x`basename $CC`" != xgcc ]
then
  FLAG64="-xarch=generic64"
else
  FLAG64="-m64"
fi

export LDFLAGS="$FLAG64"
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
%libgsf_64.build -d %name-%version/%_arch64
%endif

export LDFLAGS="%_ldflags"
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
%libgsf.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libgsf_64.install -d %name-%version/%_arch64
%endif

%libgsf.install -d %name-%version/%{base_arch}

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%attr (-, root, bin) %{_libdir}/python*
%dir %attr (0755, root, sys) %{_datadir}
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/*
%{_mandir}/man3/*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/gsf-office-thumbnailer.schemas

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/libgsf-1
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc
%ifarch amd64 sparcv9
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%doc -d %{base_arch}/libgsf-%{libgsf.version} AUTHORS ChangeLog NEWS README
%doc(bzip2) -d %{base_arch}/libgsf-%{libgsf.version} COPYING COPYING.LIB
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Mon Dec 06 2010 - brian.cameron@oracle.com
- Now use default_python_version.
* Mon Nov 08 2010 - brian.lu@oracle.com
- Add 'License' tag
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 24 2009 - jeff.cai@sun.com
- Since /usr/lib/amd64/pkgconfig/libgsf-1.pc (SUNWlibgsf-devel) requires
  /usr/lib/amd64/pkgconfig/glib-2.0.pc which is found in
  SUNWgnome-base-libs-devel, add the dependency.
- Since /usr/lib/amd64/pkgconfig/libgsf-1.pc (SUNWlibgsf-devel) requires
  /usr/lib/amd64/pkgconfig/gobject-2.0.pc which is found in
  SUNWgnome-base-libs-devel, add the dependency.
- Since /usr/lib/amd64/pkgconfig/libgsf-1.pc (SUNWlibgsf-devel) requires
  /usr/lib/amd64/pkgconfig/libxml-2.0.pc which is found in
  SUNWlxml-devel, add the dependency.
- Since /usr/lib/amd64/pkgconfig/libgsf-gnome-1.pc (SUNWlibgsf-devel) requires
  /usr/lib/amd64/pkgconfig/libbonobo-2.0.pc which is found in
  SUNWgnome-component-devel, add the dependency.
* Wed Mar 11 2009 - dave.lin@sun.com
- Add %{_datadir}/man/man3 in %files
* Fri Sep 19 2008 - rick.ju@sun.com
- Add %doc for copyright files and fix an install issue.
* Wed Sep 17 2008 - rick.ju@sun.com
- Use gio and support 64bit build
* Tue Sep 02 2008 - halton.huo@sun.com
- Remove useless /usr/sfw stuff to CFLAGS and LDFLAGS
- Add /usr/share/aclocal to ACLOCAL_FLAGS to fix build issue
* Fri Aug 08 2008 - dave.lin@sun.com
- Correct the dependency as below to fix the integration issues(CR6734966)
    Requires: SUNWlibms, BuildRequires: SUNWlibm
* Mon Apr 14 2008 - halton.huo@sun.com
- Spilit from SUNWdesktop-search-libs.spec

