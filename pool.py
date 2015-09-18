#!/usr/bin/env python

# Must be before salt.client
# q.v. https://github.com/saltstack/salt/issues/4994
import logging
logger = logging.getLogger()

import salt.client
import salt.config
import salt.output

import time

__opts__ = salt.config.client_config('/etc/salt/master')

client = salt.client.LocalClient()

################################################################################

def create_job(client, minion, val):
  return client.cmd_iter(
    minion,
    'cmd.shell',
    ['sleep %d; echo %d' %(val, val)]
  )

minions = [
  'minion1',
  'minion2',
]

values_to_work_on = [3, 2, 1, 1, 2, 3]
iterators = []
for minion in minions:
  iterators.append(create_job(client, minion, values_to_work_on.pop()))

while iterators:
  ret = iterators.pop(0)
  for i in ret:
    print(i)
    minion = i.keys()[0]
    if values_to_work_on:
      iterators.append(create_job(client, minion, values_to_work_on.pop()))
