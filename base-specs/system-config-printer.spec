#
# spec file for package system-config-printer
#
# includes module(s): system-onfig-printer
#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner gheet
#

%define OSR 10483&10484:1.0.x

%include l10n.inc

Name:         system-config-printer
License:      GPL V2
Group:        Development/Languages/Python
Version:      1.0.16
Release:      1
Distribution: Java Desktop System
Vendor:       Other
Summary:      Print Manager for CUPS
Source:       http://cyberelk.net/tim/data/%{name}/1.0.x/%{name}-%{version}.tar.bz2
Source1:      %{name}-po-sun-%{po_sun_version}.tar.bz2
# Source2: safaridoc from tech writer. Renamed PMOLH.xml to %{name}.xml
# Modified DOCTYPE to point at 4.1.2/docbookx.dtd
Source2:      %{name}-online-help.tar
Patch1:	      system-config-printer-01-temp-for-2.4.diff
Patch2:	      system-config-printer-02-no-manpage.diff
#owner:gheet date:2006-11-03 type:branding
Patch3:	      system-config-printer-03-app-path.diff
#owner:gheet date:2006-11-03 type:branding bugster:6780731
Patch4:	      system-config-printer-04-remove-fedora-specific.diff
#owner:gheet date:2009-12-10 type:bug doo:13117
Patch5:	      system-config-printer-05-init-monitor-timer.diff
#owner:gheet date:2009-12-18 type:branding 
Patch6:	      system-config-printer-06-python-version.diff
#owner:gheet date:2011-06-16 type:branding bugster:7049775 
Patch7:	      system-config-printer-07-online-help.diff
#owner:gheet date:2011-08-18 type:branding bugster:7076227
Patch8:	      system-config-printer-08-desktop-files.diff
URL:          http://cyberelk.net/tim/software/%{name}
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Docdir:       %{_defaultdocdir}/doc
Autoreqprov:  off
Prereq:       /sbin/ldconfig
Requires:     SUNWpycups
# uncomment this once we sorted samba 3.2.x
#Requires:     SUNWpysmbc
BuildRequires: SUNWpycups
#BuildRequires: SUNWpysmbc

%description
System Config Printer is a tool is to configure a CUPS server (often the local machine) 
using the CUPS API. The tool is written in Python, using pygtk for the graphical parts 
and with some Python bindings (pycups) for the CUPS API.

It is largely the same as using the CUPS web interface for configuring printers, but 
has the advantage of being a native application rather than a web page.

%prep
%setup -q -n %{name}-%{version}
mkdir -p help/C
cd help/C
tar xf %{SOURCE2}
cd ../..
bzcat %SOURCE1 | tar xf -
cd po-sun; make; cd ..

%patch01 -p1
%patch02 -p0
%patch03 -p0
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1

%build
export PYTHON=/usr/bin/python%{default_python_version}

cp /usr/share/gnome-common/data/*.make .
cp /usr/share/gnome-doc-utils/gnome-doc-utils.make .
intltoolize --force --copy
aclocal
automake -a -c -f
autoconf
./configure --prefix=/usr --libdir=/usr/lib --sysconfdir=/etc
make
make install DESTDIR=$RPM_BUILD_ROOT

%install
python%{default_python_version} setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

# move private directory from /usr/share to /usr/lib
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/*.py \
   $RPM_BUILD_ROOT%{_libdir}/%{name}
# move troubleshoot to /ur/lib
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/troubleshoot \
   $RPM_BUILD_ROOT%{_libdir}/%{name}

# Move system-config-printer-applet to /usr/lib/%{name}
mv $RPM_BUILD_ROOT%{_bindir}/system-config-printer-applet \
   $RPM_BUILD_ROOT%{_libdir}/%{name}

# do not deliver my-default-printer
rm $RPM_BUILD_ROOT%{_bindir}/my-default-printer
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/my-default-printer.py

# Remove desktop files which are not delivered in Solaris
rm -rf $RPM_BUILD_ROOT%{_datadir}/applications/redhat-my-default-printer.desktop
rm -rf $RPM_BUILD_ROOT%{_datadir}/applications/redhat-manage-print-jobs.desktop

# move to vendor-packages, but don't provide .pyc files
# deliver cupshelper into 2.6/vendor-packages 
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/vendor-packages
rm $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages/cupshelpers/*.pyc
rm $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages/*egg-info

mv $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/vendor-packages/

rmdir $RPM_BUILD_ROOT%{_libdir}/python%{default_python_version}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jun 16 2011 - ghee.teo@oracle.com
- Added online-help from Tech writer.
* Tue Dec 07 2010 - brian.cameron@oracle.com
- No longer provide the Python 2.4 bindings.
* Tue Dec 15 2009 - ghee.teo@sun.com
- Fix doo#13356. Move troubleshoot to %{_libdir}
- also make a copy of cupshelpers in 2.4 vendor-packages for hal-cups-utils
* Sun Dec 06 2009 - dave.lin@sun.com
- Remove the duplicated directory %{_datadir}/%{name}/troubleshoot
- Remove the python2.4 lines
* Wed Aug 12 2009 - christian.kelly@sun.com
- Bump to 1.0.16.
* Mon Jan 19 2009 - ghee.teo@sun.com
- Bump tarball to 1.0.13. Removed upteram l10n patch.
* Mon Dec 15 2008 - takao.fujiwara@sun.com
- Add l10n tarball.
* Fri Dec 12 2008 - takao.fujiwara@sun.com
- Add patch 05-g11n-textdomain.diff to set textdomain.
* Thu Dec 11 2008 - ghee.teo@sun.com
  uprev to 1.0.12 tarball and added patch 04-remove-fedora-specific.diff
* Wed Nov 05 2008 - ghee.teo@sun.com
- initial version
