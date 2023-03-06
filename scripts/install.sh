#!/usr/bin/env bash
# It installs software used by this project
set -eou pipefail

BASE_DIR=${BASE_DIR:-..}
cd "`dirname "$0"`/$BASE_DIR"
source ./scripts/common.sh

case "${1:-}" in
  aws-cli)
    # Ref: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
    echo Installing aws-cli ...
    mkdir -p $build_dir $downloads_dir
    aws_url=https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip
    zip=$(basename $aws_url)
    echo Downloading $aws_url ...
    curl "$aws_url" -s -L -C - -o $downloads_dir/$zip
    echo Extracting $downloads_dir/$zip to $build_extracted_dir ...
    rm -rf $build_extracted_dir && mkdir -p $_
    unzip -q -d $build_extracted_dir $downloads_dir/$zip
    echo Calling installer ...
    sudo $build_extracted_dir/aws/install
    ;;
  *) cat <<EOF
Usage: $0 <aws-cli>
EOF
esac
