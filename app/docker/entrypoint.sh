#!/bin/sh

: '
Starter script for docker container
set -e option: instructs bash to immediately exit if any command [1] has a non-zero exit status.
exec: executable receives the Unix signals, $@ as arguments.
'

set -e

exec "$@"
