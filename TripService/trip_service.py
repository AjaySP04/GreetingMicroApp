#!/usr/bin/env python

import uuid
import json

from nameko.rpc import rpc
from nameko_redis import Redis

class TripService:
	""""""
	name = 'trip_service'

	redis = Redis('development')

	@rpc
	def get(self, trip_id):
		""""""
		trip = self.redis.get(trip_id)
		return trip

	@rpc
	def create(self, airport_from_id, airport_to_id):
		trip_id = uuid.uuid4().hex
		self.redis.set(trip_id, json.dumps({
			"from": airport_from_id,
			"to": airport_to_id
			}))
		return trip_id

if __name__=='__main__':

	from_id = "559e8fdf4d26426f8b799b53dc5b34a6"
	to_id = "30181283b44b400a8a0ab069f3049af4"

	trip_1 = TripService()
	trip_1.create(from_id, to_id)

	pass
