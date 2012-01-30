#
# spec file for package SUNWavant.spec
#
%define owner jouby
#

%include Solaris.inc

%define OSR 9430:0.x

%define X11_DIR %{_prefix}/X11
%define source_name avant-window-navigator

Name:           SUNWavant
IPS_package_name: desktop/avant-window-navigator
Meta(info.classification): %{classification_prefix}:Applications/Panels and Applets
Summary:        Avant Window Navigator - fully customizable dock-like navigator
Version:        0.3.2.1
Source:		http://launchpad.net/awn/0.2/%{version}/+download/avant-window-navigator-%{version}.tar.gz
Source1:        l10n-configure.sh
URL:            http://launchpad.net/awn/
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
License:        GPL v2, LGPL v2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# date:2006-06-06 type:bug owner:dkenny bugster:6887512 bugzilla:447163
Patch1:         avant-01-uninit-memory.diff
# date:2009-12-01 type:bug owner:yippi doo:12965
Patch2:         avant-02-python.diff
Source2:        %{name}-manpages-0.1.tar.gz

%ifnarch sparc
# these packages are only avavilable on i386/x64
# ===========================================

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%include	default-depend.inc
%include        desktop-incorporation.inc
Requires:       SUNWgtk2
Requires:       SUNWcompiz
Requires:       SUNWdbus
Requires:       SUNWdesktop-cache
Requires:       SUNWgnome-themes-only
Requires:       SUNWbash
Requires:       SUNWPython26
Requires:       SUNWpycairo26
Requires:       SUNWpygtk2-26
Requires:       SUNWpython26-xdg
Requires:       %{name}-root
BuildRequires:  SUNWgtk2-devel
BuildRequires:  SUNWcompiz-devel
BuildRequires:  SUNWdbus-devel
BuildRequires:  SUNWxwinc
BuildRequires:  SUNWPython26
BuildRequires:  SUNWpython26-xdg
BuildRequires:  SUNWpython26-setuptools
BuildRequires:  SUNWvala-devel
BuildRequires:  consolidation/desktop/gnome-incorporation

%package devel
Summary:		 %summary - developer files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
%include desktop-incorporation.inc
Requires:		 %name

%package root
Summary:                 %{summary} - / filesystem
SUNW_BaseDir:            /
%include default-depend.inc
%include desktop-incorporation.inc

%package l10n
Summary:                 %{summary} - l10n files
Requires:        %{name}

%prep
%setup -q -c -n %name-%{version}
cd %{source_name}-%{version}
cd %{_builddir}/%name-%version
gzcat %SOURCE2 | tar xf -
cd %{source_name}-%{version}
%patch1 -p1
%patch2 -p1
cd ..

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
export PKG_CONFIG_PATH=%{_prefix}/lib/pkgconfig:%{X11_DIR}/lib/pkgconfig

PROTO_LIB=$RPM_BUILD_DIR/%{name}/usr/X11/lib

export CFLAGS="%optflags -I%{X11_DIR}/include" 
export LDFLAGS="-L$PROTO_LIB -L%{X11_DIR}/lib -R%{X11_DIR}/lib"

export PYTHON=/usr/bin/python%{default_python_version}

cd %{source_name}-%{version}
intltoolize --force --copy --automake

sh %SOURCE1 --enable-copyright

aclocal
autoconf
automake -a -c -f
./configure --prefix=%{_prefix}		\
	    --bindir=%{_bindir}         \
	    --sysconfdir=%{_sysconfdir}	\
	    --libdir=%{_libdir}         \
            --includedir=%{_includedir} \
            --mandir=%{_mandir}   \
	    --datadir=%{_datadir}	

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
cd %{source_name}-%{version}
make install DESTDIR=$RPM_BUILD_ROOT

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages

rm -f ${RPM_BUILD_ROOT}/x11.pc
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

find $RPM_BUILD_ROOT -type f -name "*.pyo" -exec rm -f {} ';'

cd $RPM_BUILD_ROOT%{_datadir}/locale
# Rename dirs that are symlinks on the installed system.
for ling in de_DE fi_FI fr_FR it_IT ru_RU no_NO
do
  sling=`echo $ling | awk -F_ '{print $1}'`
  if [ -d $ling -a -d $sling ] ; then
    rm -rf $ling
  elif [ -d $ling ] ; then
    mv $ling $sling
  fi
done

