#!/bin/sh
#
# Copyright (c) 2006 Yann Dirson
#

test_description='Branch renames.

Exercises branch renaming commands.
'

. ./test-lib.sh

test_expect_success \
    'Create an stgit branch from scratch' \
    'stg init &&
     stg branch -c foo &&
     stg new p1 -m "p1"
'

test_expect_success \
    'Rename the current stgit branch' \
    'command_error stg branch -r foo bar
'

test_expect_success \
    'Rename an stgit branch' \
    'stg branch -c buz &&
     stg branch -r foo bar &&
     [ -z "$(find .git -type f | grep foo | tee /dev/stderr)" ] &&
     test -z "$(git config -l | grep branch\\.foo)"
'

test_done
