# python-debauto-br


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/python-debauto-br.svg)](https://pypi.python.org/pypi/python-debauto-br/)
[![PyPI version fury.io](https://badge.fury.io/py/python-debauto-br.svg)](https://pypi.python.org/pypi/python-debauto-br/)
![PyPI - License](https://img.shields.io/pypi/l/python-debauto-br.svg)
[![Beerpay](https://beerpay.io/flaviomilan/python-debauto-br/badge.svg?style=beer-square)](https://beerpay.io/flaviomilan/python-debauto-br)  [![Beerpay](https://beerpay.io/flaviomilan/python-debauto-br/make-wish.svg?style=flat-square)](https://beerpay.io/flaviomilan/python-debauto-br?focus=wish)

Criação de remessas de débito automático no formato CNAB 150 da Febraban.

**Bancos**

| Banco           | Criado | Validado |
| -----           | ---    | ---      |
| Santander       | Sim    | Sim      |
| Banco do Brasil | Sim    | Sim      |
| Caixa           | Sim    | Sim      |


## Começando


### Pré-requisitos

Este pacote não possui nenhum pré-requisito.


### Instalação

Instale o pacote via pip

```
pip install python-debauto-br
```

## Utilização

Para criar uma remessa, devemos primeiro criar uma classe de configuração.

```python
from debauto.remessa import Configuracao

cfg = Configuracao(
    agencia='0001',             # Agência bancária
    conta='11-1',               # Conta bancária
    convenio='222222222222',    # Número de convênio
    empresa='Empresa Exemplo',  # Nome da empresa
    sequencial='1',             # Número sequencial
    vencimento='01/01/1900'     # Data de criação
)
```

Agora podemos importar a remessa e passar o arquivo de configuração

```python
from debauto.bancos.caixa import Caixa

remessa = Caixa(cfg)
```

Com a remessa devidamente instanciada, podemos inserir os débitos

```python
from debauto.remessa import Debito

remessa.debitos = Debito(
        9999,               # identificacao      25 posições
        9999,               # agência            04 posições
        9999,               # conta              13 posições
        "01/01/1900",       # data vencimento    08 posições
        10.00,              # valor              15 posições
        "03",               # código da moeda    02 posições
        "Exemplo 1",        # identificação co   59 posições
        0)                  # 0 - Normal    1 - Cancelamento
```

Após inserir os débitos, temos tudo pronto para criar o arquivo de remessa

```python
path = '/tmp/'
remessa.gerar_txt(path)
```

## Authors

* **Flávio Milan**

Veja a lista completa de contribuidores em [contribuidores](https://github.com/flaviomilan/python-debauto-br/contributors).

## Licença

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Gostou do projeto?
Aceito uma :cerveja:!

[![Beerpay](https://beerpay.io/flaviomilan/python-debauto-br/badge.svg?style=beer-square)](https://beerpay.io/flaviomilan/python-debauto-br)  [![Beerpay](https://beerpay.io/flaviomilan/python-debauto-br/make-wish.svg?style=flat-square)](https://beerpay.io/flaviomilan/python-debauto-br?focus=wish)