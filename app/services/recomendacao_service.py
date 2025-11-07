import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.core.arvore_avl import ArvoreAVL
from app.utils.timer import Timer
from app.utils.logger import Logger
from typing import List, Dict, Optional


class RecomendacaoService:
    """
    Serviço de recomendação hierárquica de produtos (SRHP).

    Complexidade:
        - buscar_categoria_recursiva: O(log n)
        - sugerir_por_prefixo: O(1) + O(k)
        - recomendar_produtos: O(log n) + O(m)
    """

    def __init__(self, arvore_avl: ArvoreAVL):
        """
        Inicializa o serviço de recomendação com referência à árvore AVL.

        Args:
            arvore_avl: instância de ArvoreAVL
        """
        self.arvore = arvore_avl
        self.timer = Timer()
        self.logger = Logger(__name__)

        self.indice_produtos = {}     # {'F': [produtos...], 'N': [...]}
        self.indice_categorias = {}   # {'fone jbl': 'Eletrônicos > Acessórios'}

        self._construir_indices()

    # =============================================================
    # 🔧 Construção e manutenção de índices
    # =============================================================

    def _construir_indices(self):
        """
        Constrói índices invertidos para busca O(1) por prefixo.
        Deve ser executado uma vez na inicialização.
        """
        self.logger.info("Construindo índices de produtos...")
        self.indice_produtos.clear()
        self.indice_categorias.clear()

        categorias = self._obter_todas_categorias()

        for categoria in categorias:
            # Produtos da categoria principal
            for produto in categoria.produtos:
                self._adicionar_ao_indice(produto, categoria.nome)

            # Produtos das subcategorias
            for subcategoria in categoria.subcategorias:
                for produto in subcategoria.produtos:
                    caminho = f"{categoria.nome} > {subcategoria.nome}"
                    self._adicionar_ao_indice(produto, caminho)

        self.logger.info(
            f"Índices construídos com sucesso: {len(self.indice_categorias)} produtos indexados."
        )

    def _adicionar_ao_indice(self, produto: str, caminho_categoria: str):
        """Adiciona um produto ao índice invertido."""
        letra = produto[0].upper()
        if letra not in self.indice_produtos:
            self.indice_produtos[letra] = []

        self.indice_produtos[letra].append({
            "nome": produto,
            "categoria": caminho_categoria
        })

        self.indice_categorias[produto.lower()] = caminho_categoria

    def _obter_todas_categorias(self) -> List:
        """Obtém todas as categorias da AVL via percurso in-order."""
        categorias = []

        def percorrer_inorder(no):
            if no is None:
                return
            percorrer_inorder(no.esquerda)
            categorias.append(no.categoria)
            percorrer_inorder(no.direita)

        percorrer_inorder(self.arvore.raiz)
        return categorias

    # =============================================================
    # 🔍 Funcionalidades principais
    # =============================================================

    def buscar_categoria_recursiva(self, nome: str) -> Optional[object]:
        self.timer.start()
        self.logger.info(f"Buscando categoria: {nome}")

    # Passa raiz como primeiro argumento
        resultado = self.arvore.buscar(self.arvore.raiz, nome)

        self.timer.stop()
        tempo = self.timer.get_elapsed_time()

        if resultado:
            self.logger.info(f"Categoria '{nome}' encontrada em {tempo:.4f}s")
        else:
            self.logger.warning(f"Categoria '{nome}' não encontrada")

        return resultado


    def sugerir_por_prefixo(self, prefixo: str, limite: int = 7) -> List[Dict]:
        """
        Sugere produtos que começam com o prefixo informado.
        (Autocomplete)
        """
        self.timer.start()

        if not prefixo:
            return []

        letra = prefixo[0].upper()
        candidatos = self.indice_produtos.get(letra, [])

        prefixo_lower = prefixo.lower()
        resultados = [
            p for p in candidatos
            if p["nome"].lower().startswith(prefixo_lower)
        ]

        sugestoes = resultados[:limite]

        self.timer.stop()
        tempo = self.timer.get_elapsed_time()

        self.logger.info(
            f"Sugestão '{prefixo}': {len(sugestoes)} resultados em {tempo:.4f}s."
        )

        return sugestoes

    def recomendar_produtos(
        self,
        categoria_nome: str,
        incluir_subcategorias: bool = True,
        limite: Optional[int] = None
    ) -> Dict:
        """
        Retorna produtos recomendados de uma categoria,
        incluindo (opcionalmente) subcategorias.
        """
        self.timer.start()
        self.logger.info(f"Gerando recomendações para '{categoria_nome}'...")

        categoria = self.buscar_categoria_recursiva(categoria_nome)

        if not categoria:
            self.timer.stop()
            return {
                "sucesso": False,
                "mensagem": f"Categoria '{categoria_nome}' não encontrada",
                "produtos": []
            }

        produtos_recomendados = []

        # Produtos da categoria principal
        for produto in categoria.produtos:
            produtos_recomendados.append({
                "produto": produto,
                "categoria": categoria_nome,
                "nivel": "principal"
            })

        # Produtos das subcategorias (recursivo)
        if incluir_subcategorias:
            produtos_recomendados.extend(
                self._coletar_produtos_subcategorias(
                    categoria.subcategorias,
                    categoria_nome
                )
            )

        if limite:
            produtos_recomendados = produtos_recomendados[:limite]

        self.timer.stop()
        tempo = self.timer.get_elapsed_time()

        resultado = {
            "sucesso": True,
            "categoria": categoria_nome,
            "total_produtos": len(produtos_recomendados),
            "produtos": produtos_recomendados,
            "tempo_execucao": f"{tempo:.4f}s"
        }

        self.logger.info(
            f"Recomendação concluída: {len(produtos_recomendados)} produtos em {tempo:.4f}s."
        )

        return resultado

    def _coletar_produtos_subcategorias(
        self,
        subcategorias: List,
        caminho_pai: str
    ) -> List[Dict]:
        """
        Coleta produtos de subcategorias de forma recursiva.
        """
        produtos = []

        for subcategoria in subcategorias:
            caminho = f"{caminho_pai} > {subcategoria.nome}"

            for produto in subcategoria.produtos:
                produtos.append({
                    "produto": produto,
                    "categoria": caminho,
                    "nivel": "subcategoria"
                })

            if hasattr(subcategoria, "subcategorias") and subcategoria.subcategorias:
                produtos.extend(
                    self._coletar_produtos_subcategorias(
                        subcategoria.subcategorias,
                        caminho
                    )
                )

        return produtos

    def gerar_relatorio_performance(self) -> dict:
        """
        Gera relatório sobre a árvore AVL:
        - total de categorias
        - altura da árvore
        - balanceamento
    Inclui estimativa da complexidade Big O para cada métrica.
    """
    # ===== Funções auxiliares =====
        def calcular_altura(no):
            # Percorre todos os nós recursivamente: O(n)
            if no is None:
                return 0
            return 1 + max(calcular_altura(no.esquerda), calcular_altura(no.direita))

        def verificar_balanceamento(no):
        # Percorre todos os nós recursivamente: O(n)
            if no is None:
                return True
            fb = self.arvore.fator_balanceamento(no)
            if fb < -1 or fb > 1:
                return False
            return verificar_balanceamento(no.esquerda) and verificar_balanceamento(no.direita)
            

    # ===== Coleta métricas =====
        total_categorias = self.arvore.get_tamanho()  # O(1)
        altura_arvore = calcular_altura(self.arvore.raiz)  # O(n)
        balanceada = verificar_balanceamento(self.arvore.raiz)  # O(n)

    # ===== Complexidade estimada =====
        complexidade = {
            "total_categorias": "O(1) (consulta direta ao atributo tamanho)",
            "altura_arvore": "O(n) (percorrer todos os nós)",
            "balanceada": "O(n) (verificar fator de balanceamento de todos os nós)"
    }

        return {
            "total_categorias": total_categorias,
            "altura": altura_arvore,
            "balanceada": balanceada,
            "complexidade": complexidade
    }


    def reindexar(self):
        """
        Reconstrói os índices após modificações na árvore.
        """
        self.logger.warning("Reindexando produtos...")
        self._construir_indices()