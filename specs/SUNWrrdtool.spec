#
# spec file for package SUNWrrdtool
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner stephen
#

%include Solaris.inc

%define OSR 8313:1.2.19

%define version 1.4.3

Name:                SUNWrrdtool
IPS_package_name:    image/rrdtool
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
Summary:             Data analysis tool generating graphical representations
License:             GPL v2
Version:             %{version}
Source:              http://oss.oetiker.ch/rrdtool/pub/rrdtool-%{version}.tar.gz
URL:                 http://oss.oetiker.ch/rrdtool/
SUNW_Copyright:      %{name}.copyright
SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlxmlr
Requires: SUNWpango
Requires: SUNWgccruntime
Requires: SUNWlua
BuildRequires: text/groff
BuildRequires: SUNWpango-devel

%prep
%setup -q -n rrdtool-%{version}

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export LDFLAGS="%_ldflags"

# FIXME: Punted on building w/ perl, ruby and python enabled...

./configure --prefix=%{_prefix}  \
            --mandir=%{_mandir} \
            --disable-perl \
            --disable-python \
            --disable-ruby \
	    --enable-tcl \
	    --disable-libintl \
            --enable-static=no

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm ${RPM_BUILD_ROOT}%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*.so*
%{_libdir}/lua
%{_libdir}/rrdtool
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man1/*
%{_mandir}/man3/*
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/*
%dir %attr (0755, root, other) %{_datadir}/rrdtool
%{_datadir}/rrdtool/*

%changelog
* Tue Jun 01 2010 - brian.cameron@oracle.com
- Bump to 1.4.3.
* Tue Jun 02 2009 - dave.lin@sun.com
- fixed dependency issue(CR6845030).
* Tue Jan 13 2009 - dave.lin@sun.com
- Fixed attribute issue /usr/lib/pkgconfig.
* Mon Jan 12 2009 - stephen.browne@sun.com
- Fix owner, uprev tarball, fix build issues, enable tcl, compile with SunStudio
* Thu Mar 15 2008 - lin.ma@sun.com
- Add SUNWgccruntime dependency.
* Tue Mar 11 2008 - damien.carbery.com
- Add SUNWgnome-base-libs/-devel dependencies so that pango found.
* Mon Mar  3 2008 - damien.carbery.com
- Define version and tarball_version so that pkg version is only numeric.
* Wed Feb 20 2008 - takao.fujiwara@sun.com
- Use 1.3beta4 to support cairo/pango.
* Fri Feb 15 2008 - dermot.mccluskey@sun.com
- use %gcc_optflags
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version



