
from django.http import HttpResponse
from rest_framework import generics
from postapp.models import Model
from postapp.serializers import Demoserializer
from postapp.utils import api_response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
@method_decorator(csrf_exempt, name="dispatch")
class userCreateView(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = Demoserializer
    
    def post(self, request, *args, **kwargs):
        # Get the data from the request
        student_data = request.data
        
        # Ensure 'sno' is provided in the data
        sno = student_data.get('sno')
        if sno is None:
            # If 'sno' is missing, return an error response
            return Response({ 'Error': 'Missing sno in request data'},status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new student instance
        created_student = Model.objects.create(
            sno=student_data.get('sno'),
            student=student_data.get('student'),
            classroom=student_data.get('classroom')
        )
        
        # Access the created student's attributes correctly
        created_student_name = created_student.student
        
        # Return the response with the created student's information
        return Response({'Error': 'Successfully created. Please check once', "created_student": created_student_name},status=status.HTTP_201_CREATED)





