# -*- encoding: utf-8 -*-

from random import randint
from debauto.remessa import Configuracao, Debito
from debauto.bancos.caixa import Caixa
from debauto.bancos.bb import BancoBrasil
from debauto.bancos.santander import Santander


cfg = Configuracao(
    agencia='0001',
    conta='11-1',
    convenio='222222222222',
    empresa='Empresa Exemplo',
    sequencial='1',
    vencimento='01/01/1900'
)

a = Caixa(cfg)
b = BancoBrasil(cfg)
c = Santander(cfg)


a.debitos = Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1999",       # data vencimento    08 posições
        123.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 1",        # identificação co   59 posições
        0)                  # 0 - Normal    1 - Cancelamento

a.debitos = Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1999",       # data vencimento    08 posições
        243.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 2",        # identificação co   59 posições
        0)                  # 0 - Normal    1 - Cancelamento

b.debitos = Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1999",       # data vencimento    08 posições
        123.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 1",        # identificação co   59 posições
        0)                  # 0 - Normal    1 - Cancelamento

b.debitos = Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1999",       # data vencimento    08 posições
        243.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 2",        # identificação co   59 posições
        0)                  # 0 - Normal    1 - Cancelamento

c.debitos = Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1999",       # data vencimento    08 posições
        123.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 1",        # identificação co   59 posições
        0)                  # 0 - Normal    1 - Cancelamento

c.debitos = Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1999",       # data vencimento    08 posições
        243.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 2",        # identificação co   59 posições
        0)                  # 0 - Normal    1 - Cancelamento

a.gerar_txt('.')
b.gerar_txt('.')
c.gerar_txt('.')
