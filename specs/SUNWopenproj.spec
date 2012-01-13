#
# spec file for package SUNWopenproj
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%define owner wangke
# bugdb: http://sourceforge.net/tracker/index.php?func=detail&aid=2275545&group_id=199315&atid=
%include Solaris.inc

%define OSR 9393:1.x

Name:                   SUNWopenproj
IPS_package_name:       desktop/project-management/openproj
Meta(info.classification): %{classification_prefix}:Applications/Office
Summary:                A project management tool. 
Version:                1.4
License:                CPAL v1.0
Distribution:           Java Desktop System
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:         %{name}.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
Source:                 http://downloads.sourceforge.net/openproj/openproj-%{version}-src.tar.gz
Source1:		%{name}-manpages-0.1.tar.gz
# date:2008-11-13 owner:wangke type:bug bugid:968997
Patch1:			openproj-01-jre-1.6.0.diff

Requires: SUNWj6rt
Requires: SUNWbash
Requires: service/gnome/desktop-cache
BuildRequires:  SUNWj6dev
BuildRequires:	SUNWant

%include desktop-incorporation.inc

%description
A project management tool. It is compatible with other popular project management tools and can be used for planning, scheduling and tracking projects. It supports Gantt, PERT diagram, histogram, charts, reports, detailed usage, as well as tree views.

%package l10n
Summary:                 %{summary} - l10n files
Requires:                %{name}

%prep
%setup -q -n openproj-%{version}-src
gzcat %SOURCE1 | tar xf -
%patch1 -p1

%build
# openproj can only be built with j2se 1.5.0. When it can be built
# works with 1.6.0 the following line should be removed.
export PATH=/usr/jdk/instances/jdk1.5.0/bin:$PATH
cp -r ./openproj_build/license/* .

LANG_DIR=sun-l10n
DQ='"'
mkdir -p $LANG_DIR
for properties in `find . -name "*_*.properties"`
do
  installed_path=`echo $properties | sed -e 's|^./openproj_.*/src/\(.*\)|\1|'`
  filename=`basename $installed_path`
  dirname=`dirname $installed_path`
  lang_ext=`echo $filename | sed -e "s|[^_]*_\(.*\)|\1|"`
  lang_ext=`basename $lang_ext .properties`

  # en .properties files should be in base packages.
  case $lang_ext in
  en*) ;;
  *) 
    mkdir -p $LANG_DIR/$lang_ext/$dirname
    mv $properties $LANG_DIR/$lang_ext/$installed_path
    ;;
  esac
done

cd $LANG_DIR
for lang_ext in `/bin/ls`
do
  if [ ! -d $lang_ext ] ; then
    printf "#### Warning: $lang_ext is not dir.\n"
    continue
  fi

  cd $lang_ext
  jar cfv openproj_$lang_ext.jar *
  cd ..

  before="value=$DQ\(.*\)$DQ\/>"
  after="value=$DQ\1 lib\/openproj_$lang_ext.jar$DQ\/>"
  if [ -f ../openproj_build/build.xml ] ; then
    sed -e "/name=${DQ}Class-Path$DQ/s/$before/$after/" \
      ../openproj_build/build.xml > /tmp/build.xml.$$
    mv /tmp/build.xml.$$ ../openproj_build/build.xml
  else
    printf "#### Error: ../openproj_build/build.xml not found\n"
    exit 1
  fi
done
cd ..

JAVA_OPTS="-Xmx128m"
cd openproj_contrib
ant build-contrib build-script build-exchange build-reports
java $JAVA_OPTS -jar ant-lib/proguard.jar @openproj_contrib.conf
java $JAVA_OPTS -jar ant-lib/proguard.jar @openproj_script.conf
java $JAVA_OPTS -jar ant-lib/proguard.jar @openproj_exchange.conf
java $JAVA_OPTS -jar ant-lib/proguard.jar @openproj_exchange2.conf
java $JAVA_OPTS -jar ant-lib/proguard.jar @openproj_reports.conf
cd ../openproj_build
ant -Dbuild_contrib=false

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/openproj
mkdir -p $RPM_BUILD_ROOT%{_datadir}/openproj/lib
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages
mkdir -p $RPM_BUILD_ROOT%{_datadir}

install openproj_build/resources/openproj $RPM_BUILD_ROOT%{_bindir}
install openproj_build/dist/openproj.jar $RPM_BUILD_ROOT%{_datadir}/openproj
install openproj_build/dist/lib/*.jar $RPM_BUILD_ROOT%{_datadir}/openproj/lib
install openproj_build/resources/openproj.png $RPM_BUILD_ROOT%{_datadir}/icons/openproj.png
install openproj_build/resources/openproj.desktop $RPM_BUILD_ROOT%{_datadir}/applications/openproj.desktop
install openproj_build/resources/openproj.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages/openproj.xml

LANG_DIR=sun-l10n
install $LANG_DIR/*/*.jar $RPM_BUILD_ROOT%{_datadir}/openproj/lib

cd sun-manpages
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, sys) %{_datadir}/openproj
%{_datadir}/openproj/openproj.jar
%dir %attr(0755, root, sys) %{_datadir}/openproj/lib
%{_datadir}/openproj/lib/openproj-*.jar
%dir %attr(0755, root, other) %{_datadir}/icons
%{_datadir}/icons/openproj.png
%dir %attr(0755, root, other) %{_datadir}/applications
%{_datadir}/applications/openproj.desktop
%dir %attr(0755, root, root) %{_datadir}/mime
%dir %attr(0755, root, root) %{_datadir}/mime/packages
%{_datadir}/mime/packages/openproj.xml
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%doc(bzip2) index.html
%doc(bzip2) third-party/index.html
%doc(bzip2) third-party/Apache-LICENSE-2.0.txt
%doc third-party/Jasper-LGPL.txt
%doc third-party/antlr.txt
%doc third-party/bsd-generic.txt
%doc third-party/groovy.txt
%doc third-party/jgoodies-forms.txt
%doc third-party/lgpl-2.1.txt
%doc third-party/sun.txt
%doc third-party/sun-jwsdp.txt
%dir %attr (0755, root, other) %{_datadir}/doc

%files l10n
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, sys) %{_datadir}/openproj
%dir %attr(0755, root, sys) %{_datadir}/openproj/lib
%{_datadir}/openproj/lib/openproj_*.jar

%changelog
* Mon Dec 21 2009 - dave.lin@sun.com
- Change dependency SUNWj5rt/dev to SUNWj6rt/dev as no SUNWj5rt/dev any more on OpenSolaris. 
* Tue Feb 10 2009 - halton.huo@sun.com
- Add dependency on SUNWbash, CR #6755918
* Thu Nov 13 2008 - jim.li@sun.com
- bump to 1.4
- fix bug#968997
- remove l10n patch cause it exists in new release.
* Fri Aug 22 2008 - takao.fujiwara@sun.com
- Add %name-l10n package.
* Fri Jul 11 2008 - Jim.li@sun.com
- initial release


