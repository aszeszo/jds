#
# spec file for package gtk3
#
# Copyright (c) 2012, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner erwannc
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

%include l10n.inc
Name:         gtk3
License:      LGPL v2
Group:        System/Libraries
Version:      3.4.1
Release:      1
Distribution: Java Desktop System
Vendor:	      Gnome Community
Summary:      GTK+ - GIMP Toolkit Library for creation of graphical user interfaces
Source:       http://ftp.gnome.org/pub/GNOME/sources/gtk+/3.4/gtk+-%{version}.tar.xz
Source1:      gtk.unset-hack.sh
Source2:      gtk.unset-hack.csh
#Source3:      %{name}-po-sun-%{po_sun_version}.tar.bz2
Source4:      l10n-configure.sh
#owner:erwannc date:2000-00-00 type:feature
Patch1:       gtk+-01-window-icons-for-message-dialog.diff
#owner:erwannc date:2003-07-11 type:feature
Patch2:       gtk+-02-fileseldlg-navbuttons.diff
#owner:erwannc date:2004-05-17 bugster:5035382 type:bug
Patch3:       gtk+-03-use-xim-for-all-locales.diff
#owner:erwannc date:2004-08-12 type:feature
Patch4:       gtk+-04-sun-copy-paste-keybindings.diff
#owner:erwannc date:2004-08-12 bugzilla:74223 type:feature
Patch5:       gtk+-05-sun-pgdn-pgup-keybindings.diff
#owner:laca    date:2004-09-18 type:feature
Patch6:       gtk+-06-solaris-2.0.0-compat.diff
#owner:erwannc date:2006-05-01 type:feature
Patch7:       gtk+-07-trusted-extensions.diff
# date:2009-04-22 owner:gheet type:bug bugster:6795517
Patch8:       gtk+-08-default-print-ps.diff
# date:2009-03-17 doo:7438 owner:erwannc type:bug
Patch9:       gtk+-09-fix-deprecated.diff
# date:2008-01-11 bugster:6630867 bugzilla:505857 owner:erwannc type:bug
Patch10:      gtk+-10-filechooser-enterkey.diff

# Note the dlopen-medialib patch does not need to be applied to GTK3
# since GTK3 no longer uses mediaLib at all.  The dlopen-medialib patch
# is now only applied to GTK2.

# date:2009-09-25 owner:gheet type:branding doo:11575
Patch12:      gtk+-12-show-lpr-backend.diff
# date:2009-10-11 owner:gheet type:bug doo:11830
Patch13:      gtk+-13-check-libs.diff
# date:2010-01-07 owner:gheet type:bug doo:13625
Patch14:      gtk+-14-handle-copies.diff
# date:2011-08-15 owner:gheet type:bug bugster:7076227
Patch16:      gtk+-16-remove-papi.diff
# date:2012-03-27 owner:padraig type:bug bugster:7149817
Patch17:      gtk+-17-unregister-callback.diff
# date:2010-07-16 owner:yippi type:branding
Patch30:      gtk3+-01-libtool.diff
# date:2010-07-16 owner:yippi type:bug bugzilla:654720
Patch31:      gtk3+-02-configure.diff
# This just worksaround a compile issue and should be fixed properly.
Patch32:      gtk3+-03-disable-papi.diff
# date:2012-05-02 owner:yippi type:bug
Patch33:      gtk3+-04-compile.diff

BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/doc
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%define cairo_version 0.9.2
%define atk_version 1.7.0
%define pango_version 1.9.0
%define glib2_version 2.7.1
%define libpng_version 1.2.5
%define libjpeg_version 6.2.0

