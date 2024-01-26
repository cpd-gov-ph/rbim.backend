from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rbimapi.utilities import round_up
from rbimapi.validations import PageValidation
from rbimapi.mongoaggregate.notificationHistory import mdb_notification_list_count, mdb_notification_list, mdb_web_notification_list, mdb_notification_header_count
from rbim.models import NotificationHistory
import staticContent
import constants
from operator import itemgetter
class GetNotificationListView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]

    def pagination_param(self, request):
        PageValidation.validate_page(data=request.data)
        page = request.data['page']
        page_size = request.data['page_size']
        if (page == 1):
            skip = 0
        else:
            skip = (page - 1) * page_size
        notification_param = {}
        notification_param['skip'] = skip
        notification_param['page_size'] = page_size
        notification_param['sort'] = {'created_at': -1}
        # Condition Added Here
        conditions_match = {}
        conditions_match['receiver_id'] = request.user.id
        conditions_match['is_clear'] = False
        notification_param['match'] = conditions_match
        return notification_param
    def post(self,request):
        try:
            page = request.data['page']
            page_size = request.data['page_size']
            notification_param = self.pagination_param(request)
            notification_list_count = mdb_notification_list_count(notification_param)
            notification_list = mdb_notification_list(notification_param)
            total_records = notification_list_count
            num_pages = (total_records / page_size)
            num_pages = round_up(num_pages)
            return Response({
                "status":1,
                "message":"Fetched",
                "paginator": staticContent.pagination_param(total_records=total_records, num_pages=num_pages, page=page, obj_info=notification_list),
                "data":notification_list
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class GetWebHeaderNotificationListView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    def get(self,request):
        try:
            notification_param = {}
            notification_param['skip'] = 0
            notification_param['page_size'] = 5
            notification_param['sort'] = {'created_at':-1}
            # Condition Added Here
            conditions_match = {}
            conditions_match['receiver_id'] = request.user.id
            conditions_match['is_clear'] = False
            notification_param['match'] = conditions_match           
            notification_list = mdb_web_notification_list(notification_param)
            nh_param = {}
            nh_param['match'] = {'is_seen':False,'receiver_id':request.user.id}
            notification_header_count = mdb_notification_header_count(nh_param)
            return Response({
                "status":1,
                "message":"Fetched",
                "notification_header_count":notification_header_count,
                "data":sorted(notification_list, key=itemgetter('date'), reverse=True)
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class GetWebViewAllNotificationListView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    def post(self,request):
        try:
            page = request.data['page']
            page_size = request.data['page_size']
            get_notifiaction_cls = GetNotificationListView
            notification_param = get_notifiaction_cls.pagination_param(get_notifiaction_cls,request=request)
            notification_list_count = mdb_notification_list_count(notification_param)
            notification_list = mdb_web_notification_list(notification_param)
            total_records = notification_list_count
            num_pages = (total_records / page_size)
            num_pages = round_up(num_pages)
            return Response({
                "status":1,
                "message":"Fetched",
                "paginator": staticContent.pagination_param(total_records=total_records, num_pages=num_pages, page=page, obj_info=notification_list),
                "data":sorted(notification_list, key=itemgetter('date'), reverse=True)
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class ClearAllNotificationView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    def delete(self,request):
        try:
            notification_obj = NotificationHistory.objects.filter(receiver_id=request.user.id)
            for notification in notification_obj:
                notification.is_clear = True
                notification.save()
            return Response({
                "status":1,
                "message":constants.NOTIFICATION_CLEAR_MSG
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class DeleteNotificationView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    def delete(self,request,id):
        try:
            notification_obj = NotificationHistory.objects.filter(id=id).first()
            notification_obj.is_clear = True
            notification_obj.save()
            return Response({
                "status":1,
                "message": constants.NOTIFICATION_DELETE_MSG
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class SeenAllNotificationView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    def put(self,request):
        try:
            notification_obj = NotificationHistory.objects.filter(receiver_id=request.user.id)
            for notification in notification_obj:
                notification.is_seen = True
                notification.save()
            return Response({
                "status":1,
                "message":"Success"
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

class GetNotificationHeaderCount(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes  = [IsAuthenticated,]
    def get(self,request):
        try:
            nh_param = {}
            nh_param['match'] = {'is_seen':False,'receiver_id':request.user.id}
            notification_header_count = mdb_notification_header_count(nh_param)
            return Response({
                "status":1,
                "message":"Success",
                "notification_header_count": notification_header_count
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status":0,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)