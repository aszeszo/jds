#
# spec file for package SUNWirssi
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby
#

%include Solaris.inc

%define OSR 9487:0.x

Name:                SUNWirssi
IPS_package_name:    network/chat/irssi
Meta(info.classification): %{classification_prefix}:Applications/Internet
Summary:             irssi - a terminal based IRC client
Version:             0.8.15
Source:              http://www.irssi.org/files/irssi-%{version}.tar.gz
# date:2008-08-18 owner:fujiwara type:feature bugster:6737999 bugzilla:617
Patch1:              irssi-01-textdomain.diff
# date:2008-08-18 owner:jouby type:bug
Patch2:              irssi-02-manpage.diff
SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
License:             GPL v2 
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires:       SUNWglib2
Requires:       SUNWopenssl-libraries
BuildRequires:  SUNWglib2-devel

%define perl_archlib /usr/perl5/vendor_perl/5.8.4/i86pc-solaris-64int
%define perl_version 5.8.4
%ifarch sparc
%define perl_dir sun4-solaris-64int
%else
%define perl_dir i86pc-solaris-64int
%endif

BuildRequires: runtime/perl-512

%description
Irssi is a terminal based IRC client for UNIX systems.

%prep
%setup -q -n irssi-%version
%patch1 -p1
%patch2 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%{_ldflags}"

./configure --prefix=%{_prefix}                 \
             --bindir=%{_bindir}                 \
             --sysconfdir=%{_sysconfdir}         \
             --includedir=%{_includedir}         \
             --mandir=%{_mandir}                 \
             --libdir=%{_libdir}                 \
             --with-perl=yes	                  \
             --with-proxy	                \
             --with-perl-lib=%{_prefix}/perl5/vendor_perl/%{perl_version}

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm ${RPM_BUILD_ROOT}%{_libdir}/irssi/modules/*.la
rm ${RPM_BUILD_ROOT}%{_prefix}/perl5/vendor_perl/%{perl_version}/%{perl_dir}/auto/Irssi/.packlist
rm ${RPM_BUILD_ROOT}%{_prefix}/perl5/vendor_perl/%{perl_version}/%{perl_dir}/auto/Irssi/*/.packlist
rm ${RPM_BUILD_ROOT}%{_prefix}/perl5/vendor_perl/%{perl_version}/%{perl_dir}/perllocal.pod
rm ${RPM_BUILD_ROOT}/etc/irssi.conf
rm -r ${RPM_BUILD_ROOT}%{_docdir} ${RPM_BUILD_ROOT}%{_includedir}
rmdir $RPM_BUILD_ROOT/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README AUTHORS
%doc(bzip2) COPYING NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%{_bindir}/*
%{_libdir}/irssi/
%dir %attr(0755, root, bin) %{_prefix}/perl5
%dir %attr(0755, root, bin) %{_prefix}/perl5/vendor_perl
%dir %attr(0755, root, bin) %{_prefix}/perl5/vendor_perl/%{perl_version}
%{_prefix}/perl5/vendor_perl/%{perl_version}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/irssi/
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%changelog
* Thu Apr 15 2010 - brian.cameron@sun.com
- Bump to 0.8.15.
* Wed Aug 12 2009 - christian.kelly@sun.com
- Bump to 0.8.14.
- Remove irssi-03-awk.diff, upstream.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change spec and patch owner to jouby.
* Tue Apr 21 2009 - chris.wang@sun.com
- add irssi-03-awk.diff to make the grammar comfort with /usr/bin/awk.
* Thu Apr 16 2009 - chris.wang@sun.com
- bump to 0.8.13.1
* Web Mar 04 2009 - chris.wang@sun.com
- Transfer the ownership to bewitche.
* Tue Feb 10 2009 - halton.huo@sun.com
- Add dependency on SUNWgnome-base-libs SUNWopenssl-libraries, CR #6755918.
* Fri Jan 16 2009 - Henry Zhang <hua.zhang@sun.com>
- change --with-perl=yes to load perl automatically.
* Fri Sep 12 2008 - Henry Zhang <hua.zhang@sun.com>
- Add  %doc to %files for copyright.
* Mon Aug. 21 2008 - Henry Zhang hua.zhang@sun.com
- Add irssi-02-manpage.diff.
* Mon Aug 18 2008 - takao.fujiwara@sun.com
- Add irssi-01-textdomain.diff to enable i18n.
* Thu Aug 07 2008 - damien.carbery@sun.com
- Fix %install and %files to work on sparc.
* Mon Jul 21 2008 - Henry Zhang hua.zhang@sun.com
- Change to SUNWirssi.
* Fri Oct 09 2007 - Petr Sobotka sobotkap@centrum.cz
- bump to 0.8.12.
* Sun Apr 08 2007 - Thomas Wagner
- bump to 0.8.11-rc1, removed tarball_version (re-add if ever needed).
* Fri Sep 01 2006 - Eric Boutilier
- Initial spec.



