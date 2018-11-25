# -*- encoding: utf-8 -*-

import datetime


def formata_data(data):
    data = datetime.datetime.strptime(data, '%d/%m/%Y').date()
    return data.strftime("%Y%m%d")


def formata_valor(valor):
    return str("%.2f" % valor).replace(".", "")
