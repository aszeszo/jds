#
# spec file for package SUNWgnome-cd
#
# includes module(s): sound-juicer
#
# Copyright 2009, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner yippi
#
%include Solaris.inc
%use soundjuicer = sound-juicer.spec

Name:                    SUNWgnome-cd
IPS_package_name:        desktop/cd-ripping/sound-juicer
Meta(info.classification): %{classification_prefix}:Applications/Sound and Video
Summary:                 CD ripping tool
Version:                 %{soundjuicer.version}
Source:                  %{name}-manpages-0.1.tar.gz
Source1:                 solaris-cdda.schemas
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{soundjuicer.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
                                                                                
%include default-depend.inc
%include desktop-incorporation.inc
BuildRequires: SUNWlibglade-devel
BuildRequires: SUNWgnome-cd-burner-devel
BuildRequires: SUNWgnome-config-devel
BuildRequires: SUNWgnome-libs-devel
BuildRequires: SUNWlibgnome-media-devel
BuildRequires: SUNWgnome-media-devel
BuildRequires: SUNWgnome-vfs-devel
BuildRequires: SUNWmusicbrainz-devel
BuildRequires: SUNWgnome-doc-utils
Requires: SUNWlibglade
Requires: SUNWlibcanberra
Requires: SUNWgnome-cd-burner
Requires: SUNWgnome-config
Requires: SUNWgnome-libs
Requires: SUNWlibgnome-media
Requires: SUNWgnome-media
Requires: SUNWgnome-vfs
Requires: SUNWlibC
Requires: SUNWlibms
Requires: SUNWmusicbrainz
Requires: SUNWdesktop-cache
Requires: %{name}-root

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%prep
rm -rf %name-%version
mkdir %name-%version
%soundjuicer.prep -d %name-%version
cd %{_builddir}/%name-%version
gzcat %SOURCE0 | tar xf -
cd %{_builddir}/%name-%version/sound-juicer-%{soundjuicer.version}
cd ..

%build
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export CXXFLAGS="%cxx_optflags -I/usr/sfw/include -lCrun -lCstd"
export LDFLAGS="%_ldflags -L/usr/sfw/lib"
export CFLAGS="%optflags -I/usr/sfw/include"
%soundjuicer.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%soundjuicer.install -d %name-%version
install --mode=0644 %SOURCE1 $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/solaris-cdda.schemas
# rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

# RBAC related
mkdir -p $RPM_BUILD_ROOT/etc/security/exec_attr.d
# exec_attr(4)
cat >> $RPM_BUILD_ROOT/etc/security/exec_attr.d/desktop-cd-ripping-sound-juicer <<EOF
Desktop Removable Media User:solaris:cmd:RO::/usr/bin/sound-juicer:privs=sys_devices
EOF

cd $RPM_BUILD_ROOT%{_bindir}
ln -s sound-juicer gnome-cd

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri desktop-mime-cache gconf-cache

%postun
%restart_fmri desktop-mime-cache

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/applications
%attr (0755, root, bin)%{_bindir}/*
%{_datadir}/applications/*
%doc -d sound-juicer-%{soundjuicer.version} AUTHORS README
%doc(bzip2) -d sound-juicer-%{soundjuicer.version} COPYING NEWS
%doc(bzip2) -d sound-juicer-%{soundjuicer.version} ChangeLog po/ChangeLog
%doc(bzip2) -d sound-juicer-%{soundjuicer.version} help/sound-juicer/ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/C
%attr (-, root, other) %{_datadir}/icons
%{_datadir}/sound-juicer
%{_datadir}/omf/*/*-C.omf
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/*/??
%{_datadir}/gnome/help/*/??_??
%{_datadir}/omf/*/*-??.omf
%{_datadir}/omf/*/*-??_??.omf

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/solaris-cdda.schemas
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
%attr (0755, root, sys) %dir /etc/security
%attr (0755, root, sys) %dir /etc/security/exec_attr.d
%config %ips_tag(restart_fmri=svc:/system/rbac:default) %attr (0444, root, sys) /etc/security/exec_attr.d/*

%changelog
* Fri Nov 04 2011 - brian.cameron@oracle.com
- Change SUNWgnome-media-apps dependency to SUNWlibgnome-media.
* Wed Apr 06 2011 - brian.cameron@oracle.com
- Add "RO" to exec_attr config.
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Tue Mar 03 2009 - lin.ma@sun.com
- Renamed SUNWbrasero to SUNWgnome-cd-burner.
* Thu Feb 19 2009 - brian.cameron@sun.com
- Add SUNWbrasero as a dependency.
* Fri Sep 26 2008 - brian.cameron@sun.com
- Add new copyright files.
* Thu Mar 27 2008 - brian.cameron@sun.com
- Add SUNW_Copyright.
* Thu Jan  3 2008 - laca@sun.com
- use gconf-install.script instead of an inline script
* Tue Jun 26 2007 - irene.huang@sun.com
- remove libcdio as dependency.
* Tue Apr 24 2007 - laca@sun.com
- s/0755/-/ in defattr so that files are not made all executable
* Mon Apr 16 2007 - damien.carbery@sun.com
- Add en_GB files to l10n package for new tarball.
* Tue Oct 31 2006 - takao.fujiwara@sun.com
- Added /usr/share/locale in files l10n. Fixes 6488189.
* Fri Sep 08 2006 - Matt.Keenan@sun.com
- Add manpage tarball
* Sat Aug 12 2006 - laca@sun.com
- change datadir/icons permissions back to root:other since it's a stable
  interface and wasn't supposed to be changed
* Fri Jul 28 2006 - damien.carbery@sun.com
- Omit locale files from packaging as not installed.
* Fri Jul 14 2006 - laca@sun.com
- update %post/%postun/etc scripts to support diskless client setup,
  part of 6448317
* Fri Jul 14 2006 - brian.cameron@sun.com
- Install schemas file for CDDA URL Handler.
* Thu Jun 29 2006 - laca@sun.com
- update postrun scripts
* Wed Jun 21 2006 - brian.cameron@sun.com
- Fix packaging.
* Sun Jun 11 2006 - laca@sun.com
- change group from other to bin/sys
* Thu Jun  1 2006 - laca@sun.com
- use post/preun scripts to install schemas into the merged gconf files
* Fri May 12 2006 - damien.carbery@sun.com
- Small update to dependency list after check-deps.pl run.
* Wed May 10 2006 - laca@sun.com
- merge -share pkg(s) into the base pkg(s)
* Fri May 5  2006 - brian.cameron@sun.com
- Backing out "merged" GCONF change, since it doesn't work right.  For now
  it seems you need to delete /etc/gconf/gconf.xml.defaults/%gconf-tree*.xml
  and run /usr/bin/gconf-merge-tree /etc/gconf/gconf.xml.defaults to get
  the GCONF set up for this to work.  I talked with Laca and he plans to 
  fix this in the build process so this is not necessary.
* Sun Apr 20 2006 - damien.carbery@sun.com
- Correct %install line that removes omf files for non-l10n build.
* Sun Apr  9 2006 - damien.carbery@sun.com
- Add help files to share and l10n packages.
* Tue Mar 28 2006 - brian.cameron@sun.com
- Now building Sound Juicer as CD player on Solaris.
* Thu Feb 16 2006 - damien.carbery@sun.com
- Update Build/Requires after running check-deps.pl script.
* Tue Nov 29 2005 - laca@sun.com
- remove javahelp stuff
* Mon Jul 25 2005 - balamurali.viswanathan@wipro.com
- Add dependency SUNWgnome-media-apps, SUNWmusicbrainz
  and SUNWgnome-cd-burner
* Fri Jul 22 2005 - balamurali.viswanathan@wipro.com
- Changed the name to SUNWgnome-cd from SUNWsound-juicer
* Thu Jul 07 2005 - balamurali.viswanathan@wipro.com
- Initial spec-file created

