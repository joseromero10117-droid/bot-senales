from datetime import datetime
import re

def actualizar_html(tiempo, porcentaje, direccion, activo="PAXG"):
    try:
        # Lee el contenido actual del índice.html en español
        with open("índice.html", "r", encoding="utf-8") as f:
            contenido = f.read()
        
        # Crea la nueva fila para la tabla del historial en el HTML
        color_clase = "text-emerald-400" if direccion.lower() == "alcista" else "text-red-400"
        nueva_fila = f"""
            <tr class="border-b border-gray-800 hover:bg-darkBg/50">
                <td class="py-3 px-4 text-gray-300">{tiempo}</td>
                <td class="py-3 px-4 font-semibold text-accentGold">{activo}</td>
                <td class="py-3 px-4 font-bold text-gray-100">{porcentaje}%</td>
                <td class="py-3 px-4 font-bold {color_clase}">{direccion}</td>
            </tr>
        """
        
        # Inserta la nueva señal justo en el marcador de la tabla dentro del índice.html
        if "<!-- SEÑALES_INJECT_POINT -->" in contenido:
            contenido = contenido.replace("<!-- SEÑALES_INJECT_POINT -->", nueva_fila + "\n<!-- SEÑALES_INJECT_POINT -->")
        else:
            # Respaldo si no encuentra el marcador exacto
            contenido = contenido.replace("</body>", f"""
            <div id="historial-emergencia" style="display:none;">{nueva_fila}</div>
            </body>
            """)

        # Guarda los cambios de vuelta en el índice.html
        with open("índice.html", "w", encoding="utf-8") as f:
            f.write(contenido)
            
        print("Historial HTML (índice.html) actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar el HTML: {e}")

# --- LÓGICA DE DETECCIÓN DE SEÑAL ---
# Obtiene la fecha y hora exacta (hora y minuto)
tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M")

# Condición de ejemplo (puedes ajustarla a tu estrategia real de análisis)
porcentaje_actual = 70 
tendencia = "Alcista" # Cambiar a "Bajista" según corresponda
activo_mercado = "PAXG"

if porcentaje_actual >= 70:
    actualizar_html(tiempo_actual, porcentaje_actual, tendencia, activo_mercado)
