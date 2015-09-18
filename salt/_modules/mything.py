import salt

__virtualname__ = 'thing1'

def __virtual__():
  return __virtualname__

def echosize(value):
  return __salt__['cmd.shell']('echo -n %s%s | wc -c' % (value,value))
