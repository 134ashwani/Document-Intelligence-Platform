from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer

@api_view(['POST'])
def upload_document(request):
    file = request.FILES.get('file')
    if not file:
        return Response({'error': 'No file provided'}, status=400)
    doc = Document.objects.create(title=file.name, file=file)
    return Response(DocumentSerializer(doc).data)

@api_view(['GET'])
def list_documents(request):
    documents = Document.objects.all()
    return Response(DocumentSerializer(documents, many=True).data)
