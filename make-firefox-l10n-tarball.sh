#!/bin/sh

VERS=10.0.2

#LANG_LIST="ar be bg ca cs da de el es-AR es-CL es-ES et fi fr he hi-IN hr hu id is it ja kk ko lt lv mk nb-NO nl nn-NO pl pt-BR pt-PT ro ru sk sl sq sr sv-SE th tr uk vi zh-CN zh-HK zh-TW"
LANG_LIST="ar be bg ca cs da de el es-AR es-CL es-ES et fi fr he hi-IN hr hu id is it ja kk ko lt lv mk nb-NO nl nn-NO pl pt-BR pt-PT ro ru sk sl sq sr sv-SE th tr uk vi zh-CN zh-TW"

[ -d firefox-l10n-$VERS ] || mkdir firefox-l10n-$VERS
cd firefox-l10n-$VERS
for lang in $LANG_LIST; do
    [ -f $lang.xpi ] || wget http://ftp.mozilla.org/pub/firefox/releases/$VERS/linux-i686/xpi/$lang.xpi
done

cp zh-TW.xpi zh-HK.xpi

tar cf - *.xpi | gzip -9 >../firefoxl10n-$VERS.tar.gz
