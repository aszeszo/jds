#
# spec file for package SUNWcompiz-bcop
#
# Copyright 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
%define owner erwannc 
#

####################################################################
#  beryl compiz XML option parser
####################################################################

%include Solaris.inc

%define OSR 8297:1.6.2

%define src_name compiz-bcop

Name:                    SUNWcompiz-bcop
Summary:                 beryl compiz XML option parser
License:                 GPL v2
Version:                 0.8.4
Source:			 http://releases.compiz.org/%{version}/%{src_name}-%{version}.tar.bz2
Patch1:			 compiz-bcop-01-solaris-port.diff
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Requires:		 SUNWgnugetopt
Requires:		 SUNWlxsl
Requires:                SUNWbash
BuildRequires:		 SUNWgnugetopt
BuildRequires:           SUNWgnome-common-devel
BuildRequires:		 library/libxslt
%include default-depend.inc
%include gnome-incorporation.inc

%prep
%setup -q -n %{src_name}-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

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
	    --with-getopt=/usr/gnu/bin/getopt

make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr(0755, root, sys) %{_datadir}
%{_datadir}/bcop
%doc(bzip2) COPYING
%dir %attr (0755, root, other) %{_datadir}/doc

%changelog
* Wed Sep 17 2008 - matt.keenn@sun.com
- Update copyright
* Wed Jun 18 2008 - damien.carbery@sun.com
- Add Requires SUNWbash as /usr/bin/bcop is a bash script.
* Tue May 27 2008 - damien.carbery@sun.com
- Add BuildRequires SUNWgnome-common-devel and Build/Requires SUNWlxsl/-devel
  to prevent build error.
* Wed Feb 13 2008 - erwann@sun.com
- remove SFE deps and added to SFO
* Mon Oct 29 2007 - trisk@acm.jhu.edu
- Bump to 0.6.0
* Sat Sep 08 2007 - trisk@acm.jhu.edu
- Change XSLT for plugins
* Fri Aug 31 2007 - trisk@acm.jhu.edu
- Fix dir attributes
* Tue Aug 28 2007 - erwann@sun.com
- init spec for the new package format


