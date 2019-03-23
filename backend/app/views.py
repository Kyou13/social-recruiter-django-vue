from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse

import django_filters
from rest_framework import viewsets, filters
from .models import UserInfo, Like
from .serializer import UserInfoSerializer, LikeSerializer
from django.http import HttpRequest
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer

class Top(View):
  def get(self, request, *args, **kwargs):
    assert isinstance(request, HttpRequest)
    return render(request, 'dist/index.html')

class UserInfoViewSet(viewsets.ModelViewSet):
  queryset = UserInfo.objects.all()
  serializer_class = UserInfoSerializer

class LikeViewSet(viewsets.ModelViewSet):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer

class TwitterLogin(SocialLoginView):
  serializer_class = TwitterLoginSerializer
  adapter_class = TwitterOAuthAdapter
# APP_NAME = 'app'
#
# class DashBoard(TemplateView):
#
#   def get(self, request, *args, **kwargs):
#     # ログインしていないとき
#     if request.user.is_anonymous:
#       template_name = '%s/top.html' % APP_NAME
#       return render(request, template_name, {})
#
#     # ログインしているとき
#     elif request.user.is_authenticated:
#       template_name = '%s/dashboard.html' % APP_NAME
#       user = User.objects.get(id=request.user.id)
#       socialAccount = SocialAccount.objects.get(user=user).extra_data
#
#       return render(request, template_name, {'user': user, 'social_data': socialAccount})
#
#
# class Tables(View):
#   def get(self, request, *args, **kwargs):
#     users = UserInfo.objects.order_by('-followers_count')
#     # is_like = Like.objects.filter(user=request.user).values_list('twitter_user__id', flat=True)
#     is_like = Like.objects.filter(user=request.user).values_list('twitter_user', flat=True)
#     if request.GET.get('q'):
#       q = request.GET.get('q')
#       q_words = q.strip().split()
#
#       users = users.filter()
#       for q_word in q_words:
#         users=users.filter(description__icontains=q_word)
#     return render(request, 'app/tables.html', {'twitter_users': users, 'liked_user': is_like})
#
# # class Tables(ListView):
# #   template_name = '%s/tables.html' % APP_NAME
# #   model = UserInfo
# #   paginate_by = 40
# #
# #   def get_queryset(self):
# #     users = UserInfo.objects.order_by('-followers_count')
# #     if self.request.GET.get('q'):
# #       q = self.request.GET.get('q')
# #       q_words = q.strip().split()
# #
# #       users = users.filter()
# #       for q_word in q_words:
# #         users=users.filter(description__icontains=q_word)
# #       return users
# #
# #     else:
# #       return users
# #
# #   def get_context_data(self, **kwargs):
# #     context = super().get_context_data(**kwargs)
# #     context['q'] = self.request.GET.get('q')
# #     # context['count'] = self.get_queryset().count()
# #     # context['page'] = self.request.GET.get('page')
# #     return context
# #
# #   # def post(self, request, *args, **kwargs):
# #   #   ids = request.POST.getlist("checks[]")
# #   #   for id in ids:
# #   #     relation = Relationship(user=request.user, liked_user=UserInfo.objects.get(pk=id))
# #   #     relation.save()
# #   #   return redirect("app:tables")
#
# class LikeUser(View):
#   def get(self, request, *args, **kwargs):
#     twitter_user = UserInfo.objects.get(id=kwargs['twitter_user_id'])
#     is_like = Like.objects.filter(user=request.user).filter(twitter_user=twitter_user).count()
#     if is_like > 0:
#       liking = Like.objects.get(twitter_user__id=kwargs['twitter_user_id'], user=request.user)
#       liking.delete()
#       twitter_user.like_num -= 1
#       twitter_user.save()
#       return redirect(reverse('app:tables'))
#     twitter_user.like_num += 1
#     twitter_user.save()
#     like = Like()
#     like.user = request.user
#     like.twitter_user = twitter_user
#     like.save()
#     return redirect(reverse('app:tables'))
#
# dashBoard = DashBoard.as_view()
# tables = login_required(Tables.as_view())
# like = LikeUser.as_view()
top = Top.as_view()
