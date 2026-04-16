
FEDummy = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEDummy/>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECAESolicitar = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECAESolicitar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:FeCAEReq>
                <ar:FeCabReq>
                    <ar:CantReg>{{ FeCAEReq.FeCabReq.CantReg }}</ar:CantReg>
                    <ar:PtoVta>{{ FeCAEReq.FeCabReq.PtoVta }}</ar:PtoVta>
                    <ar:CbteTipo>{{ FeCAEReq.FeCabReq.CbteTipo }}</ar:CbteTipo>
                </ar:FeCabReq>
                <ar:FeDetReq>
                {% for item in FeCAEReq.FeDetReq.FECAEDetRequest %}
                    <ar:FECAEDetRequest>
                        <ar:Concepto>{{ item.Concepto }}</ar:Concepto>
                        <ar:DocTipo>{{ item.DocTipo }}</ar:DocTipo>
                        <ar:DocNro>{{ item.DocNro }}</ar:DocNro>
                        <ar:CbteDesde>{{ item.CbteDesde }}</ar:CbteDesde>
                        <ar:CbteHasta>{{ item.CbteHasta }}</ar:CbteHasta>
                        <ar:CbteFch>{{ item.CbteFch }}</ar:CbteFch>
                        <ar:ImpTotal>{{ item.ImpTotal }}</ar:ImpTotal>
                        <ar:ImpTotConc>{{ item.ImpTotConc }}</ar:ImpTotConc>
                        <ar:ImpNeto>{{ item.ImpNeto }}</ar:ImpNeto>
                        <ar:ImpOpEx>{{ item.ImpOpEx }}</ar:ImpOpEx>
                        <ar:ImpTrib>{{ item.ImpTrib }}</ar:ImpTrib>
                        <ar:ImpIVA>{{ item.ImpIVA }}</ar:ImpIVA>
                    {% if item.FchServDesde %}
                        <ar:FchServDesde>{{ item.FchServDesde }}</ar:FchServDesde>
                    {% endif %}
                    {% if item.FchServHasta %}
                        <ar:FchServHasta>{{ item.FchServHasta }}</ar:FchServHasta>
                    {% endif %}
                    {% if item.FchVtoPago %}
                        <ar:FchVtoPago>{{ item.FchVtoPago }}</ar:FchVtoPago>
                    {% endif %}
                        <ar:MonId>{{ item.MonId }}</ar:MonId>
                    {% if item.MonCotiz %}
                        <ar:MonCotiz>{{ item.MonCotiz }}</ar:MonCotiz>
                    {% endif %}
                    {% if item.CanMisMonExt %}
                        <ar:CanMisMonExt>{{ item.CanMisMonExt }}</ar:CanMisMonExt>
                    {% endif %}
                        <ar:CondicionIVAReceptorId>{{ item.CondicionIVAReceptorId }}</ar:CondicionIVAReceptorId>

                        {% if item.CbtesAsoc %}
                        <ar:CbtesAsoc>
                            {% for i in item.CbtesAsoc %}
                            <ar:CbteAsoc>
                                <ar:Tipo>{{ i.Tipo }}</ar:Tipo>
                                <ar:PtoVta>{{ i.PtoVta }}</ar:PtoVta>
                                <ar:Nro>{{ i.Nro }}</ar:Nro>
                                <ar:Cuit>{{ i.Cuit }}</ar:Cuit>
                                <ar:CbteFch>{{ i.CbteFch }}</ar:CbteFch>
                            </ar:CbteAsoc>
                            {% endfor %}
                        </ar:CbtesAsoc>
                        {% endif %}

                        {% if item.Tributos %}
                        <ar:Tributos>
                            {% for i in item.Tributos %}
                            <ar:Tributo>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Desc>{{ i.Desc }}</ar:Desc>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Alic>{{ i.Alic }}</ar:Alic>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:Tributo>
                            {% endfor %}
                        </ar:Tributos>
                        {% endif %}

                        {% if item.Iva %}
                        <ar:Iva>
                            {% for i in item.Iva %}
                            <ar:AlicIva>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:AlicIva>
                            {% endfor %}
                        </ar:Iva>
                        {% endif %}

                        {% if item.Opcionales %}
                        <ar:Opcionales>
                            {% for i in item.Opcionales %}
                            <ar:Opcional>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Valor>{{ i.Valor }}</ar:Valor>
                            </ar:Opcional>
                            {% endfor %}
                        </ar:Opcionales>
                        {% endif %}

                        {% if item.Compradores %}
                        <ar:Compradores>
                            {% for i in item.Compradores %}
                            <ar:Comprador>
                                <ar:DocTipo>{{ i.DocTipo }}</ar:DocTipo>
                                <ar:DocNro>{{ i.DocNro }}</ar:DocNro>
                                <ar:Porcentaje>{{ i.Porcentaje }}</ar:Porcentaje>
                            </ar:Comprador>
                            {% endfor %}
                        </ar:Compradores>
                        {% endif %}

                        {% if item.PeriodoAsoc %}
                        <ar:PeriodoAsoc>
                            {% for i in item.PeriodoAsoc %}
                                <ar:FchDesde>{{ i.FchDesde }}</ar:FchDesde>
                                <ar:FchHasta>{{ i.FchHasta }}</ar:FchHasta>
                            {% endfor %}
                        </ar:PeriodoAsoc>
                        {% endif %}

                        {% if item.Actividades %}
                        <ar:Actividades>
                            {% for i in item.Actividades %}
                            <ar:Actividad>
                                <ar:Id>{{ i.Id }}</ar:Id>
                            </ar:Actividad>
                            {% endfor %}
                        </ar:Actividades>
                        {% endif %}

                    </ar:FECAEDetRequest>
                    {% endfor %}
                </ar:FeDetReq>
            </ar:FeCAEReq>
        </ar:FECAESolicitar>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECompTotXRequest = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECompTotXRequest>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FECompTotXRequest>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECompUltimoAutorizado = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECompUltimoAutorizado>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:PtoVta>{{ PtoVta }}</ar:PtoVta>
            <ar:CbteTipo>{{ CbteTipo }}</ar:CbteTipo>
        </ar:FECompUltimoAutorizado>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECompConsultar = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECompConsultar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:FeCompConsReq>
                <ar:CbteTipo>{{ FeCompConsReq.CbteTipo }}</ar:CbteTipo>
                <ar:CbteNro>{{ FeCompConsReq.CbteNro }}</ar:CbteNro>
                <ar:PtoVta>{{ FeCompConsReq.PtoVta }}</ar:PtoVta>
            </ar:FeCompConsReq>
        </ar:FECompConsultar>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECAEARegInformativo = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECAEARegInformativo>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:FeCAEARegInfReq>
                <ar:FeCabReq>
                    <ar:CantReg>{{ FeCAEARegInfReq.FeCabReq.CantReg }}</ar:CantReg>
                    <ar:PtoVta>{{ FeCAEARegInfReq.FeCabReq.PtoVta }}</ar:PtoVta>
                    <ar:CbteTipo>{{ FeCAEARegInfReq.FeCabReq.CbteTipo }}</ar:CbteTipo>
                </ar:FeCabReq>
                <ar:FeDetReq>
                {% for item in FeCAEARegInfReq.FeDetReq.FECAEADetRequest %}
                    <ar:FECAEADetRequest>
                        <ar:Concepto>{{ item.Concepto }}</ar:Concepto>
                        <ar:DocTipo>{{ item.DocTipo }}</ar:DocTipo>
                        <ar:DocNro>{{ item.DocNro }}</ar:DocNro>
                        <ar:CbteDesde>{{ item.CbteDesde }}</ar:CbteDesde>
                        <ar:CbteHasta>{{ item.CbteHasta }}</ar:CbteHasta>
                        <ar:CbteFch>{{ item.CbteFch }}</ar:CbteFch>
                        <ar:ImpTotal>{{ item.ImpTotal }}</ar:ImpTotal>
                        <ar:ImpTotConc>{{ item.ImpTotConc }}</ar:ImpTotConc>
                        <ar:ImpNeto>{{ item.ImpNeto }}</ar:ImpNeto>
                        <ar:ImpOpEx>{{ item.ImpOpEx }}</ar:ImpOpEx>
                        <ar:ImpTrib>{{ item.ImpTrib }}</ar:ImpTrib>
                        <ar:ImpIVA>{{ item.ImpIVA }}</ar:ImpIVA>
                    {% if item.FchServDesde %}
                        <ar:FchServDesde>{{ item.FchServDesde }}</ar:FchServDesde>
                    {% endif %}
                    {% if item.FchServHasta %}
                        <ar:FchServHasta>{{ item.FchServHasta }}</ar:FchServHasta>
                    {% endif %}
                    {% if item.FchVtoPago %}
                        <ar:FchVtoPago>{{ item.FchVtoPago }}</ar:FchVtoPago>
                    {% endif %}
                        <ar:MonId>{{ item.MonId }}</ar:MonId>
                    {% if item.MonCotiz %}
                        <ar:MonCotiz>{{ item.MonCotiz }}</ar:MonCotiz>
                    {% endif %}
                    {% if item.CanMisMonExt %}
                        <ar:CanMisMonExt>{{ item.CanMisMonExt }}</ar:CanMisMonExt>
                    {% endif %}
                        <ar:CondicionIVAReceptorId>{{ item.CondicionIVAReceptorId }}</ar:CondicionIVAReceptorId>

                        {% if item.CbtesAsoc %}
                        <ar:CbtesAsoc>
                            {% for i in item.CbtesAsoc %}
                            <ar:CbteAsoc>
                                <ar:Tipo>{{ i.Tipo }}</ar:Tipo>
                                <ar:PtoVta>{{ i.PtoVta }}</ar:PtoVta>
                                <ar:Nro>{{ i.Nro }}</ar:Nro>
                                <ar:Cuit>{{ i.Cuit }}</ar:Cuit>
                                <ar:CbteFch>{{ i.CbteFch }}</ar:CbteFch>
                            </ar:CbteAsoc>
                            {% endfor %}
                        </ar:CbtesAsoc>
                        {% endif %}

                        {% if item.Tributos %}
                        <ar:Tributos>
                            {% for i in item.Tributos %}
                            <ar:Tributo>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Desc>{{ i.Desc }}</ar:Desc>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Alic>{{ i.Alic }}</ar:Alic>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:Tributo>
                            {% endfor %}
                        </ar:Tributos>
                        {% endif %}

                        {% if item.Iva %}
                        <ar:Iva>
                            {% for i in item.Iva %}
                            <ar:AlicIva>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:BaseImp>{{ i.BaseImp }}</ar:BaseImp>
                                <ar:Importe>{{ i.Importe }}</ar:Importe>
                            </ar:AlicIva>
                            {% endfor %}
                        </ar:Iva>
                        {% endif %}

                        {% if item.Opcionales %}
                        <ar:Opcionales>
                            {% for i in item.Opcionales %}
                            <ar:Opcional>
                                <ar:Id>{{ i.Id }}</ar:Id>
                                <ar:Valor>{{ i.Valor }}</ar:Valor>
                            </ar:Opcional>
                            {% endfor %}
                        </ar:Opcionales>
                        {% endif %}

                        {% if item.Compradores %}
                        <ar:Compradores>
                            {% for i in item.Compradores %}
                            <ar:Comprador>
                                <ar:DocTipo>{{ i.DocTipo }}</ar:DocTipo>
                                <ar:DocNro>{{ i.DocNro }}</ar:DocNro>
                                <ar:Porcentaje>{{ i.Porcentaje }}</ar:Porcentaje>
                            </ar:Comprador>
                            {% endfor %}
                        </ar:Compradores>
                        {% endif %}

                        <ar:CAEA>{{ item.CAEA }}</ar:CAEA>

                        {% if item.CbteFchHsGen %}
                            <ar:CbteFchHsGen>{{ item.CbteFchHsGen }}</ar:CbteFchHsGen>
                        {% endif %}

                        {% if item.PeriodoAsoc %}
                        <ar:PeriodoAsoc>
                            {% for i in item.PeriodoAsoc %}
                                <ar:FchDesde>{{ i.FchDesde }}</ar:FchDesde>
                                <ar:FchHasta>{{ i.FchHasta }}</ar:FchHasta>
                            {% endfor %}
                        </ar:PeriodoAsoc>
                        {% endif %}

                        {% if item.Actividades %}
                        <ar:Actividades>
                            {% for i in item.Actividades %}
                            <ar:Actividad>
                                <ar:Id>{{ i.Id }}</ar:Id>
                            </ar:Actividad>
                            {% endfor %}
                        </ar:Actividades>
                        {% endif %}

                    </ar:FECAEADetRequest>
                    {% endfor %}
                </ar:FeDetReq>
            </ar:FeCAEARegInfReq>
        </ar:FECAEARegInformativo>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECAEASolicitar = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECAEASolicitar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:Periodo>{{ Periodo }}</ar:Periodo>
            <ar:Orden>{{ Orden }}</ar:Orden>
        </ar:FECAEASolicitar>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECAEASinMovimientoConsultar = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECAEASinMovimientoConsultar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:CAEA>{{ CAEA }}</ar:CAEA>
            <ar:PtoVta>{{ PtoVta }}</ar:PtoVta>
        </ar:FECAEASinMovimientoConsultar>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECAEASinMovimientoInformar = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECAEASinMovimientoInformar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
            <ar:PtoVta>{{ PtoVta }}</ar:PtoVta>
            <ar:CAEA>{{ CAEA }}</ar:CAEA>
        </ar:FECAEASinMovimientoInformar>
    </soapenv:Body>
