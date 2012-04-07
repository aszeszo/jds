#!/bin/sh

SUDO=pfexec

TOPDIR=`cd \`dirname $0\`; pwd`
BLDDIR=$TOPDIR/build.`uname -p`

for i in `(cd $BLDDIR/PKGS; ls)`; do
    echo :: Installing $i ::
    [ -d /var/sadm/pkg/$i ] && $SUDO rm -rf /var/sadm/pkg/$i
    $SUDO pkgadd -a $TOPDIR/autoresponse -d $BLDDIR/PKGS $i
done
