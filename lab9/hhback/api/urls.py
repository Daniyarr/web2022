from django.urls import path
#from api.views import companies_list, company_details, vacancies_list, vacancy_detail, company_vacancies, vacancies_top_ten
from api.viewss.cbv_view import CompanyListAPIView, CompanyDetailAPIView
from api.viewss.fbv_view import company_list, company_details
urlpatterns=[
    path('companies/',company_list),
    path('companies/<int:pk>/', company_details),

    #path('companies/<int:company_id>/vacancies/', company_vacancies),

    #path('vacancies/',vacancies_list),
    #path('vacancies/<int:vacancy_id/>',vacancy_detail),
    #path('vacancies/top_ten/',vacancies_top_ten)

    ]