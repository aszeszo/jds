#
# spec file for package SUNWgroff
#
# includes module(s): groff
#
# Copyright (c) 2008, 2011, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner padraig
#
%include Solaris.inc

%define OSR 9396:1.19.2

Name:              SUNWgroff
IPS_package_name:  text/groff
Meta(info.classification): %{classification_prefix}:System/Text Tools
License:           GPL v2
Summary:           GNU roff Text Formatting
# Do not bump to 1.20 since the license changed to GPLv3.  Legal review is
# required before updating. 
version:           1.19.2
Source:            http://ftp.gnu.org/gnu/groff/groff-%{version}.tar.gz
# date:2009-02-25 owner:mattman type:branding
Patch1:            groff-01-manpages.diff
# date:2011-06-28 owner:padraig type:bug bugster:6828304
Patch2:            groff-02-grog-fix.diff
SUNW_BaseDir:      %{_basedir}
SUNW_Copyright:    %{name}.copyright
License:           GPL v2
BuildRoot:         %{_tmppath}/%{name}-%{version}-build
%include desktop-incorporation.inc
%include default-depend.inc
Requires: SUNWlibC
Requires: SUNWlibms
BuildRequires: runtime/perl-512
Requires: SUNWesu
Requires: SUNWdbus
Requires: SUNWdbus-glib
Requires: SUNWflexruntime
Requires: SUNWfontconfig
Requires: SUNWfreetype2
Requires: SUNWgccruntime
Requires: SUNWlibgcrypt
Requires: SUNWgroff-core
BuildRequires: SUNWxwrtl
BuildRequires: SUNWxwplt
BuildRequires: SUNWxwice
BuildRequires: SUNWgtk2
BuildRequires: SUNWglib2
BuildRequires: print/filter/ghostscript
BuildRequires: text/gnu-sed
BuildRequires: SUNWpsutils

%package -n SUNWgroff-core
IPS_package_name: text/groff/groff-core
Meta(info.classification): %{classification_prefix}:System/Text Tools
Summary:           GNU roff Text Formatting (core system components)
IPS_legacy: false
%include default-depend.inc
%include desktop-incorporation.inc

%prep
%setup -q -n groff-%version
%patch1 -p1
%patch2 -p1

%build
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif

libtoolize --force
aclocal $ACLOCAL_FLAGS -I .
if (which autoconf-2.61 >/dev/null 2>&1); then
    autoconf-2.61
else
    autoconf
fi
if (which autoheader-2.61 >/dev/null 2>&1); then
    autoheader-2.61
else
    autoheader
fi
bash ./configure     --prefix=%{_prefix}             \
                --datadir=%{_datadir}           \
                --with-appresdir=%{_prefix}/X11/lib/X11/app-defaults \
                --sysconfdir=%{_sysconfdir}
make

%install
rm -rf $RPM_BUILD_ROOT%{_prefix}
mkdir -p $RPM_BUILD_ROOT%{_prefix}
make appresdir=$RPM_BUILD_ROOT%{_prefix}/X11/lib/X11/app-defaults datadir=$RPM_BUILD_ROOT%{_datadir} prefix=$RPM_BUILD_ROOT%{_prefix} man5ext=4 man7ext=5 install

test -f $RPM_BUILD_ROOT/%{_datadir}/info/dir && \
  rm $RPM_BUILD_ROOT/%{_datadir}/info/dir
# remove a man page groff_out.n which is handled poorly by catman(1) see 6768097
rm $RPM_BUILD_ROOT/%{_datadir}/man/man4/groff_out.4
 
mkdir -p $RPM_BUILD_ROOT%{_prefix}/gnu/bin
rmdir $RPM_BUILD_ROOT%{_datadir}/groff/site-font

BINARIES="diffmk eqn grn indxbib neqn nroff pic refer soelim"
cd $RPM_BUILD_ROOT%{_bindir}

for file in $BINARIES ; do
    [ -f g$file ] || mv $file g$file
    cp g$file ../gnu/bin/$file
    rm g$file
    ln -s ../gnu/bin/$file g$file
