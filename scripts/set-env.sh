#!/usr/bin/env bash
# It configures variables and functions
TPTTPA_DIR=$(cd $(dirname "${BASH_SOURCE[0]}")/..; pwd)

PATH=$PATH:$TPTTPA_DIR/scripts

! [ -d "$TPTTPA_DIR/private/scripts" ] || \
  PATH=$PATH:$TPTTPA_DIR/private/scripts

tpttpa() { cd "$TPTTPA_DIR"; }

export PATH
