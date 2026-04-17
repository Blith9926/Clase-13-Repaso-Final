from datetime import date

def ingresar_ventas():
    """Función para ingresar nuevas ventas y guardar los datos en un archivo CSV."""
    Ventas = []
    fecha = ""
    cliente = ""
    while True:
        try:
            producto = input("Ingrese el nombre del producto: ").upper()
            cantidad = int(input("Ingrese la cantidad vendida: "))
            precio = float(input("Ingrese el precio por unidad: "))
            if fecha == "" or cliente =="":
                fecha = date.strptime(input("Ingrese la fecha de la venta YYYY-MM-DD: "), "%Y-%m-%d")
                cliente = input("Ingrese el nombre del cliente: ")
            
            #Validacion de datos
            if cantidad <=0:
                print("🚫 La cantidad debe ser positiva.")
                continue
            if precio <0:
                print("🚫 El precio debe ser positivo.")
                continue
        except ValueError:
            print("🚫Entrada no valida, ingrese los datos correctos")
            continue
        
        #Crear un diccionario con lo0s datos de la venta
        venta = {
            "Producto": producto,
            "Cantidad": cantidad,
            "Precio": precio,
            "Fecha": fecha,
            "Cliente": cliente,
        }
        
        Ventas.append(venta)
        continuar = input("Desea ingresar otra venta? (Si/No): ").lower()
        if continuar != "Si":
            print("Guardando en ventas.csv...")
            
            print("\n-- Ticket de Venta --")
            for venta in Ventas:
                print(f"Producto: {venta['Producto']}")
                print(f"Cantidad: {venta['Cantidad']}")
                print(f"Precio: ${venta['Precio']:.2f}")
                print(f"Fecha: {venta['Fecha']}")
                print(f"Cliente: {venta['Cliente']}")
                print("-" * 30)


            print("""Subtotal: ${:.2f}""".format(sum(v["Cantidad"] * v["Precio"] for v in Ventas)))
            print("""IVA (13%): ${:.2f}""".format(sum(v["Cantidad"] * v["Precio"] for v in Ventas) * IVA))
            print(
                "Total a pagar: ${:.2f}".format(
                    sum(v["Cantidad"] * v["Precio"] for v in Ventas)
                )
            )
            break

if __name__ == "__main__":
    ingresar_ventas()