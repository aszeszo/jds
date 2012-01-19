%include Solaris.inc
%include default-depend.inc
%include gnome-incorporation.inc

%use gtkdoc = gtk-doc.spec

Name:                    SUNWgtk-doc
IPS_package_name:        developer/documentation-tool/gtk-doc
Meta(info.classification): %{classification_prefix}:Desktop (GNOME)/Libraries
Summary:                 GTK+ DocBook Documentation Generator
Version:                 %{gtkdoc.version}
SUNW_BaseDir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
License:                 %{gtkdoc.license}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

Requires: SUNWPython26
Requires: data/sgml-common
Requires: data/docbook/docbook-dtds
Requires: data/xml-common
Requires: data/docbook/docbook-style-xsl
Requires: data/docbook/docbook-style-dsssl
Requires: SUNWgnome-common-devel
BuildRequires: SUNWPython26-devel
BuildRequires: SUNWPython26
BuildRequires: SUNWgnome-doc-utils
BuildRequires: SUNWdesktop-cache
Requires: SUNWlxml
Requires: SUNWlxml-python26
Requires: editor/vim

%package l10n
Summary:		 %{summary} - l10n files
Requires:		 %{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%gtkdoc.prep -d %name-%version
cd %{_builddir}/%name-%version

%build
cd %{_builddir}
export PYTHON="/usr/bin/python2.6"
export CXXFLAGS="%{cxx_optflags}"
export ACLOCAL_FLAGS="-I /usr/share/gnome-doc-utils -I./m4"
%gtkdoc.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%gtkdoc.install -d %name-%version

# Normally we build this package before we build scrollkeeper, but
# remove any scrollkeeper files if user happens to rebuild this
# package after scrollkeeper is already on the system.
#
rm -rf $RPM_BUILD_ROOT%{_prefix}/var

# Remove /usr/share/info/dir, it's a generated file and shared by multiple
# packages
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%doc -d gtk-doc-%{gtkdoc.version} README MAINTAINERS
%doc(bzip2) -d gtk-doc-%{gtkdoc.version} COPYING COPYING-DOCS NEWS ChangeLog
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/gtk-doc.m4
%dir %attr (0755, root, bin) %{_datadir}/omf
%{_datadir}/sgml/gtk-doc/gtk-doc.cat
%{_datadir}/gtk-doc/data/*
%{_datadir}/pkgconfig/gtk-doc.pc
%dir %attr (0755, root, other) %{_datadir}/gnome
%{_datadir}/gnome/help/gtk-doc-manual/C/fdl-appendix.xml
%{_bindir}/gtkdoc*
%{_datadir}/omf/gtk-doc-manual/gtk-doc-manual-*.omf
%{_datadir}/gnome/help/gtk-doc-manual/*/gtk-doc-manual.xml


%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}

%changelog
* Tue Jun 08 2010 - Michal.Pryc@Oracle.Com
- Updated BuildRequires to fit SourceJuicer.
* Tue Oct 13 2009 - dave.lin@sun.com
- Correct Summary line(doo9505).
* Mon Mar 23 2009 - dave.lin@sun.com
* Add 'BuildRequires: SUNWgnome-doc-utils'.
* Mon Mar 23 2009 - dave.lin@sun.com
- Change BuildRequires to SUNWPython26-devel.
* Thu Mar 19 2009 - dave.lin@sun.com
- Add BuildRequires: SUNWPython-devel



