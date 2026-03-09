from django.urls import path
from .views import (
    SemanticSearchAPIView,
    SimilarProductsAPIView,
)

urlpatterns = [
    path("semantic-search/", SemanticSearchAPIView.as_view(), name="semantic-search"),
    path("git add README.md", SimilarProductsAPIView.as_view(), name="similar-products"),
    
]