#
# spec file for package ttf-freefont
#
# Copyright (c) 2005, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner dermot
#

%define OSR delivered in s10:n/a

Name:         ttf-freefont
License:      GPLv3
Group:        User Interface/X
Version:      20100919
Release:      54
Distribution: Java Desktop System
Vendor:	      Other
Summary:      Free UCS TrueType Fonts
Source:       http://ftp.gnu.org/gnu/freefont/freefont-ttf-20100919.tar.gz
URL:          http://savannah.gnu.org/projects/freefont/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/doc
Autoreqprov:  on
BuildArchitectures:    noarch

PreReq:       aaa_base

%define font_dir %{_datadir}/fonts/TrueType/freefont

%description
A set of free scalable fonts covering the ISO 10646/Unicode UCS.

%prep
%setup -q -c -n ttf-freefont


%install
install -d ${RPM_BUILD_ROOT}%{font_dir}
install --mode=0444 freefont-%{version}/*.ttf ${RPM_BUILD_ROOT}%{font_dir}
if [ -x /usr/bin/mkfontscale -a -x /usr/bin/mkfontdir ]; then
	cd ${RPM_BUILD_ROOT}%{font_dir} \
	  && /usr/bin/mkfontscale \
	  && /usr/bin/mkfontdir \
	  && /usr/bin/chmod 0444 fonts.dir fonts.scale
fi

%clean
rm -rf $RPM_BUILD_ROOT

%post 
test -x /sbin/SuSEconfig && /sbin/SuSEconfig --module fonts

%postun
test -x /sbin/SuSEconfig && /sbin/SuSEconfig --module fonts

%files
%defattr(-,root,root)
%doc README AUTHORS CREDITS INSTALL ChangeLog
%{font_dir}/*.ttf

%changelog
* Wed Mar 30 2011 - jan.hnatek@oracle.com
- update freefont to 20100919

* Thu Oct 15 2009 - alan.coopersmith@sun.com
- move from /usr/openwin to /usr/share/fonts

* Fri Dec 02 2005 - damien.carbery@sun.com
- Remove %{version} from Source URL as there isn't one on website.

* Wed Feb 16 2005 - dermot.mccluskey@sun.com
- prereq aaa_base

* Sat Oct 30 2004 - laca@sun.com
- test if SuSEconfig is installed before running it, fixes 4911608

* Sat May 01 2004 - laca@sun.com
- install fonts into /usr/openwin on Solaris

* Tue Feb 24 2004 - michael.twomey@sun.com
- Updated to Cinnabar.

* Thu Jul 17 2003 - michael.twomey@sun.com
- Changed to invoke SuSEconfig directly.

* Thu Jul 10 2003 - michael.twomey@sun.com
- Initial release
- Using version numbered copy of freefont-ttf.tar.gz as original is not version numbered.
