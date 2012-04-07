#!/bin/sh

[ -d passed ] || mkdir passed

for i in *.log; do grep ^INFO:\ .*PASSED $i >/dev/null && mv $i passed; done
