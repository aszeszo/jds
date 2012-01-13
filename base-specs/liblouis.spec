# Copyright 2009, 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
Summary:	Support for contracted braille
Name:		liblouis
Version:	2.1.1
License:	LGPLv3 for library, GPLv3 for binaries
Group:		Libraries
Source: 	http://liblouis.googlecode.com/files/%{name}-%{version}.tar.gz

%define python_version 2.6

%description
An open source braille translator and back-translator with support for computer
and literary braille; contracted and uncontracted translation; and supports
hypenation.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir} --enable-ucs4
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
cd python
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib:$LD_LIBRARY_PATH python setup.py build
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib:$LD_LIBRARY_PATH python setup.py install --root $RPM_BUILD_ROOT --install-lib %{_libdir}/python%{python_version}/vendor-packages
cd ..

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}/
%{_datadir}/liblouis/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/liblouis*
%dir %attr (0755, root, bin) %{_infodir}
%{_infodir}/liblouis.info
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/liblouis.pc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}/
%{_includedir}/liblouis/*
%dir %attr (0755, root, bin) %{_libdir}/python?.?
%dir %attr (0755, root, bin) %{_libdir}/python?.?/vendor-packages
%dir %attr (0755, root, bin) %{_libdir}/python?.?/vendor-packages/louis
%{_libdir}/python?.?/vendor-packages/louis/*

%changelog
* Wed Nov 03 2010 - Li Yuan <lee.yuan@oracle.com>
- Update description.
* Mon Aug 30 2010 - Brian Cameron
- Bump to 2.1.1.
* Thu Apr 01 2010 - Brian Cameron
- Update to 1.8.0.
* Mon Jan 11 2010 - Willie Walker
- Update to use python 2.6.
* Tue Aug 25 2009 - Willie Walker
- Upgrade to liblouis 1.7.0.
* Tue Jun 16 2009 - Willie Walker
- Upgrade to liblouis 1.6.2 to get us the 'louis' python module.
* Fri Feb 13 2009 - Willie Walker
- Initial spec.
