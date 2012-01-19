#
# spec file for package SUNWxdg-user-dirs-gtk
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner lin
#

%include Solaris.inc

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:                SUNWxdg-user-dirs-gtk
IPS_package_name:    desktop/xdg/xdg-user-dirs-gtk
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:             GTK Frontend for handling user directories
Version:             0.8
License:             GPL v2
Source:              http://ftp.gnome.org/pub/gnome/sources/xdg-user-dirs-gtk/%{version}/xdg-user-dirs-gtk-%{version}.tar.bz2
Source1:           	 %{name}-manpages-0.1.tar.gz
Source2:                 l10n-configure.sh
SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc

Requires: SUNWgtk2
Requires: %name-root
Requires: SUNWxdg-user-dirs
BuildRequires: SUNWgtk2-devel

%package l10n
Summary:             %{summary} - l10n files
Requires:            %{name}

%package root
Summary:             %{summary} - / filesystem
SUNW_BaseDir:        /
%include default-depend.inc
%include gnome-incorporation.inc

%prep
%setup -c -q -n %{name}-%{version}
#unzip the manpage tarball
cd %{_builddir}/%{name}-%{version}
gzcat %SOURCE1 | tar xf -
cd ..

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

cd xdg-user-dirs-gtk-%{version}
intltoolize -c -f --automake

bash -x %SOURCE2 --enable-copyright

aclocal
autoconf
automake -a -c -f
./configure --prefix=%{_prefix}  \
            --bindir=%{_bindir} \
            --sysconfdir=/etc

make -j$CPUS
cd ..

%install
rm -rf $RPM_BUILD_ROOT
cd xdg-user-dirs-gtk-%{version}
make install DESTDIR=$RPM_BUILD_ROOT
#Install manpages
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_bindir}
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%doc -d xdg-user-dirs-gtk-%{version} AUTHORS README NEWS
%doc(bzip2) -d xdg-user-dirs-gtk-%{version} COPYING ChangeLog po/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%files root
%defattr (-, root, sys)
%dir %attr (0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/*

%changelog
* Fri Sep 12 2008 - matt.keenn@sun.com
- Update copyright
* Tue Sep 09 2008 - christian.kelly@sun.com
- Bump to 0.8, change from gz to bz2.
* Fri Apr 04 2008 - darren.kenny@sun.com
- Add manpages
* Fri Feb 22 2008 - darren.kenny@sun.com
- initial version - 0.7



