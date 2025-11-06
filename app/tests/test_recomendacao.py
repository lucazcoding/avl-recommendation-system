import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.utils.timer import Timer
from app.core.arvore_avl import ArvoreAVL
from app.core.categoria import Categoria
from app.services.recomendacao_service import RecomendacaoService
from app.utils.logger import Logger
# Cria logger para o teste
arvore = ArvoreAVL()

# Categoria principal
eletronicos = Categoria("Eletrônicos")
eletronicos.adicionar_produto("Fone JBL")
eletronicos.adicionar_produto("Notebook Dell")
eletronicos.adicionar_produto("Fone multilaser")

# Subcategoria
acessorios = Categoria("Acessórios")
acessorios.adicionar_produto("Cabo HDMI")
eletronicos.adicionar_subcategoria(acessorios)

# Insere categoria na árvore usando método público
arvore.inserir_publico(eletronicos)

# ===== Cria serviço =====
service = RecomendacaoService(arvore)
logger = service.logger  # usa o logger do serviço
timer = Timer()

# ===== Teste 1: Sugestão por prefixo =====
logger.info("===== Teste 1: Sugestões por prefixo =====")
timer.start()
sugestoes = service.sugerir_por_prefixo("Ca")
timer.stop()
logger.info(f"Sugestões para 'Ca': {sugestoes}")
logger.info(f"Tempo de execução: {timer.get_elapsed_time():.6f}s")
logger.info("Complexidade Big O: O(1) para buscar índice + O(k) para filtrar k produtos")

# ===== Teste 2: Recomendação de produtos =====
logger.info("===== Teste 2: Recomendação de produtos =====")
timer.start()
recomendados = service.recomendar_produtos("Eletrônicos")
timer.stop()
logger.info(f"Produtos recomendados para 'Eletrônicos': {recomendados}")
logger.info(f"Tempo de execução: {timer.get_elapsed_time():.6f}s")
logger.info("Complexidade Big O: O(log n) para buscar categoria + O(m) para coletar m produtos")

# ===== Teste 3: Relatório de performance =====
logger.info("===== Teste 3: Relatório de performance =====")
timer.start()
relatorio = service.gerar_relatorio_performance()
timer.stop()
logger.info(f"Total de categorias: {relatorio['total_categorias']}")
logger.info(f"Altura da árvore: {relatorio['altura']}")
logger.info(f"Árvore balanceada: {relatorio['balanceada']}")
logger.info(f"Tempo de execução: {timer.get_elapsed_time():.6f}s")
logger.info("Complexidade Big O estimada:")
logger.info(" - Contar categorias: O(n)")
logger.info(" - Calcular altura: O(n)")
logger.info(" - Verificar balanceamento: O(n)")