import os

# Flag to select WSFE environment:
# True = production, False = testing (homologation)
IS_WSFE_PRODUCTION = False

def get_wsfe_url() -> str:
    if IS_WSFE_PRODUCTION:
        return "https://servicios1.afip.gov.ar/wsfev1/service.asmx"
    else:
        return "https://wswhomo.afip.gov.ar/wsfev1/service.asmx"
