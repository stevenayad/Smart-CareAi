from django.urls import path
from .views import (
    SemanticSearchAPIView,
    SimilarProductsAPIView,
)

urlpatterns = [
    path("semantic-search/", SemanticSearchAPIView.as_view(), name="semantic-search"),
    path("wsimilar-search/", SimilarProductsAPIView.as_view(), name="similar-products"),
    
]