#
# spec file for package SUNWgtkspell
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
#

%define OSR 9389:2.x

%include Solaris.inc
Name:                    SUNWgtkspell
IPS_package_name:        library/desktop/gtkspell
Meta(info.classification): %{classification_prefix}:Applications/Accessories
Summary:                 Gtkspell provides word-processor-style highlighting and replacement of misspelled words in a GtkTextView widget.
License:                 GPL v2
Version:                 2.0.16
Source:                  http://gtkspell.sourceforge.net/download/gtkspell-%{version}.tar.gz
Source1:                 l10n-configure.sh
Source2:                 %{name}-manpages-0.1.tar.gz
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
Requires:                SUNWgtk2
Requires:		 SUNWgnome-spell
BuildRequires:           SUNWgtk2-devel
BuildRequires:		 SUNWgnome-spell-devel

Patch1:                  gtkspell-01-fixxref-modules.diff

%package devel
Summary:                 Gtkspell - developer files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name
Requires: SUNWgtk2-devel
Requires: SUNWgnome-spell-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n gtkspell-%version
cd %{_builddir}/gtkspell-%version
gzcat %SOURCE2 | tar xf -
%patch1 -p0

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS="%optflags"
export CPPFLAGS="%optflags"
export LDFLAGS="%_ldflags"

intltoolize --force --copy

sh %SOURCE1 --enable-copyright

aclocal $ACLOCAL_FLAGS
libtoolize --force
autoheader
automake -a -c -f
autoconf

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/*.la
cd %{_builddir}/gtkspell-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc README AUTHORS
%doc(bzip2) COPYING ChangeLog
%doc(bzip2) po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/gtk-doc
%dir %attr (0755, root, bin) %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Jan 27 2010 - christian.kelly@sun.com
- Add gtkspell-01-fixxref-modules to fix build issue.
* Thu Dec 17 2009 - ke.wang@sun.com
- Bump to 2.0.16
* Fri Sep 19 2008 - dave.lin@sun.com
- Set the attribute of the dir %{_datadir}/doc in base pkg.
* Wed Sep 17 2008 - jim.li@sun.com
- Revised new format copyright file
* Thu Jul 03 2008 - Jim Li
- Copied from SFEgtkspell and rename to SUNWgtkspell
* Sun Mar 02 2008 - Petr Sobotka
- Source tar file was moved
* Wed July 26 2006 - lin.ma@sun.com
- Initial spec file



