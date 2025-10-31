from typing import List


class Categoria:
    
    # Inicialização da categoria
    def __init__(self, nome: str, produtos: List[str] = None, peso_popularidade: float = 1.0):
        self.nome = nome
        self.produtos = produtos if produtos is not None else []
        self.subcategorias: List['Categoria'] = []
        self.peso_popularidade = peso_popularidade
    
    # Gerenciamento de produtos
    
    # Adiciona produto à categoria
    def adicionar_produto(self, produto: str) -> None:
        if produto not in self.produtos:
            self.produtos.append(produto)
    
    # Remove produto da categoria
    def remover_produto(self, produto: str) -> bool:
        if produto in self.produtos:
            self.produtos.remove(produto)
            return True
        return False
    
    # Adiciona subcategoria
    def adicionar_subcategoria(self, subcategoria: 'Categoria') -> None:
        if subcategoria not in self.subcategorias:
            self.subcategorias.append(subcategoria)
    
    # Retorna total de produtos
    def get_total_produtos(self) -> int:
        return len(self.produtos)
    
    # Métodos de representação
    
    # Representação em string
    def __str__(self) -> str:
        return f"Categoria({self.nome}, {len(self.produtos)} produtos)"
    
    # Representação oficial
    def __repr__(self) -> str:
        return self.__str__()
    
    # Métodos de comparação
    
    # Comparação de igualdade
    def __eq__(self, other) -> bool:
        if isinstance(other, Categoria):
            return self.nome == other.nome
        return False
    
    # Comparação menor que
    def __lt__(self, other) -> bool:
        if isinstance(other, Categoria):
            return self.nome < other.nome
        return NotImplemented
    
    # Comparação maior que
    def __gt__(self, other) -> bool:
        if isinstance(other, Categoria):
            return self.nome > other.nome
        return NotImplemented
    
    # Comparação menor ou igual
    def __le__(self, other) -> bool:
        if isinstance(other, Categoria):
            return self.nome <= other.nome
        return NotImplemented
    
    # Comparação maior ou igual
    def __ge__(self, other) -> bool:
        if isinstance(other, Categoria):
            return self.nome >= other.nome
        return NotImplemented
