#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%include Solaris.inc
%{?!python_version:%define python_version 2.6}

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:                pygtksourceview
Summary:             Python bindings for GtkSourceView 2
License:             LGPLv2
Vendor:              Gnome Community
Version:             2.10.1
Source:              http://ftp.gnome.org/pub/GNOME/sources/pygtksourceview/2.10/pygtksourceview-%{version}.tar.bz2
URL:                 http://www.gnome.org
SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %name

%prep
%setup -q -n pygtksourceview-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

libtoolize --force --copy
aclocal $ACLOCAL_FLAGS
autoconf
./configure --prefix=%{_prefix}  \
	     %{gtk_doc_option}   \
            --sysconfdir=%{_sysconfdir}
make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT \
    pyexecdir=%{_libdir}/python%{python_version}/vendor-packages \
    pythondir=%{_libdir}/python%{python_version}/vendor-packages
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.pyo" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python?.?/vendor-packages

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/pygtk
%{_datadir}/gtk-doc

%changelog
* Tue Apr 20 2010 - christian.kelly@oracle.com
- Bump to 2.10.1.
* Fri Apr 16 2010 - christian.kelly@oracle.com
- Bump to 2.10.0.
* Mon Mar  1 2010 - christian.kelly@sun.com
- Bump to 2.9.2.
* Thu Jan 28 2010 - brian.cameron@sun.com
- Bump to 2.9.1.
* Wed Sep 23 2009 - brian.cameron@sun.com
- Clean up patches.
* Tue Sep 22 2009 - brian.cameron@sun.com
- Bump to 2.8.0.
* Thu Aug 27 2009 - christian.kelly@sun.com
- Bump to 2.7.0.
* Thu Mar 26 2009 - dave.lin@sun.com
- Bump to 2.6.0
* Fri Mar 13 2009 - dave.lin@sun.com
- Bump to 2.5.0
- Run libtoolize to ensure configured correctly for (Open)Solaris.
* Mon Nov 24 2008 - laca@sun.com
- use %{python_version} macro to select with version of Python to build which
* Mon Sep 29 2008 - christian.kelly@sun.com
- Bump to 2.4.0.
* Mon Aug 11 2008 - damien.carbery@sun.com
- Bump to 2.3.0.
* Mon Mar 10 2008 - damien.carbery@sun.com
- Bump to 2.2.0.
* Mon Feb 04 2008 - damien.carbery@sun.com
- Bump to 2.1.1.
* Tue Jan 22 2008 - damien.carbery@sun.com
- Bump to 2.1.0.
* Wed Oct 17 2007 - damien.carbery@sun.com
- Call autoconf because configure.ac is being patched.
* Sun Oct 07 2007 - damien.carbery@sun.com
- Add patches, 01-skip-codegen-test and 02-pygobject-xsl-dir, to get the module
  to build within the JDS environment where pygobject and pygtk are not yet
  installed.
* Tue Sep 04 2007 - damien.carbery@sun.com
- Initial spec
