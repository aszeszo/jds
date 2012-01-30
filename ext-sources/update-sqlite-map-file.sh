#!/bin/bash
# usage: 
# update-sqlite-map-file new-version new-sqlite-lib old-sqlite-lib old-map-file

Usage()
{
  echo "Usage: $0 new-version new-sqlite-lib old-sqlite-lib old-map-file [new-map-file]"
  echo "If new-map-file is missing, default is new-map-file"
}

if [ $# -ne 4 -a $# -ne 5 ]
then
  Usage
  exit 1
fi

NEW_VERSION=$1
NEW_SQLITE_LIB=$2
NEW_GLOBAL_SYMBOL_FILE="/tmp/new-sqlite-lib-global-symobl.$$"

OLD_SQLITE_LIB=$3
OLD_MAP_FILE=$4
OLD_GLOBAL_SYMBOL_FILE="/tmp/old-sqlite-lib-global-symobl.$$"
OLD_VERSION=""

if [ $# -eq 5 ]
then 
  NEW_MAP_FILE=$5
else
  NEW_MAP_FILE="new-map-file"
fi

# get parent interface
PARENT_INTERFACE=`grep "^sqlite_" $OLD_MAP_FILE | sed -n -s '1p' | cut -d ' ' -f 1`

nm $NEW_SQLITE_LIB | grep GLOB | grep FUNC | grep -v 'UNDEF' | cut -d '|' -f 8 | uniq |sort > $NEW_GLOBAL_SYMBOL_FILE 

nm $OLD_SQLITE_LIB | grep GLOB | grep FUNC | grep -v 'UNDEF' | cut -d '|' -f 8 | uniq |sort > $OLD_GLOBAL_SYMBOL_FILE 

new_global_symbols=`diff -u $OLD_GLOBAL_SYMBOL_FILE $NEW_GLOBAL_SYMBOL_FILE | grep '^+[a-zA-Z][a-zA-Z]*' | sed -e 's,^+,,'`

# output License HEAD
cat >$NEW_MAP_FILE <<END_OF_LICENSE
#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#
# Copyright 2009 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.
#
# ident "@(#)mapfile-libsqlite3 1.4     09/06/05 SMI"
#
# Defines the public interface to SQLite3
#                    
END_OF_LICENSE

# output new interface
cat >>$NEW_MAP_FILE <<INTERFACE_END
sqlite_$NEW_VERSION { 
    global: 
INTERFACE_END

# output new global symbols
for global_symbol in `echo $new_global_symbols`
do
  echo "        $global_symbol;" 
done >> $NEW_MAP_FILE

echo "} $PARENT_INTERFACE;\n" >> $NEW_MAP_FILE

# output the old interfaces
# ^sqlite_ : catch the first section
# $ : match the last line in the file
# p : print the line in the range
cat $OLD_MAP_FILE | sed -n -s '/^sqlite_/,$p' >> $NEW_MAP_FILE

rm -f $NEW_GLOBAL_SYMBOL_FILE $OLD_GLOBAL_SYMBOL_FILE_
exit 0
