#!/bin/sh

TOPDIR=`cd \`dirname $0\`; pwd`
BLDDIR=$TOPDIR/build.`uname -p`

SS12u2_SPECS="SUNWfirefox.spec|SUNWthunderbird.spec"

case $1 in
    $SS12u2_SPECS)
        COMPILER=ss12.2
        ;;
    *)
        COMPILER=ss12.1
        ;;
esac

JDS_CBE_ENV_QUIET=1
. /opt/dtbld/bin/env.sh $COMPILER

export LANG=C
export PKGBUILD_IPS_SERVER=file:///ws/jds-s11/jds-repo
export PKGBUILD_SRC_IPS_SERVER=file:///ws/jds-s11/jds-repo-src
#export PATH=/opt/sunstudio12.1/bin:/usr/gnu/bin:/usr/bin:/usr/sbin

pkgtool -v --topdir=$BLDDIR \
--tarballdirs=$TOPDIR/downloads:$TOPDIR/downloads-oi:$TOPDIR/manpages/sun-manpage-tarballs:$TOPDIR/manpages-roff/sun-manpage-tarballs:$TOPDIR/po-sun/po-sun-tarballs:$BLDDIR/SOURCES \
--download --logdir=$BLDDIR/logs --live --with-l10n --ips \
--nosourcepkg --define "desktop_build 175.0.0.0.0.0" \
--without-gtk-doc \
build-only specs/$1

grep pkg:// build.i386/logs/`echo $1|sed s/\.spec/.log/`|sed s%^pkgbuild:%pfexec\ pkg\ install\ -v%
