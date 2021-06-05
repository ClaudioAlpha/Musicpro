from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombre,apellido,password):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        usuario = self.model(
           username = username,
           email = self.normalize_email(email),
           nombre=nombre,
           apellido=apellido,
           )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username,email,nombre,apellido,password):
        usuario = self.create_user(
           email,
           username = username,
           nombre=nombre,
           apellido=apellido,
           password=password,
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario



class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de Usuario', unique=True, max_length=50)
    email = models.EmailField('Correo Electrónico', unique=True, max_length=70)
    nombre = models.CharField('Nombres', blank=False, max_length=100, null=True)
    apellido = models.CharField('Apellidos', blank=False, max_length=100, null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/',  max_length=100, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    historico = HistoricalRecords()
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def __str__(self):
        return '{}/{}/{}'.format(self.nombre, self.apellido, self.email)

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
