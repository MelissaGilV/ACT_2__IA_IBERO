"""
Archivo de pruebas para el Sistema de Búsqueda de Rutas
"""

from sistema_transporte import (
    inicializar_sistema_transmilenio,
    BuscadorRutas,
    BaseConocimiento,
    Estacion,
    TipoTransporte,
    Conexion
)


def prueba_busqueda_basica():
    """Prueba básica de búsqueda de rutas"""
    print("\n" + "="*60)
    print("PRUEBA 1: Búsqueda básica")
    print("="*60)
    
    bc = inicializar_sistema_transmilenio()
    buscador = BuscadorRutas(bc)
    
    origen = "Portal Norte"
    destino = "Centro"
    
    print(f"\nBuscando ruta de '{origen}' a '{destino}'...")
    ruta = buscador.buscar_mejor_ruta(origen, destino, 'a_estrella')
    
    assert ruta is not None, "La ruta debería existir"
    assert origen in ruta.estaciones, "El origen debe estar en la ruta"
    assert destino in ruta.estaciones, "El destino debe estar en la ruta"
    
    print(f"[OK] Ruta encontrada: {' -> '.join(ruta.estaciones)}")
    print(f"[OK] Tiempo: {ruta.tiempo_total} minutos")
    print(f"[OK] Costo: ${ruta.costo_total:,.0f} COP")
    print("[OK] Prueba exitosa")


def prueba_busqueda_con_transbordos():
    """Prueba de búsqueda con transbordos"""
    print("\n" + "="*60)
    print("PRUEBA 2: Búsqueda con transbordos")
    print("="*60)
    
    bc = inicializar_sistema_transmilenio()
    buscador = BuscadorRutas(bc)
    
    origen = "Portal Sur"
    destino = "Portal Suba"
    
    print(f"\nBuscando ruta de '{origen}' a '{destino}'...")
    ruta = buscador.buscar_mejor_ruta(origen, destino, 'a_estrella')
    
    assert ruta is not None, "La ruta debería existir"
    
    print(f"[OK] Ruta encontrada: {' -> '.join(ruta.estaciones)}")
    print(f"[OK] Transbordos: {len(ruta.transbordos)}")
    if ruta.transbordos:
        print(f"[OK] Estaciones de transbordo: {', '.join(ruta.transbordos)}")
    print("[OK] Prueba exitosa")


def prueba_comparacion_algoritmos():
    """Compara resultados entre A* y BFS"""
    print("\n" + "="*60)
    print("PRUEBA 3: Comparación de algoritmos")
    print("="*60)
    
    bc = inicializar_sistema_transmilenio()
    buscador = BuscadorRutas(bc)
    
    origen = "Terminal Norte"
    destino = "Bosa"
    
    print(f"\nBuscando ruta de '{origen}' a '{destino}'...")
    
    ruta_a_estrella = buscador.buscar_mejor_ruta(origen, destino, 'a_estrella')
    ruta_bfs = buscador.buscar_mejor_ruta(origen, destino, 'anchura')
    
    assert ruta_a_estrella is not None, "A* debería encontrar una ruta"
    assert ruta_bfs is not None, "BFS debería encontrar una ruta"
    
    print("\n--- Algoritmo A* ---")
    print(f"Ruta: {' -> '.join(ruta_a_estrella.estaciones)}")
    print(f"Tiempo: {ruta_a_estrella.tiempo_total} minutos")
    print(f"Costo: ${ruta_a_estrella.costo_total:,.0f} COP")
    
    print("\n--- Algoritmo BFS ---")
    print(f"Ruta: {' -> '.join(ruta_bfs.estaciones)}")
    print(f"Tiempo: {ruta_bfs.tiempo_total} minutos")
    print(f"Costo: ${ruta_bfs.costo_total:,.0f} COP")
    
    print("[OK] Prueba exitosa")


