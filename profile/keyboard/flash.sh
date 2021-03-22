#!/bin/bash -e

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
qmk flash $script_dir/preonic.json
