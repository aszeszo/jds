#
# spec file for package SUNWcompiz-fusion-main.spec
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc 

%include Solaris.inc

%define OSR 8297:1.6.2

%define src_name compiz-plugins-main

Name:                    SUNWcompiz-fusion-main
IPS_package_name:        desktop/compiz/plugin/compiz-fusion-main
Meta(info.classification): %{classification_prefix}:Applications/Plug-ins and Run-times
License:                 GPL v2
Summary:                 main effects plugins for compiz
Version:                 0.8.4
Source:			 http://releases.compiz.org/%{version}/%{src_name}-%{version}.tar.bz2
Source1:                 l10n-configure.sh
Patch1:			 compiz-fusion-main-01-solaris-port.diff
Patch2:			 compiz-fusion-main-02-compvector.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRequires: consolidation/desktop/gnome-incorporation

%ifnarch sparc
# these packages are only available on x86
# =========================================

BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWcompiz-bcop
BuildRequires: SUNWcompiz-devel
BuildRequires: SUNWxorg-mesa
Requires: SUNWcompiz
Requires: SUNWxorg-mesa
# the base pkg should depend on the -root subpkg, if there is one:
Requires: %{name}-root
Requires: SUNWdesktop-cache

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package devel
Summary:		 %summary - developer files
sUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:		 %name

%package l10n
Summary:                 %summary - l10n files
Requires:                %{name}

%prep
%setup -q -n %{src_name}-%version
%patch1 -p1
%patch2 -p1
# Ensure option code is regenerated by bcop XSLT
find . -name '*_options.c' -o -name '*_options.h' -exec rm -f {} \;

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

intltoolize --copy --force --automake

bash -x %SOURCE1 --enable-copyright

rm -f ltmain.sh
libtoolize --force
aclocal
autoheader
automake -a -c -f
autoconf

export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
export LDFLAGS="%{_ldflags}"
export MSGFMT="/usr/bin/msgfmt"

./configure --prefix=%{_prefix}			\
	    --bindir=%{_bindir}			\
	    --sysconfdir=%{_sysconfdir}		\
	    --includedir=%{_includedir}		\
	    --mandir=%{_mandir}			\
            --libdir=%{_libdir}			\
	    --enable-schemas 

make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/compiz/*.la
rm $RPM_BUILD_ROOT%{_libdir}/compiz/*.a

%post
%restart_fmri gconf-cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/compiz
%{_libdir}/compiz/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_datadir}/compiz
%{_datadir}/compiz/*
%doc AUTHORS po/ChangeLog
%doc(bzip2) COPYING
%dir %attr (0755, root, other) %{_datadir}/doc

%files root
%defattr (0755, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755,root,other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%files l10n
%defattr (-, root, other)
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/locale

# endif for "ifnarch sparc"
%endif

%changelog
* Tue Jan 12 2010 - dave.lin@sun.com
- Remove OpenGL check, use 'BuildRequires: SUNWxorg-mesa' instread.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Wed Sep 16 2008 - matt.keenn@sun.com
- Update copyright
* Wed May 21 2008 - damien.carbery@sun.com
- Add Build/Requires: SUNWxorg-mesa after check-deps.pl run.
* Mon Apr 07 2008 - damien.carbery@sun.com
- Break the build if the openGL headers and libraries are not present on the
  machine.
* Wed Mar 26 2008 - dave.lin@sun.com
- change to not build this component on SPARC
* Thu Mar 20 2008 - takao.fujiwara@sun.com
- Add compiz-fusion-main-02-po.diff for ar, es, hu, ko, pt_BR, ru
* Sun Mar 09 2008 - erwann@sun.com
- add standard gconf script
* Wed Feb 20 2008 - damien.carbery@sun.com
- Fix l10n build.
* Mon Oct 29 2007 - trisk@acm.jhu.edu
- Bump to 0.6.0
* Wed Sep 19 2007 - trisk@acm.jhu.edu
- Drop unnecessary patch2
* Fri Sep 07 2007 - trisk@acm.jhu.edu
- Fix rules, add patch2
* Wed Aug 29 2007 - erwann@sun.com
- Initial spec


