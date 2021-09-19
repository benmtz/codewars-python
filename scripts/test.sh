#!/usr/bin/env bash

for kata in katas/*; do
    echo "testing $kata"
    ./env/bin/python3.9 -m unittest $kata
done