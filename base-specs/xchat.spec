#
# spec file for package xchat
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner laca
# bugdb: http://sourceforge.net/tracker/?func=browse&group_id=239&atid=100239&aid=
#

%define OSR 9555:2.8.6

# Define whether we have gtk+ 2.13.x as it defines GType while 2.12.x defines
# GtkType (which is used in xchat source).
%define use_gtype  %(pkg-config --atleast-version=2.13 gtk+-2.0 && echo 1 || echo 0)

Name:                    xchat
Summary:                 XChat IRC Client
License:                 GPL v2
Vendor:                  xchat.org
Version:                 2.8.8
Source:                  http://www.xchat.org/files/source/2.8/xchat-%{version}.tar.bz2
# owner:laca type:bug date:2006-07-28
# this should go away once we build on GNU-compatible Solaris gettext
Patch1:                  xchat-01-gettext.diff
Patch2:                  xchat-02-ctcp-version.diff
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n %name-%version
%patch1 -p1 -b .patch01
%patch2 -p1
touch NEWS

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

glib-gettextize -f
libtoolize --copy --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f 
autoconf

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --enable-dbus                    \
            --enable-ipv6                    \
            --sysconfdir=%{_sysconfdir}

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm  $RPM_BUILD_ROOT%{_libdir}/xchat/plugins/*.la

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jul 15 2010 - brian.cameron@oracle.com
- Bump to 2.8.8.
* Wed Oct 21 2009 - trisk@opensolaris.org
- Add patch xchat-03-xc286-smallfixes.diff from upstream
- Add patch xchat-05-button-underline.diff to fix button mnemonics
- Enable IPv6
* Wed Dec 10 2008 - halton.huo@sun.com
- Remove zero-index.diff since SS12 support zero index array.
* Fri Jul 25 2008 - damien.carbery@sun.com
- Add patch 03-new-gtk-GtkType to use GType instead of GtkType. This is only
  applied when gtk+ 2.13.x is on the system, established by grep of
  /usr/lib/pkgconfig/gtk+-2.0.pc file.
* Thu Jul 24 2008 - laca@sun.com
- create xchat.spec from SFExchat.spec and move to spec-files-other
* Thu Jun 12 2008 - brian.cameron@sun.com
- Bump to 2.8.6.
* Mon Oct 22 2007 - brian.cameron@sun.com
- Remove patch xchat-03-dbus-LDADD.diff since it is not longer needed.
* Wed Oct 17 2007 - laca@sun.com
- add /usr/gnu to CFLAGS/LDFLAGS
* Thu Aug 02 2007 - Brian Cameron <brian.cameron@sun.com>
- Bump to 2.8.4.
* Tue May 29 2007 - Thomas Wagner
- bump to 2.8.2
- /usr/bin/msgfmt errors, use /opt/sfw/bin/msgfmt
- reworked patch for 2.8.2
* Sun Jan  7 2007 - laca@sun.com
- bump to 2.8.0, merge patches, update %files
* Mon Jul 31 2006 - glynn.foster@sun.com
- bump to 2.6.6
* Mon Jun 12 2006 - laca@sun.com
- bump to 2.6.4
- rename to SFExchat
- add -l10n pkg
- change to root:bin to follow other JDS pkgs.
- add patch that fixes the proxy in 2.6.4
* Fri Jun  2 2006 - laca@sun.com
- use post/postun scripts to install schemas into the merged gconf files
- merge -share pkg into base
* Thu Apr 20 2006 - damien.carbery@sun.com
- Bump to 2.6.2.
* Mon Mar 20 2006 - brian.cameron@sun.com
- Remove unneeded intltoolize call.
* Thu Jan 26 2006 - brian.cameron@sun.com
- Update to 2.6.1
* Wed Dec 07 2005 - brian.cameron@sun.com
- Update to 2.6.0
* Wed Oct 12 2005 - laca@sun.com
- update to 2.4.5; fix
* Thu Jan 06 2004 - Brian.Cameron@sun.com
- created
