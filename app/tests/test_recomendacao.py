import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.utils.timer import Timer
from app.core.arvore_avl import ArvoreAVL
from app.core.categoria import Categoria
from app.services.recomendacao_service import RecomendacaoService
from app.utils.logger import Logger
# Cria logger para o teste
arvore = ArvoreAVL()

#Cria categorias para o logger
cat1 = Categoria("Pokébolas", ["Poké ball, Great Ball, Ultra ball"])
cat2 = Categoria("Medicamentos", ["Poção", "Super-poção", "Hiper-poção", "Poção Máxima", "Restauração completa"])
cat3 = Categoria("Itens de evolução", ["Bloco de turfa", "Augurita preta", "Disco Duvidoso", "Sachê", "DenteDoFundoDoMar", "Revestimento Metálico", "Pedra do Rei"])
cat4 = Categoria("Mega-Pedras", ["Venusaurite", "Blastoisenite", "Charizardite X", "Charizardite Y", "Meganiumite", "Feraligite", "Emboarite", "Chesnaughtite", "Delphoxite", "Greninjite"])
#Cria subcategorias e as associa as categorias principais
sub1 = Categoria("Pokébolas especiais", ["Safari ball", "Dream Ball", "Sport Ball", "Beast Ball"])
sub2 = Categoria("Pokébolas de Johto", ["Friend Ball", "Love Ball", "Fast Ball", "Moon Ball", "Heavy ball", "Lure Ball", "Level Ball"])
cat1.adicionar_subcategoria(sub1)
cat1.adicionar_subcategoria(sub2)
sub1 = Categoria("Cura de status", ["Antídoto", "Despertar", "Cura de Paralisia", "Descongelante", "Antiqueimadura", "Cura total", "Reviver"])
sub2 = Categoria("Proteínas", ["Carbos", "Vitamina", "Zinco", "Ferro", "Cálcio", "HP Up", "PP Up", "PP Max"])
cat2.adicionar_subcategoria(sub1)
cat2.adicionar_subcategoria(sub2)
sub1 = Categoria("Pedras evolutivas", ["Pedra do Fogo", "Pedra do Trovão", "Pedra d'Água", "Pedra da Folha", "Pedra da Lua", "Pedra do Sol", "Pedra do Crepúsculo", "Pedra Brilhante", "Pedra da alvorada", "Pedra do Gelo"])
cat3.adicionar_subcategoria(sub1)
#Adciona as categorias ao logger
arvore.inserir_publico(cat1)
arvore.inserir_publico(cat2)
arvore.inserir_publico(cat3)
arvore.inserir_publico(cat4)
#Inicializa o serviço de recomendação
servico_recomendacao = RecomendacaoService(arvore)
#Teste de autocompleção
busca = input("Digite para buscar algo: ")
lista_autocomplecao = servico_recomendacao.sugerir_por_prefixo(busca)
print(f"Possíveis resultados para {busca}:")
for i in lista_autocomplecao:
    print(i)
#Teste de recomendação
busca = input("Digite o nome uma categoria ou subcategoria para ver recomendações de produtos:")
print(servico_recomendacao.recomendar_produtos(busca))
#Teste de autocompleção após a adição de outro produto
arvore.buscar_publico("Pokébolas").adicionar_produto("Master ball")
servico_recomendacao.reindexar()
print(servico_recomendacao.sugerir_por_prefixo("Master"))