#install man page
rm -rf $RPM_BUILD_ROOT%{_mandir}
cd %{_builddir}/%name-%version/sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri icon-cache gconf-cache

%files
%doc -d avant-window-navigator-%{version} README AUTHORS
%doc(bzip2) -d avant-window-navigator-%{version} COPYING COPYING.LIB NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python%{default_python_version}
%dir %attr (0755, root, bin) %{_libdir}/python%{default_python_version}/vendor-packages
%dir %attr (0755, root, bin) %{_libdir}/python%{default_python_version}/vendor-packages/awn/
%{_libdir}/lib*so*
%{_libdir}/python%{default_python_version}/vendor-packages/awn/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_datadir}/avant-window-navigator
%{_datadir}/avant-window-navigator/*
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/icons
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/48x48/apps/
%{_datadir}/icons/hicolor/48x48/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/32x32/apps/
%{_datadir}/icons/hicolor/32x32/apps/*
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/
%dir %attr (0755, root, other) %{_datadir}/icons/hicolor/24x24/apps/
%{_datadir}/icons/hicolor/24x24/apps/*
%dir %attr(0755, root, bin) %{_mandir}
%{_mandir}/*/*
%{_datadir}/vala/vapi/awn.deps
%{_datadir}/vala/vapi/awn.vapi

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/gtk-doc

%files root
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%{_sysconfdir}/gconf/schemas/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

# endif for "ifnarch sparc"
%endif

%changelog
* Mon Jun 21 2010 - dave.lin@sun.com
- Add 'BuildRequires:  SUNWvala-devel'.
* Tue Dec 01 2009 - brian.cameron@sun.com
- Add patch avant-02-python.diff to make avant python scripts work with Python
  2.6.
* Thu Oct 15 2009 - yuntong.jin@sun.com
- use %{default_python_version} and remove .pyo file from package 
* Fri Oct 09 2009 - darren.kenny@sun.com
- Patch to fix bug#6887512 where awn was crashing due to uninit memory.
* Tue Aug 25 2009 - brian.cameron@sun.com
- Bump to 0.3.2.1.
* Fri Jun 26 2009 - chris.wang@sun.com
- Change owner to jouby
* Thu Apr 16 2009 - chris.wang@sun.com
- bump to 0.3.2 and remove upstreamed patches
* Fri Apr  7 2009 - jeff.cai@sun.com
- Remove dependency on SUNWpython-lxml since this package is only found in
  OpenSolaris.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun
* Mon Mar 23 2009 - jeff.cai@sun.com
- Because /usr/bin/awn-launcher-editor (SUNWavant) requires /usr/bin/bash which
  is found in SUNWbash, add the dependency on SUNWbash
- Because /usr/bin/awn-manager (SUNWavant) requires
  /usr/lib/python2.4/vendor-packages/pygtk.pyc which is found in
  SUNWgnome-python-libs, add the dependency on SUNWgnome-python-libs
- Because /usr/bin/awn-schema-to-gconf (SUNWavant) requires
  /usr/lib/python2.4/vendor-packages/lxml/etree.pyc which is found in
  SUNWpython-lxml, add the dependency on SUNWpython-lxml
* Web Mar 04 2009 - chris.wang@sun.com
- Transfer the ownership to bewitche
* Tue Mar 03 2009 - brian.cameron@sun.com
- Use find command to remove .la and .a files.
* Mon Dec 22 2008 - takao.fujiwara@sun.com
- Removed duplicated language directories.
* Wed Sep 17 2008 - Henry Zhang <hua.zhang@sun.com>
- Add  %doc to %files for copyright
* Fri Jul 25 2008 - takao.fujiwara@sun.com
- Add avant-04-g11n-i18n-ui.diff to set textdomain().
* Tue Jul 22 2008 - damien.carbery@sun.com
- Add Build/Requires SUNWpython-xdg for python-xdg.
* Fri Jul 18 2008 - damien.carbery@sun.com
- Add owner, url; fix Source (s/.tar/.tar.gz/). Fix l10n packaging - Rename
  some locale dirs because they are symlinks on the installed system (e.g.
  de_DE to de).
* Fri Jul 18 2008 - Henry Zhang <hua.zhang@sun.com>
- Add check to ensure not build on SPARC
* Tue Jul 15 2008 - Henry Zhang <hua.zhang@sun.com>
- bump to 0.2.6, and fix bugs in spec file
* Tue Feb 05 2008 - Moinak Ghosh <moinak.ghosh@sun.com>
- Initial spec.



