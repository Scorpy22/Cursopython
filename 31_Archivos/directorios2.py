from pathlib import Path, PureWindowsPath

carpeta = Path('C:\\Users\\jessy\\Documents\\Cursopython\\31_Archivos\\otra_carpeta') #obtener la ruta

ruta_windows = PureWindowsPath(carpeta) #determina como debe ir los directoriso
print(ruta_windows)
#validar si existe la carpeta
if not carpeta.exists():
  print("Este archivo no existe")
else:
  print("Genial, existe")