</soapenv:Envelope>
"""

FECAEAConsultar = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FECAEAConsultar>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
                <ar:Periodo>{{ Periodo }}</ar:Periodo>
                <ar:Orden>{{ Orden }}</ar:Orden>
        </ar:FECAEAConsultar>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetCotizacion = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetCotizacion>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
                <ar:MonId>{{ MonId }}</ar:MonId>
                <ar:FchCotiz>{{ FchCotiz }}</ar:FchCotiz>
        </ar:FEParamGetCotizacion>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetTiposTributos = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposTributos>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposTributos>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetTiposMonedas = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposMonedas>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposMonedas>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetTiposIva = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposIva>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposIva>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetTiposOpcional = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposOpcional>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposOpcional>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetTiposConcepto = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposConcepto>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposConcepto>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetPtosVenta = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetPtosVenta>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetPtosVenta>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetTiposCbte = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposCbte>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposCbte>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetCondicionIvaReceptor = """<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
<soap-env:Body>
    <ns0:FEParamGetCondicionIvaReceptor xmlns:ns0="http://ar.gov.afip.dif.FEV1/">
        <ns0:Auth>
            <ns0:Token>{{ Auth.Token }}</ns0:Token>
            <ns0:Sign>{{ Auth.Sign }}</ns0:Sign>
            <ns0:Cuit>{{ Auth.Cuit }}</ns0:Cuit>
        </ns0:Auth>
        {% if ClaseCmp %}
        <ns0:ClaseCmp>{{ ClaseCmp }}</ns0:ClaseCmp>
        {% endif %}
    </ns0:FEParamGetCondicionIvaReceptor>
    </soap-env:Body>
</soap-env:Envelope>
"""

FEParamGetTiposDoc = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposDoc>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposDoc>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetTiposPaises = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
    <soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetTiposPaises>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetTiposPaises>
    </soapenv:Body>
</soapenv:Envelope>
"""

FEParamGetActividades = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:ar="http://ar.gov.afip.dif.FEV1/">
<soapenv:Header/>
    <soapenv:Body>
        <ar:FEParamGetActividades>
            <ar:Auth>
                <ar:Token>{{ Auth.Token }}</ar:Token>
                <ar:Sign>{{ Auth.Sign }}</ar:Sign>
                <ar:Cuit>{{ Auth.Cuit }}</ar:Cuit>
            </ar:Auth>
        </ar:FEParamGetActividades>
    </soapenv:Body>
</soapenv:Envelope>
"""