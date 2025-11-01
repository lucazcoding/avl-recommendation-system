from arvore_avl import ArvoreAVL
from categoria import Categoria

#Inicialização da árvore
arvore = ArvoreAVL()

#Categorias para teste
cat1 = Categoria("Pokébolas", ["Poké ball", "Great ball", "Ultra ball"], 3)
cat2 = Categoria("Medicamentos", ["Poção", "Super Poção", "Hiper poção"], 2)
cat3 = Categoria("Itens de batalha", ["X-Attack", "X-Defense", "Dire hit"])
cat4 = Categoria("Itens de evolução", ["Disco duvidoso", "Revestimento metálico", "Magmarizer", "Electrizer"], 5)
#Subcategorias para teste
subcat1 = Categoria("Pokébolas de apricorn", ["Heavy ball", "Moon ball", "Lure Ball"], 3)
subcat2 = Categoria("Pokébolas especiais", ["Dream ball"], 5)
cat1.adicionar_subcategoria(subcat1)
cat1.adicionar_subcategoria(subcat2)
subcat3 = Categoria("Medicamentos para condição de status", ["Antídoto", "Reviver", "Despertar"], 3)
cat2.adicionar_subcategoria(subcat3)
subcat4 = Categoria("Flautas", ["Flauta vermelha", "Flauta azul"])
subcat5 = Categoria("Itens de fuga", ["Poké-doll", "Fluffy tail", "Poké-toy"])
cat3.adicionar_subcategoria(subcat4)
cat3.adicionar_subcategoria(subcat5)
subcat6 = Categoria("Pedras evolutivas", ["Pedra d'água", "Pedra do trovão", "Pedra do fogo"], 7)
cat4.adicionar_subcategoria(subcat6)

#Preenchimento da árvore
print("=======TESTE1=======")
arvore.inserir_publico(cat1)
arvore.inserir_publico(cat2)
arvore.inserir_publico(cat3)
arvore.inserir_publico(cat4)
arvore.imprimir_arvore()

#testes de adição de novas categoria
print("=======TESTE2=======")
cat5 = Categoria("TMs e HMs", ["TM 067", "TM 044", "TM 100"], 4)
arvore.inserir_publico(cat5)
arvore.imprimir_arvore()
print("=======TESTE3======")
cat6 = Categoria("Mega pedras", ["Meganiumite", "Feraligite", "Emboarite"], 9)
arvore.inserir_publico(cat6)
arvore.imprimir_arvore()

#teste de remoção de produto
print("=======TESTE4=======")
arvore.buscar_publico("Itens de evolução").remover_produto("Disco duvidoso")
arvore.imprimir_arvore()

#Teste de adição de produto a categoria e subcategoria
print("=======TESTE5=======")
arvore.buscar_publico("Pokébolas").adicionar_produto("Master ball")
arvore.buscar_publico("Pokébolas").subcategorias[1].adicionar_produto("Safari ball")
arvore.imprimir_arvore()

#Teste de adição de subcategoria a árvore
print("=======TESTE6=======")
subcat = Categoria("Vitaminas", ["Ferro", "Zinco", "Proteína", "HP up", "PP max"], 9)
arvore.buscar_publico("Medicamentos").adicionar_subcategoria(subcat)
arvore.imprimir_arvore()

#teste de remoção de categoria
print("=======TESTE7=======")
arvore.remover_publico("Itens de batalha")
arvore.imprimir_arvore()
print("=======TESTE8=======")
arvore.remover_publico("Mega pedras")
arvore.imprimir_arvore()
