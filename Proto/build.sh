#!/bin/bash
mkdir -p compiled

cd "$(dirname "$0")"

# Compile all .proto files into ./compiled/
/usr/bin/protoc -I=. --python_out=./compiled --experimental_allow_proto3_optional *.proto

# Fix imports to use package-style paths
sed -i 's/^import \(.*_pb2\)/from Proto.compiled import \1/' compiled/*.py