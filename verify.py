from app.core.categoria import Categoria
import inspect, os

print("Arquivo:", inspect.getfile(Categoria))
print("Métodos:", [m for m in dir(Categoria) if not m.startswith("_")])