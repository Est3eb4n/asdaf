
from reguistro import menu
from reguistro import creacion
from reguistro import registro_de_records



while True:

    print("""
        Bienvenido a ACME SAS

        Porfavor escoja una de la siguientes opcciones
        """)
    menu()
    opc = input(" => ")

    if opc == "1":
        creacion()
    elif opc == "2":
        registro_de_records()
    # elif opc == "3":
    #     bonos()
    # elif opc == "4":
    #     buscar()
    # elif opc == "5":
    #     historico()
    # elif opc == "6":
    #     reporte()    
    # elif opc == "7":
    #     historico()