#!/usr/bin/env bash

set -ex

mkdir $1
cp _template.py $1/main.py
touch $1/input.txt
touch $1/sample_one.txt
touch $1/sample_two.txt

git add $1/main.py $1/*.txt