#!/bin/sh
curl -sS -I "$1" | grep -i '^location:' | cut -d ' ' -f 2