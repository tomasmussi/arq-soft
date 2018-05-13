#!/bin/sh
npm run artillery --max-old-space-size=8192 -- run $1.yaml -e $2
