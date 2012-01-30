#
# spec file for package SUNWgnu-findutils
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#

%include Solaris.inc

%define OSR 9641:4.2.32

%define _gnudir %{_basedir}/gnu
%define _gnubin %{_gnudir}/bin
%define _gnudata %{_gnudir}/share
%define _gnuman %{_gnudata}/man

# Do NOT bump past 4.2.31.  Later versions are GPLv3 and this needs to be
# reviewed and approved before we can release with the newer license.

Name:           SUNWgnu-findutils
IPS_package_name: file/gnu-findutils
Meta(info.classification): %{classification_prefix}:Applications/System Utilities
License:        GPLv2
Summary:        GNU utilities find and xargs
Version:        4.2.31
Source:         http://ftp.gnu.org/pub/gnu/findutils/findutils-%{version}.tar.gz
Source1:        l10n-configure.sh
# owner:mattman date:2009-02-27 type:branding
Patch1:         gnu-findutils-01-manpages.diff
URL:            http://www.gnu.org/software/findutils/
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:        %{summary} - l10n files
Requires:       %{name}

%description
The GNU Find Utilities are the basic directory searching utilities of 
the GNU operating system. These programs are typically used in 
conjunction with other programs to provide modular and powerful 
directory search and file locating capabilities to other commands. The 
tools supplied with this package are: find - search for files in a 
directory hierarchy and xargs - build and execute command lines from standard input.

%prep
%setup -q -n findutils-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"

sh %SOURCE1 --enable-copyright
./configure --disable-leaf-optimisation \
            --prefix=%{_gnudir} \
            --mandir=%{_gnuman} \
	    --infodir=%{_gnudata}/info \
            --libexecdir=%{_gnudir}/lib

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
rmdir $RPM_BUILD_ROOT%{_gnudir}%{_localstatedir}
rm -rf $RPM_BUILD_ROOT%{_gnudir}/lib/charset.alias

#remove unused files
rm -rf $RPM_BUILD_ROOT%{_gnudir}/lib
rm -rf $RPM_BUILD_ROOT%{_gnudata}/info/dir
rm -rf $RPM_BUILD_ROOT%{_gnubin}/locate
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/glocate.1
rm -rf $RPM_BUILD_ROOT%{_gnubin}/updatedb
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/gupdatedb.1
rm -rf $RPM_BUILD_ROOT%{_mandir}/man5

#create links in gnu dir
cd $RPM_BUILD_ROOT
install -m 755 -d usr/bin

ln -s ../gnu/bin/find usr/bin/gfind
ln -s ../gnu/bin/xargs usr/bin/gxargs
install -m 755 -d usr/share/man/man1
ln -s ../../../gnu/share/man/man1/find.1 usr/share/man/man1/gfind.1
ln -s ../../../gnu/share/man/man1/xargs.1 usr/share/man/man1/gxargs.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING AUTHORS NEWS ChangeLog README THANKS
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_gnudata}/info
%{_mandir}
%dir %attr (0755, root, bin) %{_gnubin}
%{_gnubin}/*
%dir %attr (0755, root, sys) %{_gnudata}
%{_gnuman}

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_gnudata}
%dir %attr (-, root, bin) %{_gnudata}/locale
%{_gnudata}/locale/*

%changelog
* Fri Aug 12 2011 - ghee.teo@oracle.com
- Fixes stopper bugster#7077970.
* Thu Apr 07 2011 - ghee.teo@oracle.com
- Fixes bugster#7031707.
* Tue Aug 25 2009 - brian.cameron@sun.com
- Rever to 4.2.31.  Newer versions are GPLv3.
* Tue Aug 25 2009 - brian.cameron@sun.com
- Bump to 4.2.33.
* Fri Feb 27 2009 - matt.keenan@sun.com
- Add manpage patch for Attributes and ARC Comment
* Thu Sep 11 2008 - kevin.mcareavey@sun.com
- Add %doc to %files for copyright
* Fri Aug 15 2008 - kevin.mcareavey@sun.com
- Cleanup for spec-files-other integration
- Rollback to 4.2.31 for GPLv2
- Create links in gnu directory
- Remove unused files
* Thu Feb 21 2008 - nonsea@users.sourceforge.net
- Bump to 4.2.33
* Thu Nov 15 2007 - daymobrew@users.sourceforge.net
- Correct path to charset.alias file.
* Sun Oct 14 2007 - laca@sun.com
- fix l10n installation
* Tue Sep 18 2007 - nonsea@users.sourceforge.net
- Bump to 4.2.31
* Sun Sep 24 2006 - Eric Boutilier
- Initial spec


