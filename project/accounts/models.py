from django.db import models
from django.contrib.auth.models import UserManager , AbstractUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self , username,display_name,group,password=None):
        if not username:
            raise ValueError('usenameLoss')
        
        user=self.model(
            username=username,
            display_name=display_name,
            group=group
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self , username,display_name,group):
        if not username:
            raise ValueError('usenameLoss')
        
        user=self.model(
            username=username,
            display_name=display_name,
            group=group
        )
        user.is_admin=True
        user.save(using=self._db)
        return user
    

class User(AbstractUser):
    username = models.CharField(
        verbose_name='ユーザID',
        max_length=50,
        unique=True,
    )
    display_name = models.CharField(
        max_length=30, null=False, verbose_name='氏名')
    email = models.EmailField(
        max_length=255, null=True, blank=True, verbose_name='e-mail')
    is_active = models.BooleanField(default=True, verbose_name='アクセス許可')
    is_admin = models.BooleanField(default=False, verbose_name='管理者権限')
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['displgeneralay_name', 'group', 'teamgroup']

    def __str__(self):
        return self.username

    # 管理画面内での権限は全て許可でオーバーライド
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # 管理者画面に入るための権限 is_adminのbooleanで判定
    @property
    def is_staff(self):
        return self.is_admin
