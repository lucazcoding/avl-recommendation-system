import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f'Tempo de execução: {fim - inicio:.4f}s')
        return resultado
    return wrapper
