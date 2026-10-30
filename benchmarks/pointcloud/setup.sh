#!/usr/bin/env bash
# Exact native macOS ARM64 baseline, isolated from system installations.
set -euo pipefail
BENCHMARK_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$BENCHMARK_ROOT"
if [[ "$(uname -s)" != Darwin || "$(uname -m)" != arm64 ]]; then
    echo 'The committed explicit lock and RSS runner target macOS ARM64.' >&2
    exit 1
fi
mkdir -p .tools
if [[ ! -x .tools/bin/micromamba ]]; then
    curl -fL --max-time 120 \
        https://micro.mamba.pm/api/micromamba/osx-arm64/2.10.0 \
        -o .tools/micromamba-2.10.0.tar.bz2
    printf '%s  %s\n' \
        acef4eaab19ec2174ad5a449e5aad981ca326270db819502ff096a92fc31caa6 \
        .tools/micromamba-2.10.0.tar.bz2 | shasum -a 256 -c -
    tar -xjf .tools/micromamba-2.10.0.tar.bz2 -C .tools bin/micromamba
fi
if [[ "$(.tools/bin/micromamba --version)" != 2.10.0 ]]; then
    echo 'Expected micromamba 2.10.0; review the bootstrap before proceeding.' >&2
    exit 1
fi
if [[ -e .env ]]; then
    echo '.env already exists; leaving it intact. Use verify_environment.py to check it.' >&2
    exit 0
fi
MAMBA_ROOT_PREFIX="$BENCHMARK_ROOT/.tools/mamba" \
CONDA_PKGS_DIRS="$BENCHMARK_ROOT/.tools/mamba/pkgs" \
XDG_CACHE_HOME="$BENCHMARK_ROOT/.tools/cache" \
    .tools/bin/micromamba --no-rc create -y -p "$BENCHMARK_ROOT/.env" \
    --file environment-osx-arm64.lock
.env/bin/python verify_environment.py
