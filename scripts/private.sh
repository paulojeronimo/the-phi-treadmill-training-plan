#!/usr/bin/env bash
# It is used by premium users
set -eou pipefail

BASE_DIR=${BASE_DIR:-..}
cd "`dirname "$0"`/$BASE_DIR"
source ./scripts/common.sh

case "${1:-}" in
  extract-docs)
    private_docs=private-docs.tar.gz
    ! [ -f $private_docs ] || tar xvfz $private_docs
    ;;
  *)
    cat <<EOF
Usage: $0 <extract-docs>
EOF
esac
