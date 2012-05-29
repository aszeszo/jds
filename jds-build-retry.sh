#!/bin/sh

TOPDIR=`cd \`dirname $0\`; pwd`
BLDDIR=$TOPDIR/build.`uname -p`

[ -d $BLDDIR/logs/passed ] || mkdir 

for i in $BLDDIR/logs/*.log; do grep ^INFO:\ .*PASSED $i >/dev/null && mv $i $BLDDIR/logs/passed; done
for i in $BLDDIR/logs/*.log; do rm $i; touch $BLDDIR/queue/`basename $i|sed s/\.log$/\.spec/`; done

./jds-build.sh -i
