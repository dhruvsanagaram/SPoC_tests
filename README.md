This repository contains tests for KLEE, a symbolic execution engine.

binary_search.cpp -- POC of KLEE generating tests for primitive CPP converted to LLVM bitcode
compile_bitcode_c.py -- POC of KLEE generating tests from C converted to LLVM bitcode
compile_bitcode_tests.py - Attempt to run complex CPP programs from SPoC dataset on KLEE that failed
    -> Hypothesis: KLEE can only generate tests for shared C/C++ constructs not C++-specific constructs
    -> Select between programs using -1, -simple_io in command line

Python: 3.10.6
Docker Inspect: 
❯ docker inspect klee/klee
[
    {
        "Id": "sha256:673d72c9b2d775f7e5baf15cdc8f5856c4d8105373aede90599dd28957f88042",
        "RepoTags": [
            "klee/klee:3.0",
            "klee/klee:latest"
        ],
        "RepoDigests": [
            "klee/klee@sha256:05a6be25f3d58cfbc3a5592b965ea06e00405a475ad3f418f3f900f09d31d9bd",
            "klee/klee@sha256:8f76ff8a820e255b5b6503eb84dfb2e9e48dae52f46b6d82d1e67e492f63f2d2"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2023-06-07T20:07:23.481779283Z",
        "Container": "",
        "ContainerConfig": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": null,
            "Cmd": null,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "DockerVersion": "",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "klee",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/tmp/llvm-130-install_O_D_A/bin:/home/klee/klee_build/bin:/home/klee/.local/bin",
                "COVERAGE=0",
                "USE_TCMALLOC=1",
                "BASE=/tmp",
                "LLVM_VERSION=13.0",
                "ENABLE_DOXYGEN=1",
                "ENABLE_OPTIMIZED=1",
                "ENABLE_DEBUG=1",
                "DISABLE_ASSERTIONS=0",
                "REQUIRES_RTTI=0",
                "SOLVERS=STP:Z3",
                "GTEST_VERSION=1.11.0",
                "UCLIBC_VERSION=klee_uclibc_v1.3",
                "TCMALLOC_VERSION=2.9.1",
                "SANITIZER_BUILD=",
                "STP_VERSION=2.3.3",
                "MINISAT_VERSION=master",
                "Z3_VERSION=4.8.15",
                "USE_LIBCXX=1",
                "KLEE_RUNTIME_BUILD=Debug+Asserts",
                "SQLITE_VERSION=3400100",
                "LD_LIBRARY_PATH=/home/klee/klee_build/lib/"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "",
            "Volumes": null,
            "WorkingDir": "/home/klee",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "maintainer": "KLEE Developers",
                "org.opencontainers.image.created": "2023-06-07T20:00:51.359Z",
                "org.opencontainers.image.description": "KLEE Symbolic Execution Engine",
                "org.opencontainers.image.licenses": "NOASSERTION",
                "org.opencontainers.image.ref.name": "ubuntu",
                "org.opencontainers.image.revision": "dfa53ed4f5711ee2d378abb267bff1da8623f7e7",
                "org.opencontainers.image.source": "https://github.com/klee/klee",
                "org.opencontainers.image.title": "klee",
                "org.opencontainers.image.url": "https://github.com/klee/klee",
                "org.opencontainers.image.version": "v3.0"
            }
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 10443519264,
        "VirtualSize": 10443519264,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/14816cdd09f3a12737ffef81517b09bb3119893c43d18e12ed750440e1414d84/diff:/var/lib/docker/overlay2/930f51e380063f4b30fc25b65b7a9758c60cdc26bd2b5d917aa4ae6dd40f07e3/diff:/var/lib/docker/overlay2/c5364a9ab0f9d790fbd6792da435b7c66befddaca712f5b647d4ea659fcbef28/diff:/var/lib/docker/overlay2/2ea1608acc2da66a4b5941d8cc478d2e5ec54396568ed681817a178a6f9d2a85/diff:/var/lib/docker/overlay2/758c92ea496f755f1552ea3860e4812bcbed3871a8dc26a0274a988476db3d18/diff:/var/lib/docker/overlay2/34143c002c98218332950f22c3be49d100a76a4ebd7f66181eb6d6d2f7fbc279/diff:/var/lib/docker/overlay2/d53866df839d7ffb44fbbc62044310b33984275cc32732745c7b26b72cedbd95/diff:/var/lib/docker/overlay2/fa35c07a26ff0fb48d0e59e76727c230df54f97aca37815c1304566211a4992c/diff:/var/lib/docker/overlay2/d44c5f373759a2933dad164c9ba6968f5247403e55404ad0b3f026cf18f0c43a/diff:/var/lib/docker/overlay2/9dfc9ce33c1d6752d2a92d0963e828a760501e1d0d67a0179662833dd2e655b3/diff:/var/lib/docker/overlay2/a1b72e3e36e81cdeca31160373c31420dcac42ec7681d9925d859c984d050681/diff:/var/lib/docker/overlay2/e2a76ac313a3281cae7e6dfc7aaced6a0aea514c4261bfebc02e9a7cfacdc942/diff:/var/lib/docker/overlay2/30a9ec47838538f3e30d92576028b026e562eb7e65b9739f9b394d4dc3b3c905/diff:/var/lib/docker/overlay2/771cb00bd7574eb80149f721a57a1135da6fdb737b4d09013fefff23aca8b3f6/diff:/var/lib/docker/overlay2/673439a3138511b97b954428d0d5cf7e373294c8c0b23a2dac9ff302bf2a3914/diff:/var/lib/docker/overlay2/878590dd38ff9eab85efb4f8cbaf4184f9656cb86e60e0c57c341fa44863ea0a/diff",
                "MergedDir": "/var/lib/docker/overlay2/072ffc6e10cee41348a35613202ae0fead82eb6d9d8902cc86d4a7130ec0da57/merged",
                "UpperDir": "/var/lib/docker/overlay2/072ffc6e10cee41348a35613202ae0fead82eb6d9d8902cc86d4a7130ec0da57/diff",
                "WorkDir": "/var/lib/docker/overlay2/072ffc6e10cee41348a35613202ae0fead82eb6d9d8902cc86d4a7130ec0da57/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:c5ff2d88f67954bdcf1cfdd46fe3d683858d69c2cadd6660812edfc83726c654",
                "sha256:fb945e40d2df1250b29ff2c598a22ffa03c169b313b4709a95da5687560ce700",
                "sha256:ff64f92913ceec4f085c10d50c38178dee3d708a777a82c99d926a1bf84d8c03",
                "sha256:a60a03a4e4a02c1be70edf13d0a6377018ba4fe608ae554a227ef0ed1733ce6c",
                "sha256:cd50ca7b6abdb85b994e0243afad41587507bfcdbdd9a6ccc5b7bed806d1cf84",
                "sha256:85b05c6ffd33a0aaa188de62e6ed81a71b07e1ab3d1aac4687fb6f89e24e0315",
                "sha256:500b00974fe7427b3bf5414cc9c4b00e9380f8a768ea46b4c18420ee2e6d75a3",
                "sha256:bff60259d6b32f7dcb9858a4908edd10f249ce28376a5dfccac989b5b7594d2b",
                "sha256:be212b384ac01870192a20a310da2339ada1ed1d1ab8069d0f9a87d34e2f5d24",
                "sha256:d148594598287e970eba4ee396cd315c68679d9c35fc8326efd55b79db28a386",
                "sha256:6e447af392e2744599fefacb29946c0338cfe754fb52c3d20538249f6852b53d",
                "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
                "sha256:ba11e3da042dfeef933cad34a7b79a07e2004053fb392d25a2eb1111ed12b9f1",
                "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
                "sha256:f3532d434995014f6591efdf5920d37bb59ea317d015001e0950974f0f37e387",
                "sha256:168847002f990e9cfae80fa6e8d005bb0ffa51377f6d6f1bb8c345bd6e82f12a",
                "sha256:40a7150743eb90adcba784e25fe6b4fa90fa38e2c854d66cc0c108c40244cd15"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]

