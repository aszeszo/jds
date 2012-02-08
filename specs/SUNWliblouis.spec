# Copyright 2009, 2011 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc

%define pythonver 2.6
%use liblouis = liblouis.spec

Summary:	   %liblouis.summary
Name:              SUNWliblouis
IPS_package_name:  library/liblouis
Meta(info.classification): %{classification_prefix}:System/Libraries
Version:           %{liblouis.version}
SUNW_BaseDir:      %{_basedir}
SUNW_Copyright:    %{name}.copyright
License:           %{liblouis.license}
BuildRoot:         %{_tmppath}/%{name}-%{liblouis.version}-build
%include gnome-incorporation.inc
%include default-depend.inc

%package devel
Summary:           %{summary} - development files
SUNW_BaseDir:      %{_basedir}
%include default-depend.inc
Requires:          %{name}

%prep
rm -rf %name-%liblouis.version
mkdir %name-%liblouis.version
%liblouis.prep -d %name-%liblouis.version
cd %{_builddir}/%name-%liblouis.version
ls ../../SOURCES
gzcat ../../SOURCES/%{liblouis.name}-%{liblouis.version}.tar.gz | tar xf -

%build
export PYTHON="/usr/bin/python%{pythonver}"
%liblouis.build -d %name-%liblouis.version

%install
export PYTHON="/usr/bin/python%{pythonver}"
%liblouis.install -d %name-%liblouis.version
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

# Move demo to demo directory.
#
install -d $RPM_BUILD_ROOT%{_prefix}/demo/jds/bin
mv $RPM_BUILD_ROOT%{_bindir}/* $RPM_BUILD_ROOT%{_prefix}/demo/jds/bin
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_mandir}

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{liblouis.version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
( echo 'PATH=/usr/bin:/usr/sfw/bin; export PATH' ;
  echo 'infos="';
  echo 'liblouis.info' ;
  echo '"';
  echo 'retval=0';
  echo 'for info in $infos; do';
  echo '  install-info --info-dir=%{_infodir} %{_infodir}/$info || retval=1';
  echo 'done';
  echo 'exit $retval' ) | $PKG_INSTALL_ROOT/usr/lib/postrun -b -c JDS

%preun
( echo 'PATH=/usr/bin:/usr/sfw/bin; export PATH' ;
  echo 'infos="';
  echo 'liblouis.info' ;
  echo '"';
  echo 'for info in $infos; do';
  echo '  install-info --info-dir=%{_infodir} --delete %{_infodir}/$info';
  echo 'done';
  echo 'exit 0' ) | $PKG_INSTALL_ROOT/usr/lib/postrun -b -c JDS

%files
%doc -d liblouis-%{liblouis.version} AUTHORS README
%doc(bzip2) -d liblouis-%{liblouis.version} ChangeLog
%doc(bzip2) -d liblouis-%{liblouis.version} COPYING COPYING.LIB
%doc(bzip2) -d liblouis-%{liblouis.version} NEWS
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %dir %{_prefix}/demo
%dir %attr (0755, root, bin) %dir %{_prefix}/demo/jds
%dir %attr (0755, root, bin) %dir %{_prefix}/demo/jds/bin
%{_prefix}/demo/jds/bin/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/liblouis*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/liblouis.pc
%dir %attr (0755, root, bin) %{_infodir}
%attr (0444, root, bin) %{_infodir}/liblouis.info
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_datadir}/doc/liblouis
%{_datadir}/doc/liblouis/*
%dir %attr (0755, root, sys) %{_datadir}/liblouis
%dir %attr (0755, root, sys) %{_datadir}/liblouis/tables
%{_datadir}/liblouis/tables/*
%dir %attr (0755, root, bin) %{_libdir}/python?.?
%dir %attr (0755, root, bin) %{_libdir}/python?.?/vendor-packages
%dir %attr (0755, root, bin) %{_libdir}/python?.?/vendor-packages/louis
%dir %attr (0755, root, bin) %{_libdir}/python?.?/vendor-packages/louis-%{version}-py%{pythonver}.egg-info
%{_libdir}/python?.?/vendor-packages/louis/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}/
%{_includedir}/liblouis/*

%changelog
* Fri Feb 03 2012 - Li Yuan <lee.yuan@oracle.com>
- Fix 7142110. Correct files permission.
* Tue Jan 04 2011 - Li Yuan <lee.yuan@oracle.com>
- Fix build error.
* Mon Nov 22 2010 - Li Yuan <lee.yuan@oracle.com>
- Move demo to demo directory.
* Wed Nov 03 2010 - Li Yuan <lee.yuan@oracle.com>
- Add copyright info.
* Fri Sep 24 2010 - Brian Cameron  <brian.cameron@oracle.com>
- Remove all .la files.
* Mon Jan 11 2010 - Willie Walker
- Update to use python 2.6 and use %{pythonver}.
* Tue Aug 25 2009 - Willie Walker
- Get this working again on b121. Also use the liblouis version number
  instead of the default version number.  Bump to 1.7.0.
* Tue Jun 16 2009 - Willie Walker
- Upgrade to liblouis 1.6.2 to get us the 'louis' python module
* Fri Feb 13 2009 - Willie Walker
- Initial spec
