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
    Debito(1,1,1,1,1,1,1,1),
    Debito(2,2,2,2,2,2,2,1),
    Debito(3,3,3,3,3,3,3,1),
    Debito(4,4,4,4,4,4,4,1),
    Debito(5,5,5,5,5,5,5,1),
    Debito(6,6,6,6,6,6,6,1),
])

a.gerar_arquivo_txt()
