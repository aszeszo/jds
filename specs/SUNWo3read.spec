#
# spec file for package SUNWo3read
#
# includes module(s): o3read
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai

%include Solaris.inc

%use o3read = o3read.spec

Name:                    SUNWo3read
IPS_package_name:        text/o3read
Meta(info.classification): %{classification_prefix}:Applications/Office
Summary:                 A standalone converter for the OpenOffice.org swriter (*.sxw) and scalc (*.sxc) formats into plain text and html 
Version:                 %{o3read.version}
SUNW_Copyright:          %{name}.copyright
License:                 %{o3read.license}
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

BuildRequires: SUNWgcc

%prep
rm -rf %name-%version
mkdir %name-%version
%o3read.prep -d %name-%version

%build
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"

%o3read.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%o3read.install -d %name-%version

# TODO: Remove this line when o3totxt removed from SUNWdesktop-search (tracker).
#rm $RPM_BUILD_ROOT%{_bindir}/o3totxt

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}(o3read):$RPM_ARCH:%(date +%%Y-%%m-%%d):unsupported" $RPM_BUILD_ROOT/usr}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d o3read-%{o3read.version} README 
%doc(bzip2) -d o3read-%{o3read.version} COPYING ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%changelog
* Thu Sep 4 2008 -  jerry.tan@sun.com
- Add o3totxt back, remove o3totxt from desktop-search
* Sat Jul 12 2008 - damien.carbery@sun.com
- Remove %{_bindir}/o3totxt because it is delivered by SUNWdesktop-search too.
* Tue Jul 04 2008 - damien.carbery@sun.com
- Remove l10n package because no l10n files are installed.
* Fri Jul 4 2008 - jerry.tan@sun.com
- Create new spec for SUNWo3read

