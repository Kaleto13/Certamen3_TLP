from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class CreacionUsuario(BaseUserManager):
    def create_user(self,rol,username,nombre,apellido,password=None):
        if not rol:
            raise ValueError('Debe tener un rol asociado')
        
        user = self.model(
            username = username,
            rol = self.normalize_rol(rol),
            nombre=nombre,
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,rol,nombre,apellido,password):
        user = self.create_user(
            rol,
            username=username,
            nombre=nombre,
            password=password,
        )
        user.usuario_administrador = True
        user.save()
        return user
    
class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    rol = models.IntegerField('Rol sin guion', unique=True)
    nombre = models.CharField('Nombre',max_length=200,blank=True,null=True)
    apellido = models.CharField('Apellido',max_length=200,blank=True,null=True)
    usuario_administrador = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol', 'nombres']

    def __str__(self):
        return f'{self.nombre},{self.apellido}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador