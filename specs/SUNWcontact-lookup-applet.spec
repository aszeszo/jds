#
# spec file for package SUNWcontact-lookup-applet
#
# includes module(s): contact-lookup-applet
#
%define owner jedy
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%include Solaris.inc

%define OSR 9206:0.x

Name:                    SUNWcontact-lookup-applet
IPS_package_name:        gnome/applet/contact-lookup-applet
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:                 Contact lookup applet
Version:                 0.17
URL:                     http://burtonini.com
License:                 GPL v2
Source:                  http://burtonini.com/computing/contact-lookup-applet-%{version}.tar.gz
Source1:                 l10n-configure.sh
# date:2008-06-25 owner:jedy type:branding
Patch1:                  contact-lookup-applet-01-suncc.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:               SUNWlibglade
Requires:               SUNWgnome-libs
Requires:               SUNWevolution-data-server
Requires:               SUNWgnome-panel
BuildRequires:          SUNWlibglade-devel
BuildRequires:          SUNWgnome-libs-devel
BuildRequires:          SUNWevolution-data-server-devel
BuildRequires:          SUNWgnome-panel-devel
BuildRequires:          SUNWgnome-common-devel
BuildRequires:          SUNWgnome-keyring
BuildRequires:          SUNWlibgnome-keyring
 
%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n contact-lookup-applet-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags" 
export LDFLAGS="%_ldflags"

libtoolize --copy --force
intltoolize --force --copy --automake

sh %SOURCE1 --enable-copyright

aclocal
automake -a -f
autoconf -f

./configure --prefix=%{_prefix}  \
            --libexecdir=%{_libexecdir}

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS
%doc(bzip2) ChangeLog COPYING
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755,root,bin) %{_libdir}
%{_libdir}/*
%dir %attr(0755, root, sys) %{_datadir}
%{_datadir}/lookup-applet

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 0.17.
* Wed Nov 05 2008 - Jedy Wang (jedy.wang@sun.com)
- Update license.
* Tue Sep 16 2008 - Jedy Wang (jedy.wang@sun.com)
- Add copyright files.
* Mon Jun 30 2008 - Jedy Wang (jedy.wang@sun.com)
- Updated patch comment
* Wed Jun 25 2008 - Jedy Wang (jedy.wang@sun.com)
- Moved from spec-files-extra
* Fri May 30 2008 - Jedy Wang (jedy.wang@sun.com)
- Initial spec



