from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # write-only field for password, meaning it can be set when creating or updating a user but won't be included in the serialized output. this is important for security reasons, as you don't want to expose passwords in api responses.

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"] 
    
    def create(self, validated_data): # overriding the create method to handle user creation properly, especially for password hashing.
        user = User( # creating a new user instance
            username=validated_data["username"], # setting the username from the validated data.
            email=validated_data.get("email", ""), # setting the email from the validated data, defaulting to an empty string if not provided.
        )
        user.set_password(validated_data["password"]) # using set_password method to hash the password before saving it to the database. this is crucial for security, as storing plain-text passwords is a major vulnerability.
        user.save() # saving the user instance to the database.
        return user # returning the newly created user instance.