loginCmsResponse = """<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://wsaa.view.sua.dvadac.desein.afip.gov">
    <soapenv:Body>
        <ns1:loginCmsResponse>
            <ns1:loginCmsReturn><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
                <loginTicketResponse version="1.0">
                    <header>
                        <source>CN=wsaahomo, O=AFIP, C=AR, SERIALNUMBER=CUIT 33693450239</source>
                        <destination>SERIALNUMBER=CUIT 30740253022, CN=certificadodefinitivo</destination>
                        <uniqueId>3634574819</uniqueId>
                        <generationTime>2026-01-07T02:40:09.235-03:00</generationTime>
                        <expirationTime>2026-01-07T14:40:09.235-03:00</expirationTime>
                    </header>
                    <credentials>
                        <token>fake_token</token>
                        <sign>fake_sign</sign>
                    </credentials>
                </loginTicketResponse>]]>
            </ns1:loginCmsReturn>
        </ns1:loginCmsResponse>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECAESolicitarResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header/>
    <soap:Body>
        <FECAESolicitarResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FECAESolicitarResult>
                <FeCabResp>
                    <Cuit>30740253022</Cuit>
                    <PtoVta>1</PtoVta>
                    <CbteTipo>6</CbteTipo>
                    <FchProceso>20251226123045</FchProceso>
                    <CantReg>1</CantReg>
                    <Resultado>A</Resultado>
                    <Reproceso>N</Reproceso>
                </FeCabResp>
                <FeDetResp>
                    <FECAEDetResponse>
                        <Concepto>1</Concepto>
                        <DocTipo>99</DocTipo>
                        <DocNro>0</DocNro>
                        <CbteDesde>2</CbteDesde>
                        <CbteHasta>2</CbteHasta>
                        <CbteFch>20260224</CbteFch>
                        <Resultado>A</Resultado>
                        <CAE>80050022488317</CAE>
                        <CAEFchVto>20260306</CAEFchVto>
                    </FECAEDetResponse>
                </FeDetResp>
            </FECAESolicitarResult>
        </FECAESolicitarResponse>
    </soap:Body>
</soap:Envelope>
"""

FECompTotXRequestResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap-env:Envelope
    xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ar="http://ar.gov.afip.dif.FEV1/">
    <soap-env:Header/>
    <soap-env:Body>
        <FECompTotXRequestResponse>
            <FECompTotXRequestResult>
                <RegXReq>1</RegXReq>
            </FECompTotXRequestResult>
        </FECompTotXRequestResponse>
    </soap-env:Body>
</soap-env:Envelope>
"""

FeCompUltimoAutorizadoResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap-env:Envelope
    xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ar="http://ar.gov.afip.dif.FEV1/">
    <soap-env:Header/>
    <soap-env:Body>
        <FECompUltimoAutorizadoResponse>
            <FECompUltimoAutorizadoResult>
                <PtoVta>1</PtoVta>
                <CbteTipo>6</CbteTipo>
                <CbteNro>1548</CbteNro>
            </FECompUltimoAutorizadoResult>
        </FECompUltimoAutorizadoResponse>
    </soap-env:Body>
</soap-env:Envelope>
"""

FECompConsultarResponse = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <FECompConsultarResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FECompConsultarResult>
            <ResultGet>
                <Concepto>1</Concepto>
                <DocTipo>96</DocTipo>
                <DocNro>12345678</DocNro>
                <CbteDesde>100</CbteDesde>
                <CbteHasta>100</CbteHasta>
                <CbteFch>20251226</CbteFch>
                <ImpTotal>1210</ImpTotal>
                <ImpTotConc>0</ImpTotConc>
                <ImpNeto>1000</ImpNeto>
                <ImpOpEx>0</ImpOpEx>
                <ImpTrib>0</ImpTrib>
                <ImpIVA>210</ImpIVA>
                <FchServDesde/>
                <FchServHasta/>
                <FchVtoPago/>
                <MonId>PES</MonId>
                <MonCotiz>1</MonCotiz>
                <CondicionIVAReceptorId>5</CondicionIVAReceptorId>
                <Iva>
                    <AlicIva>
                    <Id>5</Id>
                    <BaseImp>1000</BaseImp>
                    <Importe>210</Importe>
                    </AlicIva>
                </Iva>
                <Resultado>A</Resultado>
                <CodAutorizacion>75522302377893</CodAutorizacion>
                <EmisionTipo>CAE</EmisionTipo>
                <FchVto>20260105</FchVto>
                <FchProceso>20251226010205</FchProceso>
                <PtoVta>1</PtoVta>
                <CbteTipo>6</CbteTipo>
            </ResultGet>
            </FECompConsultarResult>
        </FECompConsultarResponse>
    </soap:Body>
</soap:Envelope>
"""

FECAEARegInformativoResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap-env:Envelope
    xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ar="http://ar.gov.afip.dif.FEV1/">
    <soap-env:Header/>
    <soap-env:Body>
        <FECAEARegInformativoResponse>
            <FECAEARegInformativoResult>
                <FeCabResp>
                    <Cuit>30740253022</Cuit>
                    <PtoVta>1</PtoVta>
                    <CbteTipo>1</CbteTipo> 
                    <FchProceso>20260221101530</FchProceso>
                    <CantReg>1</CantReg>
                    <Resultado>A</Resultado> 
                </FeCabResp>
                <FeDetResp>
                    <FECAEADetResponse>
                        <Concepto>1</Concepto> 
                        <DocTipo>80</DocTipo> 
                        <DocNro>20123456789</DocNro>
                        <CbteDesde>1</CbteDesde>
                        <CbteHasta>1</CbteHasta>
                        <CbteFch>20260224</CbteFch>
                        <Resultado>A</Resultado>
                        <CAEA>26081234567890</CAEA> 
                    </FECAEADetResponse>
                </FeDetResp>
            </FECAEARegInformativoResult>
        </FECAEARegInformativoResponse>
    </soap-env:Body>
</soap-env:Envelope>
"""

FECAEASolicitarResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FECAEASolicitarResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FECAEASolicitarResult>
                <ResultGet>
                    <CAEA>87080030400901</CAEA> 
                    <Periodo>202602</Periodo>
                    <Orden>2</Orden>
                    <FchVigDesde>20260216</FchVigDesde>
                    <FchVigHasta>20260228</FchVigHasta>
                    <FchProceso>20260222223015</FchProceso>
                </ResultGet>
            </FECAEASolicitarResult>
        </FECAEASolicitarResponse>
    </soap:Body>
</soap:Envelope>
"""

FECAEASinMovimientoConsultarResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FECAEASinMovimientoConsultarResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FECAEASinMovimientoConsultarResult>
                <ResultGet>
                    <FECAEASinMov>
                        <CAEA>87080030400901</CAEA>
                        <PtoVta>1</PtoVta>
                        <FchProceso>20260224</FchProceso>
                    </FECAEASinMov>
                </ResultGet>
            </FECAEASinMovimientoConsultarResult>
        </FECAEASinMovimientoConsultarResponse>
    </soap:Body>
</soap:Envelope>
"""

FECAEASinMovimientoInformarResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
            <FECAEASinMovimientoInformarResponse xmlns="http://ar.gov.afip.dif.FEV1/">
                <FECAEASinMovimientoInformarResult>
                    <CAEA>87080030400901</CAEA>
                    <FchProceso>20260224</FchProceso>
                    <PtoVta>1</PtoVta>
                    <Resultado>A</Resultado>
                </FECAEASinMovimientoInformarResult>
            </FECAEASinMovimientoInformarResponse>
        </soap:Body>
    </soap:Envelope>
