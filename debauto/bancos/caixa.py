from debauto.remessa import Remessa
from debauto.utils import formata_data, formata_valor


class Caixa(Remessa):
    """
    Caixa
    """
    __a = "A{:1}{:20}{:20}{:3}{:20}{:8}{:6}{:2}{:17}{:45}{:0>7}\r\n"
    __e = "E{:0>25}{:0<4}{:14}{:8}{:0<15}{:2}{:60}{:6}{:8}{:0>6}{:1}\r\n"
    __z = "Z{:0>6}{:0>17}{:119}{:0>6}{:1}"

    def __init__(self, *args, **kwargs):
        super(Caixa, self).__init__(*args, **kwargs)

        self.__cod_remessa = 1
        self.__banco = "CAIXA"
        self.__codigo = "104"
        self.__versao = '04'
        self.__identificacao = "DEB AUTOMAT"

    def get_header(self):
        """ retorna o header do arquivo """
        cfg = self.configuracao

        return self.__a.format(
            self.__cod_remessa,             # 1  - Código da remessa
            cfg.convenio,                   # 20 - Código do convênio
            cfg.empresa,                    # 20 - Nome da empresa
            self.__codigo,                  # 3  - Código do banco
            self.__banco,                   # 20 - Nome do banco
            formata_data(cfg.vencimento),   # 8  - Data do movimento
            cfg.sequencial,                 # 6  - Número sequencial
            self.__versao,                  # 2  - Versão do layout
            self.__identificacao,           # 17 - Identificação do serviço
            '', '0'
        )

    def get_debitos(self):
        """ retorna as linhas e do arquivo """
        linhas = []

        for n, x in enumerate(self.debitos, 1):
            linhas.append(self.__e.format(
                x.identificacao,
                x.agencia,
                x.conta,
                formata_data(x.vencimento),
                formata_valor(x.valor),
                x.moeda,
                x.livre,
                "",
                "",
                n,
                x.tipo
            ))

        return linhas

    def get_trailler(self):
        """ retorna o trailler do arquivo """
        return self.__z.format(
            self.quantidade() + 2,
            formata_valor(self.valor_total()),
            '',
            self.quantidade() + 1,
            ''
        )
