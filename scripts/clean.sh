#!/usr/bin/env bash
# It cleans the project directory
set -eou pipefail

BASE_DIR=${BASE_DIR:-..}
cd "`dirname "$0"`/$BASE_DIR"
source ./scripts/common.sh

rm -rf \
  .pytest_cache \
  .coverage \
  htmlcov

find . ! \( -path './.venv/*' \) -type d \
  -name __pycache__ | xargs rm -rf

if [ $# = 1 ]
then
  case "$1" in
    all)
      rm -rf .venv build
  esac
fi