done

for file in lookbib tbl troff; do
    [ -f $file ] && mv $file g$file
done

MANPAGES="eqn neqn nroff pic soelim grn indxbib lookbib refer tbl troff"
cd $RPM_BUILD_ROOT/%{_datadir}/man/man1
for file in $MANPAGES; do
    [ -f $file.1 ] && mv $file.1 g$file.1
done

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/addftinfo
%{_bindir}/afmtodit
%{_bindir}/eqn2graph
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/ggrn
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/gindxbib
%{_bindir}/glookbib
%{_bindir}/grap2graph
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/grefer
%{_bindir}/grodvi
%{_bindir}/groffer
%{_bindir}/grolbp
%{_bindir}/grolj4
%{_bindir}/gxditview
%{_bindir}/hpftodit
%{_bindir}/lkbib
%{_bindir}/mmroff
%{_bindir}/pdfroff
%{_bindir}/pfbtops
%{_bindir}/pic2graph
%{_bindir}/post-grohtml
%{_bindir}/pre-grohtml
%{_bindir}/tfmtodit
%{_bindir}/xtotroff

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/groff
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/groff/%{version}/font/devX100-12/*
%{_datadir}/groff/%{version}/font/devX100/*
%{_datadir}/groff/%{version}/font/devX75-12/*
%{_datadir}/groff/%{version}/font/devX75/*
%{_datadir}/groff/%{version}/font/devdvi/*
%{_datadir}/groff/%{version}/font/devhtml/*
%{_datadir}/groff/%{version}/font/devlbp/*
%{_datadir}/groff/%{version}/font/devlj4/*
%{_datadir}/groff/%{version}/tmac/X.tmac
%{_datadir}/groff/%{version}/tmac/Xps.tmac
%{_datadir}/groff/%{version}/tmac/a4.tmac
%{_datadir}/groff/%{version}/tmac/cp1047.tmac
%{_datadir}/groff/%{version}/tmac/dvi.tmac
%{_datadir}/groff/%{version}/tmac/e.tmac
%{_datadir}/groff/%{version}/tmac/ec.tmac
%{_datadir}/groff/%{version}/tmac/html.tmac
%{_datadir}/groff/%{version}/tmac/html-end.tmac
%{_datadir}/groff/%{version}/tmac/lbp.tmac
%{_datadir}/groff/%{version}/tmac/lj4.tmac
%{_datadir}/groff/%{version}/tmac/me.tmac
%{_datadir}/groff/%{version}/tmac/mm/*
%{_datadir}/groff/%{version}/tmac/mom.tmac
%{_datadir}/groff/%{version}/tmac/ms.tmac
%{_datadir}/groff/%{version}/tmac/om.tmac
%{_datadir}/groff/%{version}/tmac/pdfmark.tmac
%{_datadir}/groff/%{version}/tmac/spdf.tmac
%{_datadir}/groff/%{version}/tmac/trace.tmac
%{_datadir}/info/groff*
%{_datadir}/doc/groff*
%{_prefix}/X11/lib/X11/app-defaults/*
%{_libdir}/groff/*
%{_mandir}/man1/addftinfo.1
%{_mandir}/man1/afmtodit.1
%{_mandir}/man1/eqn2graph.1
%{_mandir}/man1/ggrn.1
%{_mandir}/man1/gindxbib.1
%{_mandir}/man1/glookbib.1
%{_mandir}/man1/grap2graph.1
%{_mandir}/man1/grefer.1
%{_mandir}/man1/grodvi.1
%{_mandir}/man1/groffer.1
%{_mandir}/man1/grohtml.1
%{_mandir}/man1/grolbp.1
%{_mandir}/man1/grolj4.1
%{_mandir}/man1/gxditview.1
%{_mandir}/man1/hpftodit.1
%{_mandir}/man1/lkbib.1
%{_mandir}/man1/mmroff.1
%{_mandir}/man1/pdfroff.1
%{_mandir}/man1/pfbtops.1
%{_mandir}/man1/pic2graph.1
%{_mandir}/man1/tfmtodit.1
%{_mandir}/man1/xtotroff.1
%{_mandir}/man4/*
%{_mandir}/man5/*

%dir %attr (0755, root, bin) %{_prefix}/gnu
%dir %attr (0755, root, bin) %{_prefix}/gnu/bin
%defattr(0755, root, root)
%{_prefix}/gnu/bin/grn
%{_prefix}/gnu/bin/indxbib
%{_prefix}/gnu/bin/refer
%defattr(-, root, bin)

%files core
%defattr(-, root, bin)
%doc(bzip2) COPYING ChangeLog
%doc NEWS README
%dir %attr (0755, root, bin) %{_bindir}
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/gdiffmk
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/geqn
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/gpic
%{_bindir}/groff
%{_bindir}/grog
%{_bindir}/grops
%{_bindir}/grotty
%{_bindir}/gtbl
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/gneqn
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/gnroff
%ips_tag(facet.compat.gnulinks=true) %{_bindir}/gsoelim
%{_bindir}/gtroff

%dir %attr (0755, root, bin) %{_prefix}/gnu
%dir %attr (0755, root, bin) %{_prefix}/gnu/bin
%{_prefix}/gnu/bin/diffmk
%{_prefix}/gnu/bin/eqn
%{_prefix}/gnu/bin/pic
%{_prefix}/gnu/bin/neqn
%{_prefix}/gnu/bin/nroff
%{_prefix}/gnu/bin/soelim

%{_datadir}/groff/%{version}/eign
%{_datadir}/groff/%{version}/font/devascii
%{_datadir}/groff/%{version}/font/devlatin1
%{_datadir}/groff/%{version}/font/devps
%{_datadir}/groff/%{version}/font/devutf8
%{_datadir}/groff/%{version}/tmac/an-old.tmac
%{_datadir}/groff/%{version}/tmac/andoc.tmac
%{_datadir}/groff/%{version}/tmac/composite.tmac
%{_datadir}/groff/%{version}/tmac/devtag.tmac
%{_datadir}/groff/%{version}/tmac/doc-old.tmac
%{_datadir}/groff/%{version}/tmac/doc.tmac
%{_datadir}/groff/%{version}/tmac/eqnrc
%{_datadir}/groff/%{version}/tmac/gan.tmac
%{_datadir}/groff/%{version}/tmac/gm.tmac
%{_datadir}/groff/%{version}/tmac/gmm.tmac
%{_datadir}/groff/%{version}/tmac/gmmse.tmac
%{_datadir}/groff/%{version}/tmac/gmse.tmac
%{_datadir}/groff/%{version}/tmac/gs.tmac
%{_datadir}/groff/%{version}/tmac/hyphen.us
%{_datadir}/groff/%{version}/tmac/hyphenex.us
%{_datadir}/groff/%{version}/tmac/latin1.tmac
%{_datadir}/groff/%{version}/tmac/latin2.tmac
%{_datadir}/groff/%{version}/tmac/latin9.tmac
%{_datadir}/groff/%{version}/tmac/man.tmac
%{_datadir}/groff/%{version}/tmac/mandoc.tmac
%{_datadir}/groff/%{version}/tmac/mdoc.tmac
%{_datadir}/groff/%{version}/tmac/mdoc/doc-common
%{_datadir}/groff/%{version}/tmac/mdoc/doc-ditroff
%{_datadir}/groff/%{version}/tmac/mdoc/doc-nroff
%{_datadir}/groff/%{version}/tmac/mdoc/doc-syms
%{_datadir}/groff/%{version}/tmac/papersize.tmac
%{_datadir}/groff/%{version}/tmac/pic.tmac
%{_datadir}/groff/%{version}/tmac/europs.tmac
%{_datadir}/groff/%{version}/tmac/ps.tmac
%{_datadir}/groff/%{version}/tmac/psatk.tmac
%{_datadir}/groff/%{version}/tmac/psold.tmac
%{_datadir}/groff/%{version}/tmac/pspic.tmac
%{_datadir}/groff/%{version}/tmac/safer.tmac
%{_datadir}/groff/%{version}/tmac/troffrc
%{_datadir}/groff/%{version}/tmac/troffrc-end
%{_datadir}/groff/%{version}/tmac/tty-char.tmac
%{_datadir}/groff/%{version}/tmac/tty.tmac
%{_datadir}/groff/%{version}/tmac/unicode.tmac
%{_datadir}/groff/%{version}/tmac/www.tmac
%{_datadir}/groff/site-tmac/man.local
%{_datadir}/groff/site-tmac/mdoc.local

%{_mandir}/man1/gdiffmk.1
%{_mandir}/man1/geqn.1
%{_mandir}/man1/gneqn.1
%{_mandir}/man1/gnroff.1
%{_mandir}/man1/gpic.1
%{_mandir}/man1/groff.1
%{_mandir}/man1/grog.1
%{_mandir}/man1/grops.1
%{_mandir}/man1/grotty.1
%{_mandir}/man1/gsoelim.1
%{_mandir}/man1/gtbl.1
%{_mandir}/man1/gtroff.1

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/groff
%dir %attr (0755, root, other) %{_datadir}/doc

%actions core
depend fmri=pkg:/text/groff@%{version}-%{ips_vendor_version} type=incorporate

%changelog
* Thu Aug 25 2011 - padraig.obriain@oracle.com
- Use -norunpath to fix  CR 7076612
* Tue Jun 28 2011 - padraig.obriain@oracle.com
- Add patch 02-grog-fix for CR 6828304
* Fri May  6 2011 - padraig.obriain@oracle.com
- Change base to core based on David Comay's comments.
* Thu Apr 28 2011 - laszlo.peter@oracle.com
- updates based on Danek's comments:
  - no dependency on gnome-incorporation
  - no dependencies on compatibility X package names
  - incorporate dependency on groff in groff-base
  - conditional dependency on groff in groff-base is libx11 is installed
  - no original_name tags needed
* Thu Apr 21 2011 - padraig.obriain@oracle.com
- Split into two packages text/groff and text/groff-base (CR7010324)
* Mon Apr  4 2011 - padraig.obriain@oracle.com
- Instead of delivering a binary in /usr/bin and link in /usr/gnu/bin
- deliver binary in /usr/gnu/bin and link in /usr/bin; set facet on link.
* Wed Nov 10 2010 - padraig.obriain@oracle.com
- Add license tag.
* Wed May 25 2010 - brian.cameron@oracle.com
- Revert to 1.19.2 since 1.20.x is GPLv3.
* Tue May 25 2010 - brian.cameron@oracle.com
- Bump to 1.20.1.
* Fri Mar 19 2010 - christian.kelly@sun.com
- Add 'exit 1' to disable build, keeps getting stuck in a loop.
* Sun Sep 13 2009 - alan.coopersmith@sun.com
- Fix typo in summary (reported by timeless on #opensolaris irc)
* Wed Jul 08 2009 - christian.kelly@sun.com
- %{_datadir}/info/dir has changed from a dir to a file. Still check if it 
  exists and remove. It clashes with SUNWsfinf.
* Tue Mar 24 2009 - dave.lin@sun.com
- Check dir %{_datadir}/info/dir existence before remove it.
* Wed Mar 04 2009 - dave.lin@sun.com
- Removed empty dirs {_datadir}/info/dir, %{_datadir}/groff/site-font
* Wed Feb 25 2009 - matt.keenan@sun.com
- Add manpages patch for Attributes and ARC Comments
* Tue Feb 10 2009 - halton.huo@sun.com
- Add Requires to fix issue #4 for CR6753371
* Wed Sep 10 2008 - padraig.obriain@sun.com
- Add %doc to %files for copyright
* Fri Aug 08 2008 - damien.carbery@sun.com
- Remove reference to %SOURCE1 as it is not defined. Remove deletion of
  %{_datadir}/info/dir because it is not installed.
* Wed Aug 05 2008 - padraig.obriain@sun.com
- Update following review
* Mon Jun 23 2008 - padraig.obriain@sun.com
- initial version


