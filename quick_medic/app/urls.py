from django.urls import path

from .views import (
    Home,
    CreateDoctor,
    CreateSpecialization,
    SpecializationDetail,
    SpecializationList,
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('doctor', CreateDoctor.as_view(), name="create-doctor"),
    path('specializations', CreateSpecialization.as_view(), name="specialization"),
    path('specializations/<pk>', CreateSpecializationDetail.as_view(), name="specialization_detail"),
    path('specializations/all', CreateSpecialization.as_view(), name="specialization_list"),
]

class CreateDoctor(CreateView):
    model

