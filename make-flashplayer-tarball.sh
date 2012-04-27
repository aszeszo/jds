#!/bin/sh

VERS=11.1.102.62

[ -f flash_player_11_solaris_x86.tar.bz2 ] || wget http://download.macromedia.com/pub/flashplayer/pdc/$VERS/flash_player_11_solaris_x86.tar.bz2
[ -f flash_player_11_solaris_sparc.tar.bz2 ] || wget http://download.macromedia.com/pub/flashplayer/pdc/$VERS/flash_player_11_solaris_sparc.tar.bz2

bzip2 -dc flash_player_11_solaris_x86.tar.bz2 | tar xf -
bzip2 -dc flash_player_11_solaris_sparc.tar.bz2 | tar xf -

mkdir flashplayer
mv flash_player_solaris_*_x86 flashplayer/x86
mv flash_player_solaris_*_sparc flashplayer/sparc

tar cf - flashplayer | gzip -9 >flashplayer-$VERS-bin-solaris.tar.gz

rm -rf flashplayer
