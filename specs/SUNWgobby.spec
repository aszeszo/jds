#
# spec file for package SUNWgobby
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner kevmca
#

%include Solaris.inc

%define OSR 9643:0.4

Name:           SUNWgobby
IPS_package_name: editor/gobby
Meta(info.classification): %{classification_prefix}:Development/Editors,%{classification_prefix}:System/Text Tools
License:        GPLv2
Summary:        A collaborative text editor
Version:        0.4.12
Source:         http://releases.0x539.de/gobby/gobby-%{version}.tar.gz
Source1:        l10n-configure.sh
# owner:trisk date:2007-8-17 type:bug
Patch1:         gobby-01-prototype.diff
# owner:trisk date:2007-8-17 type:bug
Patch2:         gobby-02-const.diff
# owner:trisk date:2007-8-17 type:bug
Patch3:         gobby-03-auto_ptr.diff
# owner:mattman date:2009-02-27 type:branding
Patch8:         gobby-08-manpage.diff
SUNW_Basedir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
URL:            http://gobby.0x539.de/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
%include desktop-incorporation.inc
Requires:       SUNWgtk2
Requires:       SUNWgnutls
Requires:       SUNWobby
Requires:       SUNWgnome-gtksourceview
Requires:       SUNWgnome-libs
Requires:       SUNWlibxmlpp
Requires:       SUNWgtkmm
Requires:       SUNWdesktop-cache
BuildRequires:  SUNWgtk2-devel
BuildRequires:  SUNWgnutls-devel
BuildRequires:  SUNWobby-devel
BuildRequires:  SUNWgnome-gtksourceview-devel
BuildRequires:  SUNWgnome-libs-devel
BuildRequires:  SUNWlibxmlpp-devel
BuildRequires:  SUNWgtkmm-devel

%package l10n
Summary:        %{summary} - l10n files
Requires:       %{name}

%description
Gobby is a free collaborative editor. This means that it
provides you with the possibility to edit files simultaneously
with other users over a network. It supports multiple
documents in one session and a multi-user chat. The platforms
on which you could use Gobby are so far Microsoft Windows,
Linux, Mac OS X and other Unix-like ones. Developed with the
Gtk+ toolkit it integrates nicely into the GNOME desktop
environment if you want it to.

%prep
%setup -q -n gobby-%version
bash %SOURCE1 --enable-sun-linguas

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch8 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

# compiler seems to run out of space when running on a 24-core system
if [ $CPUS -gt 4 ]; then
    CPUS=4
fi

CXXFLAGS="-xO2"
export LDFLAGS="%_ldflags"

%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif

intltoolize --copy --force --automake

bash -x %SOURCE1 --enable-copyright

aclocal -I m4
autoconf
automake -a --copy --force
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}                     \
            --libexecdir=%{_libexecdir}             \
            --sysconfdir=%{_sysconfdir}             \
            --with-gnome

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%restart_fmri icon-cache desktop-mime-cache

%postun
%restart_fmri desktop-mime-cache

%files
%doc AUTHORS
%doc(bzip2) COPYING NEWS ChangeLog README
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, other) %{_datadir}/applications
%{_datadir}/applications/*
%dir %attr (0755, root, other) %{_datadir}/icons
%attr (0755, root, other) %{_datadir}/icons/*
%{_datadir}/gobby
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%attr (-, root, other) %{_datadir}/locale

%changelog
* Wed Jan 27 2010 - brian.cameron@sun.com
- Bump to 0.4.12.
* Fri Apr  3 2009 - laca@sun.com
- use desktop-cache instead of postrun.
* Tue Mar 3 2009 - kevin.mcareavey@sun.com
- Bump to 0.4.10.
* Fri Feb 27 2009 - matt.keenan@sun.com
- Add manpage patch for Attributes and ARC Comment.
* Mon Dec 22 2008 - takao.fujiwara@sun.com
- Add gobby-06-g11n-desktop.diff for desktop.in
- Add gobby-07-g11n-po.diff for upstreamed translations.
* Fri Nov 28 2008 - takao.fujiwara@sun.com
- Add gobby-04-g11n-encoding.diff to support the current encoding.
- Add gobby-05-g11n-filename.diff to show the status on none UTF-8 locales.
* Tue Sep 23 2008 - dave.lin@sun.com
- Set attribute to %{_datadir} in base & l10n pkg.
* Fri Sep 19 2008 - kevin.mcareavey@sun.com
- Changed %doc files to bzip2.
- Changed %post and %postun to use scripts.
* Thu Sep 18 2008 - kevin.mcareavey@sun.com
- Cleanup for spec-files-other integration.
* Wed Nov 14 2007 - daymobrew@users.sourceforge.net
- Add l10n package.
* Mon Sep 17 2007 - trisk@acm.jhu.edu
- Bump to 0.4.5.
* Fri Aug 17 2007 - trisk@acm.jhu.edu
- Initial version.
