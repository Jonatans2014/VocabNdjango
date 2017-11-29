
# Register your models here.
from django.contrib import admin


#from .models import User

from .models import User
from .models import Word
from .models import Classification



# Register your models here.


#admin.site.register(User)

admin.site.register(User)

admin.site.register(Word)
admin.site.register(Classification)