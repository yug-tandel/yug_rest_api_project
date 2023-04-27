from rest_framework import serializers
from .models import User
class DataConverter(serializers.ModelSerializer):
    class Meta:  # Meta means information about information
        model = User
        fields = '__all__'    # if you need all the fields of User class

        # fields = ('email','first_name','last_name')      # if you need particular fields of User class



