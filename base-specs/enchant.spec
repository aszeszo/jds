#
# spec file for package enchant
#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
# bugdb: bugzilla.abisource.com
#

%define OSR 5805:1.3.0

Name:     	enchant
License:	LGPL v2.1
Version: 	1.6.0
Release:	1
Vendor:		AbiWord
Distribution:	Java Desktop System
Copyright:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Docdir:         %{_datadir}/doc
Autoreqprov:    on
URL:		http://www.abisource.com/projects/enchant/
Source:		http://www.abisource.com/downloads/%{name}/%{version}/%{name}-%{version}.tar.gz
# date:2008-11-19 owner:jefftsai type:branding
Patch2:         enchant-02-build-request-dict.diff
# This patch is applied until zemberek-server is implemented.
# date:2009-01-14 owner:fujiwara type:feature bugster:6793551
Patch3:         enchant-03-zemberek-segv.diff
# date:2009-01-14 owner:fujiwara type:feature
Patch4:         enchant-04-ordering.diff
# date:2009-08-20 owner:wangke type:branding
Patch5:		enchant-05-build-ispell.diff
Summary:	Generic spell checking library
Group:		Applications/Text

%description
Enchant is a generic spell checking library that presents an API/ABI to 
applications.

%files
%defattr(-, root, root)

%prep
%setup  -q -n %{name}-%{version}
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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

libtoolize --force
aclocal 
autoconf
automake -a -c -f
export CFLAGS="%optflags"
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%{_ldflags}"
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --bindir=%{_bindir} \
    --sysconfdir=%{_sysconfdir} \
    --mandir=%{_mandir} \
    --infodir=%{_datadir}/info \
    --localstatedir=/var \
	--with-myspell-dir=/usr/share/spell/myspell \
	--disable-aspell \
    --disable-static

make -j $CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 13 2010 - brian.cameron@oracle.com
- Bump to 1.6.0.  Remove upstream patch
  enchant-06-zemberek-dict-only-if-installed.diff.
* Wed Nov 04 2009 - hemantha.holla@sun.com
- Add patch -06-zemberek-dict-only-if-installed as fix for 6887232
* Thu Jul 16 2009 - ke.wang@sun.com
- Bump to 1.5.0.
- Removed upstreamed patch enchant-01-define_FILE.diff.
- Updated patch enchant-02-build-request-dict.diff.
- Updated patch enchant-03-zemberek-segv.diff.
- Added "libtoolize --force" to recreate aclocal.m4 because of version mismatch.
* Wed Jan 14 2009 - takao.fujiwara@sun.com
- Add patch zemberek-segv.diff to avoid segv on tr_TR.UTF-8.
- Add patch ordering.diff so that we configure myspell by default.
* Wed Nov 19 2008 - jeff.cai@sun.com
- Add patch -02-build-request-dic to solve the build issue
  with SunStudio 12.
* Mon Nov 10 2008 - jeff.cai@sun.com
- Remove patch -02-aspell-conversion.diff  because 
  it looks like not many users need to convert the local 
  aspell dictionary to myspell format. We don't like to 
  maintain a large Solaris only patch.
* Fri Oct 31 2008 - jeff.cai@sun.com
- Bump to 1.4.2.
- Remove upstream patch -02-uninstalled-pc.diff.
- Remove upstream patch -03-personaldic.diff.
- Remove unused patch -02-aspell-conversion.diff.
- Rework patch -01-define-FILE.diff.
* Fri Oct 31 2008 - jeff.cai@sun.com
- Change the license tag.
* Mon Jul 07 2008 - jeff.cai@sun.com
- Move 'rm' lines to SUNgnome-spell.spec.
* Sat Apr 28 2007 - irene.huang@sun.com
- split patch -03-personaldic.diff into two patches:
  -03-personaldic.diff and -04-apsell-conversion.diff, since 
  -03 has been upsteamed to community and will be removed
  when enchant is bumped to a new version. 
* Sat Apr 28 2007 - irene.huang@sun.com
- change the dictionary path to /usr/share/spell/myspell
  this is the place where the dictionaries should go according
  to LASRC 2007/231, targeting build 65.
* Fri Apr 13 2007 - irene.huang@sun.com
- put enchant++.h back to the package. 
* Tue Apr 10 2007 - irene.huang@sun.com	
- Add patch enchant-02-personaldic.diff to enable personal dictionary support
  of enchant myspell backend and conversion of aspell personal dict to myspell
  format. Fixes bug 6529848 and 6529853.
* Wed Feb 14 2007 - jeff.cai@sun.com
- Make enchant use myspell instead of aspell.
- Add patch enchant-02-uninstalled-pc.diff to enable building in one spec file
  for gnome-spell and enchant.
* Mon Dec 11 2006 - damien.carbery@sun.com
- Remove unnecessary automake call; add autoconf and adjust aclocal calls.
* Fri Dec 08 2006 - damien.carbery@sun.com
- Initial spec.
