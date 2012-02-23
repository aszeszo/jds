#
# spec file for package SUNWpython26-coherence
#
# includes module(s): coherence
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# bugdb: http://coherence.beebits.net/ticket/$bugid
%define owner jouby
#

%include Solaris.inc

%define pythonver 2.6
%define src_url         http://coherence.beebits.net/download
%define src_name        Coherence

%use coherence = coherence.spec

Name:                   SUNWpython26-coherence
IPS_package_name:       library/python-2/coherence-26
Meta(info.classification): %{classification_prefix}:Development/Python
Summary:                DLNA/UPnP framework for the digital living
URL:                    %{coherence.url}
SUNW_Copyright:         SUNWpython26-coherence.copyright
License:		MIT
Version:                %{coherence.version}
Source1:                coherence.xml
Source2:                coherence.conf
Source3:                coherence
Source4:                %{name}-manpages-0.1.tar.gz
Patch1:                 coherence-01-youtubedl.diff
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:               runtime/python-26
Requires:               library/python-2/python-twisted-26
Requires:               library/python-2/python-zope-interface-26
BuildRequires:          runtime/python-26
BuildRequires:          library/python-2/setuptools-26

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /

%prep
rm -rf %name-%version
mkdir -p %name-%version
%coherence.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %{SOURCE4} | tar xf -

%patch1 -p1

%build
export PYTHON="/usr/bin/python%{pythonver}"
export CFLAGS="%optflags -I/usr/xpg4/include -I%{_includedir} -I/usr/include/python%{pythonver}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags"
export PYCC_CC="$CC"
export PYCC_CXX="$CXX"
%coherence.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%coherence.install -d %name-%version

# install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

# Install SMF related files.
mkdir -p $RPM_BUILD_ROOT/lib/svc/manifest/application
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/coherence
mkdir -p $RPM_BUILD_ROOT/lib/svc/method

install -c -m 644 %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/manifest/application/
install -c -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_localstatedir}/coherence/
install -c -m 644 %{SOURCE3} $RPM_BUILD_ROOT/lib/svc/method/

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%actions
group gid=52 groupname=upnp
user gcos-field="UPnP Server Reserved UID" group=upnp home-dir=/var/coherence login-shell=/bin/ksh password=NP uid=52 username=upnp

%files
%defattr (-, root, bin)
%doc(bzip2) -d Coherence-%version LICENCE NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_datadir}/dbus-1
%dir %attr (0755, root, bin) %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.Coherence.service
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{pythonver}/vendor-packages
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files root
%defattr (-, root, bin)
/lib/svc/method/coherence
%dir %attr (0755, root, sys)  /lib/svc/manifest
%dir %attr (0755, root, sys)  /lib/svc/manifest/application
%class(manifest) %attr (0444, root, sys) /lib/svc/manifest/application/coherence.xml
%dir %attr (0755, root, sys)  %{_localstatedir}
%dir %attr (0755, upnp, upnp) %{_localstatedir}/coherence
%attr (0644, upnp, upnp) %{_localstatedir}/coherence/coherence.conf

%changelog
* Fri Feb 10 2012 - padraig.obriain@oracle.com
- Update Requires and BuildRequires to be IPS package names.
* Wen Jan 01 2010 - yuntong.jin@sun.com
- Bump to 0.6.6.2, del upstream patch: coherence-01-appletrailers-storage.diff 
* Thu Dec 03 2009 - yuntong.jin@sun.com
- Add dependency
* Wen Dec 02 2009 - yuntong.jin@sun.com
- Fixed appletrailer backend is broken issue 
* Wen Oct 21 2009 - yuntong.jin@sun.com
- Fixed doo bug 11433
* Tue Sep 29 2009 - dave.lin@sun.com
- Fixed file attribute issue.
* Fri Sep 17 2009 - brian.lu@sun.com
- Add support to ship org.Coherence.service fil
* Thu Aug 27 2009 - yuntong.jin@sun.com
- change owner to jouby, add license info
* Fri Mar 06 2009 - alfred.peng@sun.com
- Create SFEpython24-coherence.spec and coherence.spec to replace
  SFEcoherence.spec.
* Mon Mar 02 2009 - alfred.peng@sun.com
- Bump to 0.6.2. Remove the upstream patch path-blank.diff.
* Mon Feb 16 2009 - alfred.peng@sun.com
- Add patch path-blank.diff to fix packaging problem.
  Bump to 0.6.0.
* Thu Oct 09 2008 - jijun.yu@sun.com
- Initial version.


