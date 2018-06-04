"""
poego.core
~~~~~~~~~~~

This module provides the CLI interface for our algorithms using the `Click`
library. Always check this as a reference to use PoEGO as a library.
"""

import sys
import click
from poego import __version__ as poego_version

@click.group()
@click.option('--verbose', '-v', help='Display logging messages', is_flag=True)
@click.pass_context
def main(ctx, verbose):
  ctx.obj = {
    'verbose': verbose
  }