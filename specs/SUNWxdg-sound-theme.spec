 
# spec file for package SUNWxdg-sound-theme
#
# includes module(s): xdg-sound-theme
#
%define owner yippi
#
%include Solaris.inc

%define OSR 9865:n/a

Name:                    SUNWxdg-sound-theme
IPS_package_name:        gnome/theme/sound/xdg-sound-theme
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Theming
Summary:                 XDG FreeDesktop Sound Theme
License:                 cc sa 2.0, cc sa 3.0 Unported, cc by-sa 2.0 Generic, cc by 3.0 Unported, GPLv2, LGPLv2, Artistic
Version:                 0.6
URL:                     http://0pointer.de/blog/projects/sixfold-announcement.html
Source:                  http://0pointer.de/public/sound-theme-freedesktop-%{version}.tar.bz2
SUNW_Copyright:          %{name}.copyright
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%include desktop-incorporation.inc

BuildRequires: runtime/perl-512

%prep
%setup -n sound-theme-freedesktop-%{version}

%build
./configure --prefix=%{_prefix} 
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_datadir}/sounds
%{_datadir}/sounds/*

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Fri Aug 28 2009 - brian.cameron@sun.com
- Bump to 0.6.
* Thu Aug 27 2009 - brian.cameron@sun.com
- Bump to 0.5.
* Wed Sep 10 2008 - dave.lin@sun.com
- Add default attribute definition in %file section.
* Thu Aug 20 2008 - brian.cameron@sun.com
- Created.


