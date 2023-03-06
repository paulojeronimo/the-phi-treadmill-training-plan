#!/usr/bin/env bash
# It is included by other scripts
config=config.sample.sh
! [ -f ./scripts/config.sh ] || config=config.sh
source ./scripts/"$config"
