#!/bin/sh

SUDO=pfexec

$SUDO sh /usr/share/sgml/docbook/docbook-catalog-uninstall.sh
$SUDO sh /usr/share/sgml/docbook/docbook-catalog-install.sh
$SUDO gsed -i -e '/^OVERRIDE YES$/d' /usr/share/sgml/docbook/*/catalog
$SUDO gsed -i -e '1iOVERRIDE YES' /usr/share/sgml/docbook/*/catalog

