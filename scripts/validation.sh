#!/bin/bash

result=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/)
if [[ "$result" =~ "200" ]]; then
  exit 0
else
  exit 1
fi
