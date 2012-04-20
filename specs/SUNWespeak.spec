#
# spec file for package SUNWespeak
#
# Copyright (c) 2008, 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner liyuan
%define OSR 8874:1.37

%include Solaris.inc

%define src_name espeak
%define src_url http://downloads.sourceforge.net/%{src_name}
# remember to update the Version tag but make sure it's IPS compliant,
# so no leading 0-s allowed.  1.44.05 should be 1.44.0.5
%define tarball_version 1.44.05

Name:		SUNWespeak
IPS_package_name: library/speech/espeak
Meta(info.classification): %{classification_prefix}:Applications/Universal Access
Summary:	eSpeak - compact open source software speech synthesizer
Version:	1.44.0.5
License:	GPL v3
Source:		%{src_url}/%{src_name}-%{tarball_version}-source.zip
Source1:        %{name}-manpages-0.1.tar.gz
# date:2008-08-15 owner:ww36193 type:bug
Patch1:         espeak-01-makefile.diff
# date:2010-10-27 owner:yippi type:bug
Patch2:         espeak-02-samplerate.diff
# date:2010-12-28 owner:liyuan type:bug
Patch3:         espeak-03-Wall.diff
SUNW_BaseDir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:	%{_tmppath}/%{name}-%{tarball_version}-build

%include default-depend.inc
%include desktop-incorporation.inc

Requires: SUNWgccruntime
BuildRequires: SUNWgcc
BuildRequires: compress/unzip
BuildRequires: system/header
BuildRequires: library/audio/pulseaudio
BuildRequires: library/gc
BuildRequires: library/json-c
BuildRequires: library/libsndfile

BuildRequires: system/library/c++-runtime
BUildRequires: system/library/math

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires: %name

%prep
%setup -q -n %{src_name}-%{tarball_version}-source
%patch1 -p1
%patch2 -p1
%patch3 -p1
gzcat %SOURCE1 | tar xf -

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi
%ifarch sparc
%define endian_macro "-DBYTE_ORDER=BIG_ENDIAN"
cd platforms/big_endian
make -j$CPUS CFLAGS="%{endian_macro}"
./espeak-phoneme-data ../../espeak-data ../../espeak-data
cd ../..
%else
%define endian_macro ""
%endif
cd src
make -j$CPUS EXTRA_LIBS=-lm AUDIO=pulseaudio CXXFLAGS="-norunpath -O2 %{endian_macro}"
make install EXTRA_LIBS=-lm AUDIO=pulseaudio DESTDIR=$RPM_BUILD_ROOT CXXFLAGS="-norunpath -O2 %{endian_macro}"
rm $RPM_BUILD_ROOT/%{_libdir}/lib*.a

%install
#Install manpages
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%src_name-%tarball_version-source/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/*

%files devel
%defattr (-, root, bin)
%{_includedir}

%changelog
* Fri Mar 02 2012 - brian.cameron@oracle.com
- Now depends on PulseAudio.
* Tue Jul 26 2011 - dave.lin@oracle.com
- Added '-norunpath' in CXXFLAGS to fix 6754651.
* Thu Dec 30 2010 - brian.cameron@oracle.com
- The Version was not the same as tarball_version.  Corrected so they are now
  both 1.44.05.
* Tue Nov 09 2010 - lee.yuan@oracle.com
- Fix build error on sparc.
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 1.44.05.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Wed Sep 23 2009 - william.walker@sun.com
- Add patch to fix yet another hang - sourceforge:2860912 bugzilla:595336
  This should be fixed in 1.41.03 when it is released, so the patch can be
  removed when upreving to 1.41.03.
* Tue Aug 28 2009 - william.walker@sun.com
- Bump to 1.41.01.  This resolves bgo#580389 - Orca hangs
  when clicking "Ok" or "Apply" button in Orca Preference dialog
  and doo#10858 - eSpeak_Synchronize hangs Orca
* Fri Aug 21 2009 - li.yuan@sun.com
- Change owner to liyuan.
* Mon Aug 17 2009 - william.walker@sun.com
- Add Vendor and License
* Tue Jul 28 2009 - christian.kelly@sun.com
- Bump to 1.40.02.
* Mon May 04 2009 - brian.cameron@sun.com
- Bump to 1.40.
* Tue Feb 10 2009 - halton.huo@sun.com
- Add dependency on SUNWlibC and SUNWlibmsr, CR #6755918
* Fri Sep 19 2008 - Willie Walker
- Add BuildRequires: SUNWaudh
* Mon Sep 02 2008 - Harry Lu
- Add bug ID for espeak-02-endian.diff
* Fri Aug 29 2008 - Willie Walker
- Fix SPARC build endian-ness
* Thu Aug 21 2008 - Dermot McCluskey
- added manpages and file header
* Wed Aug 20 2008 - Willie Walker
- Migrate to JDS (SFEespeak.spec to SUNWespeak.spec)
* Tue Aug 12 2008 - Willie Walker
- Port to SunStudio (thanks Brian Cameron!)
* Tue Apr 15 2008 - Willie Walker
- Upgrade to version 1.37 which contains direct SADA support and eliminates
  all PulseAudio and other dependencies.
* Tue Jan 29 2008 - Willie Walker
- Initial spec


