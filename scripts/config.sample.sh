#!/usr/bin/env bash
# It define variables used by other scripts
build_dir=build
downloads_dir=downloads
project_name=$(basename "$PWD")
project_name=${project_name%-private}
build_extracted_dir=$build_dir/extracted
build_docs_dir=${build_dir}/docs
build_docs_includes_dir=${build_dir}/docs.includes
build_src_dir=${build_dir}/src
