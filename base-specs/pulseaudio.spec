#
# spec file for package pulseaudio
#
# Copyright (c) 2011, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
# bugdb: bugzilla.freedesktop.org
#

%define src_name pulseaudio
%define src_url http://freedesktop.org/software/pulseaudio/releases

Name:                    pulseaudio
Summary:                 Sample Rate Converter for audio
Version:                 1.1
License:                 LGPLv2.1, MIT, Sun Public Domain
Source:                  %{src_url}/%{src_name}-%{version}.tar.gz
# date:2011-09-27 owner:yippi type:bug bugid:41537
Patch1:                  pulseaudio-01-esdcompat.diff
# This patch is very rough, but gets the code to compile.
# date:2011-09-27 owner:yippi type:bug bugid:41538
Patch2:                  pulseaudio-02-solaris.diff
# date:2011-10-05 owner:yippi type:feature bugid:41539
Patch3:                  pulseaudio-03-fixlink.diff
# /usr/include/sys/stream.h also defines module_info.
# date:2011-10-14 owner:yippi type:bug bugid:41823
Patch4:                  pulseaudio-04-gconf.diff
# date:2011-10-14 owner:yippi type:bug
Patch5:                  pulseaudio-05-shm.diff
# date:2011-10-31 owner:yippi type:branding
# This patch configures PulseAudio for Solaris, by enabling the OSSv4 module
# for example, instead of using the SunAudio (solaris) module.
Patch6:                  pulseaudio-06-configure.diff
# date:2011-11-30 owner:yippi type:bug
Patch7:                  pulseaudio-07-sada.diff
# date:2011-12-13 owner:yippi type:bug
Patch8:                  pulseaudio-08-oss4.diff
# date:2011-10-06 owner:yippi type:feature
Patch9:                  pulseaudio-09-amd64.diff
# date:2012-05-14 owner:yippi type:bug
Patch10:                 pulseaudio-10-endian.diff
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n pulseaudio-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

perl -pi -e 's,/bin/sh,/bin/ksh,' src/daemon/esdcompat.in

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

# Build PulseAudio
# Need to specify /usr/include/gc as an include directory since the atomic_ops
# headers are delivered there on Solaris.
#
export ACLOCAL=aclocal-1.11
export AUTOMAKE=automake-1.11
export CPPFLAGS="-xc99"
export LDFLAGS="$SOLARIS_PULSE_LDFLAGS"

autoreconf --force --install

# We build PulseAudio without samplerate or bluez support since these are GPL
# and it is not desirable to build PulseAudio with GPL code.  Bluez is not 
# available anyway yet in Solaris, but disabling it just to ensure that it does
# not build if bluez is added.
#
# We must turn off avahi for amd64 since avahi 64-bit is not available.
./configure --prefix=%{_prefix}         \
            --mandir=%{_mandir}         \
            --bindir=%{_bindir}         \
            --libdir=%{_libdir}         \
            --libexecdir=%{_libexecdir} \
            --sysconfdir=%{_sysconfdir} \
            --disable-samplerate        \
            --disable-bluez             \
            $SOLARIS_PULSE_ARGS

make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir}/ -name "*.a" -exec rm {} \; -print -o -name  "*.la" -exec rm {} \; -print

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue May 15 2012 - Brian Cameron  <brian.cameron@oracle.com>
- Add patch pulseaudio-10-endian.diff.
* Fri May 04 2012 - Brian Cameron  <brian.cameron@oracle.com>
- Now set optimization -xO2 on sparc to fix CR #7166622.
* Thu Oct 20 2011 - Brian Cameron <brian.cameron@oracle.com>
- Bump to 1.1.
* Thu Oct 06 2011 - Brian Cameron <brian.cameron@oracle.com>
- Split from SUNWpulseaudio.spec and now build amd64.  Add the
  pulseaudio-05-amd64.diff patch.

