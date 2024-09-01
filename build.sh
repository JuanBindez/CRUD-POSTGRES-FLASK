#!/bin/bash

git add .
git commit -m 'add bootstrap and search'
git push -u origin search
git tag v1.0-rc1
git push --tag
