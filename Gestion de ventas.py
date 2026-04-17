from datetime import date

def ingresar_ventas():
    """Función para ingresar nuevas ventas y guardar los datos en un archivo CSV."""
    Ventas = []
    IVA = 0.13  # Tasa de IVA del 13%
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
        continuar = input("Desea ingresar otra venta? (n/n): ").lower()
        if continuar != "s":
            print("Guardando en ventas.csv...")
            
            print("\n-- Ticket de Venta --")
            print(f"Cliente: {Ventas[0]['Cliente']} | Fecha: {Ventas[0]['Fecha']} ")
            for venta in Ventas:
                # Imprime los detalles de cada venta ingresada en un sola linea con formato de ticket
                print("-" * 30)
                print(
                    f"Producto: {venta['Producto']} | Cantidad: {venta['Cantidad']} | Precio: ₡{venta['Precio']:.2f}"
                )

            subtotal = sum(
                v["Cantidad"] * v["Precio"] for v in Ventas
            )  # Calcula el subtotal sumando el precio total de cada venta (cantidad * precio)
            iva = (
                subtotal * IVA
            )  # Calcula el IVA multiplicando el subtotal por la tasa de IVA (13%)
            print("""Subtotal: ₡{:.2f}""".format(subtotal))
            print("""IVA (13%): ₡{:.2f}""".format(iva))
            print("Total a pagar: ₡{:.2f}".format(subtotal + iva))
            break

if __name__ == "__main__":
    ingresar_ventas()