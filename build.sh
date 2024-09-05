#!/bin/bash

git add .
git commit -m 'add bootstrap and search'
git push -u origin main
git tag v1.0-rc2
git push --tag
