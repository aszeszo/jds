#
# spec file for package SUNWgnome-dialog
#
# includes module(s): zenity
#
# Copyright (c) 2004, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner migi
#
%include Solaris.inc

%use zenity = zenity.spec

Name:                    SUNWgnome-dialog
IPS_package_name:        gnome/zenity
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:                 GNOME graphical dialog box generator
Version:                 %{zenity.version}
Source:                  %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{zenity.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlibglade
BuildRequires: runtime/perl-512
Requires: SUNWgnome-panel
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWgnome-panel-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
rm -rf %name-%version
mkdir %name-%version
%zenity.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
export PKG_CONFIG_PATH=%{_pkg_config_path}
export PERL=/usr/perl5/bin/perl
export CFLAGS="%optflags -I%{_includedir}"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%_ldflags -lX11"
%zenity.build -d %name-%version

%install
%zenity.install -d %name-%version
rm -rf $RPM_BUILD_ROOT%{_localstatedir}
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc -d zenity-%{zenity.version} README AUTHORS COPYING THANKS
%doc(bzip2) -d zenity-%{zenity.version} ChangeLog help/ChangeLog po/ChangeLog NEWS
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/gnome/help/zenity/C
%{_datadir}/zenity
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/gnome
%attr (-, root, other) %{_datadir}/locale
%{_datadir}/gnome/help/zenity/[a-z]*

%changelog
* Fri May 11 2012 - brian.cameron@oracle.com
- Fix packaging after updating to 3.4.0.
* Fri Apr  3 2009 - laca@sun.com
- stop using postrun
* Fri Sep 19 2008 - christian.kelly@sun.com
- Set permissions on /usr/share/doc.
* Wed Sep 10 2008 - Michal.Pryc@Sun.Com
- Add %doc to %files for new copyright
* Tue Jun 24 2008 - damien.carbery@sun.com
- Remove "-lgailutil" from LDFLAGS. Root cause found in gtk+: bugzilla 536430.
* Thu Jun 05 2008 - damien.carbery@sun.com
- Add "-lgailutil" to LDFLAGS so that libgailutil is linked in when
  libgnomecanvas is linked. libgnomecanvas.so includes some gail functions.
* Wed Oct 10 2007 - damien.carbery@sun.com
- Remove 'Requires: SUNWgnome-doc-utils' as it is only used during building;
  change SUNWgnome-doc-utils-devel to SUNWgnome-doc-utils to match change in
  SUNWgnome-doc-utils.spec.
* Fri Sep 28 2007 - laca@sun.com
- delete Nevada X dep
* Mon May 21 2007 - laca@sun.com
- change SUNWgnome-panel-devel dep from Requires to BuildRequires
* Fri Sep 01 2006 - Matt.Keenan@sun.com
- New Manpage tarball
* Sat Aug 12 2006 - laca@sun.com
- delete some unnecessary env variables
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Tue May 09 2006 - damien.carbery@sun.com
- Change BuildRequires to SUNWgnome-doc-utils as the -share package has been
  merged into the base package.
* Sun Feb 18 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Thu Jan 05 2006 - damien.carbery@sun.com
- Remove empty /var/lib/scrollkeeper dir structure.
* Fri Dec 02 2005 - damien.carbery@sun.com
- Add Build/Requires SUNWgnome-doc-utils/-share for gnome-doc-utils.make.
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Tue Sep 13 2005 - laca@sun.com
- add unpackaged files
* Tue Aug 30 2005 - damien.carbery@sun.com
- Remove some help files from %files.
* Tue May 24 2005 - brian.cameron@sun.com
- Bump to 2.10.
* Thu Oct 28 2004 - kazuhiko.maekawa@sun.com
- Updated l10n help tarball and added pt_BR
* Wed Oct 06 2004 - matt.keenan@sun.com
- added l10n help files section
* Sat Oct 02 2004 - laca@sun.com
- added %pkgbuild_postprocess
* Mon Aug 23 2004 - laca@sun.com
- s/SUNWpl5u/SUNWperl584usr/
* Sat Jun 26 2004  shirley.woo@sun.com
- Changed install location to /usr/...
* Wed Jun  2 2004 - takao.fujiwara@sun.com
- Added %{_datadir}/locale to install l10n messages
* Wed Mar 24 2004 - brian.cameron@sun.com
- Added SGML man page integration
* Mon Mar 01 2004 - <laca@sun.com>
- define PERL5LIB.

