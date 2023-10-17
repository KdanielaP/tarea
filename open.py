from distutils import archive_util
import openpyxl
import datetime
def main():
    # Crea un archivo Excel llamado "informe_gastos.xlsx" con una hoja de cálculo llamada "Gastos".
    archivo_excel ="./excel/gastos.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Gastos"
    # Crea un programa en Python que solicite al usuario ingresar detalles de gastos, como la fecha, la descripción y el monto del gasto. El programa debe permitir al usuario ingresar múltiples gastos.
    gastos = []
    while True:
        fecha = input("Fecha (dd/mm/aaaa): ")
        descripcion = input("Descripción: ")
        monto = float(input("Monto: "))
        gastos.append([fecha, descripcion, monto])
        continuar = input("¿Desea continuar ingresando gastos? (s/n): ")
        if continuar == "n":
            break
    # Utiliza la biblioteca `openpyxl` para guardar los datos de los gastos en el archivo Excel. Cada gasto debe almacenarse en una fila separada en la hoja de cálculo.
    for gasto in gastos:
        ws.append(gasto)
    # Una vez que el usuario haya ingresado todos los gastos, el programa debe calcular el total de gastos y mostrar un resumen en la consola.
    total_gastos = 0
    for gasto in gastos:
        total_gastos += gasto[2]
    print("Resumen de gastos:")
    print("Número total de gastos:", len(gastos))
    max_gasto = max(gastos, key=lambda x: x[2])
    print("Fecha y descripción del gasto más caro:", max_gasto[0], max_gasto[1])
    min_gasto = min(gastos, key=lambda x: x[2])
    print("Fecha y descripción del gasto más barato:", min_gasto[0], min_gasto[1])
    print("Monto total de gastos:", total_gastos)
    # 
    # Guarda el informe de gastos en el archivo Excel "informe_gastos.xlsx" y muestra un mensaje indicando que se ha completado la tarea.
    wb_save =("informe_gastos.xlsx")
    print ("El informe de gastos se ha guardado en el archivo 'informe_gastos.xlsx'.")
def new_func():
    archive_excel=()
if __name__ == "__main__":
    main()

    