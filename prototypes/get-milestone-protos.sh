#!/bin/bash

# Copy the prototype files from the milestone build machines.


# Ensure that the script is executed from the script's directory.
ScriptDir=`dirname $0`    # Get potentially relative script directory.
ScriptDir=`( cd $ScriptDir; /usr/bin/pwd )`  # Get absolute directory.
cd $ScriptDir

# Just to be sure...
if [ ! -f `basename $0` ]
then
  echo "ERROR: You must run this script from the directory where it exists."
  exit 1
fi

if [ ! -d x86 -o ! -d sparc ]
then
  echo "ERROR: The x86 and sparc dirs for the prototype files are not present."
  exit 1
fi

echo "Copy files from goto10.ireland..."
cd x86
scp -p -q  goto10.ireland:/jails/snv-mile/root/jds/packages/PKGMAPS/proto/*.proto .
cd ..

echo "Copy files from astro.ireland..."
cd sparc
scp -p -q  astro.ireland:/jails/snv-mile/root/jds/packages/PKGMAPS/proto/*.proto .
cd ..

# Remove proto files for 'src' packages as we are not interested in them.
rm -f x86/*-src.proto sparc/*-src.proto

echo "Done."

