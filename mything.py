#!/usr/bin/env python

# Must be before salt.client
# q.v. https://github.com/saltstack/salt/issues/4994
import logging
logger = logging.getLogger()

import salt.client
import salt.config
import salt.output

__opts__ = salt.config.client_config('/etc/salt/master')

client = salt.client.LocalClient()

################################################################################


res = client.cmd(
  '*',
  'thing1.echosize',
  ['xyz'],
)


################################################################################

salt.output.display_output(res, 'key', __opts__)
