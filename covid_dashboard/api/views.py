from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .util import Backup_Csv, Get_Filtered_Data, Create_Csv, Delete_Csv, Get_Top_5_Countries_Deaths, Get_Top_5_States_Cases, Get_Top_5_States_Deaths, Get_Top_5_States_Recovered, Update_Csv
import time


# from covid_dashboard.api.data_layer.load_csv import Country
from .util import Reverse_String

# from .serializers import *
import json

# # in myproject/backend/backend.py or myproject/api/api.py
# from .data_layer.load_csv import *

# # import the data layer object to the views
# from .apps import *

# Create your views here.


class SampleEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data
		output_payload = None

		output_payload = Reverse_String(input_payload)

		return Response(output_payload, status=status.HTTP_200_OK)


class CountriesEndpoint(APIView):
	def get(self, request):
		# import the data layer object to the views
		from .urls import data_layer, ComplexEncoder

		countries = data_layer.get_countries()
		# print(countries["US"].states["California"].dates["01/21/2021"])

		# results = CountrySerializer(countries, many=True).data
		# this is returning str instead of json literal
		# double encoding happening
		result = json.dumps(
			# 	# countries["US"].states["California"].dates["01/21/2021"].reprJSON()
			countries["US"].states["California"],
			cls=ComplexEncoder,
		)
		countries["US"].states["California"].dates

		# print(countries["US"].states["California"].dates["01/21/2021"])
		# return Response(countries["US"].states["California"].reprJSON())
		# TODO: add encoder for states
		return Response(countries["Taiwan"].reprJSON())


# def informationList(self, request):
#   if request.method == 'GET':
#      data = Country.objects.all()
# or
# data =  [ {"country: ": CountrySerializer.country_name,
# "states:": CountrySerializer.states}
# for data in Country.objects.all() ]
# return Response(data)

# country_query = request.GET.get('country_name')
# state_query = request.GET.get('state')
# date_query = request.GET.get('date')

# if country_query != '' and
#     serializer = CountrySerializer(data, context={'request': request}, many=True)

#    return Response(serializer.data)

#    elif request.method == 'POST':
#        serializer = CountrySerializer(data=request.data)
#        if serializer.is_valid():
# serializer.save()
#            return Response(status=status.HTTP_201_CREATED)


class QueryEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Filtered_Data(country_query, state_query, type_query, date_query)
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for query endpoint is : " + str(elapsed_time) + " seconds")
		return Response(payload, status=status.HTTP_200_OK)
	

class AddEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		#TODO : Implement backend logic

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]
		amount_query = input_payload["payload"]["amountVal"]

		start_time = time.time()
		payload = Create_Csv(country_query, state_query, type_query, date_query, amount_query)
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for add endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)

class EditEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		#TODO : Implement backend logic

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]
		amount_query = input_payload["payload"]["amountVal"]

		start_time = time.time()
		payload = Update_Csv(country_query, state_query, type_query, date_query, amount_query)
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for edit endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)

class DeleteEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		#TODO : Implement backend logic

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]
		amount_query = input_payload["payload"]["amountVal"]

		start_time = time.time()
		payload = Delete_Csv(country_query, state_query, date_query)
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for delete endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)

class BackupEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		#TODO : Implement backend logic

		#Backup doesn't require any data to be passed in from the frontend

		start_time = time.time()
		payload = Backup_Csv("api/data/archive/Copy_covid_19_data.csv")
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for backup endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)

class CountryTopDeathsEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_Countries_Deaths()
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for country top deaths endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)


class StateTopCasesEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_States_Cases()
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for state top cases endpoint is : " + str(elapsed_time) + " seconds")


		return Response(payload, status=status.HTTP_200_OK)

class StateTopDeathsEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_States_Deaths()
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for state top deaths endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)

class StateTopRecoveryEndpoint(APIView):
	def post(self, request, format=None):

		input_payload = self.request.data

		country_query = input_payload["payload"]["countryVal"]
		state_query = input_payload["payload"]["stateVal"]
		type_query = input_payload["payload"]["typeVal"]
		date_query = input_payload["payload"]["dateVal"]

		start_time = time.time()
		payload = Get_Top_5_States_Recovered()
		elapsed_time = (time.time() - start_time)
		print("Time elapsed for state top recovery endpoint is : " + str(elapsed_time) + " seconds")

		return Response(payload, status=status.HTTP_200_OK)
