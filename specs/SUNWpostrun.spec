#
# spec file for package SUNWpostrun
#
# includes module(s): postrun
#
# Copyright (c) 2005, 2010, Oracle and/or its affiliates. All rights reserved.
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#

%define OSR developed in the open, no OSR needed:n/a

%include Solaris.inc
Name:                    SUNWpostrun
IPS_package_name:        service/postrun
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:                 Delayed execution environment for procedural package scripts
License:                 cr_Oracle
Version:                 1.0
Source1:                 postrun
Source2:                 postrun.usr
Source3:                 postrun-runq
Source4:                 postrun-query
Source5:                 postrun.xml
SUNW_BaseDir:            /usr
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %{name}-root

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlxml

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p \
    $RPM_BUILD_ROOT/usr/lib \
    $RPM_BUILD_ROOT/var/spool/postrun \
    $RPM_BUILD_ROOT/var/log \
    $RPM_BUILD_ROOT/var/lib/postrun \
    $RPM_BUILD_ROOT/lib/svc/manifest/system

install --mode=0755 %SOURCE1 $RPM_BUILD_ROOT/var/lib/postrun
install --mode=0755 %SOURCE2 $RPM_BUILD_ROOT/usr/lib/postrun
install --mode=0755 %SOURCE3 $RPM_BUILD_ROOT/var/lib/postrun
install --mode=0755 %SOURCE4 $RPM_BUILD_ROOT/usr/lib
install --mode=0444 %SOURCE5 $RPM_BUILD_ROOT/lib/svc/manifest/system
touch $RPM_BUILD_ROOT/var/log/postrun.log

%clean
rm -rf $RPM_BUILD_ROOT

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) /usr/lib
/usr/lib/*

%files root
%defattr (-, root, sys)
%dir %attr (0755, root, other) /var/lib
/var/lib/postrun
%dir %attr (0755, root, bin) /var/spool
%attr (0755, root, bin) /var/spool/postrun
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%class(manifest) /lib/svc/manifest/system/postrun.xml
%ghost %ips_tag(original_name=SUNWpostrun:%{@} preserve=true) /var/log/postrun.log

%changelog
* Mon Aug 16 2010 - laszlo.peter@oracle.com
- copyright update
* Thu Jul 13 2006 - laca@sun.com
- move postrun to /var/lib, add a wrapper script (postrun.usr) to /usr/lib
* Thu Jun 29 2006 - laca@sun.com
- add postrun-query
* Sat Dec  3 2005 - laca@sun.com
- created


