from random import randint
from debauto.remessa import Caixa, Config, Debito, Inclusao

cfg = Config(
    banco='Caixa',
    codigo='104',
    agencia='0001',
    conta='11-1',
    convenio='222222222222',
    empresa='Empresa Exemplo',
    sequencial='1',
    vencimento='01/01/1900'
)

a = Caixa(cfg, [
    Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1900",       # data vencimento    08 posições
        200.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 1",        # identificação co   59 posições
        1),                 # 0 - Normal    1 - Cancelamento

    Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1900",       # data vencimento    08 posições
        200.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 2",        # identificação co   59 posições
        1),                 # 0 - Normal    1 - Cancelamento

    Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1900",       # data vencimento    08 posições
        200.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 3",        # identificação co   59 posições
        1),                 # 0 - Normal    1 - Cancelamento

    Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1900",       # data vencimento    08 posições
        200.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 4",        # identificação co   59 posições
        1),                 # 0 - Normal    1 - Cancelamento

    Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1900",       # data vencimento    08 posições
        200.00,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 5",        # identificação co   59 posições
        1),                 # 0 - Normal    1 - Cancelamento

    Debito(
        randint(1,9999),    # identificacao      25 posições
        randint(1,9999),    # agência            04 posições
        randint(1,9999),    # conta              13 posições
        "01/01/1900",       # data vencimento    08 posições
        200,             # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 6",        # identificação co   59 posições
        1),                 # 0 - Normal    1 - Cancelamento
])

a.gerar_arquivo_txt()
