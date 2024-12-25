from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            
            send_mail(
                subject="Contacto Portafolio",
                message=f"Has recibido un nuevo mensaje:\n\n"
                        f"Nombre: {serializer.validated_data['name']}\n"
                        f"Email: {serializer.validated_data['email']}\n"
                        f"Mensaje:\n{serializer.validated_data['message']}",
                from_email="crowshadow123@gmail.com",
                recipient_list=["diegogelvis14@gmail.com"],
                fail_silently=False,
            )

            return Response({"message": "¡Mensaje enviado con éxito!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
