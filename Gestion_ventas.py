from datetime import date
import csv
import pandas as pd

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
        continuar = input("Desea ingresar otra venta? (s/n): ").lower()
        if continuar != "s":
            if not guardar_ventas_csv(Ventas):
                print("Ingrese los productos de nuevo.")
                break
        
        
            print("\n-- Ticket de Venta --")
            print(f"Cliente: {Ventas[0]['Cliente']} | Fecha: {Ventas[0]['Fecha']} ")
            for venta in Ventas:
                # Imprime los detalles de cada venta ingresada en un sola linea con formato de ticket
                print("-" * 30)
                print(f"Producto: {venta['Producto']} | Cantidad: {venta['Cantidad']} | Precio: ₡{venta['Precio']:.2f}")

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

def guardar_ventas_csv(Ventas):
    
    
    """Funcion para guardar las ventas en CSV."""
    ARCHIVO_CSV = "Ventas.csv"
    if not (Ventas):
        print("No hay ninguna venta.")
        return False
    try:
        #Abrir  el archivo CSV en modo escritura y guardar las ventas utilizando csv.DictWriter
        with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
            campos = ["Producto", "Cantidad", "Precio", "Fecha", "Cliente"]
            writer = csv.DictWriter(archivo, fieldnames=campos)
            if archivo.tell() == 0:  # Si el archivo está vacío, escribir la cabecera
                writer.writeheader()
            for venta in Ventas:
                writer.writerow(venta)
            print(f"Ventas guardadas exitosamente en {ARCHIVO_CSV}")
            return True

        
        
    except Exception as e:
        print(f"Error al guardar los datos al archivo CSV: {e}")
        return False

def cargar_ventas(archivo_csv="ventas.csv"):
    """Función para cargar las ventas desde un archivo CSV"""
    try:
        ventas = pd.read_csv(archivo_csv)
        print(f"Ventas cargadas exitosamente {len(ventas)} desde {archivo_csv}")
        return ventas
    except FileNotFoundError:
        print(f"Archivo {archivo_csv} no encontrado.")
        return None
    except Exception as e:
        print(f"Error al cargar los datos del archivo CSV: {e}")
        return None

if __name__ == "__main__":
    ingresar_ventas()