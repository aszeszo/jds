#!/bin/sh

VERS=1.2.1
TAG=CALENDAR_1_2_RELEASE

LANG_LIST="bg ca cs da de es-AR es-ES et eu fi fr gl hu id is it ja ko lt nb-NO nl nn-NO pa-IN pl pt-PT ro ru sk sl sq sv-SE tr uk zh-CN zh-HK zh-TW"

[ -d l10n-release ] || mkdir l10n-release
cd l10n-release
for lang in $LANG_LIST; do
    remote_lang=$lang
    remote_tag=$TAG
    case $lang in
        uk)
            remote_tag=CALENDAR_1_1b1_RELEASE
            ;;
        ro)
            remote_tag=CALENDAR_1_1b1_RELEASE
            ;;
        id)
            remote_tag=CALENDAR_1_1b1_RELEASE
            ;;
        tr)
            remote_tag=CALENDAR_1_1b1_RELEASE
            ;;
        zh-HK)
            remote_lang=zh-TW
            ;;
    esac

    [ ! -d $lang ] && mkdir $lang

    cd $lang
    [ -f $remote_tag.tar.bz2 ] || wget http://hg.mozilla.org/releases/l10n/mozilla-release/$remote_lang/archive/$remote_tag.tar.bz2
    rm -rf calendar
    bzip2 -dc $remote_tag.tar.bz2 | tar xf -
    mv $remote_lang-$remote_tag/calendar .
    rm -rf $remote_lang-$remote_tag
    cd ..

done
cd ..

gtar cf - l10n-release --exclude '*.tar.bz2' | bzip2 -9  >lightning-l10n-$VERS.tar.bz2
