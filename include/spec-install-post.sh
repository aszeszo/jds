#!/bin/bash

# This script runs after the %install scriptlet of the Desktop spec files,
# The purpose of the script is post-processing files before packaging.
# 
# Currently it does two things:
#
# 1) delete CDDL header from text files, if found
# 2) validate smf manifests
#
# command line arguments:
#
# spec-post-install [DIR|FILE]...
#
# Processes a single file or all files in a directory, recursively
#
# returns 0 on success or 1 on failure (breaks the build)
#
# requires file/gnu-coreutils

SED=/usr/xpg4/bin/sed
TR=/usr/xpg4/bin/tr
NL=/usr/xpg4/bin/nl
STAT=/usr/bin/stat

# deletes the CDDL header from a text file
# returns 0 on success, 1 on error
delete_cddl() {
    mode=$(${STAT} -c '%a' "$1")
    chmod +w "$1"
    tmpfile=$(mktemp)
    ${SED} -e '/CDDL HEADER START/,/CDDL HEADER END/d' < "$1" > $tmpfile \
	|| return 1
    mv $tmpfile "$1" || return 1
    chmod $mode "$1"
    return 0
}

# return 0 is arg is an integer number
is_int() {
    echo "$1" | grep '^[1-9][0-9]*$' > /dev/null
}

# verifies if a given file needs the CDDL header removed
has_cddl() {
    start_line=$(${NL} -ba "$1" | ${TR} -cd 'a-z0-9A-Z 	\n' | \
	grep '^ *[0-9]*[ 	]*CDDL HEADER START *$' | awk '{print $1}')
    end_line=$(${NL} -ba "$1" | ${TR} -cd 'a-z0-9A-Z 	\n' | \
	grep '^ *[0-9]*[ 	]*CDDL HEADER END *$' | awk '{print $1}')
    is_int "$start_line" || return 1
    is_int "$end_line" || return 1
    if [ $start_line -gt $end_line ]; then
	return 1
    fi
    if [ $start_line -gt 15 ]; then
	echo "WARNING: CDDL-like header starts after the 15th line"
	return 1
    fi
    diff=$(($end_line - $start_line))
    if [ $diff != 17 -a $diff != 18 -a $diff != 11 -a $diff != 12 ]; then
	echo "WARNING: $1: unrecognised CDDL-like header, $diff lines long"
	return 1
    fi
}

# runs svccfg validate on arg
validate_manifest() {
    svccfg validate "$1" || return 1

    return 0
}

# processes a single file
process_file() {
    grep 'CDDL HEADER' "$1" > /dev/null && has_cddl "$1" && {
	echo "Deleting CDDL header from $1"
	delete_cddl "$1" || return 1
    }

    echo "$1" | egrep '/(var|lib)/svc/manifest/' > /dev/null && {
	echo "Validating SMF manifest $1"
	validate_manifest "$1" || return 1
    }

    return 0
}

# processes all files in a directory, recursively
process_dir() {
    files=$(find "$1" -type f -print)
    for file in $files; do
	process_file "$file" || return 1
    done

    return 0
}

for arg in "${@}"; do
    echo "Post-processing $arg"
    if [ -d "$arg" ]; then
	process_dir "$arg"
    elif [ -f "$arg" ]; then
	process_file "$arg"
    else
	echo "$0: $arg not found" 1>&2
	exit 1
    fi
done
