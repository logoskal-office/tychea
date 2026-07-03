from .models import ClientInfo


def site_info(request):
    return {
        'SITE_NAME': 'Tychea',
        'SITE_FULL_NAME': 'Tychea LLC'
    }

def client_info(request):
    client = ClientInfo.objects.first()
    return {
        'CLIENT_NAME_SOLO': client.name_solo,
        'CLIENT_NAME': client.name,
        'CLIENT_FULL_NAME': client.full_name,
        'CLIENT_PHONE_NUMBER': client.phone_number,
        'CLIENT_PHONE_NUMBER_2': client.phone_number_2,
        'CLIENT_EMAIL': client.email,
        'CLIENT_EMAIL_2': client.email_2,
        'CLIENT_ADDRESS': client.address,
        'CLIENT_LOGO': client.logo
    }