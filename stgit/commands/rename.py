# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from stgit import argparse
from stgit.argparse import opt
from stgit.commands.common import CmdException, DirectoryHasRepository
from stgit.out import out

__copyright__ = """
Copyright (C) 2005, Catalin Marinas <catalin.marinas@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see http://www.gnu.org/licenses/.
"""

help = 'Rename a patch'
kind = 'patch'
usage = ['[options] [--] [oldpatch] <newpatch>']
description = """
Rename <oldpatch> into <newpatch> in a series. If <oldpatch> is not
given, the top-most patch will be renamed."""

args = [argparse.applied_patches, argparse.unapplied_patches,
        argparse.hidden_patches]
options = [
    opt(
        '-b',
        '--branch',
        args=[argparse.stg_branches],
        short='use BRANCH instead of the default one',
    )
]

directory = DirectoryHasRepository(log=True)
crt_series = None


def func(parser, options, args):
    """Rename a patch in the series
    """
    crt = crt_series.get_current()

    if len(args) == 2:
        old, new = args
    elif len(args) == 1:
        if not crt:
            raise CmdException("No applied top patch to rename exists.")
        old, [new] = crt, args
    else:
        parser.error('incorrect number of arguments')

    out.start('Renaming patch "%s" to "%s"' % (old, new))
    crt_series.rename_patch(old, new)

    out.done()
