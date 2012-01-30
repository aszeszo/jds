#
# spec file for package SUNWdialog
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#
%include Solaris.inc

%define OSR 9391:1.x

Name:                    SUNWdialog
IPS_package_name:        terminal/dialog
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:                 dialog - display dialog boxes from shell scripts
License:                 LGPL v2.1
%define year 2010
%define month  04
%define day    28
Version:		 1.1
%define tarball_version  %{version}-%{year}%{month}%{day}
Source:                  ftp://invisible-island.net/dialog/dialog-%{tarball_version}.tgz
# date:2009-02-24 owner:wangke type:branding
Patch1:                  dialog-01-manpages.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{tarball_version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWsndmu
Requires: SUNWlibms
Requires: SUNWbash
BuildRequires: SUNWncurses
BuildRequires: SUNWgnu-gettext
BuildRequires: SUNWncurses-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n dialog-%tarball_version
%patch1 -p1

%build
export CFLAGS="-I/usr/include/ncurses -D_XOPEN_SOURCE_EXTENDED %optflags"
export LDFLAGS="-L/usr/gnu/lib -R/usr/gnu/lib %_ldflags -lncurses"

./configure --prefix=%{_prefix}			\
	    --enable-included-msgs		\
	    --enable-nls			\
	    --enable-widec			\
	    --mandir=%{_mandir}

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/doc/dialog/examples
rm -fr samples/copifuncs
rm -fr samples/install
install samples/* $RPM_BUILD_ROOT%{_datadir}/doc/dialog/examples/
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, bin) %{_datadir}/doc/dialog
%dir %attr (0755, root, bin) %{_datadir}/doc/dialog/examples
%{_datadir}/doc/dialog/examples/*
%doc README
%doc(bzip2) COPYING CHANGES

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 1.1-20100428
* Fri Jan 22 2010 - ke.wang@sun.com
- Bump to 1.1-20100119
* Thu Mar 26 2009 - takao.fujiwara@sun.com
- Remove patch build.diff and g11n-multibyte-input.diff because
  SUNWncurses is available now. Use /usr/gnu instead of /usr/xpg4.
* Tue Feb 10 2009 - halton.huo@sun.com
- Add Requires: SUNWbash to fix issue #10 for CR6753371
* Wed Sep 17 2008 - jim.li@sun.com
- Revised new copyright file
* Mon Aug 11 2008 - takao.fujiwara@sun.com
- Add dialog-02-g11n-multibyte-input.diff to support multi-byte CLI.
* Fri Aug 08 2008 - takao.fujiwara@sun.com
- Bumped to 1.1-20080727 to enable USE_WIDE_CURSES & HAVE_WGET_WCH in dlg_config.h
- Add --enable-widec option in configure.
* Wed Jul 23 2008 - takao.fujiwara@sun.com
- Add l10n packages
* Tue Jul 22 2008 - damien.carbery@sun.com
- Remove l10n package because no l10n files are installed.
* Wed Jul  9 2008 - jim.li@sun.com
- Copied from SFEdialog and rename to SUNWdialog
* Thu Jan 11 2007 - laca@sun.com
- fix version string to be numeric; use the versioned tarball
* Thu Jun 22 2006 - laca@sun.com
- rename to SFEdialog
- delete -share pkg
- remove unnecessary CFLAGS and LDFLAGS
- add missing dep
* Thu May 04 2006 - damien.carbery@sun.com
- Bump version to match dir name inside tarball. Fix share package perms.
* Sun Jan 29 2006 - mike kiedrowski (lakeside-AT-cybrzn-DOT-com)
- Initial spec



