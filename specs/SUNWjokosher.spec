#
# spec file for package SUNWjokosher
#
# Copyright (c) 2007, 2012, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi

%define OSR 11994:0.11.1

#
# includes module(s): jokosher
#
# bugdb: https://bugs.launchpad.net/jokosher
#
%include Solaris.inc

Name:           SUNWjokosher
IPS_package_name: desktop/studio/jokosher
Meta(info.classification): %{classification_prefix}:Applications/Sound and Video
License:        GPL v2
Version:        0.11.5
Distribution:   Java Desktop System
Summary:        Jokosher is a multi-track studio application
Source0:        http://launchpad.net/jokosher/trunk/%{version}/+download/jokosher-%{version}.tar.gz
# date:2010-12-30 owner:yippi type:bug bugid:695805
Patch1:         jokosher-01-byteorder.diff
# date:2010-12-30 owner:yippi type:branding
Patch2:         jokosher-02-py26.diff
SUNW_Copyright: %{name}.copyright
URL:            http://jokosher.org
BuildRoot:      %{_tmppath}/jokosher-%{version}-build
SUNW_BaseDir:   %{_basedir}

Requires:       runtime/python-26
Requires:       library/python-2/python-dbus-26
Requires:       library/audio/gstreamer
Requires:       library/python-2/pygtk2-26
Requires:       library/python-2/python-gst-26
Requires:       library/audio/gstreamer/plugin/gnonlin
Requires:       library/python-2/setuptools-26
BuildRequires:  runtime/python-26
BuildRequires:  library/python-2/python-dbus-26
BuildRequires:  library/audio/gstreamer
BuildRequires:  library/python-2/pygtk2-26
BuildRequires:  library/python-2/python-gst-26
BuildRequires:  library/python-2/setuptools-26
BuildRequires:  library/audio/gstreamer/plugin/gnonlin
BuildRequires:  gnome/preferences/control-center

%include default-depend.inc
%include desktop-incorporation.inc

%description
Jokosher is a simple yet powerful multi-track studio. 

%package l10n
Summary:                 %{summary} - l10n files

%prep
%setup -q -n jokosher-%version
%patch1 -p1
%patch2 -p1

%build
python%{default_python_version} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{default_python_version} setup.py install --root=%{buildroot}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf %{buildroot}

%post
( echo 'test -x /usr/bin/gtk-update-icon-cache || exit 0';
  echo '/usr/bin/gtk-update-icon-cache --force %{_datadir}/icons/hicolor'
) | $PKG_INSTALL_ROOT/usr/lib/postrun -b -u -t 5
( echo 'test -x /usr/bin/update-desktop-database || exit 0';
  echo '/usr/bin/update-desktop-database'
) | $BASEDIR/lib/postrun -b -u -c JDS_wait
( echo 'test -x /usr/bin/scrollkeeper-update || exit 0';
  echo '/usr/bin/scrollkeeper-update'
) | $BASEDIR/lib/postrun -b -u -c JDS

%postun
test -x $BASEDIR/lib/postrun || exit 0
( echo 'test -x /usr/bin/update-desktop-database || exit 0';
  echo '/usr/bin/update-desktop-database'
) | $BASEDIR/lib/postrun -b -u -c JDS
( echo 'test -x /usr/bin/scrollkeeper-update || exit 0';
  echo '/usr/bin/scrollkeeper-update'
) | $BASEDIR/lib/postrun -b -u -c JDS

%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/jokosher

%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{default_python_version}/vendor-packages/Jokosher
%{_libdir}/python%{default_python_version}/vendor-packages/jokosher*egg-info

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%attr (-, root, other) %{_datadir}/icons
%{_datadir}/jokosher
%dir %attr (0755, root, root) %{_datadir}/mime
%dir %attr (0755, root, root) %{_datadir}/mime/packages
%{_datadir}/mime/packages/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/jokosher/C
%{_datadir}/omf/jokosher/*-C.omf
%doc AUTHORS README
%doc(bzip2) COPYING COPYING-DOCS
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome

%changelog
* Mon Feb 13 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Thu Apr 15 2010 - brian.cameron@sun.com
- Bump to 0.11.5.  Remove code to replace the FreeSound plugin since it now
  uses gnome-keyring.
* Mon Dec 07 2009 - yuntong.jin@sun.com
- Explicitly use python2.6 in JokosherApp.py&Profiler.py.
* Mon Oct 12 2009 - brian.cameron@sun.com
- Now use %{default_python_version}.
* Mon Aug 17 2009 - brian.cameron@sun.com
- Add copyright file, minor cleanup.
* Mon Jun 15 2009 - brian.cameron@sun.com
- Add patch jokosher-01-byteorder.diff so that Jokosher works on Sparc.
* Thu Jun 04 2009 - brian.cameron@sun.com
- Bump to 0.11.3.
* Tue May 12 2009 - brian.cameron@sun.com
- Now build with Python 2.6.
* Thu Mar 19 2009 - brian.cameron@sun.com
- Bump to 0.11.1.
* Sun Mar 01 2009 - brian.cameron@sun.com
- Bump to 0.11.
* Tue Sep 30 2008 - brian.cameron@sun.com
- Bump to 0.10.1.
* Fri Aug 29 2008 - brian.cameron@sun.com
- Bump to 0.10.  Yay!  Remove patch jokosher-01-fixdesktop.diff as it is no
  longer needed.
* Thu Apr 10 2008 - brian.cameron@sun.com
- Change SFEgst-python to SUNWgst-python.
* Thu Feb 07 2008 - brian.cameron@sun.com.
- Add jokosher-01-fixdesktop.diff file so package builds.
* Wed Nov 14 2007 - daymobrew@users.sourceforge.net
- Add l10n package.
* Sat Sep 01 2007 - trisk@acm.jhu.edu
- Fix help and l10n install rules.
* Wed Aug 15 2007 - trisk@acm.jhu.edu
- Update dependencies and paths.
* Tue Jul 10 2007 Brian Cameron <brian.cameron@sun.com>
- New spec file.


