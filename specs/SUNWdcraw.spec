#
# spec file for package SUNWdcraw
#
# Copyright 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner bnitz
#

%include Solaris.inc

%define OSR 8098:8.81

Name:                    SUNWdcraw
IPS_package_name:        image/dcraw
Meta(info.classification): %{classification_prefix}:System/Media
Summary:                 dcraw - Decoding RAW digital photos
License:                 GPL
URL:                     http://www.cybercom.net/~dcoffin/dcraw/
Version:                 8.99
SUNW_BaseDir:		 %{_basedir}
SUNW_Copyright:          %{name}.copyright
Source:                  http://cybercom.net/~dcoffin/dcraw/archive/dcraw-%{version}.tar.gz
# date:2008-02-22 owner:fujiwara type:bug bugster:6666520
Patch1:                  dcraw-01-locale-h.diff
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc
Requires:		SUNWlibmsr
BuildRequires:  	SUNWjpg
Requires:		SUNWlcms
BuildRequires:		SUNWlcms
BuildRequires:		SUNWgnome-common-devel

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -c -n %{name}-%{version}
cd dcraw
%patch1 -p1
cd ..

%build
cd dcraw
# There's no Makefiles - it's just a single .c file
export CFLAGS="%optflags `pkg-config --cflags lcms` -o dcraw -lm -ljpeg `pkg-config --libs lcms`"
export CFLAGS="$CFLAGS -DLOCALEDIR=\"%{_datadir}/locale\""
${CC} $CFLAGS dcraw.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cd dcraw
cp dcraw $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp dcraw.1 $RPM_BUILD_ROOT%{_mandir}/man1

for po in dcraw_*.po
do
	lang=`basename $po .po | sed -e 's/^dcraw_//'`
	mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	msgfmt -o $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/dcraw.mo dcraw_$lang.po
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/dcraw
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/dcraw.1

%files l10n
%defattr(-, root, other)
%dir %attr(0755, root, sys) %{_datadir}
%{_datadir}/locale/*

%changelog
* Thu Jan 28 2010 - brian.cameron@sun.com
- Bump to 8.99.
* Thu Oct 22 2009 - harry.lu@sun.com
* Remove "in Linux" from summary
* Wed Aug 12 2009 - christian.kelly@sun.com
- Bump to 8.95.
* Tue Sep 23 2008 - dave.lin@sun.com
- Remove %{_datadir}/doc since it doesn't exist.
* Fri May 16 2008 - damien.carbery@sun.com
- Use pkg-config to determine CFLAGS and LIBS for lcms.
* Fri Feb 22 2008 - takao.fujiwara@sun.com
- Add dcraw-01-locale-h.diff to avoid build errors.
* Mon Feb 18 2008 - damien.carbery@sun.com
- Set %attr for %_datadir in l10n package.
* Fri Feb 15 2008 - dermot.mccluskey@sun.com
- put l10n files in optionally build -l10n pkg
- use CC and CFLAGS to compile
* Tue Feb 12 2008 - dermot.mccluskey@sun.com
- initial version