"""

FECAEAConsultarResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FECAEAConsultarResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FECAEAConsultarResult>
                <ResultGet>
                    <CAEA>87080030400901</CAEA>
                    <Periodo>202602</Periodo>
                    <Orden>2</Orden>
                    <FchVigDesde>20260216</FchVigDesde>
                    <FchVigHasta>20260228</FchVigHasta>
                    <FchTopeInf>20260305</FchTopeInf>
                    <FchProceso>20260222005406</FchProceso>
                    <Observaciones>
                        <Obs>
                            <Code>2</Code>
                            <Msg>string</Msg>
                        </Obs>
                    </Observaciones>
                </ResultGet>
            </FECAEAConsultarResult>
        </FECAEAConsultarResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetCotizacionResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetCotizacionResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetCotizacionResult>
                <ResultGet>
                    <MonId>DOL</MonId>
                    <MonCotiz>1130.034</MonCotiz>
                    <FchCotiz>20260222</FchCotiz>
                </ResultGet>
            </FEParamGetCotizacionResult>
        </FEParamGetCotizacionResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposTributosResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposTributosResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposTributosResult>
                <ResultGet>
                    <TributoTipo>
                        <Id>1</Id>
                        <Desc>Impuestos nacionales</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>2</Id>
                        <Desc>Impuestos provinciales</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>3</Id>
                        <Desc>Impuestos municipales</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>4</Id>
                        <Desc>Impuestos Internos</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>99</Id>
                        <Desc>Otro</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>5</Id>
                        <Desc>IIBB</Desc>
                        <FchDesde>20170719</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>6</Id>
                        <Desc>Percepci�n de IVA</Desc>
                        <FchDesde>20170719</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>7</Id>
                        <Desc>Percepci�n de IIBB</Desc>
                        <FchDesde>20170719</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>8</Id>
                        <Desc>Percepciones por Impuestos Municipales</Desc>
                        <FchDesde>20170719</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>9</Id>
                        <Desc>Otras Percepciones</Desc>
                        <FchDesde>20170719</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                    <TributoTipo>
                        <Id>13</Id>
                        <Desc>Percepci�n de IVA a no Categorizado</Desc>
                        <FchDesde>20170719</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </TributoTipo>
                </ResultGet>
            </FEParamGetTiposTributosResult>
        </FEParamGetTiposTributosResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposMonedasResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposMonedasResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposMonedasResult>
                <ResultGet>
                    <Moneda>
                        <Id>PES</Id>
                        <Desc>Pesos Argentinos</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>DOL</Id>
                        <Desc>D�lar Estadounidense</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>002</Id>
                        <Desc>D�lar Libre EEUU</Desc>
                        <FchDesde>20090416</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>010</Id>
                        <Desc>Pesos Mejicanos</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>011</Id>
                        <Desc>Pesos Uruguayos</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>014</Id>
                        <Desc>Coronas Danesas</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>015</Id>
                        <Desc>Coronas Noruegas</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>016</Id>
                        <Desc>Coronas Suecas</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>018</Id>
                        <Desc>D�lar Canadiense</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>019</Id>
                        <Desc>Yens</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>021</Id>
                        <Desc>Libra Esterlina</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>023</Id>
                        <Desc>Bol�var Venezolano</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>024</Id>
                        <Desc>Corona Checa</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>025</Id>
                        <Desc>Dinar Serbio</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>026</Id>
                        <Desc>D�lar Australiano</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>028</Id>
                        <Desc>Flor�n (Antillas Holandesas)</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>029</Id>
                        <Desc>G�aran�</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>031</Id>
                        <Desc>Peso Boliviano</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>032</Id>
                        <Desc>Peso Colombiano</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>033</Id>
                        <Desc>Peso Chileno</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>034</Id>
                        <Desc>Rand Sudafricano</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>051</Id>
                        <Desc>D�lar de Hong Kong</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>052</Id>
                        <Desc>D�lar de Singapur</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>053</Id>
                        <Desc>D�lar de Jamaica</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>054</Id>
                        <Desc>D�lar de Taiwan</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>055</Id>
                        <Desc>Quetzal Guatemalteco</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>056</Id>
                        <Desc>Forint (Hungr�a)</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>057</Id>
                        <Desc>Baht (Tailandia)</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>059</Id>
                        <Desc>Dinar Kuwaiti</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>012</Id>
                        <Desc>Real</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>030</Id>
                        <Desc>Shekel (Israel)</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>035</Id>
                        <Desc>Nuevo Sol Peruano</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>060</Id>
                        <Desc>Euro</Desc>
                        <FchDesde>20090403</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>040</Id>
                        <Desc>Leu Rumano</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>042</Id>
                        <Desc>Peso Dominicano</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>043</Id>
                        <Desc>Balboas Paname�as</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>044</Id>
                        <Desc>C�rdoba Nicarag�ense</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>045</Id>
                        <Desc>Dirham Marroqu�</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>046</Id>
                        <Desc>Libra Egipcia</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>047</Id>
                        <Desc>Riyal Saudita</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>061</Id>
                        <Desc>Zloty Polaco</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>062</Id>
                        <Desc>Rupia Hind�</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>063</Id>
                        <Desc>Lempira Hondure�a</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>064</Id>
                        <Desc>Yuan (Rep. Pop. China)</Desc>
                        <FchDesde>20090415</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>009</Id>
                        <Desc>Franco Suizo</Desc>
                        <FchDesde>20091110</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>041</Id>
                        <Desc>Derechos Especiales de Giro</Desc>
                        <FchDesde>20100125</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>049</Id>
                        <Desc>Gramos de Oro Fino</Desc>
                        <FchDesde>20100125</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>RUB</Id>
                        <Desc>Rublo (Rusia)</Desc>
                        <FchDesde>20250115</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                    <Moneda>
                        <Id>NZD</Id>
                        <Desc>D�lar Neozelandes</Desc>
                        <FchDesde>20250115</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </Moneda>
                </ResultGet>
            </FEParamGetTiposMonedasResult>
        </FEParamGetTiposMonedasResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposIvaResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposIvaResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposIvaResult>
                <ResultGet>
                    <IvaTipo>
                        <Id>3</Id>
                        <Desc>0%</Desc>
                        <FchDesde>20090220</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </IvaTipo>
                    <IvaTipo>
                        <Id>4</Id>
                        <Desc>10.5%</Desc>
                        <FchDesde>20090220</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </IvaTipo>
                    <IvaTipo>
                        <Id>5</Id>
                        <Desc>21%</Desc>
                        <FchDesde>20090220</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </IvaTipo>
                    <IvaTipo>
                        <Id>6</Id>
                        <Desc>27%</Desc>
                        <FchDesde>20090220</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </IvaTipo>
                    <IvaTipo>
                        <Id>8</Id>
                        <Desc>5%</Desc>
                        <FchDesde>20141020</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </IvaTipo>
                    <IvaTipo>
                        <Id>9</Id>
                        <Desc>2.5%</Desc>
                        <FchDesde>20141020</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </IvaTipo>
                </ResultGet>
            </FEParamGetTiposIvaResult>
        </FEParamGetTiposIvaResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposOpcionalResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposOpcionalResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposOpcionalResult>
                <ResultGet>
                    <OpcionalTipo>
                        <Id>2</Id>
                        <Desc>RG Empresas Promovidas - Indentificador de proyecto vinculado a R�gimen de Promoci�n Industrial</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>91</Id>
                        <Desc>RG Bienes Usados 3411 - Nombre y Apellido o Denominaci�n del vendedor del bien usado.</Desc>
                        <FchDesde>20130401</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>92</Id>
                        <Desc>RG Bienes Usados 3411 - Nacionalidad del vendedor del bien usado.</Desc>
                        <FchDesde>20130401</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>93</Id>
                        <Desc>RG Bienes Usados 3411 - Domicilio del vendedor del bien usado.</Desc>
                        <FchDesde>20130401</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>5</Id>
                        <Desc>Excepcion computo IVA Credito Fiscal</Desc>
                        <FchDesde>20141016</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>61</Id>
                        <Desc>RG 3668 Impuesto al Valor Agregado - Art.12 IVA Firmante Doc Tipo</Desc>
                        <FchDesde>20141016</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>62</Id>
                        <Desc>RG 3668 Impuesto al Valor Agregado - Art.12 IVA Firmante Doc Nro</Desc>
                        <FchDesde>20141016</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>7</Id>
                        <Desc>RG 3668 Impuesto al Valor Agregado - Art.12 IVA Car�cter del Firmante</Desc>
                        <FchDesde>20141016</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>10</Id>
                        <Desc>RG 3.368 Establecimientos de educaci�n p�blica de gesti�n privada - Actividad Comprendida</Desc>
                        <FchDesde>20150605</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>1011</Id>
                        <Desc>RG 3.368 Establecimientos de educaci�n p�blica de gesti�n privada - Tipo de Documento</Desc>
                        <FchDesde>20150605</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>1012</Id>
                        <Desc>RG 3.368 Establecimientos de educaci�n p�blica de gesti�n privada - N�mero de Documento</Desc>
                        <FchDesde>20150605</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>11</Id>
                        <Desc>RG 2.820 Operaciones econ�micas vinculadas con bienes inmuebles - Actividad Comprendida</Desc>
                        <FchDesde>20150605</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>12</Id>
                        <Desc>RG 3.687 Locaci�n temporaria de inmuebles con fines tur�sticos - Actividad Comprendida</Desc>
                        <FchDesde>20150605</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>13</Id>
                        <Desc>RG 2.863 Representantes de Modelos</Desc>
                        <FchDesde>20160101</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>14</Id>
                        <Desc>RG 2.863 Agencias de publicidad</Desc>
                        <FchDesde>20160101</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>15</Id>
                        <Desc>RG 2.863 Personas f�sicas que desarrollen actividad de modelaje</Desc>
                        <FchDesde>20160101</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>17</Id>
                        <Desc>RG 4004-E Locaci�n de inmuebles destino 'casa-habitaci�n'. Dato 2 (dos) = facturaci�n directa / Dato 1 (uno) = facturaci�n a trav�s de intermediario</Desc>
                        <FchDesde>20170309</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>1801</Id>
                        <Desc>RG 4004-E Locaci�n de inmuebles destino 'casa-habitaci�n'. Clave �nica de Identificaci�n Tributaria (CUIT).</Desc>
                        <FchDesde>20170309</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>1802</Id>
                        <Desc>RG 4004-E Locaci�n de inmuebles destino 'casa-habitaci�n'. Apellido y nombres, denominaci�n y/o raz�n social.</Desc>
                        <FchDesde>20170309</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>2101</Id>
                        <Desc>Factura de Cr�dito Electr�nica MiPyMEs (FCE) - CBU del Emisor</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>2102</Id>
                        <Desc>Factura de Cr�dito Electr�nica MiPyMEs (FCE) - Alias del Emisor</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>22</Id>
                        <Desc>Factura de Cr�dito Electr�nica MiPyMEs (FCE) - Anulaci�n</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>23</Id>
                        <Desc>Factura de Cr�dito Electr�nica MiPyMEs (FCE) - Referencia Comercial</Desc>
                        <FchDesde>20190308</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                    <OpcionalTipo>
                        <Id>27</Id>
                        <Desc>Factura de Credito Electronica MiPyMEs (FCE) - Transferencia</Desc>
                        <FchDesde>20201126</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </OpcionalTipo>
                </ResultGet>
            </FEParamGetTiposOpcionalResult>
        </FEParamGetTiposOpcionalResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposConceptoResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposConceptoResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposConceptoResult>
                <ResultGet>
                    <ConceptoTipo>
                        <Id>1</Id>
                        <Desc>Producto</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </ConceptoTipo>
                    <ConceptoTipo>
                        <Id>2</Id>
                        <Desc>Servicios</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </ConceptoTipo>
                    <ConceptoTipo>
                        <Id>3</Id>
                        <Desc>Productos y Servicios</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </ConceptoTipo>
                </ResultGet>
            </FEParamGetTiposConceptoResult>
        </FEParamGetTiposConceptoResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetPtosVentaResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetPtosVentaResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetPtosVentaResult> 
                <ResultGet>
                    <PtoVenta>
                        <Nro>1</Nro>
                        <EmisionTipo>CAE</EmisionTipo>
                        <Bloqueado>N</Bloqueado>
                        <FchBaja>NULL</FchBaja>
                    </PtoVenta>
                </ResultGet>
            </FEParamGetPtosVentaResult>
        </FEParamGetPtosVentaResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposCbteResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposCbteResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposCbteResult>
                <ResultGet>
                    <CbteTipo>
                        <Id>1</Id>
                        <Desc>Factura A</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>2</Id>
                        <Desc>Nota de D�bito A</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>3</Id>
                        <Desc>Nota de Cr�dito A</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>6</Id>
                        <Desc>Factura B</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>7</Id>
                        <Desc>Nota de D�bito B</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>8</Id>
                        <Desc>Nota de Cr�dito B</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>4</Id>
                        <Desc>Recibos A</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>5</Id>
                        <Desc>Notas de Venta al contado A</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>9</Id>
                        <Desc>Recibos B</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>10</Id>
                        <Desc>Notas de Venta al contado B</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>63</Id>
                        <Desc>Liquidacion A</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>64</Id>
                        <Desc>Liquidacion B</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>34</Id>
                        <Desc>Cbtes. A del Anexo I, Apartado A,inc.f),R.G.Nro. 1415</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>35</Id>
                        <Desc>Cbtes. B del Anexo I,Apartado A,inc. f),R.G. Nro. 1415</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>39</Id>
                        <Desc>Otros comprobantes A que cumplan con R.G.Nro. 1415</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>40</Id>
                        <Desc>Otros comprobantes B que cumplan con R.G.Nro. 1415</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>60</Id>
                        <Desc>Cta de Vta y Liquido prod. A</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>61</Id>
                        <Desc>Cta de Vta y Liquido prod. B</Desc>
                        <FchDesde>20100917</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>11</Id>
                        <Desc>Factura C</Desc>
                        <FchDesde>20110330</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>12</Id>
                        <Desc>Nota de D�bito C</Desc>
                        <FchDesde>20110330</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>13</Id>
                        <Desc>Nota de Cr�dito C</Desc>
                        <FchDesde>20110330</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>15</Id>
                        <Desc>Recibo C</Desc>
                        <FchDesde>20110330</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>49</Id>
                        <Desc>Comprobante de Compra de Bienes Usados a Consumidor Final</Desc>
                        <FchDesde>20130401</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>51</Id>
                        <Desc>Factura A con Leyenda "Operaci�n Sujeta a Retenci�n"</Desc>
                        <FchDesde>20150522</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>52</Id>
                        <Desc>Nota de D�bito A con Leyenda "Operaci�n Sujeta a Retenci�n"</Desc>
                        <FchDesde>20150522</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>53</Id>
                        <Desc>Nota de Cr�dito A con Leyenda "Operaci�n Sujeta a Retenci�n"</Desc>
                        <FchDesde>20150522</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>54</Id>
                        <Desc>Recibo A con Leyenda "Operaci�n Sujeta a Retenci�n"</Desc>
                        <FchDesde>20150522</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>201</Id>
                        <Desc>Factura de Cr�dito electr�nica MiPyMEs (FCE) A</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>202</Id>
                        <Desc>Nota de D�bito electr�nica MiPyMEs (FCE) A</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>203</Id>
                        <Desc>Nota de Cr�dito electr�nica MiPyMEs (FCE) A</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>206</Id>
                        <Desc>Factura de Cr�dito electr�nica MiPyMEs (FCE) B</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>207</Id>
                        <Desc>Nota de D�bito electr�nica MiPyMEs (FCE) B</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>208</Id>
                        <Desc>Nota de Cr�dito electr�nica MiPyMEs (FCE) B</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>211</Id>
                        <Desc>Factura de Cr�dito electr�nica MiPyMEs (FCE) C</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>212</Id>
                        <Desc>Nota de D�bito electr�nica MiPyMEs (FCE) C</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                    <CbteTipo>
                        <Id>213</Id>
                        <Desc>Nota de Cr�dito electr�nica MiPyMEs (FCE) C</Desc>
                        <FchDesde>20181226</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </CbteTipo>
                </ResultGet>
            </FEParamGetTiposCbteResult>
        </FEParamGetTiposCbteResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetCondicionIvaReceptorResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetCondicionIvaReceptorResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetCondicionIvaReceptorResult>
                <ResultGet>
                    <CondicionIvaReceptor>
                        <Id>1</Id>
                        <Desc>IVA Responsable Inscripto</Desc>
                        <Cmp_Clase>A/ALEY/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>6</Id>
                        <Desc>Responsable Monotributo</Desc>
                        <Cmp_Clase>A/ALEY/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>13</Id>
                        <Desc>Monotributista Social</Desc>
                        <Cmp_Clase>A/ALEY/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>16</Id>
                        <Desc>Monotributo Trabajador Independiente Promovido</Desc>
                        <Cmp_Clase>A/ALEY/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>4</Id>
                        <Desc>IVA Sujeto Exento</Desc>
                        <Cmp_Clase>B/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>7</Id>
                        <Desc>Sujeto No Categorizado</Desc>
                        <Cmp_Clase>B/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>8</Id>
                        <Desc>Proveedor del Exterior</Desc>
                        <Cmp_Clase>B/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>9</Id>
                        <Desc>Cliente del Exterior</Desc>
                        <Cmp_Clase>B/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>10</Id>
                        <Desc>IVA Liberado � Ley N� 19.640</Desc>
                        <Cmp_Clase>B/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>15</Id>
                        <Desc>IVA No Alcanzado</Desc>
                        <Cmp_Clase>B/C</Cmp_Clase>
                    </CondicionIvaReceptor>
                    <CondicionIvaReceptor>
                        <Id>5</Id>
                        <Desc>Consumidor Final</Desc>
                        <Cmp_Clase>C/49</Cmp_Clase>
                    </CondicionIvaReceptor>
                </ResultGet>
            </FEParamGetCondicionIvaReceptorResult>
        </FEParamGetCondicionIvaReceptorResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposDocResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposDocResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposDocResult>
                <ResultGet>
                    <DocTipo>
                        <Id>80</Id>
                        <Desc>CUIT</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>86</Id>
                        <Desc>CUIL</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>87</Id>
                        <Desc>CDI</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>89</Id>
                        <Desc>LE</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>90</Id>
                        <Desc>LC</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>91</Id>
                        <Desc>CI Extranjera</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>92</Id>
                        <Desc>en tr�mite</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>93</Id>
                        <Desc>Acta Nacimiento</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>95</Id>
                        <Desc>CI Bs. As. RNP</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>96</Id>
                        <Desc>DNI</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>94</Id>
                        <Desc>Pasaporte</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>0</Id>
                        <Desc>CI Polic�a Federal</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>1</Id>
                        <Desc>CI Buenos Aires</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>2</Id>
                        <Desc>CI Catamarca</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>3</Id>
                        <Desc>CI C�rdoba</Desc>
                        <FchDesde>20080725</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>4</Id>
                        <Desc>CI Corrientes</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>5</Id>
                        <Desc>CI Entre R�os</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>6</Id>
                        <Desc>CI Jujuy</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>7</Id>
                        <Desc>CI Mendoza</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>8</Id>
                        <Desc>CI La Rioja</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>9</Id>
                        <Desc>CI Salta</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>10</Id>
                        <Desc>CI San Juan</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>11</Id>
                        <Desc>CI San Luis</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>12</Id>
                        <Desc>CI Santa Fe</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>13</Id>
                        <Desc>CI Santiago del Estero</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>14</Id>
                        <Desc>CI Tucum�n</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>16</Id>
                        <Desc>CI Chaco</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>17</Id>
                        <Desc>CI Chubut</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>18</Id>
                        <Desc>CI Formosa</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>19</Id>
                        <Desc>CI Misiones</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>20</Id>
                        <Desc>CI Neuqu�n</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>21</Id>
                        <Desc>CI La Pampa</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>22</Id>
                        <Desc>CI R�o Negro</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>23</Id>
                        <Desc>CI Santa Cruz</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>24</Id>
                        <Desc>CI Tierra del Fuego</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                    <DocTipo>
                        <Id>99</Id>
                        <Desc>Doc. (Otro)</Desc>
                        <FchDesde>20080728</FchDesde>
                        <FchHasta>NULL</FchHasta>
                    </DocTipo>
                </ResultGet>
            </FEParamGetTiposDocResult>
        </FEParamGetTiposDocResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetTiposPaisesResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetTiposPaisesResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetTiposPaisesResult>
                <ResultGet>
                    <PaisTipo>
                        <Id>101</Id>
                        <Desc>BURKINA FASO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>102</Id>
                        <Desc>ARGELIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>103</Id>
                        <Desc>BOTSWANA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>104</Id>
                        <Desc>BURUNDI</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>105</Id>
                        <Desc>CAMERUN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>107</Id>
                        <Desc>REP. CENTROAFRICANA.</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>108</Id>
                        <Desc>CONGO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>109</Id>
                        <Desc>REP.DEMOCRAT.DEL CONGO EX ZAIRE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>110</Id>
                        <Desc>COSTA DE MARFIL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>111</Id>
                        <Desc>CHAD</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>112</Id>
                        <Desc>BENIN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>113</Id>
                        <Desc>EGIPTO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>115</Id>
                        <Desc>GABON</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>116</Id>
                        <Desc>GAMBIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>117</Id>
                        <Desc>GHANA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>118</Id>
                        <Desc>GUINEA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>119</Id>
                        <Desc>GUINEA ECUATORIAL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>120</Id>
                        <Desc>KENYA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>121</Id>
                        <Desc>LESOTHO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>122</Id>
                        <Desc>LIBERIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>123</Id>
                        <Desc>LIBIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>124</Id>
                        <Desc>MADAGASCAR</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>125</Id>
                        <Desc>MALAWI</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>126</Id>
                        <Desc>MALI</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>127</Id>
                        <Desc>MARRUECOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>128</Id>
                        <Desc>MAURICIO,ISLAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>129</Id>
                        <Desc>MAURITANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>130</Id>
                        <Desc>NIGER</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>131</Id>
                        <Desc>NIGERIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>132</Id>
                        <Desc>ZIMBABWE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>133</Id>
                        <Desc>RWANDA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>134</Id>
                        <Desc>SENEGAL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>135</Id>
                        <Desc>SIERRA LEONA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>136</Id>
                        <Desc>SOMALIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>137</Id>
                        <Desc>SWAZILANDIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>139</Id>
                        <Desc>TANZANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>140</Id>
                        <Desc>TOGO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>141</Id>
                        <Desc>TUNEZ</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>142</Id>
                        <Desc>UGANDA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>144</Id>
                        <Desc>ZAMBIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>145</Id>
                        <Desc>TERRIT.VINCULADOS AL R UNIDO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>146</Id>
                        <Desc>TERRIT.VINCULADOS A ESPA�A</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>147</Id>
                        <Desc>TERRIT.VINCULADOS A FRANCIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>149</Id>
                        <Desc>ANGOLA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>150</Id>
                        <Desc>CABO VERDE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>151</Id>
                        <Desc>MOZAMBIQUE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>152</Id>
                        <Desc>SEYCHELLES</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>153</Id>
                        <Desc>DJIBOUTI</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>155</Id>
                        <Desc>COMORAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>156</Id>
                        <Desc>GUINEA BISSAU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>157</Id>
                        <Desc>STO.TOME Y PRINCIPE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>158</Id>
                        <Desc>NAMIBIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>159</Id>
                        <Desc>SUDAFRICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>160</Id>
                        <Desc>ERITREA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>161</Id>
                        <Desc>ETIOPIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>162</Id>
                        <Desc>SUDAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>163</Id>
                        <Desc>SUDAN DEL SUR</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>197</Id>
                        <Desc>RESTO (AFRICA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>198</Id>
                        <Desc>INDETERMINADO (AFRICA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>200</Id>
                        <Desc>ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>201</Id>
                        <Desc>BARBADOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>202</Id>
                        <Desc>BOLIVIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>203</Id>
                        <Desc>BRASIL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>204</Id>
                        <Desc>CANADA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>205</Id>
                        <Desc>COLOMBIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>206</Id>
                        <Desc>COSTA RICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>207</Id>
                        <Desc>CUBA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>208</Id>
                        <Desc>CHILE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>209</Id>
                        <Desc>REP�BLICA DOMINICANA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>210</Id>
                        <Desc>ECUADOR</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>211</Id>
                        <Desc>EL SALVADOR</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>212</Id>
                        <Desc>ESTADOS UNIDOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>213</Id>
                        <Desc>GUATEMALA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>214</Id>
                        <Desc>GUYANA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>215</Id>
                        <Desc>HAITI</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>216</Id>
                        <Desc>HONDURAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>217</Id>
                        <Desc>JAMAICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>218</Id>
                        <Desc>MEXICO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>219</Id>
                        <Desc>NICARAGUA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>220</Id>
                        <Desc>PANAMA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>221</Id>
                        <Desc>PARAGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>222</Id>
                        <Desc>PERU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>223</Id>
                        <Desc>PUERTO RICO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>224</Id>
                        <Desc>TRINIDAD Y TOBAGO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>225</Id>
                        <Desc>URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>226</Id>
                        <Desc>VENEZUELA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>227</Id>
                        <Desc>TERRIT.VINCULADO AL R.UNIDO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>228</Id>
                        <Desc>TER.VINCULADOS A DINAMARCA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>229</Id>
                        <Desc>TERRIT.VINCULADOS A FRANCIA AMERIC.</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>230</Id>
                        <Desc>TERRIT. HOLANDESES</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>231</Id>
                        <Desc>TER.VINCULADOS A ESTADOS UNIDOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>232</Id>
                        <Desc>SURINAME</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>233</Id>
                        <Desc>DOMINICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>234</Id>
                        <Desc>SANTA LUCIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>235</Id>
                        <Desc>SAN VICENTE Y LAS GRANADINAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>236</Id>
                        <Desc>BELICE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>237</Id>
                        <Desc>ANTIGUA Y BARBUDA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>238</Id>
                        <Desc>S.CRISTOBAL Y NEVIS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>239</Id>
                        <Desc>BAHAMAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>240</Id>
                        <Desc>GRENADA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>241</Id>
                        <Desc>ANTILLAS HOLANDESAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>242</Id>
                        <Desc>ARUBA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>250</Id>
                        <Desc>AAE Tierra del Fuego - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>251</Id>
                        <Desc>ZF La Plata - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>252</Id>
                        <Desc>ZF Justo Daract - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>253</Id>
                        <Desc>ZF R�o Gallegos - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>254</Id>
                        <Desc>ARGENTINA - ISLAS MALVINAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>255</Id>
                        <Desc>ZF Tucum�n - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>256</Id>
                        <Desc>ZF C�rdoba - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>257</Id>
                        <Desc>ZF Mendoza - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>258</Id>
                        <Desc>ZF General Pico - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>259</Id>
                        <Desc>ZF Comodoro Rivadavia - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>260</Id>
                        <Desc>ZF Iquique</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>261</Id>
                        <Desc>ZF Punta Arenas</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>262</Id>
                        <Desc>ZF Salta - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>263</Id>
                        <Desc>ZF Paso de los Libres - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>264</Id>
                        <Desc>ZF Puerto Iguaz� - ARGENTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>265</Id>
                        <Desc>SECTOR ANTARTICO ARG.</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>270</Id>
                        <Desc>ZF Col�n - REP�BLICA DE PANAM�</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>271</Id>
                        <Desc>ZF Winner (Sta. C. de la Sierra) - BOLIVIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>280</Id>
                        <Desc>ZF Colonia - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>281</Id>
                        <Desc>ZF Florida - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>282</Id>
                        <Desc>ZF Libertad - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>283</Id>
                        <Desc>ZF Zonamerica - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>284</Id>
                        <Desc>ZF Nueva Helvecia - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>285</Id>
                        <Desc>ZF Nueva Palmira - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>286</Id>
                        <Desc>ZF R�o Negro - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>287</Id>
                        <Desc>ZF Rivera - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>288</Id>
                        <Desc>ZF San Jos� - URUGUAY</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>291</Id>
                        <Desc>ZF Manaos - BRASIL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>295</Id>
                        <Desc>MAR ARG ZONA ECO.EX</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>296</Id>
                        <Desc>RIOS ARG NAVEG INTER</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>297</Id>
                        <Desc>RESTO AMERICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>298</Id>
                        <Desc>INDETERMINADO (AMERICA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>301</Id>
                        <Desc>AFGANISTAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>302</Id>
                        <Desc>ARABIA SAUDITA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>303</Id>
                        <Desc>BAHREIN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>304</Id>
                        <Desc>MYANMAR (EX-BIRMANIA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>305</Id>
                        <Desc>BUTAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>306</Id>
                        <Desc>CAMBODYA (EX-KAMPUCHE)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>307</Id>
                        <Desc>SRI LANKA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>308</Id>
                        <Desc>COREA DEMOCRATICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>309</Id>
                        <Desc>COREA REPUBLICANA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>310</Id>
                        <Desc>CHINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>312</Id>
                        <Desc>FILIPINAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>313</Id>
                        <Desc>TAIWAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>315</Id>
                        <Desc>INDIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>316</Id>
                        <Desc>INDONESIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>317</Id>
                        <Desc>IRAK</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>318</Id>
                        <Desc>IRAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>319</Id>
                        <Desc>ISRAEL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>320</Id>
                        <Desc>JAPON</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>321</Id>
                        <Desc>JORDANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>322</Id>
                        <Desc>QATAR</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>323</Id>
                        <Desc>KUWAIT</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>324</Id>
                        <Desc>LAOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>325</Id>
                        <Desc>LIBANO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>326</Id>
                        <Desc>MALASIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>327</Id>
                        <Desc>MALDIVAS ISLAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>328</Id>
                        <Desc>OMAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>329</Id>
                        <Desc>MONGOLIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>330</Id>
                        <Desc>NEPAL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>331</Id>
                        <Desc>EMIRATOS ARABES UNIDOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>332</Id>
                        <Desc>PAKIST�N</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>333</Id>
                        <Desc>SINGAPUR</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>334</Id>
                        <Desc>SIRIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>335</Id>
                        <Desc>THAILANDIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>337</Id>
                        <Desc>VIETNAM</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>341</Id>
                        <Desc>HONG KONG</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>344</Id>
                        <Desc>MACAO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>345</Id>
                        <Desc>BANGLADESH</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>346</Id>
                        <Desc>BRUNEI</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>348</Id>
                        <Desc>REPUBLICA DE YEMEN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>349</Id>
                        <Desc>ARMENIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>350</Id>
                        <Desc>AZERBAIJAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>351</Id>
                        <Desc>GEORGIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>352</Id>
                        <Desc>KAZAJSTAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>353</Id>
                        <Desc>KIRGUIZISTAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>354</Id>
                        <Desc>TAYIKISTAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>355</Id>
                        <Desc>TURKMENISTAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>356</Id>
                        <Desc>UZBEKISTAN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>357</Id>
                        <Desc>ESTADO DE PALESTINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>397</Id>
                        <Desc>RESTO DE ASIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>398</Id>
                        <Desc>INDET.(ASIA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>401</Id>
                        <Desc>ALBANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>404</Id>
                        <Desc>ANDORRA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>405</Id>
                        <Desc>AUSTRIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>406</Id>
                        <Desc>BELGICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>407</Id>
                        <Desc>BULGARIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>409</Id>
                        <Desc>DINAMARCA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>410</Id>
                        <Desc>ESPA�A</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>411</Id>
                        <Desc>FINLANDIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>412</Id>
                        <Desc>FRANCIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>413</Id>
                        <Desc>GRECIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>414</Id>
                        <Desc>HUNGRIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>415</Id>
                        <Desc>IRLANDA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>416</Id>
                        <Desc>ISLANDIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>417</Id>
                        <Desc>ITALIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>418</Id>
                        <Desc>LIECHTENSTEIN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>419</Id>
                        <Desc>LUXEMBURGO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>420</Id>
                        <Desc>MALTA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>421</Id>
                        <Desc>MONACO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>422</Id>
                        <Desc>NORUEGA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>423</Id>
                        <Desc>PAISES BAJOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>424</Id>
                        <Desc>POLONIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>425</Id>
                        <Desc>PORTUGAL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>426</Id>
                        <Desc>REINO UNIDO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>427</Id>
                        <Desc>RUMANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>428</Id>
                        <Desc>SAN MARINO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>429</Id>
                        <Desc>SUECIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>430</Id>
                        <Desc>SUIZA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>431</Id>
                        <Desc>VATICANO(SANTA SEDE)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>433</Id>
                        <Desc>POS.BRIT.(EUROPA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>435</Id>
                        <Desc>CHIPRE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>436</Id>
                        <Desc>TURQUIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>438</Id>
                        <Desc>ALEMANIA,REP.FED.</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>439</Id>
                        <Desc>BIELORRUSIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>440</Id>
                        <Desc>ESTONIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>441</Id>
                        <Desc>LETONIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>442</Id>
                        <Desc>LITUANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>443</Id>
                        <Desc>MOLDAVIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>444</Id>
                        <Desc>RUSIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>445</Id>
                        <Desc>UCRANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>446</Id>
                        <Desc>BOSNIA HERZEGOVINA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>447</Id>
                        <Desc>CROACIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>448</Id>
                        <Desc>ESLOVAQUIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>449</Id>
                        <Desc>ESLOVENIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>450</Id>
                        <Desc>MACEDONIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>451</Id>
                        <Desc>REP. CHECA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>453</Id>
                        <Desc>MONTENEGRO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>454</Id>
                        <Desc>SERBIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>497</Id>
                        <Desc>RESTO EUROPA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>498</Id>
                        <Desc>INDET.(EUROPA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>501</Id>
                        <Desc>AUSTRALIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>503</Id>
                        <Desc>NAURU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>504</Id>
                        <Desc>NUEVA ZELANDIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>505</Id>
                        <Desc>VANATU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>506</Id>
                        <Desc>SAMOA OCCIDENTAL</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>507</Id>
                        <Desc>TERRITORIO VINCULADOS A AUSTRALIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>508</Id>
                        <Desc>TERRITORIOS VINCULADOS AL R. UNIDO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>509</Id>
                        <Desc>TERRITORIOS VINCULADOS A FRANCIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>510</Id>
                        <Desc>TER VINCULADOS A NUEVA. ZELANDA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>511</Id>
                        <Desc>TER. VINCULADOS A ESTADOS UNIDOS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>512</Id>
                        <Desc>FIJI, ISLAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>513</Id>
                        <Desc>PAPUA NUEVA GUINEA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>514</Id>
                        <Desc>KIRIBATI, ISLAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>515</Id>
                        <Desc>MICRONESIA,EST.FEDER</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>516</Id>
                        <Desc>PALAU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>517</Id>
                        <Desc>TUVALU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>518</Id>
                        <Desc>SALOMON,ISLAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>519</Id>
                        <Desc>TONGA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>520</Id>
                        <Desc>MARSHALL,ISLAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>521</Id>
                        <Desc>MARIANAS,ISLAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>597</Id>
                        <Desc>RESTO OCEANIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>598</Id>
                        <Desc>INDET.(OCEANIA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>652</Id>
                        <Desc>ANGUILA (TERRITORIO NO AUTONOMO DEL R. UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>653</Id>
                        <Desc>ARUBA (TERRITORIO DE PAISES BAJOS)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>654</Id>
                        <Desc>ISLA DE COOK (TERRITORIO AUTONOMO ASOCIADO A NUEVA ZELANDA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>655</Id>
                        <Desc>PATAU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>656</Id>
                        <Desc>POLINESIA FRANCESA (TERRITORIO DE ULTRAMAR DE FRANCIA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>659</Id>
                        <Desc>ANTILLAS HOLANDESAS (TERRITORIO DE PAISES BAJOS)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>662</Id>
                        <Desc>ASCENCION</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>663</Id>
                        <Desc>BERMUDAS (TERRITORIO NO AUTONOMO DEL R. UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>664</Id>
                        <Desc>CAMPIONE DITALIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>665</Id>
                        <Desc>COLONIA DE GIBRALTAR</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>666</Id>
                        <Desc>GROENLANDIA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>667</Id>
                        <Desc>GUAM (TERRITORIO NO AUTONOMO DE LOS ESTADOS UNIDOS)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>668</Id>
                        <Desc>HONG KONG (TERRITORIO DE CHINA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>669</Id>
                        <Desc>ISLAS AZORES</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>670</Id>
                        <Desc>ISLAS DEL CANAL (GUERNESEY, JERSEY, ALDERNEY, G.STARK, L.SARK, ETC)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>671</Id>
                        <Desc>ISLAS CAIMAN (TERRITORIO NO AUTONOMO DEL R UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>672</Id>
                        <Desc>ISLA CHRISTMAS</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>673</Id>
                        <Desc>ISLA DE COCOS O KEELING</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>676</Id>
                        <Desc>ISLA DE MAN (TERRITORIO DEL REINO UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>677</Id>
                        <Desc>ISLA DE NORFOLK (TERRITORIO DEL REINO UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>678</Id>
                        <Desc>ISLAS TURCAS Y CAICOS (TERRITORIO NO AUTONOMO DEL REINO UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>679</Id>
                        <Desc>ISLAS PACIFICO</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>680</Id>
                        <Desc>ISLAS DE SAN PEDRO Y MIGUELON</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>681</Id>
                        <Desc>ISLA QESHM</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>682</Id>
                        <Desc>ISLAS VIRGENES BRITANICAS (TERRITORIO NO AUTONOMO DEL REINO UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>683</Id>
                        <Desc>ISLAS VIRGENES DE ESTADOS UNIDOS DE AMERICA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>684</Id>
                        <Desc>LABUAM</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>685</Id>
                        <Desc>MADEIRA (TERRITORIO DE PORTUGAL)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>686</Id>
                        <Desc>MONSERRAT (TERRITORIO NO AUTONOMO DEL REINO UNIDO)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>687</Id>
                        <Desc>NIUE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>690</Id>
                        <Desc>PITCAIRN</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>693</Id>
                        <Desc>REGIMEN APLICABLE A LAS SA FINANCIERAS (LEY 11073 DE LA ROU)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>694</Id>
                        <Desc>SANTA ELENA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>695</Id>
                        <Desc>SAMOA AMERICANA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>696</Id>
                        <Desc>ARCHIPIELAGO DE SVBALBARD</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>697</Id>
                        <Desc>TRISTAN DA CUNHA</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>698</Id>
                        <Desc>TRIESTE (ITALIA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>699</Id>
                        <Desc>TOKELAU</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>700</Id>
                        <Desc>ZONA LIBRE DE OSTRAVA (CIUDAD DE LA ANTIGUA CHECOSLOVAQUIA)</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>997</Id>
                        <Desc>RESTO CONTINENTE</Desc>
                    </PaisTipo>
                    <PaisTipo>
                        <Id>998</Id>
                        <Desc>INDET.(CONTINENTE)</Desc>
                    </PaisTipo>
                </ResultGet>
            </FEParamGetTiposPaisesResult>
        </FEParamGetTiposPaisesResponse>
    </soap:Body>
</soap:Envelope>
"""

FEParamGetActividadesResponse = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope 
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <FEParamGetActividadesResponse xmlns="http://ar.gov.afip.dif.FEV1/">
            <FEParamGetActividadesResult>
                <ResultGet>
                    <ActividadesTipo>
                        <Id>620100</Id>
                        <Orden>1</Orden>
                        <Desc>Servicios</Desc>
                    </ActividadesTipo>
                </ResultGet>
            </FEParamGetActividadesResult>
        </FEParamGetActividadesResponse>
    </soap:Body>
</soap:Envelope>
"""

