#!/usr/bin/env python

from time import sleep

from nameko.rpc import rpc


class GreetingService:
	""""""
	name = "greeting_service"

	@rpc
	def hello(self, name=''):
		""""""
		sleep(5)
		return "Hello, {}! (version 2)".format(name)
