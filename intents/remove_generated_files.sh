#!/bin/bash
echo 'Delete unnecessary yml files'
find . -name 'generated*.yml' -delete
find . -name 'generated*.json' -delete
echo 'Done'