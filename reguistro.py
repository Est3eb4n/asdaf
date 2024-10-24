from datetime import datetime
import json

def menu():
            print("""
        ===========================================
        ============ Menu inventario ==============
        =                                         =
        =   1. Registrar Atleta                   =
        =   2. Registo de records                 =
        =   3. Reporte del ranking                =
        =   4. Historial del atleta               =
        =   5. Salir                              =
        =                                         =
        ===========================================
             """)

def creacion():
  
  reguistro_deportistas={
    "codigo_atleta": int(input("ingrece codigo: ")),
    "nombre_atleta": input("indique nombre del atleta: "),
    "genero": input("genero: "),
    "ciudad": input("Ciudad: "),
  }

  deportistas = None
  try:  # se crea un try
    file = open('registro_atletas.json', 'r')  
    deportistas = json.load(file)   
    file.close        
  except Exception as error:  
       deportistas = []   
  deportistas.append(reguistro_deportistas) 
  file = open('registro_atletas.json', 'w')
  json.dump(deportistas,file,indent=4) 
  file.close
#___________________________________________________________________________________________________________________________________________________________
def registro_de_records():
     
 
    records=open('registro_atletas.json','r')
    
   
    codigo = int(input('ingrese el codigo el atleta: '))
    for atleta in records:
        if atleta == codigo:
          nombre_de_competencia = input('ingrese el nombre de la competencia: ')
          tiempo_reguistrado = input('indique el tiempo reguistrado: ')
          fecha = datetime.today().strftime("%Y-%m-%d %H:%m:%s")

          if 'record'not in atleta:
              atleta['record'] = {}
              atleta['record'] = {
                "nombre_de_competencia": nombre_de_competencia,
                "tiempo_reguistrado": tiempo_reguistrado,
                "fecha": datetime.today().strftime("%Y-%m-%d %H:%m:%s"),
              }
    

    records = None
    try:
      file= open('reguistro_de_los_records.json', 'r')
      records = json.load(file)
      file.close
    except Exception as error:
        records = []

    records.append(atleta)
    records = open('reguistro_de_los_records.json', 'w')
    json.dump(atleta,records,indent=4)
    records.close