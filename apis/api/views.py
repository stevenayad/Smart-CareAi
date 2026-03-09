from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  aicore.services.semantic_search_service import SemanticSearchService 
from  aicore.services.drug_similars_service import SimilarityService
#from  SmartCare_AI.App.services.drug_Contradiction_service import ContradictionService



class SemanticSearchAPIView(APIView):

    def post(self, request):
        query = request.data.get("query")
        top_k = request.data.get("top_k", 10)
        with_vectors = request.data.get("with_vectors", False)

        if not query:
            return Response(
                {"error": "Query is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        service = SemanticSearchService()

        try:
            results = service.search(
                query=query,
                top_k=top_k,
                with_vectors=with_vectors
            )

            return Response(
                {
                    "query": query,
                    "results": results
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SimilarProductsAPIView(APIView):

    def post(self, request):
        product_id = request.data.get("product_id")
        top_k = request.data.get("top_k", 10)
        score_threshold = request.data.get("score_threshold")
        exclude_self = request.data.get("exclude_self", True)

        if not product_id:
            return Response(
                {"error": "product_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        service = SimilarityService()

        try:
            results = service.find_similar_by_id(
                product_id=product_id,
                top_k=top_k,
                score_threshold=score_threshold,
                exclude_self=exclude_self
            )

            return Response(
                {
                    "product_id": product_id,
                    "similar_products": results
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        