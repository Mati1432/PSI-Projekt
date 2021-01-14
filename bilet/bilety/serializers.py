from rest_framework import serializers
from .models import *
from .views import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk','url','Name','Surname','Login','Password','Mail','Ticket_Ticket']



class Ticket_OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket_Options
        fields = ['Price', 'Ticket_Name']



class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = ['Track','Date']




class TrainSerializer(serializers.ModelSerializer):
    #Train_Carriage = serializers.HyperlinkedIdentityField(many=True,read_only=True, view_name='Carriage-detail')

    class Meta:
        model = Train
        fields = ['Name']


class CarriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriage
        fields = ['Number_Of_Seats', 'Train_Carriage']


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ['Seats_Number','Ticket_Number','Carriage_Seats']


class TicketSerializer(serializers.ModelSerializer):
    #Name = serializers.HyperlinkedIdentityField(many=True,read_only=True, view_name='User-detail')

    class Meta:
        model = Ticket
        fields = ['Train_Ticket', 'Ticket_Options_Ticket','Travels_Ticket','Name']

