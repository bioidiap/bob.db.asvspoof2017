#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Pavel Korshunov <pavel.korshunov@idiap.ch>
# Fri 3 Feb 13:43:22 2017

"""Dumps lists of files.
"""

import os
import sys

# Driver API
# ==========

def dumplist(args):
  """Dumps lists of files based on your criteria"""

  from .query import Database
  db = Database()

  r = db.objects(
      protocol=args.protocol,
      attacks=args.attacks,
      groups=args.group,
      purposes=args.purposes,
      clients=args.client,
      )

  output = sys.stdout
  if args.selftest:
    from bob.db.base.utils import null
    output = null()

  for f in r:
    output.write('%s\n' % (f.make_path(args.directory, args.extension),))

  return 0

def add_command(subparsers):
  """Add specific subcommands that the action "dumplist" can use"""

  from argparse import SUPPRESS

  parser = subparsers.add_parser('dumplist', help=dumplist.__doc__)

  from .query import Database

  db = Database()

  if not db.is_valid():
    protocols = ('waiting','for','database','creation')
    clients = tuple()
  else:
    protocols = [k.name for k in db.protocols()]
    clients = [k.id for k in db.clients()]

  parser.add_argument('-d', '--directory', dest="directory", default='',
                      help="if given, this path will be prepended to every entry returned (defaults to '%(default)s')")
  parser.add_argument('-e', '--extension', dest="extension", default='',
                      help="if given, this extension will be appended to every entry returned (defaults to '%(default)s')")
  parser.add_argument('-c', '--purpose', dest="purposes", default=None,
                      help="if given, limits the dump to a particular subset of the data that corresponds to the "
                           "given purpose (defaults to '%(default)s')", choices=db.purposes())
  parser.add_argument('-g', '--group', dest="group", default=None,
                      help="if given, this value will limit the output files to those belonging to a particular "
                           "protocol group. (defaults to '%(default)s')", choices=db.groups())
  parser.add_argument('-a', '--attacks', dest="attacks", default=None,
                      help="if given, this value will limit the output files to those using this type of attack. "
                           "(defaults to '%(default)s')", choices=db.attack_supports())
  parser.add_argument('-x', '--protocol', dest="protocol", default=None,
                      help="if given, this value will limit the output files to those for a given protocol. "
                           "(defaults to '%(default)s')", choices=protocols)
  parser.add_argument('-C', '--client', dest="client", default=None, type=str,
                      help="if given, limits the dump to a particular client (defaults to '%(default)s')", choices=clients)
  parser.add_argument('--self-test', dest="selftest", default=False, action='store_true', help=SUPPRESS)

  parser.set_defaults(func=dumplist) #action
