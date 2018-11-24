from debauto.remessa import Remessa


class BancoBrasil(Remessa):
    """
    Banco do Brasil
    """
    a = "A{:1}{:20}{:20}{:3}{:20}{:8}{:6}{:2}{:17}{:52}\r\n"
    e = "E{:25}{:0<4}{:14}{:8}{:0<15}{:2}{:49}{:10}{:1}{:20}{:1}\r\n"
    z = "Z{:0>6}{:0>17}{:126}"

    def get_header(self):
        """ retorna o header do arquivo """
        cfg = self._cfg

        return self.a.format(
            1, cfg.convenio, cfg.empresa, cfg.codigo,
            cfg.banco, '', cfg.sequencial, '04', '', ''
        )

    def get_debitos(self):
        """ retorna as linhas e do arquivo """
        linhas = []

        for x in self.debitos:
            linhas.append(self.e.format(
                x.identificacao, x.agencia, x.conta, x.vencimento,
                x.valor, x.moeda, x.livre, "", "", "", x.tipo
            ))

        return linhas

    def get_trailler(self):
        """ retorna o trailler do arquivo """
        return self.z.format(
            len(self.debitos) + 2,
            str('%.2f' % sum(_.valor for _ in self.debitos)).replace('.', ''),
            ''
        )
