from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView
from app.urls import router as app_router
from django.conf import settings
from app.views import top, TwitterLogin
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from accounts.views import AuthRegister

urlpatterns = [
  path('', top),
  # 管理画面
  path('admin/', admin.site.urls),
  path('accounts/', include('allauth.urls')),
  path('api/', include(app_router.urls)),
  # APIドキュメント
  path('docs/', include_docs_urls(title='API', public=False)),
  path('login/', obtain_jwt_token),
  path('register/', AuthRegister.as_view()),
  path('auth/verify/', verify_jwt_token),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # staticfilesのファイルを配信
