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
  'test.ping',
)

from pprint import pprint
pprint(res)

salt.output.display_output(res, 'key', __opts__)
################################################################################
print "\n********\n"

res = client.cmd(
  '*',
  [ 'test.ping', 'test.echo' ],
  [ [], ['hello'] ],
)


from pprint import pprint
pprint(res)

salt.output.display_output(res, 'key', __opts__)

################################################################################
print "\n********\n"

res = client.cmd(
  '*',
  [ 'cmd.shell', 'cmd.shell' ],
  [ ['echo first'], ['echo second'] ],
)


from pprint import pprint
pprint(res)

salt.output.display_output(res, 'key', __opts__)

################################################################################


