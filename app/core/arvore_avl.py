from core.categoria import Categoria

class No:
    def __init__(self, categoria: Categoria):
        self.categoria = categoria
        self.esquerda = None
        self.direita = None
        self.altura = 1  # altura da folha é 1

class ArvoreAVL:
    def obter_altura(self, no):
        return no.altura if no else 0

    def atualizar_altura(self, no):
        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))

    def fator_balanceamento(self, no):
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita) if no else 0

    # Rotações
    def rotacao_direita(self, no):
        nova_raiz = no.esquerda
        no.esquerda = nova_raiz.direita
        nova_raiz.direita = no
        self.atualizar_altura(no)
        self.atualizar_altura(nova_raiz)
        return nova_raiz

    def rotacao_esquerda(self, no):
        nova_raiz = no.direita
        no.direita = nova_raiz.esquerda
        nova_raiz.esquerda = no
        self.atualizar_altura(no)
        self.atualizar_altura(nova_raiz)
        return nova_raiz

    # Inserção
    def inserir(self, no, categoria: Categoria):
        if not no:
            return No(categoria)
        if categoria.nome < no.categoria.nome:
            no.esquerda = self.inserir(no.esquerda, categoria)
        elif categoria.nome > no.categoria.nome:
            no.direita = self.inserir(no.direita, categoria)
        else:
            # Chave duplicada: apenas retorna o nó existente
            return no

        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)

        # Casos de rotação
        if fb > 1 and categoria.nome < no.esquerda.categoria.nome:
            return self.rotacao_direita(no)
        if fb < -1 and categoria.nome > no.direita.categoria.nome:
            return self.rotacao_esquerda(no)
        if fb > 1 and categoria.nome > no.esquerda.categoria.nome:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if fb < -1 and categoria.nome < no.direita.categoria.nome:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no  # Retorno corrigido

    # Remoção
    def menor_valor(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def remover(self, no, nome: str):
        if not no:
            return no

        if nome < no.categoria.nome:
            no.esquerda = self.remover(no.esquerda, nome)
        elif nome > no.categoria.nome:
            no.direita = self.remover(no.direita, nome)
        else:
            # Nó com 1 ou nenhum filho
            if not no.esquerda:
                return no.direita
            elif not no.direita:
                return no.esquerda
            # Nó com dois filhos
            temp = self.menor_valor(no.direita)
            no.categoria = temp.categoria
            no.direita = self.remover(no.direita, temp.categoria.nome)

        if not no:
            return no

        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)

        # Rebalanceamento
        if fb > 1 and self.fator_balanceamento(no.esquerda) >= 0:
            return self.rotacao_direita(no)
        if fb > 1 and self.fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)
        if fb < -1 and self.fator_balanceamento(no.direita) <= 0:
            return self.rotacao_esquerda(no)
        if fb < -1 and self.fator_balanceamento(no.direita) > 0:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    # Percursos
    def em_ordem(self, no, resultado=None):
        if resultado is None:
            resultado = []
        if no:
            self.em_ordem(no.esquerda, resultado)
            resultado.append((no.categoria.nome, no.altura))
            self.em_ordem(no.direita, resultado)
        return resultado

    def pre_ordem(self, no, resultado=None):
        if resultado is None:
            resultado = []
        if no:
            resultado.append((no.categoria.nome, no.altura))
            self.pre_ordem(no.esquerda, resultado)
            self.pre_ordem(no.direita, resultado)
        return resultado