BuildRequires: cairo-devel >= %{cairo_version}
BuildRequires: atk-devel >= %{atk_verGsion}
BuildRequires: pango-devel >= %{pango_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: libpng-devel >= %{libpng_version}
BuildRequires: libjpeg >= %{libjpeg_version}
Requires:      cairo >= %{cairo_version}
Requires:      glib2 >= %{glib2_version}
Requires:      atk >= %{atk_version}
Requires:      pango >= %{pango_version}
Requires:      libpng >= %{libpng_version}
Requires:      libjpeg >= %{libjpeg_version}

%description
This fast and versatile library is used all over the world for all
GNOME applications, the GIMP and several others. Originally it was
written for the GIMP and hence has the name Gimp ToolKit. Many people
like it because it is small, efficient and very configurable.

%package devel
Summary:      Library for creation of graphical user interfaces
Group:        Development/Libraries/X11
Autoreqprov:  on
Requires:     %{name} = %{version}
Requires:     cairo-devel >= %{cairo_version}
Requires:     atk-devel >= %{atk_version}
Requires:     pango-devel >= %{pango_version}

%description devel
This fast and versatile library is used all over the world for all
GNOME applications, the GIMP and several others. Originally it was
written for the GIMP and hence has the name Gimp ToolKit. Many people
like it because it is small, efficient and very configurable.

%prep
%setup -q -n gtk+-%{version} 

# Fixes build error. Solaris msgfmt does not have '-c'.
for f in po/Makefile.in.in po-properties/Makefile.in.in ; do
  sed -e 's/$(GMSGFMT) -c/$(GMSGFMT)/g' $f > $f$$
  mv $f$$ $f
  d=`dirname $f`
  touch $d/*.po
done

%if %build_l10n
# workaround for bugster 6581452, bugzilla 457863
#sh -x %SOURCE4 --disable-gnu-extensions

#bzcat %SOURCE3 | tar xf -
#cd po-sun; make; cd ..
%endif

#%patch1 -p1
#%patch2 -p1
%patch3 -p1

#%ifos solaris
#%patch4 -p1
#%endif

#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
%patch8 -p1
%patch10 -p1
#%patch11 -p1
#%patch12 -p1
%patch13 -p1
#%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1

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

export SED="/usr/gnu/bin/sed"

libtoolize --force
aclocal-1.11 $ACLOCAL_FLAGS -I .
gtkdocize
autoheader
automake-1.11 -a -c -f
autoconf
export CFLAGS="%optflags -I/usr/X11/include"
export LDFLAGS="%_ldflags"
./configure --prefix=%{_prefix} \
            --libdir=%{_libdir} \
            --bindir=%{_bindir} \
            --datadir=%{_datadir} \
            --with-native-locale=yes \
	    --with-xinput=xfree \
            --mandir=%{_mandir} \
            --infodir=%{_infodir} \
	    --enable-shm \
            --enable-xim \
            --enable-fbmanager \
            --with-gdktarget=x11 \
	    --sysconfdir=%{_sysconfdir}	\
	    --enable-explicit-deps=yes	\
	    --without-libjasper		\
	    --disable-glibtest		\
	    --disable-papi		\
	    %{gtk_doc_option}

# Build needed uninstalled.pc file
#gmake gdk-x11-2.0-uninstalled.pc

# this is broken in 2.19.6
#gmake -j $CPUS
gmake

%install
gmake DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gtk-3.0
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cp %SOURCE1 $RPM_BUILD_ROOT/etc/profile.d/
cp %SOURCE2 $RPM_BUILD_ROOT/etc/profile.d
#Copy zh_HK from zh_TW
#Fixes bug 4930405
install -d $RPM_BUILD_ROOT%{_datadir}/locale/zh_HK/LC_MESSAGES
install --mode=0644 $RPM_BUILD_ROOT%{_datadir}/locale/zh_TW/LC_MESSAGES/*.mo $RPM_BUILD_ROOT%{_datadir}/locale/zh_HK/LC_MESSAGES/

rm $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/*/printbackends/*.a
rm $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/*/printbackends/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_bindir}/gtk-query-immodules-3.0 > %{_sysconfdir}/gtk-3.0/gtk.immodules
%{_bindir}/gdk-pixbuf-query-loaders > %{_sysconfdir}/gtk-3.0/gdk-pixbuf.loaders

%postun
#If this is the last version of the package remove the config files
if [ $1 = 0 ]
then
	rm %{_sysconfdir}/gtk-3.0/gtk.immodules
	rm %{_sysconfdir}/gtk-3.0/gdk-pixbuf.loaders
fi
/sbin/ldconfig

%files 
%{_bindir}/*query*
%{_bindir}/gtk-update-icon-cache
%{_libdir}/lib*.so.*
%{_libdir}/gtk-3.0/*/immodules/*.so
%{_libdir}/gtk-3.0/*/loaders/*.so
%{_libdir}/gtk-3.0/*/engines/*.so
%{_datadir}/themes/*/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_sysconfdir}/profile.d/gtk.unset-hack.sh
%{_sysconfdir}/profile.d/gtk.unset-hack.csh
%dir %{_sysconfdir}/gtk-3.0
%{_mandir}/man1/*.gz

%files devel
%{_bindir}/*-demo
%{_bindir}/*-csource
%{_includedir}/gtk-3.0
%{_libdir}/lib*.so
%{_libdir}/gtk-3.0/include
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-3.0
%{_datadir}/aclocal/*.m4
%{_datadir}/gtk-doc/html/*
%{_mandir}/man3/*.gz

%changelog
* Wed May 02 2012 - brian.cameron@oracle.com
- Bump to 3.4.1.
* Wed Oct 19 2011 - brian.cameron@oracle.com
- Bump to 3.2.1.
* Fri Sep 30 2011 - brian.cameron@oracle.com
- Bump to 3.2.0.
* Tue Sep 13 2011 - brian.cameron@oracle.com
- Bump to 3.1.18.
* Thu Sep 08 2011 - brian.cameron@oracle.com
- Bump to 3.1.16.
* Thu Aug 18 2011 - brian.cameron@oracle.com
- Bump to 3.1.12.
* Tue Jul 12 2011 - brian.cameron@oracle.com
- Created with 3.1.8.
