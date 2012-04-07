#!/bin/sh

VERS=10.0.2

LANG_LIST="ar bg ca cs da de el es-AR es-ES et eu fi fr gl he hu id is it ja ko lt nb-NO nl nn-NO pa-IN pl pt-BR pt-PT ro ru sk sl sq sv-SE tr uk zh-CN zh-TW"

[ -d thunderbird-l10n-$VERS ] || mkdir thunderbird-l10n-$VERS
cd thunderbird-l10n-$VERS
for lang in $LANG_LIST; do
    [ -f $lang.xpi ] || wget http://ftp.mozilla.org/pub/thunderbird/releases/$VERS/linux-i686/xpi/$lang.xpi
done

ln -s zh-TW.xpi zh-HK.xpi

tar cf - *.xpi | gzip -9 >../thunderbirdl10n-$VERS.tar.gz

