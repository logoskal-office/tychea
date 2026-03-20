def company_info(request):
    return {
        'SITE_NAME': 'Tychea',
        'SITE_URL': 'https://tychea.com',
        'CONTACT_EMAIL': 'contact@tychea.com',
        'PHONE_NUMBER_1': '+251923022971',
        'PHONE_NUMBER_2': '+251984878695',
        'TELEGRAM_SUPPORT_CHAT': 'TycheaSupport',
        'TELEGRAM_CHANNEL': 'TycheaTechSolutions',
        'TELEGRAM_SUPPORT_BOT': 'TycheaTechBot',
    }

def template_site_info(request):
    return {
        'TEMPLATE_SITE_NAME': 'Memshack Furniture',
        'TEMPLATE_SITE_NAME_SHORT': 'Memshack',
        'TEMPLATE_SITE_HEADER': '',
        'TEMPLATE_SITE_SUBHEADER': '',
    }