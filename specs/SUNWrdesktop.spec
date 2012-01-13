#
# spec file for package SUNWrdesktop
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner migi
# bugdb: https://sourceforge.net/tracker/?func=detail&atid=381349&group_id=24366&aid=
#

%include Solaris.inc

%define OSR 9603:1.6.2

Name:                SUNWrdesktop
IPS_package_name:    desktop/remote-desktop/rdesktop
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:             RDP, Microsoft Terminal Services client
License:             GPL v2
Version:             1.6.0
Source:              %{sf_download}/rdesktop/rdesktop-%{version}.tar.gz
# date:2008-02-20 owner:fujiwara type:feature bugster:6665274
Patch1:              rdesktop-01-sun-keymap.diff
# date:2008-08-19 owner:fujiwara type:bug bugster:6725349 bugzilla:2018344
Patch2:              rdesktop-02-g11n-i18n-title.diff
# date:2000-02-20 owner:mattman type:branding
Patch3:              rdesktop-03-manpage.diff
# date:2011-06-13 owner:migi type:security bug bugster:7053893
Patch4:              rdesktop-04-remote-file-access.diff

SUNW_Copyright:      %{name}.copyright
SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWopenssl-libraries
BuildRequires: SUNWxwrtl
BuildRequires: SUNWxwplt
BuildRequires: SUNWbtool
BuildRequires: SUNWxwinc

%prep
%setup -q -n rdesktop-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

./configure --prefix=%{_prefix} \
            --mandir=%{_mandir} \
            --with-ipv6         \
	    --with-openssl="/usr"

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README doc/AUTHORS
%doc(bzip2) COPYING doc/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_mandir}/*
%{_datadir}/rdesktop/*

%changelog
* Mon Jun 13 2011 - Michal.Pryc@Oracle.Com
- Add rdesktop-04-remote-file-access.diff to fix CR:7053893
* Fri Feb 20 2009 - matt.keenan@Sun.Com
- Add manpages patch for Attributes and ARC Comment
* Fri Dec 08 2008 - Michal.Pryc@Sun.Com
- Changed openssl dir to allow build on snv >= 104
* Thu Sep 11 2008 - Michal.Pryc@Sun.Com
- Add %doc to %files for new copyright
* Thu Sep 11 2008 - takao.fujiwara@sun.com
- Updated rdesktop-02-g11n-i18n-title.diff for 1.6.0
* Tue Sep 10 2008 - Michal.Pryc@Sun.Com
- Bump to 1.6.0
* Tue Aug 19 2008 - takao.fujiwara@sun.com
- Add rdesktop-02-g11n-i18n-title.diff to show the right UTF-8 title.
* Thu Mar 15 2008 - lin.ma@sun.com
- Add SUNWopenssl-libraries/SUNWxwrtl/SUNWxwplt dependency.
* Wed Feb 20 2008 - takao.fujiwara@sun.com
- Add rdesktop-01-sun-keymap.diff to support Xsun and Sun Type6/7 keyboards.
* Mon Feb 18 2008 - Michal.Pryc@Sun.Com
- Enabling ipv6 support
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version


