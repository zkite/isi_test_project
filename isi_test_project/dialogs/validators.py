from rest_framework.exceptions import ValidationError


def admin_validator(data):
    participants = data.get("participants")
    if participants and len([usr for usr in participants if usr.user_type == "ADMIN"]) > 1:
        raise ValidationError("To much admins in the thread")

