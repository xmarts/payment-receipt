# -*- coding: utf-8 -*-
import base64
from xml.etree import ElementTree
from lxml.objectify import fromstring
from odoo import models, fields, api
from . import amount_to_text


class payment_receipt(models.Model):
	_inherit = 'account.payment'

	def _mount_to_text(self, monto):
		text_monto = amount_to_text.get_amount_to_text(self, float(monto), self.currency_id.name)
		return text_monto

	@api.model
	def complemento(self):
		data = base64.decodestring(self.l10n_mx_edi_cfdi)
		root =ElementTree.fromstring(data)
		count = 0
		lista = []
		cont = 0
		if count == 0:
			count += count + 1
			for child in root.findall('{http://www.sat.gob.mx/cfd/3}Complemento'):
				for pagos in child:
					for pago in pagos:
						monto =	pago.get('Monto')
						for doc in pago:
							if lista:
								result_lista = self.buscar_registro(lista,doc.attrib['Folio'])
								if result_lista == False:
									vals = {
									'serie': doc.attrib['Serie'],
									'folio': doc.attrib['Folio'],
									'moneda_DR': doc.attrib['MonedaDR'],
									'tipo_cambio_p': doc.attrib['TipoCambioP'],
									'num_parcialidad':doc.attrib['NumParcialidad'],
									'imp_saldo_ant':doc.attrib['ImpSaldoAnt'],
									'imp_pagado': doc.attrib['ImpPagado'],
									'imp_saldo_insoluto':doc.attrib['ImpSaldoInsoluto'],
									'monto':monto
									}
									lista.append(vals)
							else:
								if cont == 0:
									vals = {
									'serie': doc.attrib['Serie'],
									'folio': doc.attrib['Folio'],
									'moneda_DR': doc.attrib['MonedaDR'],
									'tipo_cambio_p': doc.attrib['TipoCambioP'],
									'num_parcialidad':doc.attrib['NumParcialidad'],
									'imp_saldo_ant':doc.attrib['ImpSaldoAnt'],
									'imp_pagado': doc.attrib['ImpPagado'],
									'imp_saldo_insoluto':doc.attrib['ImpSaldoInsoluto'],
									'monto':monto
									}
									lista.append(vals)
									cont = 1
		return lista

	def buscar_registro(self, lista, data_folio):
		res = False
		for data in lista:
			if data['folio'] == data_folio:
				res = True
				return res
		return res

	@api.model
	def complemento_pago(self, cfdi):
		data = base64.decodestring(self.l10n_mx_edi_cfdi)
		root =ElementTree.fromstring(data)
		vals = {}
		cont = 0
		for child in root.findall('{http://www.sat.gob.mx/cfd/3}Complemento'):
			for pagos in child:
				for pago in pagos:
					monto =	pago.get('Monto')
					num_operacion = pago.get('NumOperacion')
					if cont == 0:
						vals = {
						# 'fecha_pago': pago.get('FechaPago'),
						'forma_de_pago_p': pago.get('FormaDePagoP'),
						'num_operacion': pago.get('NumOperacion')
						}
						cont = 1
		return vals
