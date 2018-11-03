from remessa import Caixa, Config, Debito, Inclusao

cfg = Config(
    banco='Caixa',
    codigo='104',
    agencia='0289',
    conta='92-0',
    convenio='308478110001',
    empresa='APAE Batatais',
    sequencial='1',
    vencimento='10/10/2018'
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