def prueba_reglas_logicas():
    """Prueba de aplicación de reglas lógicas"""
    print("\n" + "="*60)
    print("PRUEBA 4: Aplicación de reglas lógicas")
    print("="*60)
    
    bc = inicializar_sistema_transmilenio()
    
    # Probar regla de misma línea
    print("\n--- Regla: Conexión misma línea ---")
    resultado = bc._misma_linea("Portal Norte", "Calle 100")
    print(f"Portal Norte y Calle 100 en misma línea: {resultado}")
    assert resultado == True, "Deberían estar en la misma línea"
    
    resultado = bc._misma_linea("Portal Norte", "Portal Sur")
    print(f"Portal Norte y Portal Sur en misma línea: {resultado}")
    assert resultado == False, "No deberían estar en la misma línea"
    
    # Probar regla de transferencia
    print("\n--- Regla: Estación de transferencia ---")
    estacion = bc.estaciones["Calle 72"]
    es_transferencia = 'transferencia' in estacion.servicios
    print(f"Calle 72 es estación de transferencia: {es_transferencia}")
    assert es_transferencia == True, "Calle 72 debería ser transferencia"
    
    print("[OK] Prueba exitosa")


def prueba_heuristica():
    """Prueba de función heurística"""
    print("\n" + "="*60)
    print("PRUEBA 5: Función heurística")
    print("="*60)
    
    bc = inicializar_sistema_transmilenio()
    buscador = BuscadorRutas(bc)
    
    h1 = buscador.heuristica("Portal Norte", "Centro")
    h2 = buscador.heuristica("Portal Norte", "Calle 100")
    h3 = buscador.heuristica("Portal Norte", "Portal Norte")
    
    print(f"\nHeuristica Portal Norte -> Centro: {h1:.2f}")
    print(f"Heuristica Portal Norte -> Calle 100: {h2:.2f}")
    print(f"Heuristica Portal Norte -> Portal Norte: {h3:.2f}")
    
    assert h3 == 0, "La heuristica a si misma debe ser 0"
    assert h2 < h1, "La distancia a Calle 100 debe ser menor que a Centro"
    
    print("[OK] Prueba exitosa")


def prueba_rutas_inexistentes():
    """Prueba de manejo de rutas que no existen"""
    print("\n" + "="*60)
    print("PRUEBA 6: Rutas inexistentes")
    print("="*60)
    
    bc = inicializar_sistema_transmilenio()
    buscador = BuscadorRutas(bc)
    
    # Estación que no existe
    ruta = buscador.buscar_mejor_ruta("EstacionInexistente", "Centro", 'a_estrella')
    assert ruta is None, "No debería encontrar ruta desde estación inexistente"
    print("[OK] Manejo correcto de estacion inexistente")
    
    print("[OK] Prueba exitosa")


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas"""
    print("\n" + "="*60)
    print("SUITE DE PRUEBAS - Sistema de Búsqueda de Rutas")
    print("="*60)
    
    pruebas = [
        prueba_busqueda_basica,
        prueba_busqueda_con_transbordos,
        prueba_comparacion_algoritmos,
        prueba_reglas_logicas,
        prueba_heuristica,
        prueba_rutas_inexistentes,
    ]
    
    exitosas = 0
    fallidas = 0
    
    for prueba in pruebas:
        try:
            prueba()
            exitosas += 1
        except AssertionError as e:
            print(f"\n[ERROR] Error en {prueba.__name__}: {e}")
            fallidas += 1
        except Exception as e:
            print(f"\n[ERROR] Excepcion en {prueba.__name__}: {e}")
            fallidas += 1
    
    print("\n" + "="*60)
    print("RESUMEN DE PRUEBAS")
    print("="*60)
    print(f"Pruebas exitosas: {exitosas}")
    print(f"Pruebas fallidas: {fallidas}")
    print(f"Total: {len(pruebas)}")
    print("="*60)


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()

