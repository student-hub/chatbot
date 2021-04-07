#!/bin/bash
echo 'Delete unnecessary yml files'
find . -name 'generated*.yml' -delete
echo 'Done'