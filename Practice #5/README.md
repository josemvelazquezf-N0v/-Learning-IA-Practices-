# Indicaciones
## Realizar un simulador Árbol de Máximo y Mínimo coste Kruskal.
    En consola que muestre paso a paso es lo mínimo, si logran parte gráfica puntitos extras.

## Parte Teórica
### ¿Qué es?

    Un Árbol de Mínimo Coste (o Árbol de Expansión Mínima, MST por sus siglas en inglés) es una estructura que conecta todos los nodos de un grafo usando la menor suma total de pesos posible y sin formar ciclos.

    Un Árbol de Máximo Coste es exactamente lo mismo… pero en lugar de buscar las aristas más ligeras, selecciona las más pesadas, obteniendo el árbol con el mayor costo total posible sin ciclos.

#### El algoritmo de Krustal funciona de la siguente manera:
    Toma las aristas en orden (ascendente si buscas mínimo, descendente si buscas máximo), y únelas siempre y cuando no formen un ciclo.

### ¿Para qué sirve?

    Los Árboles de Mínimo o Máximo Coste sirven para conectar puntos de la forma más barata (o más cara) posible, evitando redundancias.

    Se aplican en muchísimos campos:

    1. Redes físicas

    Construcción de carreteras entre ciudades.

    Redes eléctricas (tendido de cables).

    Redes de tubería o fibra óptica.

    Redes de telefonía.

    Ahí normalmente se usa árbol de mínimo coste, porque queremos gastar lo menos posible para conectar todo.

    2. Sistemas de comunicación y computación

    Diseño eficiente de routers.

    Interconexión entre servidores.

    Redes inalámbricas (WiFi mesh networks).

    Sirve para garantizar que todos los nodos estén comunicados con el mínimo de interferencia o costo de transmisión.

    3. Visualización y clustering

    Agrupación de datos.

    Segmentación de imágenes.

    Aquí a veces se usa máximo coste para asegurar que las conexiones más fuertes permanezcan.

    4. Robótica y navegación

    Ideal para:

    Calcular estructuras eficientes de caminos.

    Mapas topológicos donde los nodos representan zonas.

    Reducción de rutas posibles para análisis más rápido.

    5. Gestión de almacenes, logística y rutas (TU PROYECTO)

    En tu robot almacenista, Kruskal entra así:

    Tu almacén es un grafo:
    cada pasillo = nodo,
    cada conexión entre pasillos = arista con un "costo" (tiempo, distancia o congestionamiento).

    Puedes construir un árbol de mínimo coste para:
    ✔ definir la estructura mínima de movilidad
    ✔ evitar rutas redundantes
    ✔ optimizar la exploración inicial del mapa
    ✔ simplificar el grafo antes de aplicar algoritmos como A*, Dijkstra o decision networks

    También puedes usar un árbol de máximo coste para:
    ✔ identificar las conexiones más “difíciles” o más largas
    ✔ detectar zonas alejadas o costosas donde el robot debe evitar rutas innecesarias

    ### ¿Cómo se implementa en el mundo?

    1. Ingeniería civil e infraestructura

    Las empresas constructoras utilizan modelos de grafo para planear la red de caminos más económica entre ciudades.
    Kruskal se usa para:

    elegir qué carreteras construir primero

    minimizar el presupuesto

    evitar trazos innecesarios

    2. Redes eléctricas

    Las empresas de energía usan Kruskal para decidir:

    cómo conectar postes o subestaciones con el menor cable posible

    cómo evitar ciclos que generen pérdidas de energía

    3. Diseño de circuitos y chips

    Kruskal se usa para:

    optimizar distribución de pistas internas

    reducir interferencias

    minimizar distancia entre componentes

    4. Telecomunicaciones

    En redes como:

    telefonía móvil

    repetidores inalámbricos

    satélites
    …se diseña la red usando MST para minimizar el costo de conectividad.

    5. Empresas de logística (Amazon, UPS, DHL)

    Se usa para:

    planear layouts de almacenes

    mejorar rutas internas de robots móviles (parecido a tu proyecto)

    reducir costos entre puntos de distribución

    6. Robótica móvil real (Tu contexto)

    Un robot móvil (como tu robot almacenista) usa un grafo del ambiente.
    Kruskal se utiliza para:

    Crear un mapa estructurado de forma óptima
    sin conexiones redundantes ni caminos innecesarios.

    Reducir el grafo original que puede tener cientos de conexiones, dejándolo en una estructura limpia que optimiza la toma de decisiones.

    Preprocesar el mapa para que luego tu robot ejecute planificación de rutas
    (A*, Dijkstra, algoritmos probabilísticos, etc.) en un grafo mucho más ligero.

### ¿Cómo lo implementarías en tu vida?

### ¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño?