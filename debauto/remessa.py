from collections import namedtuple


class Remessa:
    ''' Remessa Debito Automatico '''

    def __init__(self, cfg, debitos):
        # assert
        assert isinstance(debitos, list), TypeError(
            "Você deve passar uma lista de débitos"
        )

        # configuração
        self._cfg = cfg

        # debitos
        self._debitos = debitos

    @property
    def debitos(self):
        ''' property get_debitos '''
        return self._debitos

    @debitos.setter
    def debitos(self, value):
        ''' property set_debitos '''
        self._debitos = value

    def gerar_arquivo_txt(self):
        ''' gerar remessa '''
        with open('test.txt', 'w+') as f:
            f.write(self.get_header())
            for _ in self.get_debitos():
                f.write(_)
            f.write(self.get_trailler())

    def __repr__(self):
        ''' representação do objeto '''
        return "<Remessa: %s>" % (self._cfg['arquivo']['sequencial'])


Config = namedtuple('Config', [
    'banco', 'codigo', 'agencia', 'conta',
    'convenio', 'empresa', 'sequencial', 'vencimento'
])


Debito = namedtuple('Debito', [
    'identificacao', 'agencia', 'conta',
    'vencimento', 'valor', 'moeda', 'livre', 'tipo'
])


Inclusao = namedtuple('Debito', [
    'identificacao', 'agencia', 'conta', 'tipo'
])


"""
    Bancos
"""


class BancoBrasil(Remessa):
    '''
    Banco do Brasil
    '''
    a = "A{:1}{:20}{:20}{:3}{:20}{:8}{:6}{:2}{:17}{:52}\r\n"
    e = "E{:25}{:0<4}{:14}{:8}{:0<15}{:2}{:49}{:10}{:1}{:20}{:1}\r\n"
    z = "Z{:0>6}{:0>17}{:126}"

    def get_header(self):
        ''' retorna o header do arquivo '''
        cfg = self._cfg

        return self.a.format(
            1, cfg.convenio, cfg.empresa, cfg.codigo,
            cfg.banco, '', cfg.sequencial, '04', '', ''
        )

    def get_debitos(self):
        ''' retorna as linhas e do arquivo '''
        linhas = []

        for x in self._debitos:
            linhas.append(self.e.format(
                x.identificacao, x.agencia, x.conta, x.vencimento,
                x.valor, x.moeda, x.livre, "", "", "", x.tipo
            ))

        return linhas

    def get_trailler(self):
        ''' retorna o trailler do arquivo '''
        return self.z.format(
            len(self._debitos) + 2,
            str('%.2f' % sum(_.valor for _ in self._debitos)).replace('.', ''),
            ''
        )


class Santander(Remessa):
    '''
    Santander
    '''
    a = "A{:1}{:20}{:20}{:3}{:20}{:8}{:6}{:2}{:17}{:52}\r\n"
    e = "E{:25}{:0<4}{:14}{:8}{:0<15}{:2}{:49}{:10}{:1}{:20}{:1}\r\n"
    z = "Z{:0>6}{:0>17}{:126}"

    def get_header(self):
        ''' retorna o header do arquivo '''
        cfg = self._cfg

        return self.a.format(
            1, cfg.convenio, cfg.empresa, cfg.codigo,
            cfg.banco, '', cfg.sequencial, '04', '', ''
        )

    def get_debitos(self):
        ''' retorna as linhas e do arquivo '''
        linhas = []

        for x in self._debitos:
            linhas.append(self.e.format(
                x.identificacao, x.agencia, x.conta, x.vencimento,
                x.valor, x.moeda, x.livre, "", "", "", x.tipo
            ))

        return linhas

    def get_trailler(self):
        ''' retorna o trailler do arquivo '''
        return self.z.format(
            len(self._debitos) + 2,
            str('%.2f' % sum(_.valor for _ in self._debitos)).replace('.', ''),
            ''
        )


class Caixa(Remessa):
    '''
    Caixa
    '''
    a = "A{:1}{:20}{:20}{:3}{:20}{:8}{:6}{:2}{:17}{:52}\r\n"
    e = "E{:0>25}{:0<4}{:14}{:8}{:0<15}{:2}{:60}{:6}{:8}{:0>6}{:1}\r\n"
    z = "Z{:0>6}{:0>17}{:126}"

    def get_header(self):
        ''' retorna o header do arquivo '''
        cfg = self._cfg

        return self.a.format(
            1, cfg.convenio, cfg.empresa, cfg.codigo,
            cfg.banco, '', cfg.sequencial, '04', '', ''
        )

    def get_debitos(self):
        ''' retorna as linhas e do arquivo '''
        linhas = []

        for n, x in enumerate(self._debitos, 1):
            linhas.append(self.e.format(
                x.identificacao, x.agencia, x.conta, x.vencimento,
                x.valor, x.moeda, x.livre, "", "", n, x.tipo
            ))

        return linhas

    def get_trailler(self):
        ''' retorna o trailler do arquivo '''
        return self.z.format(
            len(self._debitos) + 2,
            str('%.2f' % sum(_.valor for _ in self._debitos)).replace('.', ''),
            ''
        )
