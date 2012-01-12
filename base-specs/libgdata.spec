#
# spec file for package libgdata
#
# includes module(s): libgdata
#
%define owner jouby 

%define OSR LFI#105446 (gnome Exec. summary):n/a

%include Solaris.inc

Name:                libgdata
Summary:             libgdata is a collection library providing GObject-based interfaces and classes for commonly used data structures
Version:             0.6.5
License:             LGPL v2
Vendor:              Gnome Community
Source:              http://download.gnome.org/sources/libgdata/0.6/libgdata-%{version}.tar.bz2

BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc


%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc
Requires: %name


%prep
rm -rf libgdata-%version
%setup -q -n  libgdata-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
./configure --prefix=%{_prefix}			\
            --bindir=%{_bindir}			\
            --libdir=%{_libdir}			\
            --sysconfdir=%{_sysconfdir}		\
            --includedir=%{_includedir} 	\
            --mandir=%{_mandir}			

gmake -j$CPUS

%install
gmake install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "lib*.*a" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Mon Oct 25 2010 - brian.cameron@oracle.com
- Bump to 0.6.5.
* Fri Apr 30 2010 - yuntong.jin@sun.com
- Change ownership to jouby
* Wed Jan 13 2010 - christian.kelly@sun.com
- Fix %files.
* Tus Oct 20 2009 - jerry.tan@sun.com
- import to solaris
* Fri Jul 27 2007 - dougs@truemail.co.th
- Initial spec
