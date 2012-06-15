from django.conf import settings

def proposal_settings(request):
    return {
        "ACCEPTING_PROPOSALS": getattr(settings, 'ACCEPTING_PROPOSALS', True),
    }
