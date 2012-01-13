#
# spec file for package dia
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner jefftsai 
#

%define OSR LFI#105446 (gnome Exec. summary):n/a

Name:           dia
License:	    GPL
Group:		System/GUI/GNOME
Vendor:		Gnome Community
Summary:        Dia Diagram Editor
Version:        0.97.1
Source:		    http://ftp.gnome.org/pub/GNOME/sources/dia/0.97/dia-%{version}.tar.bz2
Source1:	l10n-configure.sh
SUNW_BaseDir:   %{_basedir}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#owner:gheet date:2011-02-25 type:bug bugster:7014628
Patch1:         dia-01-use-libpng12.diff

%prep
%setup -q -n %name-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

libtoolize --copy --force
intltoolize --automake --force --copy

bash -x %SOURCE1 --enable-copyright

aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f 
autoconf

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --enable-gnome                   \
            --with-cairo                     \
            --disable-static

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm  $RPM_BUILD_ROOT%{_libdir}/dia/*.la
rmdir  $RPM_BUILD_ROOT%{_datadir}/oaf

%if %build_l10n
%else
# REMOVE l10n FILES
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Apr 15 2009 - Matt.Keenan@sun.com
- Bump to 0.97, remove all 6 patches, All upstreamed
* Tue Jan 06 2009 - takao.fujiwara@sun.com
- Add l10n-configure.sh for copyright.
- Add patch goption.diff from trunk.
* Mon Dec 22 2008 - takao.fujiwara@sun.com
- Add patch g11n-filename.diff to fix crash on none UTF-8.
* Wed Dec 03 2008 - Matt.Keenan@sun.com
- Fix GtkSpinButton warnings because of new gtk bugster:6779724, bugzilla:563106
* Wed Oct 22 2008 - Matt.Keenan@sun.com
- created
