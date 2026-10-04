from datetime import datetime
import requests

def actualizar_html(tiempo, porcentaje, direccion, activo="PAXG"):
    try:
        with open("índice.html", "r", encoding="utf-8") as f:
            contenido = f.read()
        
        color_clase = "text-emerald-400" if direccion.lower() == "alcista" else "text-red-400"
        nueva_fila = f"""
            <tr class="border-b border-gray-800 hover:bg-darkBg/50">
                <td class="py-3 px-4 text-gray-300">{tiempo}</td>
                <td class="py-3 px-4 font-semibold text-accentGold">{activo}</td>
                <td class="py-3 px-4 font-bold text-gray-100">{porcentaje}%</td>
                <td class="py-3 px-4 font-bold {color_clase}">{direccion}</td>
            </tr>
        """
        
        if "<!-- SEÑALES_INJECT_POINT -->" in contenido:
            contenido = contenido.replace("<!-- SEÑALES_INJECT_POINT -->", nueva_fila + "\n<!-- SEÑALES_INJECT_POINT -->")
            with open("índice.html", "w", encoding="utf-8") as f:
                f.write(contenido)
            print("Señal del 51%+ registrada correctamente.")
            
    except Exception as e:
        print(f"Error: {e}")

# --- LÓGICA DE PRUEBA (>= 51%) ---
try:
    url_depth = "https://api.binance.com/api/v3/depth?symbol=PAXGUSDT&limit=50"
    response = requests.get(url_depth)
    data = response.json()
    
    total_bids = sum(float(bid[1]) for bid in data.get('bids', []))
    total_asks = sum(float(ask[1]) for ask in data.get('asks', []))
    total_sum = total_bids + total_asks
    
    bids_percent = round((total_bids / total_sum) * 100)
    asks_percent = 100 - bids_percent
    
    if bids_percent >= asks_percent:
        porcentaje_actual = bids_percent
        tendencia = "Alcista"
    else:
        porcentaje_actual = asks_percent
        tendencia = "Bajista"
        
    # FILTRO DE PRUEBA: 51% o más
    if porcentaje_actual >= 51:
        tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
        actualizar_html(tiempo_actual, porcentaje_actual, tendencia, "PAXG")
    else:
        print(f"Porcentaje actual ({porcentaje_actual}%) por debajo del 51%.")

except Exception as e:
    print(f"Error de conexión: {e}")
