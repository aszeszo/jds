#
# spec file for package SFEswig
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# temp spec for swig, needed by graphviz, until SFW integrates swig
#
%include Solaris.inc

Name:                    SFEswig
Summary:                 SWIG Interface compiler
Version:                 1.3.35
Source:                  http://downloads.sourceforge.net/swig/swig-%{version}.tar.gz
# date:2008-07-24 owner:dermot type:bug
Patch1:                  swig-01-solaris_include.diff
URL:                     http://www.swig.org/
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
Requires: SUNWlibC
Requires: SUNWlibms


%prep
%setup -q -n swig-%version
%patch1 -p0


%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="%optflags"
%if %cc_is_gcc
%else
export CXX="${CXX} -norunpath"
%endif
export CXXFLAGS="%cxx_optflags"

./configure --prefix=%{_prefix} --mandir=%{_mandir} \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/*

%changelog
* Wed Jul 30 2008 - dermot.mccluskey@sun.com
- Bump to 1.3.35 and add patch for C++/Perl header issue.
* Thu Jan 24 2008 - nonsea@users.sourceforge.net
- Bump to 1.3.33.
* Tue Mar 06 2007 - nonsea@users.sourceforge.net
- Bump to 1.3.31
* Tue Nov 11 2006 - halton.huo@sun.com
- Bump to 1.3.30
* Fri Jun 23 2006 - laca@sun.com
- rename to SFEswig
- delete -share subpkg
- update file attributes to match JDS
* Sun Jan 08 2005 - glynn.foster@sun.com
- Initial spec file


