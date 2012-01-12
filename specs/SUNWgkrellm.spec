#
# spec file for package SUNWgkrellm
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby
#

%include Solaris.inc

%define OSR 9466:2.x

Name:                SUNWgkrellm
IPS_package_name:    desktop/system-monitor/gkrellm
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:             Popular (ubiquitous) Gtk-based system monitor
Version:             2.3.4
Source:              http://members.dslextreme.com/users/billw/gkrellm/gkrellm-%{version}.tar.bz2
Source1:             gkrellm.desktop
Source2:             gkrellm.png
# date:2008-09-4 owner:jouby type:bug
Patch1:              gkrellm-01-manpage.diff
# date:2008-09-4 owner:jouby type:feature 
Patch2:              gkrellm-02-battery.diff
# date:2008-10-10 owner:jouby type:bug
Patch3:              gkrellm-03-log.diff
SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
License:             GPL v3
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       SUNWgtk2
Requires:       SUNWhal
BuildRequires:  SUNWdbus-glib
BuildRequires:  SUNWdbus-libs
BuildRequires:  SUNWgtk2-devel
BuildRequires:  SUNWdbus-glib-devel
BuildRequires:  SUNWgnu-gettext
BuildRequires:  SUNWhal
BuildRequires:  SUNWgcc

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name

%prep
%setup -q -n gkrellm-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%arch_ldadd %ldadd ${EXTRA_LDFLAGS} -L/usr/sfw/lib -R/usr/sfw/lib"
export LD_OPTIONS="-L/usr/sfw/lib -R/usr/sfw/lib"

make -j$CPUS enable_nls=1 LOCALEDIR=/usr/share/locale solaris

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} install

cd po
make do_nls=1 INSTALL_PREFIX=$RPM_BUILD_ROOT install
cd ..

cd src
#FIXME: convert doesn't work on snv_150
#convert gkrellm.ico gkrellm.png
#mv gkrellm-8.png gkrellm.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
#cp gkrellm.png $RPM_BUILD_ROOT/usr/share/pixmaps
cp %{SOURCE2} $RPM_BUILD_ROOT/usr/share/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%doc(bzip2) COPYING COPYRIGHT CREDITS Changelog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gkrellm
%{_bindir}/gkrellmd
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/gkrellm.1
%{_mandir}/man1/gkrellmd.1

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_includedir}/gkrellm2
%{_includedir}/gkrellm2/*.h
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/gkrellm.pc

%changelog
* Wed Jan 27 2010 - brian.cameron@sun.com
- Bump to 2.3.4.  Remove upstream patch gkrellm-01-ldflags.diff.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change spec and patch owner to jouby
* Thu Mar 05 2009 - brian.cameron@sun.com
- Change SUNWdbus-bindings to SUNWdbus-glib.
* Web Mar 04 2009 - chris.wang@sun.com
- Transfer the ownership to bewitche
* Thu Feb 12 2009 - halton.huo@sun.com
- Update Requires/BuildRequires after running check-deps.pl, fix CR #6798922
* Sat Jan 17 2009 - dave.lin@sun.com
- Change "Requires: SUNWgnu-gettext"to "BuildRequires: SUNWgnu-gettext".
* Wed. Oct. 22 2008 - Henry Zhang <hua.zhang@sun.com>
- Bump to 2.3.2
* Wed. Sep 17 2008 - Henry Zhang <hua.zhang@sun.com>
- Delete locale files if not build_l10n
* Fri Sep 12 2008 - takao.fujiwara@sun.com
- Add l10n package.
* Fri Sep 12 2008 - Henry Zhang <hua.zhang@sun.com>
- Add  %doc to %files for copyright
* Wed. Sep. 3 2008 - hua.zhang@sun.com
- Updated spec file, bump to 2.3.1, and add patches.
* Sun Nov 18 2007 - daymobrew@users.sourceforge.net
- Change LDFLAGS to work for gcc. Add patch, 01-ldflags, to get LDFLAGS into
  the build.
* Sun Nov 18 2007 - daymobrew@users.sourceforge.net
- Enable building with either SUNWgnu-gettext or SFEgettext.
* Fri Apr 20 2007 - dougs@truemail.co.th
- Added SFW libs (LDFLAGS,LD_OPTIONS)
* Mon Mar 19 2007 - dougs@truemail.co.th
- Fixed -fno-omit-frame-pointer flag
* Sun Mar 11 2007 - Eric Boutilier
- Initial spec



