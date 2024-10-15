from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'student-info', StudentInfoViewSet, basename='studentinfo')
router.register(r'student-registration', StudentRegistrationViewSet, basename='studentregistration')
router.register(r'student-assessment', StudentAssessmentViewSet, basename='studentassessment')
router.register(r'student-vle', StudentVleViewSet, basename='studentvle')
router.register(r'assessments', AssessmentsViewSet, basename='assessments')
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'vle', VleViewSet, basename='vle')

urlpatterns = router.urls
