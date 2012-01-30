#
# spec file for package SUNWlibgee
#
# includes module(s): vala
#
%define owner jouby 

%define OSR LFI#105446 (gnome Exec. summary):n/a

%include Solaris.inc


Name:                SUNWlibgee
IPS_package_name:    library/desktop/libgee
Meta(info.classification): %{classification_prefix}:Development/GNOME and GTK+
Summary:             libgee is a collection library providing GObject-based interfaces and classes for commonly used data structures
Version:             0.6.0
Source:              http://download.gnome.org/sources/libgee/0.6/libgee-%{version}.tar.bz2
# date:2009-10-20 owner:jouby type:branding
Patch1:              libgee-01-disable-test.diff
SUNW_BaseDir:        %{_basedir}
SUNW_Copyright:      %{name}.copyright
License:             LGPL v2.1
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include gnome-incorporation.inc
BuildRequires:       SUNWglib2
BuildRequires:       SUNWglib2-devel
Requires:            SUNWgobject-introspection

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc
%include gnome-incorporation.inc
Requires: %name


%prep
rm -rf libgee-%version
%setup -q -n  libgee-%version
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

aclocal
libtoolize --copy --force 
automake -a -f
autoconf -f 
./configure --prefix=%{_prefix}			\
            --bindir=%{_bindir}			\
            --libdir=%{_libdir}			\
            --sysconfdir=%{_sysconfdir}		\
            --includedir=%{_includedir} 	\
            --mandir=%{_mandir}			

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%{_libdir}/girepository-*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/*

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Tue Nov 09 2010 - dave.lin@oracle.com
- Add %{_libdir}/girepository-*.
* Wed Oct 27 2010 - brian.cameron@oracle.com
- Bump to 0.6.0.
* Fri Apl 30 2010 - yuntong.jin@sun.com
- change owner to jouby
* Tus Oct 20 2009 - jerry.tan@sun.com
- import to solaris
* Fri Jul 27 2007 - dougs@truemail.co.th
- Initial spec


