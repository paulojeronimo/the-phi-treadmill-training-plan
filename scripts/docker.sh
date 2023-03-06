#!/usr/bin/env bash
# It simplifies the Docker use
set -eou pipefail

BASE_DIR=${BASE_DIR:-..}
cd "`dirname "$0"`/$BASE_DIR"
source ./scripts/common.sh

case "${1:-}" in
  build)
    docker build -t $project_name .
    ;;
  run)
    docker run --rm $project_name
    ;;
esac
