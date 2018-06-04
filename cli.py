#!/usr/bin/env python

"""
The main entry point. Invoke as `poego' or `python -m poego'.

"""
import sys

def main():
  try:
    from poego.core import main
    sys.exit(main())
  except KeyboardInterrupt:
    sys.exit(130)

if __name__ == '__main__':
  main()