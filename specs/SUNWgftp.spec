#
# spec file for package SUNWgftp
#
#
# includes module(s): gftp
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#

%include Solaris.inc

%define OSR 10474:2.x

Name:                    SUNWgftp
IPS_package_name:        desktop/gftp
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:                 gFTP - Multithreaded FTP client for *NIX based machines
URL:                     http://gftp.seul.org/
Version:                 2.0.19
Source:                  http://gftp.seul.org/gftp-%{version}.tar.bz2
Source1:                 %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:           SUNWgftp.copyright
License:                 GPL v3
# date:2008-09-23 owner:alfred type:bug state:upstream
Patch1:                  gftp-01-solaris-in-trunk.diff
# date:2008-11-27 owner:alfred type:branding
Patch2:                  gftp-02-profile-dir.diff
# date:2008-12-09 owner:fujiwara type:feature bugzilla:563814 bugster:6782004
Patch3:                  gftp-03-g11n-charset.diff
# date:2008-12-09 owner:fujiwara type:feature bugzilla:563816 bugster:6782004
Patch4:                  gftp-04-g11n-lc-time.diff
# date:2008-12-09 owner:fujiwara type:feature bugzilla:563818 bugster:6782004
Patch5:                  gftp-05-g11n-im-filter.diff
# date:2008-12-09 owner:fujiwara type:feature bugzilla:563819 bugster:6782004
Patch6:                  gftp-06-g11n-ssh-login.diff
# date:2008-12-09 owner:fujiwara type:feature bugzilla:563820 bugster:6782004
Patch7:                  gftp-07-g11n-cli-utf8.diff
# date:2008-12-23 owner:alfred type:bug bugzilla:565430
Patch8:                  gftp-08-url_prefix-null.diff

%include default-depend.inc
%include desktop-incorporation.inc

Requires: SUNWgtk2
Requires: SUNWfreetype2
Requires: SUNWfontconfig
Requires: SUNWopensslr
BuildRequires: SUNWxwplt
BuildRequires: SUNWlibms
BuildRequires: SUNWmlib
BuildRequires: SUNWgtk2-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n gftp-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
gzcat %SOURCE1 | tar xf -

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/gftp-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%doc(bzip2) README ChangeLog COPYING INSTALL
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/gftp
%{_datadir}/gftp/*
%dir %attr (0755, root, bin) %{_datadir}/man
%{_datadir}/man/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Fri Aug 38 2009 - yuntong.jin@sun.com
- Change owner to jouby
* Thu Feb 19 2009 - alfred.peng@sun.com
- New manpage tarball.
* Mon Feb 02 2009 - alfred.peng@sun.com
- Fix the package dependency issue. bugster CR#6798920.
* Wed Dec 31 2008 - alferd.peng@sun.com
- Add gftp-08-url_prefix-null.diff to fix GNOME bugzilla 565430.
* Mon Dec 08 2008 - takao.fujiwara@.sun.com
- Add gftp-03-g11n-charset.diff to avoid a crash.
- Add gftp-03-g11n-lc-time.diff to work with localized "ls -l" on Solaris.
- Add gftp-04-g11n-im-filter.diff to work IM in filespec.
- Add gftp-05-g11n-ssh-login.diff to be able to login with ssh.
- Add gftp-06-g11n-cli-utf8.diff to show UTF-8 strings with CLI.
* Mon Dec 08 2008 - takao.fujiwara@sun.com
- Bumped to 2.0.19
- Update gftp-01-solaris-in-trunk.diff for trunk.
* Thu Nov 27 2008 - alfred.peng@sun.com 
- As ARC recommended, add patch profile-dir.diff to move the profile
  to $HOME/.gnome/gftp.
* Thu Nov 17 2008 - alfred.peng@sun.com
- Move from SFE.
  Add copyright file, update group bit for %{_datadir}/doc.
  Remove --disable-sm and extra flags.
* Sun Sep 28 2008 - alfred.peng@sun.com
- Update group bit for %{_datadir}/man.
* Wed Sep 24 2008 - alfred.peng@sun.com
- Backport the patch gftp-01-solaris-in-trunk.diff from trunk to build
  with Sun Studio.
* Tue Sep 04 2007  - Thomas Wagner
- bump to 0.15.1, add %{version} to Download-Dir (might change again)
- conditional !%build_l10n rmdir $RPM_BUILD_ROOT/%{_datadir}/locale
* Sat May 26 2007  - Thomas Wagner
- bump to 0.15.0
- set compiler to gcc
- builds with Avahi, if present
* Thu Apr 06 2007  - Thomas Wagner
- Initial spec



