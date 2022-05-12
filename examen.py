import pandas as pd

def dataset_conversiones():
  datos1 = pd.read_csv('conversiones(4).csv',sep=';')
  return datos1
print(dataset_conversiones())
def dataset_navegacion():
  datos2 = pd.read_csv('navegacion(4).csv',sep=';')
  return datos2
print(dataset_navegacion())

def separar_datos(URL):
  campaña = []
  adgroup = []
  advertisement = []
  site_link = []
  for url in URL:
    try:
      x = str(url).split('camp=')
      y = (x[1].split('&'))
      campaña.append(y[0])
    except:
      campaña.append(0)
  for url in URL:
    try:
      x = str(url).split('adg=')
      y = (x[1].split('&'))
      adgroup.append(y[0])
    except:
      adgroup.append(0)
  for url in URL:
    try:
      x = str(url).split('ad=')
      y = (x[1].split('&'))
      advertisement.append(y[0])
    except:
      advertisement.append(0)
  for url in URL:
    try:
      x = str(url).split('sl=')
      y = (x[1].split('&'))
      site_link.append(y[0])
    except:
      site_link.append(0)

def identificar_datos_repetidos():
  navegacion_ = pd.read_csv('navegacion',sep = ';')
  navegacion_ = navegacion_.drop_duplicates(subset=['id_user,gclid','uuid',keep='first'])
  navegacion_.to_csv('navegacion_.csv',sep=';')
Eliminar_datos()

def ordenar_datos():
  