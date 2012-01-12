#
# spec file for package poppler
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
# bugdb: bugzilla.freedesktop.org
#

%define OSR 3962:0.4.2

Name:         poppler
License:      GPLv2,LGPLv2.1,X/MIT
Group:        System/Libraries
Version:      0.18.0
Release:      1 
Distribution: Java Desktop System
Vendor:       freedesktop.org
Summary:      PDF Rendering Library
Source:       http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# date:2009-04-20 type:bug owner:dkenny bugster:6685564
Patch1:       poppler-01-ss12-compiler-bug.diff
# date:2009-08-30 type:bug owner:dkenny
Patch2:       poppler-02-compiler-errors.diff
# date:2010-01-14 type:bug owner:gheet doo:13889
Patch3:       poppler-03-null-font.diff
# date:2011-07-14 type:branding owner:gheet bugster:7059720
Patch4:       poppler-04-sun-ja-font.diff
URL:          http://poppler.freedesktop.org/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_docdir}/%{name}
Autoreqprov:  on
Prereq:       /sbin/ldconfig

%define cairo_version 0.5.0
%define gtk2_version 2.4.0

Requires:      cairo >= %{cairo_version}
Requires:      gtk2 >= %{gtk2_version}

BuildRequires: cairo-devel >= %{cairo_version}
BuildRequires: gtk2-devel >= %{gtk2_version}

Obsoletes:     xpdf <= 3.0
Provides:      xpdf = 3.0

%description
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

Second, we would like to move libpoppler forward in a number of areas
that doesn't fit within the goals of xpdf.  By design, xpdf depends on
very few libraries and runs a wide range of X based platforms.  This
is a strong feature and reasonable design goal.  However, with poppler
we would like to replace parts of xpdf that are now available as
standard components of modern Unix desktop environments.  One such
example is fontconfig, which solves the problem of matching and
locating fonts on the system, in a standardized and well understood
way.  Another example is cairo, which provides high quality 2D
rendering.

%package devel
Summary:      PDF Rendering Library
Group:        Development/Libraries
Requires:     %{name} = %{version}
Requires:     cairo-devel >= %{cairo_version}
Requires:     gtk2-devel >= %{gtk2_version}

%description devel
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenence effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situaion.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

Second, we would like to move libpoppler forward in a number of areas
that doesn't fit within the goals of xpdf.  By design, xpdf depends on
very few libraries and runs a wide range of X based platforms.  This
is a strong feature and reasonable design goal.  However, with poppler
we would like to replace parts of xpdf that are now available as
standard components of modern Unix desktop environments.  One such
example is fontconfig, which solves the problem of matching and
locating fonts on the system, in a standardized and well understood
way.  Another example is cairo, which provides high quality 2D
rendering.

%prep
%setup -q
%if %cc_is_gcc
%else
%patch1 -p1
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1

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

# create dummy config.rpath required by AC_REQUIRE_AUX_FILE
# otherwise automake complains and fails.
touch config.rpath

libtoolize --force --copy
aclocal $ACLOCAL_FLAGS -I/usr/share/aclocal -I . -I m4
autoheader
automake -a -c -f
autoconf
CFLAGS="$RPM_OPT_FLAGS"			\
./configure --prefix=%{_prefix}		\
	    --datadir=%{_datadir}       \
	    --sysconfdir=%{_sysconfdir} \
	    --enable-poppler-glib	\
            --disable-poppler-qt        \
            --disable-poppler-qt4       \
	    --mandir=%{_mandir}	        \
            --enable-zlib               \
            --enable-xpdf-headers       \
            %{gtk_doc_option}

#Workaround a bug in libtool where it's using -Qoption to pass arguments
#to ld, which causes the build to fail. See bugster#6877423.
%if %cc_is_gcc
%else
perl -p -i.orig -e 's/^whole_archive.*// if (m/^whole_archive_flag_spec=.*\\\${wl}-z.*$/);' libtool
%endif

make -j $CPUS

