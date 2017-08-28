import pytz
from models import User1
from datetime import datetime
def del_user(username):
    u = User1.objects.get(username = username)
    u.delete()

def last_logged():
    z = User1.objects.all()
    for x in z:
       if (datetime.now().replace(tzinfo=pytz.UTC) - x.last_login).days > 30:
           del_user(x.username)
       else:
           continue





