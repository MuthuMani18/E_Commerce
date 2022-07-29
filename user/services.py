from typing import TYPE_CHECKING
from . import models
import datetime
import jwt
from django.conf import settings

if TYPE_CHECKING:
    from .models import User

def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user

def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token