%install
make DESTDIR=$RPM_BUILD_ROOT GTKDOC_REBASE=/usr/bin/gtkdoc-rebase install
rm $RPM_BUILD_ROOT%{_libdir}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%{_bindir}
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/poppler/
%{_libdir}/*.so
%{_libdir}/pkgconfig/
%{_datadir}/gtk-doc

%changelog
* Wed Oct 05 2011 - brian.cameron@oracle.com
- Bump to 0.18.0.
* Wed Oct 20 2010 - brian.cameron@oracle.com
- bump to 0.14.4.
* Thu Jun 17 2010 - brian.cameorn@oracle.com
- Bump to 0.14.0.  Remove upstream patch poppler-05-handle-passwd.diff.
  Add patch poppler-05-compile.diff to fix some compile issues.
* Thu May 13 2010 - brian.cameron@oracle.com
- Bump to 0.12.4.
* Thu Oct 15 2009 - dave.lin@sun.com
- Add "--enable-xpdf-headers" to ship xpdf headers required by
  gnome-commander(1.2.8.2).
* Mon Sep 14 2009 - darren.kenny@sun.com
- Bump to 0.12.0, stable version.
* Wed Sep 02 2009 - darren.kenny@sun.com
- Replace libtool patch with a perl script to replace use of \${wl} with
  nothing since this is what later versions of libtool have done.
* Sun Aug 30 2009 - darren.kenny@sun.com
- Bump to 0.11.3, add two patches, one for compiler issues, including a memory
  allocation error if inline functions are used, and another to fix a mis-use
  of the -Qoption flages in libtool causing mis-linking.
* Fri Jul 24 2009 - christian.kelly@sun.com
- Bump to 0.10.7.
* Wed Apr 22 2009 - dave.lin@sun.com
- Removed the line "libtoolize ..." to fix build issue.
* Mon Apr 20 2009 - darren.kenny@sun.com
- Bump to 0.10.6 to get security fixes and resolve bug#6827182
- Remove upstream patch for munmap compile issue.
- Add new patch to address SS12 compiler bug#6685564
* Wed Apr 07 2009 - darren.kenny@sun.com
- Add patch poppler-02-munmap-build-issue.diff to fix build issue.
* Tue Apr 06 2009 - darren.kenny@sun.com
- Bump to 0.10.5.
* Thu Aug 07 2008 - darren.kenny@sun.com
- Bump to 0.8.5.
* Mon Jul 14 2008 - darren.kenny@sun.com
- Bump to 0.8.4,
* Fri Jun 06 2008 - brian.cameron@sun.com
- Bump to 0.8.3. Remove upstream patch poppler-02-cairo-ft-bug.diff.
* Wed Apr 04 2008 - darren.kenny
- Bump to 0.8.0.
* Wed Apr 04 2008 - darren.kenny
- Apply patch from bug at : http://bugs.freedesktop.org/show_bug.cgi?15216
  to fix a crash when handling some FT fonts in PDF documents.
* Wed Jan 30 2008 - brian.cameron@sun.com
- Bump to 0.6.4.
* Wed Dec 19 2007 - brian.cameron@sun.com
- Bump to 0.6.3.
* Tue Dec 04 2007 - damien.carbery@sun.com
- Bump to 0.6.2.
* Fri Oct 19 2007 - damien.carbery@sun.com
- Bump to 0.6.1. Remove upstream patch, 02-fixcast.
* Mon Sep 03 2007 - brian.cameron@sun.com
- Bump to 0.6.0
* Tue Aug 28 2007 - damien.carbery@sun.com
- Bump to 0.5.91. Remove upstream patch, 02-c++issues.
* Wed Jul 04 2007 - darren.kenny@sun.com
- Remove poppler-02-glib-2.diff since it appears to be already in 0.5.9.
- Add new poppler-02-c++issues.diff patch to fix some C++ Compilation issues
  in 0.5.9.
* Fri May 18 2007 - laca@sun.com
- explicitely disable qt/qt4 support.
* Fri Nov  3 2006 - laca@sun.com
- use %gtk_doc_option in configure so that it can be disabled using
  --without-gtk-doc.
* Sun Jun 11 2006 - laca@sun.com
- Bump to 0.5.3 to fix the build of evince.
- Add patch, 03-glib-2, so that configure looks for glib-2.0, not the old glib.
  Freedesktop bugzilla #8600.
* Tue Mar 14 2006 - damien.carbery@sun.com
- Bump to 0.5.1 as required by evince 0.5.2.
* Sun Jan 22 2006 - damien.carbery@sun.com
- Bump to 0.5.0, as required by evince 0.5.0.
- Point to 'm4' dir in aclocal call.
- Remove upstream patch, 01-freetype. Renumber others.
* Tue Jan 17 2006 - damien.carbery@sun.com
- Bump to 0.4.4.
* Tue Jan 03 2006 - damien.carbery@sun.com
- Remove upstream patch, 02-macrofix.
* Tue Dec 20 2005 - dermot.mccluskey@sun.com
- Bump to 0.4.3.
* Tue Nov 29 2005 - laca@sun.com
- add uninstalled.pc.diff patch so that poppler can be in the same Solaris
  pkg as evince.
* Thu Oct 13 2005 - damien.carbery@sun.com
- Enable poppler-glib as it is required by evince.
* Fri Sep 30 2005 - brian.cameron@sun.com
- Bump to 0.4.2.
* Tue Sep 20 2005 - laca@sun.com
- add FREETYPE_CFLAGS to CFLAGS where needed.
* Tue Aug 16 2005 - damien.carbery@sun.com
- Bump to 0.4.0.
* Tue Aug 16 2005 - glynn.foster@sun.com
- Initial spec file for poppler.
