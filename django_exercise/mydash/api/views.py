from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes, throttle_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .models import Message
from .serializers import MessageSerializer

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def msg_list(request):

    if request.method == 'GET':
        employees = Message.objects.all()
        serializer = MessageSerializer(employees, many=True)
        return Response(serializer.data)    

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "data": serializer.data, 
            "created_by": {
                "user_id": str(request.user.id), 
                "user": str(request.user), 
                "email": str(request.user.email)
                }
            })
        return Response(serializer.errors)

