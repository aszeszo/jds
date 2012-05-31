#
# spec file for package SUNWgnome-user-docs
#
# includes module(s): gnome-user-docs
#
# Copyright (c) 2009, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner davelam
#
%include Solaris.inc

%use gud = gnome-user-docs.spec

Name:                    SUNWgnome-user-docs
IPS_package_name:        documentation/gnome/gnome-user-docs
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Documentation
Summary:                 GNOME user documentation
Version:                 %{gud.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gud.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: library/python-2/libxml2-26
BuildRequires: developer/gnome/gnome-doc-utils
Requires: gnome/help-viewer/yelp

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%gud.prep -d %name-%version

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export MSGFMT="/usr/bin/msgfmt"
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export LDFLAGS="%_ldflags"
export CFLAGS="%optflags"
%gud.build -d %name-%version

%install
%gud.install -d %name-%version

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

# Remove scrollkeeper files before packaging.
rm -rf $RPM_BUILD_ROOT/var

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc -d gnome-user-docs-%{gud.version} README AUTHORS
%doc(bzip2) -d gnome-user-docs-%{gud.version} COPYING COPYING-DOCS
%doc(bzip2) -d gnome-user-docs-%{gud.version} NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/C
%{_datadir}/omf/*/*-C.omf

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/[a-z]*
%{_datadir}/omf/*/*-[a-z][a-z].omf
%{_datadir}/omf/*/*-[a-z][a-z]_[A-Z]*.omf


%changelog
* Thu May 31 2012 - dave.lin@oracle.com
- Changed the dependency's name to IPS name.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Apr  3 2009 - laca@sun.com
- stop using postrun
* Wed Mar 11 2009 - dave.lin@sun.com
- Took the ownership of this spec file.
* Fri Sep 19 2008 - halton.huo@sun.com
- Add %doc part to %files
* Thu Apr 03 2008 - damien.carbery@sun.com
- Add SUNW_Copyright.
* Tue Jul 10 2007 - damien.carbery@sun.com
- Add BuildRequires SUNWlxml-python.
* Wed Aug 16 2006 - damien.carbery@sun.com
- Add %files entry to pick up pt_BR and zh_CN omf files.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Wed Mar 22 2006 - damien.carbery@sun.com
- Uncomment removal of l10n files when not doing l10n build.
* Tue Mar 14 2006 - damien.carbery@sun.com
- Uncomment l10n files to pick up 'it' files.
* Tue Feb 21 2006 - damien.carbery@sun.com
- Delete scrollkeeper files before packaging.
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Fri Sep 30 2005  damien.carbery@sun.com
- Remove obsolete javahelp references.
* Thu Sep 30 2004  shirley.woo@sun.com
- Fixed dependencies lies for base package
* Wed Aug 25 2004  Kazuhiko.Maekawa@sun.com
- Updated files to extracted only l10n content
* Tue Aug 24 2004  laca@sun.com
- separated l10n content into l10n subpkg
* Thu Aug 19 2004  damien.carbery@sun.com
- Remove xml perms change - done in base spec file.
* Wed Aug 18 2004  damien.carbery@sun.com
- Change xml perms for Solaris integration.
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...


