from django.urls import path
from .views import AgentListView, AgentView, TopSellerView

urlpatterns =[
    path('', AgentListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', AgentView.as_view()),
]
