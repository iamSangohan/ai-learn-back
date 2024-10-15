from rest_framework import viewsets
from .models import *
from .serializers import *

class StudentInfoViewSet(viewsets.ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer

class StudentRegistrationViewSet(viewsets.ModelViewSet):
    queryset = StudentRegistration.objects.all()
    serializer_class = StudentRegistrationSerializer

class StudentAssessmentViewSet(viewsets.ModelViewSet):
    queryset = StudentAssessment.objects.all()
    serializer_class = StudentAssessmentSerializer

class StudentVleViewSet(viewsets.ModelViewSet):
    queryset = StudentVle.objects.all()
    serializer_class = StudentVleSerializer

class AssessmentsViewSet(viewsets.ModelViewSet):
    queryset = Assessments.objects.all()
    serializer_class = AssessmentsSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class VleViewSet(viewsets.ModelViewSet):
    queryset = Vle.objects.all()
    serializer_class = VleSerializer