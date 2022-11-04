from django.shortcuts import render
from django.http.response import JsonResponse


# Create your views here.


def get_information(request):
    dic = {
        "total_size": 7,
        "type_id": 2,
        'offset': 0,
        "infos": [
            {
                "id": 1,
                "title": "titre",
                "body": "body",
                "date_creation": "date de creation",
                "sources": "coordinations"

            },
            {
                "id": 2,
                "title": "titre",
                "body": "body",
                "date_creation": "date de creation",
                "sources": "coordinations"

            },
            {
                "id": 3,
                "title": "titre",
                "body": "body",
                "date_creation": "date de creation",
                "sources": "coordinations"

            },
            {
                "id": 4,
                "title": "titre",
                "body": "body",
                "date_creation": "date de creation",
                "sources": "coordinations"

            },
            {
                "id": 5,
                "title": "titre",
                "body": "body",
                "date_creation": "date de creation",
                "sources": "coordinations"

            },
            {
                "id": 6,
                "title": "titre",
                "body": "body",
                "date_creation": "date de creation",
                "sources": "coordinations"

            },
            {
                "id": 7,
                "title": "titre",
                "body": "body",
                "date_creation": "date de creation",
                "sources": "coordinations"

            },

        ]
    }
    return JsonResponse(data=dic)