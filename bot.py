from datetime import datetime

def registrar_alerta(porcentaje, direccion, activo="PAXG"):
    # Obtiene la fecha, hora y minuto exacto actual
    tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Crea el mensaje detallando si fue alcista o bajista
    mensaje = f"[{tiempo_actual}] Señal detectada en {activo}: {porcentaje}% - {direccion}\n"
    
    # Guarda la línea automáticamente en el archivo de texto del repositorio
    with open("historial_senales.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje)
    print(f"Registrado: {mensaje.strip()}")

# --- AQUÍ IRÁ TU LÓGICA DE MERCADO ---
# Ejemplo de prueba (puedes adaptarlo cuando tengas tu lógica real)
porcentaje_actual = 70 
tendencia = "Alcista" # O "Bajista"

if porcentaje_actual >= 70:
    registrar_alerta(porcentaje_actual, tendencia)
