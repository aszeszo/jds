#
# spec file for package SUNWpulseaudio
#
# includes module(s): pulseaudio
#
# Copyright (c) 2011,2012 Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# bugdb: www.pulseaudio.org/report/
#
%define owner yippi
#
%include Solaris.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use pulseaudio64 = pulseaudio.spec
%endif

%include base.inc
%use pulseaudio = pulseaudio.spec

Name:                      SUNWpulseaudio
IPS_package_name:          library/audio/pulseaudio
Meta(info.classification): %{classification_prefix}:System/Multimedia Libraries
Summary:                   %{pulseaudio.summary}
URL:                       http://www.pulseaudio.org/
Version:                   %{pulseaudio.version}
Source:                    %{name}-manpages-0.1.tar.gz
License:                   %{pulseaudio.license}
SUNW_BaseDir:              %{_basedir}
SUNW_Copyright:            %{name}.copyright
BuildRoot:                 %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc

# Needed to build tests.
BuildRequires: library/desktop/gtk2

# Optional dependencies
BuildRequires: system/library/libdbus-glib
BuildRequires: library/fftw-3

BuildRequires: codec/speex
BuildRequires: gnome/config/gconf
BuildRequires: library/gc
BuildRequires: library/json-c
BuildRequires: library/libtool/libltdl
BuildRequires: library/libsndfile
BuildRequires: library/security/openssl
BuildRequires: system/network/avahi
Requires:      library/security/openssl

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%if %build_l10n
%package l10n
IPS_package_name:        library/audio/pulseaudio/l10n
Summary:                 %{summary} - l10n files
SUNW_BaseDir(relocate_from:%{_prefix}): %{_gnome_il10n_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:                %{name}
%endif

%prep
rm -rf %name-%version
mkdir %name-%version
%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%pulseaudio64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%pulseaudio.prep -d %name-%version/%{base_arch}

cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -

%build
# Use no higher than -xO2 on sparc.
#
%ifarch sparc
export PA_OPTFLAGS64=`/usr/bin/echo %optflags64 | /usr/gnu/bin/sed -e 's/-xO./-xO2/'`
export PA_OPTFLAGS=`/usr/bin/echo %optflags | /usr/gnu/bin/sed -e 's/-xO./-xO2/'`
%else
export PA_OPTFLAGS64=`/usr/bin/echo %optflags64`
export PA_OPTFLAGS=`/usr/bin/echo %optflags`
%endif

%ifarch amd64 sparcv9
export CFLAGS="$PA_OPTFLAGS64 -xc99 -I/usr/include/gc -KPIC"
export SOLARIS_PULSE_ARGS="--disable-avahi"

# Need to add -Wl,-z,now and -Wl,-z-nodelete and remove -Wl,-zignore for
# PulseAudio to build.
#
%if %debug_build
export SOLARIS_PULSE_LDFLAGS="-Wl,-z,now -Wl,-z,nodelete -lxnet -lsocket -lgobject-2.0"
%else
export SOLARIS_PULSE_LDFLAGS="-Wl,-zcombreloc -Wl,-Bdirect -Wl,-z,now -Wl,-z,nodelete -lxnet -lsocket -lgobject-2.0"
%endif

%pulseaudio64.build -d %name-%version/%_arch64
%endif

# Now build 32-bit.
#
export CFLAGS="$PA_OPTFLAGS -xc99 -I/usr/include/gc -KPIC"
export SOLARIS_PULSE_ARGS=""

%if %debug_build
export SOLARIS_PULSE_LDFLAGS="-Wl,-z,now -Wl,-z,nodelete -lxnet -lsocket -lgobject-2.0"
%else
export SOLARIS_PULSE_LDFLAGS="-Wl,-zcombreloc -Wl,-Bdirect -Wl,-z,now -Wl,-z,nodelete -lxnet -lsocket -lgobject-2.0"
%endif

%pulseaudio.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%pulseaudio64.install -d %name-%version/%_arch64
%endif

%pulseaudio.install -d %name-%version/%{base_arch}

# Remove .la and .a file as we do not ship them.
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
find $RPM_BUILD_ROOT -name "*.a" -exec rm {} \;

# Remove udev features since they are not supported on Solaris.
rm -fR $RPM_BUILD_ROOT/lib

# Remove empty directory.
rm -fR $RPM_BUILD_ROOT%{_libdir}/pulse

# Remove esdcompat.  We don't use esd on Solaris.
rm -fR $RPM_BUILD_ROOT%{_bindir}/esdcompat
rm -fR $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/esdcompat
rm -fR $RPM_BUILD_ROOT%{_mandir}/man1/esdcompat.1

# The PulseAudio pulse-daemon.conf.5 and pulse-client.conf.5 manpages do not
# format readably on Solaris, so SGML versions of these manpages were written
# and are installed that format reasonably.
#
rm -fR $RPM_BUILD_ROOT%{_mandir}/man5/pulse-daemon.conf.5
rm -fR $RPM_BUILD_ROOT%{_mandir}/man5/pulse-client.conf.5
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%doc %{base_arch}/pulseaudio-%{pulseaudio.version}/README
%doc(bzip2) %{base_arch}/pulseaudio-%{pulseaudio.version}/LICENSE
%doc(bzip2) %{base_arch}/pulseaudio-%{pulseaudio.version}/GPL
%doc(bzip2) %{base_arch}/pulseaudio-%{pulseaudio.version}/LGPL
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/pa*
%{_bindir}/pulseaudio
%{_bindir}/start-pulseaudio*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/cmake
%{_libexecdir}/pulse*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/pa*
%{_bindir}/%{_arch64}/pulseaudio
%{_bindir}/%{_arch64}/start-pulseaudio*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%{_libdir}/%{_arch64}/cmake
%{_libexecdir}/%{_arch64}/pulse*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_docdir}
%{_datadir}/vala
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%attr (0755, root, sys) %dir %{_sysconfdir}/pulse
%ips_tag(preserve=true) %{_sysconfdir}/pulse/client.conf
%ips_tag(preserve=true) %{_sysconfdir}/pulse/daemon.conf
%ips_tag(preserve=true) %{_sysconfdir}/pulse/default.pa
%ips_tag(preserve=true) %{_sysconfdir}/pulse/system.pa
%{_sysconfdir}/xdg

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%endif

%changelog
* Tue May 15 2012 - Brian Cameron  <brian.cameron@oracle.com>
- Fix Requires and l10n IPS package name.
* Fri May 04 2012 - Brian Cameron  <brian.cameron@oracle.com>
- Now set optimization -xO2 on sparc to fix CR #7166622.
* Sun Oct 02 2011 - Brian Cameron  <brian.cameron@oracle.com>
- Bump to 1.0.
* Tue Sep 28 2011 - Brian Cameron  <brian.cameron@oracle.com>
- Initial spec with version 0.99.4.
