#!/usr/bin/env python

import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http

class GatewayService:
	""""""
	name = "gateway_service"

	airport_rpc = RpcProxy('airport_service')
	trip_rpc = RpcProxy('trip_service')

	@http('GET', '/airport/<string:airport_id>')
	def get_airport(self, request, airport_id):
		""""""
		airport = self.airport_rpc.get(airport_id)
		return json.dumps({'airport':airport})

	@http('POST', '/airport')
	def post_airport(self, request):
		""""""
		data = json.loads(request.get_data(as_text=True))
		airport_id = self.airport_rpc.create(data['airport'])
		return airport_id

	@http('GET', '/trip/<string:trip_id>')
	def get_trip(self, request, trip_id):
		""""""
		trip = self.trip_rpc.get(trip_id)
		return json.dumps({'trip':trip})

	@http('POST', '/trip')
	def post_trip(self, request):
		""""""
		data = json.loads(request.get_data(as_text=True))
		trip_id = self.trip_rpc.create(data['airport_from'], data['airport_to'])
		return trip_id
	