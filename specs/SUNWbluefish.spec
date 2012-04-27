#
# spec file for package SUNWbluefish
#
# includes module(s): bluefish
#
# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jouby 
#
%include Solaris.inc

%define OSR 9360 (new OSR for major rev not needed):1.x

Name:                    SUNWbluefish
IPS_package_name:        web/editor/bluefish
Meta(info.classification): %{classification_prefix}:Applications/Internet,%{classification_prefix}:Development/Editors
Summary:                 Bluefish, a powerful editor for experienced web designers.
Version:                 2.0.2
Source:                  http://www.bennewitz.com/bluefish/stable/source/bluefish-%{version}.tar.bz2
Source1:                 %{name}-manpages-0.1.tar.gz
URL:                     http://bluefish.openoffice.nl/index.html
SUNW_Copyright:          SUNWbluefish.copyright
License:                 GPL v2
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires: SUNWlibgnomecanvas
Requires: library/pcre
Requires: SUNWgnome-spell
Requires: SUNWgnome-libs
BuildRequires: SUNWlibgnomecanvas-devel
BuildRequires: SUNWgnome-libs-devel
Requires: SUNWdesktop-cache

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n bluefish-%version

gzcat %SOURCE1 | tar xf -

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="%optflags -DANSICPP"

autoconf
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --disable-update-databases
make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/bluefish-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

mv $RPM_BUILD_ROOT%{_datadir}/locale/ko_KR $RPM_BUILD_ROOT%{_datadir}/locale/ko

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri mime-types-cache

%postun
%restart_fmri mime-types-cache

%files
%doc(bzip2) COPYING NEWS ChangeLog
%doc AUTHORS README
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%{_datadir}/bluefish
%{_datadir}/xml
%attr (0755, root, other) %{_datadir}/icons

%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/bluefish

%{_datadir}/doc/bluefish
%ghost %attr (0755, root, root) %ips_tag(original_name=SUNWbluefish:%{@} preserve=true) %{_datadir}/mime
%dir %attr (0755, root, other) %{_datadir}/pixmaps
%{_datadir}/pixmaps/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 2.0.2.
* Tue May 04 2010 - harry.fu@sun.com
- Treat ko_KR.po as ko.po.
* Wen Mar 24 2010 - yuntong.jin@sun.com
- Bump to 2.0.0, remove upstreamed patch bluefish-01-no-debug.diff
  bluefish-02-pcre-cflags.diff, bluefish-04-find-maxdepth.diff,
  bluefish-05-desktop-l10n.diff
* Fir Aug 28 2009 - yuntong.jin@sun.com
- Change owner to jouby 
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Thu Feb 19 2009 - alfred.peng@sun.com
- New manpage tarball.
* Tue Feb 10 2009 - alfred.peng@sun.com
- Remove /usr/gnu/ from CFLAGS and LDFLAGS. bugster CR#6803332.
* Mon Feb 09 2009 - takao.fujiwara@sun.com
- Add patch desktop-l10n.diff from trunk.
* Fri Sep 12 2008 - alfred.peng@sun.com
- Add %doc to %files for new copyright.
* Tue Aug 26 2008 - alfred.peng@sun.com
- Add bluefish-04-find-maxdepth.diff to cope with Solaris find.
* Mon Aug 25 2008 - takao.fujiwara@sun.com
- Add bluefish-03-firefox.diff to launch the browser.
* Mon Jul 21 2008 - alfred.peng@sun.com
- remove bluefish-01-timeval.diff which isn't needed.
  add build configure --disable-update-databases to get rid of
  bluefish-03-update-mime.diff.
  add bluefish-02-pcre-cflags.diff to get rid of the build dependency on
  SUNWpcre-devel.
  update bluefish-01-no-debug.diff for Sun Studio compiler.
  remove all the /usr/sfw from CFLAGS and LDFLAGS.
  remove SUNWlibC dependency and CPPFLAGS as it's only C code.
  add SUNWpostrun to the dependency.
  update script so that  the GNOME session waits for the postrun to finish.
* Wed Oct 17 2007 - laca@sun.com
- define l10n subpkg
* Tue Oct 16 2007 - laca@sun.com
- add /usr/gnu to search paths for the indiana build
* Thu Mar 29 2007 - daymobrew@users.sourceforge.net
- Change Requires of SUNWaspell to SUNWgnome-spell. Former has been obsoleted.
* Wed Jan 24 2007 - daymobrew@users.sourceforge.net
- s/SFEpcre/SUNWpcre/ because SUNWpcre is in Vermillion Devel.
* Fri Jan 07 2007 - daymobrew@users.sourceforge.net
- Bump to 1.0.7. Update source url.
* Mon Jun 12 2006 - laca@sun.com
- rename to SFEbluefish.
- change to root:bin to follow other JDS pkgs.
* Mon Jan 30 2006 - glynn.foster@sun.com
- Initial version.



