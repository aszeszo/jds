#!/bin/sh

TOPDIR=`cd \`dirname $0\`; pwd`
BLDDIR=$TOPDIR/build.`uname -p`

REPO=file://$BLDDIR/packages
BUILDNUM=175.0.0.0.0.0
PUBLISHER=jds

PRIORITY_SPECS="SUNWgtk-doc.spec SUNWfirefox.spec SUNWthunderbird.spec SUNWsongbird.spec SUNWmysql-python.spec"
SKIP_SPECS="SUNWevolution-bdb-devel.spec SUNWos-welcome.spec"
SKIP_SPECS="$SKIP_SPECS SUNWperl-xml-parser.spec SUNWfsexam.spec SUNWPython.spec"
SKIP_SPECS="$SKIP_SPECS SFEswig.spec"

# converted to userland
SKIP_SPECS="$SKIP_SPECS SUNWpkgbuild.spec SUNWperl-authen-pam.spec SUNWavant.spec SUNWbrltty.spec"
SKIP_SPECS="$SKIP_SPECS SUNWjpg.spec SUNWlibpopt.spec SUNWlibunique.spec SUNWrdesktop.spec"
SKIP_SPECS="$SKIP_SPECS SUNWgnome-pdf-viewer.spec SUNWlibical.spec SUNWgnome-media.spec"

# will fix later
SKIP_SPECS="$SKIP_SPECS SUNWw3m.spec"

# non-redistributable
SKIP_SPECS="$SKIP_SPECS SUNWacroread.spec SUNWflash-player-plugin.spec "

SS12u2_SPECS=""
GCC3_SPECS="SUNWcompiz-fusion-extra.spec|SUNWcompiz-fusion-main.spec|SUNWcompiz.spec"
GCC3_SPECS="$GCC3_SPECS|SUNWdesktop-search.spec|SUNWlibxklavier.spec"
GCC3_SPECS="$GCC3_SPECS|SUNWgnome-desktop-prefs.spec|SUNWgnome-remote-desktop.spec"
GCC3_SPECS="$GCC3_SPECS|SUNWlibunique.spec|SUNWlibcompizconfig.spec"

if [ ! x$1 = x-s ]; then

    # Master process

    # Make manpages tarballs
    if [ ! -f $TOPDIR/.tarballs ]; then
        cd $TOPDIR; gmake; touch $TOPDIR/.tarballs
    fi

    mkdir -p $BLDDIR/{logs,queue,packages} $TOPDIR/downloads
    if [ ! -f $BLDDIR/packages/pkg5.repository ]; then
        pkgrepo create $BLDDIR/packages
        pkgrepo -s $BLDDIR/packages add-publisher $PUBLISHER
    fi

    # if not incremental build
    if [ ! x$1 = x-i ]; then
        rm -rf $BLDDIR/{logs,queue}/*
        [ -f $BLDDIR/build.log ] && rm $BLDDIR/build.log

        # Populate the queue directory
        for i in `cd specs; ls *.spec`; do touch $BLDDIR/queue/$i; done
        #touch $BLDDIR/queue/SUNWglib2.spec
    fi

    # Start multiple slave processes
    MAXSLAVES=`expr \`kstat -p cpu_info:::state | grep -c on-line\` + 2`
    PIDS=
    SLAVES=0

    while :; do
    SLAVES=`expr $SLAVES + 1`
    $0 -s &
    PIDS="$PIDS $!"
    [ $SLAVES = $MAXSLAVES ] && break
    done

    # Wait for all slave processes to terminate

    while :; do
    NOSLAVES=true
    for i in $PIDS; do
        ps $i >/dev/null && NOSLAVES=false
    done
    [ $NOSLAVES = true ] && break
    sleep 3
    done

else

    # Slave process

    for i in $SKIP_SPECS; do
       [ -f $BLDDIR/queue/$i ] && rm $BLDDIR/queue/$i 2>/dev/null
    done

    while ls $BLDDIR/queue/*.spec >/dev/null 2>&1; do

        SPEC=
        for i in $PRIORITY_SPECS; do
            [ x$SPEC = x ] && [ -f $BLDDIR/queue/$i ] && SPEC=$i
        done

        if [ x$SPEC = x ]; then
            SPEC=`basename \`ls $BLDDIR/queue/*.spec 2>/dev/null|sort|head -1\` 2>/dev/null`
        fi

        mv $BLDDIR/queue/$SPEC $BLDDIR/queue/$SPEC.$$ 2>/dev/null
        if [ -f $BLDDIR/queue/$SPEC.$$ ]; then
            rm $BLDDIR/queue/$SPEC.$$
            echo :: Building $SPEC [$$] ::

            case $SPEC in
                $GCC3_SPECS)
                    COMPILER=gcc3
                    ;;
                $SS12u2_SPECS)
                    COMPILER=ss12.2
                    ;;
                *)
                    COMPILER=ss12.2
                    ;;
            esac

            JDS_CBE_ENV_QUIET=1
            . /opt/dtbld/bin/env.sh $COMPILER

            export LANG=C
            export PKGBUILD_IPS_SERVER=$REPO
            export SUNW_NO_UPDATE_NOTIFY=true
            export UT_NO_USAGE_TRACKING=1

            if pkgtool -v --topdir=$BLDDIR \
                --tarballdirs=$TOPDIR/downloads:$TOPDIR/manpages/sun-manpage-tarballs:$TOPDIR/manpages-roff/sun-manpage-tarballs:$TOPDIR/po-sun/po-sun-tarballs \
                --download --download-to=$TOPDIR/downloads --logdir=$BLDDIR/logs --live --with-l10n --ips \
                --nosourcepkg --define "desktop_build $BUILDNUM" \
                build-only specs/$SPEC >/dev/null; then
                echo $SPEC: PASSED >>$BLDDIR/build.log
            else
                echo $SPEC: FAILED >>$BLDDIR/build.log
            fi
        fi
    done

fi
