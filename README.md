# KLEE Tests Repository

This repository contains tests for [KLEE](http://klee.github.io/), a symbolic execution engine.

## Files Overview

- `binary_search.cpp` - Proof of Concept (POC) of KLEE generating tests for primitive C++ converted to LLVM bitcode.
- `compile_bitcode_c.py` - POC of KLEE generating tests from C converted to LLVM bitcode.
- `compile_bitcode_tests.py` - Attempt to run complex C++ programs from the SPoC dataset on KLEE that failed.
  - **Hypothesis:** KLEE can only generate tests for shared C/C++ constructs, not C++-specific constructs.
  - **Usage:** Select between programs using `-1`, `-simple_io` in the command line.

## Getting Started

To start generating tests with KLEE, follow these steps:

1. **Compile to LLVM Bitcode:**
   First, compile the desired C/C++ program into LLVM bitcode using the provided Python script. For complex C++ programs that failed in our initial tests, use the following command:

   ```sh
   python3 compile_bitcode_tests.py -c -1

   klee <INSERT FILE NAME>.bc

## Environment

- **Python:** 3.10.6

## Docker Inspect for KLEE Image

Docker image details for `klee/klee`:

- **ID:** `sha256:673d72c9b2d775f7e5baf15cdc8f5856c4d8105373aede90599dd28957f88042`
- **Tags:** `klee/klee:3.0`, `klee/klee:latest`
- **Created:** 2023-06-07T20:07:23.481779283Z
- **Size:** 10,443,519,264 bytes
- **Architecture:** amd64
- **OS:** linux
- **Docker Version Used for Building:** N/A
- **Entrypoint:** `/bin/bash`
- **Working Directory:** `/home/klee`
- **User:** `klee`
- **Environment Variables:**
  - PATH, COVERAGE, USE_TCMALLOC, BASE, etc.
- **Volumes:** N/A
- **Labels:**
  - **Maintainer:** KLEE Developers
  - **Image Description:** KLEE Symbolic Execution Engine
  - **License:** NOASSERTION
  - **Image Source:** [GitHub - klee/klee](https://github.com/klee/klee)
  - **More labels** related to the image version, build, and configurations.

For a complete and detailed view of the environment and configurations, please refer to the Docker inspect output.
