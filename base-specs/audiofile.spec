#
# spec file for package audiofile
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#

%define OSR delivered in s10:0.2.6

Name:         audiofile
License:      LGPL v2, MIT, Sun Public Domain, binaries use GPL v2
Group:        System/Library/GNOME
Version:      0.2.7
Release:      1
Distribution: Java Desktop System
Vendor:       68k.org
Summary:      audiofile - 
Source:       http://www.68k.org/~michael/audiofile/audiofile-%{version}.tar.gz
URL:          http://www.68k.org/~michael/audiofile/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/%{name}
Autoreqprov:  on
Requires:     audiofile

%description
The Audio File Library provides a uniform and elegant API for accessing
a variety of audio file formats, such as AIFF/AIFF-C, WAVE, NeXT/Sun
.snd/.au, Berkeley/IRCAM/CARL Sound File, Audio Visual Research, Amiga
IFF/8SVX, and NIST SPHERE. Supported compression formats are currently
G.711 mu-law and A-law and IMA and MS ADPCM.

%prep
%setup -q

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

libtoolize --force
aclocal
autoconf
automake -a -c -f
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
./configure --prefix=%{_prefix}				\
            --libdir=%{_libdir}                         \
            --bindir=%{_bindir}                         \
	    --sysconfdir=%{_sysconfdir} 		\
            --with-esd-dir=%{_libexecdir}		\
            --libexecdir=%{_libexecdir}                 \
	    --mandir=%{_mandir}
make -j$CPUS


%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%{_libdir}/*
%{_bindir}/*

%changelog
* Thu Dec 02 2010 - brian.cameron@oracle.com
- No longer need the unintalled-pc patch since we no longer build ESounD.
* Tue Apr 13 2010 - brian.cameron@sun.com
- Bump to 0.2.7.
* Fri Jan 22 2009 - brian.cameron@sun.com
- Add patch audiofile-02-22_CVE-2008-5824.patch to fix bugster bug 
  #6917569.
* Wed Apr  4 2007 - laca@sun.com
- convert to new style 64-bit build
* Wed Mar 15 2007 - dougs@truemail.co.th
- Removed adding ccdir to PATH
* Wed Feb 28 2007 - laca@sun.com
- update patch to use an uninstalled pkg-config .pc file instead of
  an uninstalled audiofile-config file, because the new esound only
  uses the .pc files
* Sun Feb 18 2007 - laca@sun.com
- create (split from SUNWgnome-audio.spec)
