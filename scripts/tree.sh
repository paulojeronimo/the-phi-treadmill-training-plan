#!/usr/bin/env bash
# It shows the main directory tree of this project
set -eou pipefail

BASE_DIR=${BASE_DIR:-..}
cd "`dirname "$0"`/$BASE_DIR"
source ./scripts/common.sh

tree -av -I ".git|\
.venv|\
.private|\
private|\
$build_dir|\
$downloads_dir\
"
