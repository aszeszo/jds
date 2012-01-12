#
# spec file for package SUNWpyatspi
#
# includes module(s): pyatspi
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan

%include Solaris.inc

Name:                    SUNWpyatspi
IPS_package_name:        library/python-2/pyatspi2-26
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
License:                 LGPL v2, MIT/X
Vendor:                  Gnome Community
Summary:                 Python bindings for accessibility implementation on D-Bus for GNOME
Version:                 2.2.1
Source:	                 http://ftp.gnome.org/pub/GNOME/sources/pyatspi/2.2/pyatspi-%{version}.tar.bz2
Patch1:                  pyatspi-01-configure.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
Requires:       SUNWglib2
Requires:       SUNWdbus
Requires:       SUNWdbus-glib
Requires:       SUNWgtk2
Requires:       SUNWlxml
Requires:       SUNWlibatk
Requires:       SUNWdbus-python26
Requires:       SUNWPython26
Requires:       SUNWgnome-python26-libs
Requires:       SUNWat-spi2-core
BuildRequires:  SUNWglib2-devel
BuildRequires:  SUNWdbus-devel
BuildRequires:  SUNWdbus-glib-devel
BuildRequires:  SUNWgtk2-devel
BuildRequires:  SUNWlxml
BuildRequires:  SUNWlibatk-devel
BuildRequires:  SUNWdbus-python26
BuildRequires:  SUNWPython26-devel
BuildRequires:  SUNWgobject-introspection

%{?!pythonver:%define pythonver 2.6}

%prep
%setup -q -n pyatspi-%{version}
%patch1 -p1

%build
export PYTHON=/usr/bin/python%{pythonver}
libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f
autoconf
CFLAGS="%optflags"

LDFLAGS="%{_ldflags}"
./configure --prefix=%{_prefix}			\
            --libdir=%{_libdir}			\
            --bindir=%{_bindir}			\
            --sysconfdir=%{_sysconfdir}		\
            --mandir=%{_mandir}			\
            --libexecdir=%{_libexecdir}		\
            %{gtk_doc_option}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Move to vendor-packages
if [ -x $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages ]; then
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
rm -rf $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages/*
mv $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/vendor-packages
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{pythonver}/site-packages
fi

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d  pyatspi-%{version}/AUTHORS
%doc -d  pyatspi-%{version}/COPYING
%doc -d  pyatspi-%{version}/INSTALL
%doc -d  pyatspi-%{version}/README
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.6
%dir %attr (0755, root, bin) %{_libdir}/python2.6/vendor-packages
%{_libdir}/python2.6/vendor-packages/*

%changelog
* Mon Oct 24 2011 - brian.cameron@oracle.com
- Bump to 2.2.1.
* Mon Aug 15 2011 - lee.yuan@oracle.com
- Bump to 2.1.4.
* Fri Aug 06 2010 - li.yuan@sun.com
- Bump to 0.3.6.
* Thu Jul 01 2010 - li.yuan@sun.com
- Bump to 0.3.4.
* Fri Jun 11 2010 - li.yuan@sun.com
- Bump to 0.3.3.
* Fri Jun 04 2010 - li.yuan@sun.com
- Bump to 0.3.2
* Sat Apr  3 2010 - christian.kelly@sun.com
- Bump to 0.1.8.
* Tue Feb 23 2010 - li.yuan@sun.com
- Bump to 0.1.7.
* Wed Feb 10 2010 - li.yuan@sun.com
- Bump to 0.1.6.
* Tue Jan 12 2010 - li.yuan@sun.com
- Bump to 0.1.5.
* Tue Dec 22 2009 - li.yuan@sun.com
- Bump to 0.1.4.
* Tue Dec 01 2009 - li.yuan@sun.com
- Bump to 0.1.3.
* Fri Nov 20 2009 - li.yuan@sun.com
- Initial version.
