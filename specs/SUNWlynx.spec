#
# spec file for package SUNWlynx
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner dermot
#

%include Solaris.inc

%define OSR 9837:2.8.6

Name:                    SUNWlynx
IPS_package_name:        web/browser/lynx
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:                 Text-mode web browser
License:                 LGPL v2
Version:                 2.8.7
URL:                     http://lynx.browser.org/
Source:			 http://lynx.isc.org/lynx%{version}/lynx%{version}.tar.bz2
# date:2009-02-20 owner:mattman type:feature
Patch1:			 lynx-01-manpage.diff
# date:2010-01-27 owner:yippi type:bug state:upstream
Patch2:                  lynx-02-locale.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                %{name}-root
Requires:                SUNWopenssl-libraries
Requires:                SUNWncurses

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n lynx2-8-7
%patch1 -p1
%patch2 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS="-I/usr/include/ncurses -D_XPG6 %optflags"
export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib -L/usr/gnu/lib -R/usr/gnu/lib"

./configure --prefix=/usr \
	--enable-nls \
	--enable-japanese-utf8 \
	--enable-widec \
	--sysconfdir=%{_sysconfdir}/lynx \
	--mandir=%{_mandir} \
	--with-ssl \
	--with-screen=ncurses

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%doc AUTHORS
%doc COPYHEADER
%doc COPYING
%dir %attr (0755, root, other) %{_datadir}/doc

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%attr (0755, root, sys) %dir %{_sysconfdir}/lynx
%{_sysconfdir}/lynx/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Jan 27 2010 - brian.cameron@sun.com
- Bump to 2.8.7.
* Mon Dec 22 2008 - takao.fujiwara@sun.com
- Add patch g11n-iconv.diff to use Solaris iconv.
- Add patch g11n-use-local-char.diff. The default charset is the current encoding.
- Add patch g11n-utf8-bookmark.diff so that input method works on UTF-8.
- Add configure option --enable-japanese-utf8 --enable-widec
- Add l10n package.
* Tue Dec 16 2008 - dermot.mccluskey@sun.com
- ssl is now in /usr, not /usr/sfw
* Mon Nov 24 2008 - dermot.mccluskey@sun.com
- fix default permissions for -root
* Fri Nov 21 2008 - dermot.mccluskey@sun.com
- use ncurses and add openssl support
* Thu nov 20 2008 - dermot.mccluskey@sun.com
- initial version


