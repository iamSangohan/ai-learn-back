from rest_framework import serializers
from .models import *


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'  # Cela inclut tous les champs du modèle


class StudentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegistration
        fields = '__all__'


class StudentAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAssessment
        fields = '__all__'


class StudentVleSerializer(serializers.ModelSerializer):
    student = StudentInfoSerializer(read_only=True)

    class Meta:
        model = StudentVle
        fields = '__all__'


class AssessmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessments
        fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class VleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vle
        fields = '__all__'
