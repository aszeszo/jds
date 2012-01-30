#
# spec file for package SUNWxchat
#
# includes module(s): xchat
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
#
%include Solaris.inc
%use xchat = xchat.spec

Name:                    SUNWxchat
IPS_package_name:        desktop/irc/xchat
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:                 XChat IRC Client
Version:                 %{xchat.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{xchat.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWgtk2-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWPython26
Requires: SUNWgtk2
Requires: SUNWPython26
BuildRequires: runtime/perl-512
Requires: SUNWopenssl-libraries
BuildRequires: SUNWopenssl-include
Requires: SUNWlibsexy
BuildRequires: SUNWlibsexy-devel
Requires: SUNWgnome-spell
Requires: SUNWgnome-libs
Requires: SUNWdbus
Requires: SUNWdesktop-cache
Requires: %name-root
BuildRequires: SUNWdbus-devel

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
mkdir -p %name-%version
%xchat.prep -d %name-%version

%build
%xchat.build -d %name-%version

%install
%xchat.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri gconf-cache desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%{_datadir}/dbus-1/services/org.xchat.*

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/apps_xchat_url_handler.schemas

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Fri Jul 25 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-base-libs/-devel.
* Fri Jul 25 2008 - laca@sun.com
- add missing deps
* Thu Jul 24 2008 - laca@sun.com
- create SUNWxchat.spec from SFExchat.spec and move to spec-files-other
* Thu Jun 12 2008 - brian.cameron@sun.com
- Bump to 2.8.6.
* Mon Oct 22 2007 - brian.cameron@sun.com
- Remove patch xchat-03-dbus-LDADD.diff since it is not longer needed.
* Wed Oct 17 2007 - laca@sun.com
- add /usr/gnu to CFLAGS/LDFLAGS
* Thu Aug 02 2007 - Brian Cameron <brian.cameron@sun.com>
- Bump to 2.8.4.
* Tue May 29 2007 - Thomas Wagner
- bump to 2.8.2
- /usr/bin/msgfmt errors, use /opt/sfw/bin/msgfmt
- reworked patch for 2.8.2
* Sun Jan  7 2007 - laca@sun.com
- bump to 2.8.0, merge patches, update %files
* Mon Jul 31 2006 - glynn.foster@sun.com
- bump to 2.6.6
* Mon Jun 12 2006 - laca@sun.com
- bump to 2.6.4
- rename to SFExchat
- add -l10n pkg
- change to root:bin to follow other JDS pkgs.
- add patch that fixes the proxy in 2.6.4
* Fri Jun  2 2006 - laca@sun.com
- use post/postun scripts to install schemas into the merged gconf files
- merge -share pkg into base
* Thu Apr 20 2006 - damien.carbery@sun.com
- Bump to 2.6.2.
* Mon Mar 20 2006 - brian.cameron@sun.com
- Remove unneeded intltoolize call.
* Thu Jan 26 2006 - brian.cameron@sun.com
- Update to 2.6.1
* Wed Dec 07 2005 - brian.cameron@sun.com
- Update to 2.6.0
* Wed Oct 12 2005 - laca@sun.com
- update to 2.4.5; fix
* Thu Jan 06 2004 - Brian.Cameron@sun.com
- created



