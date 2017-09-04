#!/usr/bin/env python
from fabric.api import *
import fabric

env.hosts = [
    'server.domain.tld',
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
]
# Set the username
env.user   = "root"

# Set the password [NOT RECOMMENDED]
# env.password = "passwd"

def command():
	// running commands on server
	run("echo hello")
  run("hostname -i")
  run("date")
  
  
  
  
