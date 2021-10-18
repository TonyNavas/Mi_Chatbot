from nltk.chat.util import Chat, reflections

pares = [
    [
    r"(.*)hola(.*)",
    ["Bienvenido, ¿como puedo ayudarte?"]
    ],
    [
        r"(.*)como te llamas?(.*)",
        ["Mi nombre es chatbot"]
    ],
    [
        r"(.*)dime los servicios(.*)",
        ["Los servicios que ofresemos son:\n"
         "1 - Productos electronicos,\n"
         "2 - Pago de facturas,\n"
         "3 - Reconexión de servicios,\n"
         "4 - Promociones,\n"
         "5 - Atención al cliente\n"
         "¿Te interesa alguno?"]
    ],
    [
        r"(.*)productos electronicos(.*)",
        ["Tenemos productos como:\n"
         "Routers inalambricos,\n"
         "WiFi móvil,\n"
         "Conmutadores,\n"
         "probador de cables"]
    ],
    [
        r"(.*)routers inalambricos(.*)",
        ["Este es un dispositivo que convierte tu conexión entrante"
        "(cable coaxial, línea telefónica, línea de fibra óptica u otra entrada) "
        "en una conexión Ethernet, lo que permite que tu router Wi-Fi se conecte a Internet."]
    ],
    [
        r"(.*)wifi movil(.*)",
        ["Este WiFi portátil funciona de una manera muy similar a un router WiFi común."
         " Es decir, toman la señal de la red móvil más cercana a la que se pueda conectar"
         " su tarjeta SIM, y mediante la creación de una red WiFi la distribuirán haciendo"
         " exactamente las mismas funciones que un router."]
    ],
    [
        r"(.*)conmutadores(.*)",
        ["Estos conmutadores son dispositivos que se utilizan cuando quieras conectar múltiples tramos de una red"
         ", fusionándolos en una sola red."]
    ],
    [
        r"(.*)probador de cables(.*)",
        ["El Network Cable Tester nos permite comprobar los cables de nuestra red de una manera bastante fácil."
         " Solo deberemos conectar cada extremo del cable a cada una de las partes del tester y este nos indicará cual es el fallo "
         "de ese cable, si lo tiene, claro"]
    ],
    [
        r"(.*)pago de facturas(.*)",
        ["Para realizar el pago de las facturas puedes visitar nuestra pagina web www.ejemplo.com"]
    ],
    [
        r"(.*)reconexion de servicios(.*)",
        ["Se hace reconexion de conectores y fibra optica"]
    ],
    [
        r"(.*)promociones(.*)",
        ["Tenemos promociones de internet:\n"
         "50mbps a $36.99 el mes, mas tres meses de cortesia en amazon prime,\n"
         "70mbps a $41.99 el mes, mas tres meses de cortesia en amazon prime\n"
         "100mbps a $45.99 el mes, mas tres meses de cortesia en amazon prime"]
    ],
    [
        r"(.*)atencion al cliente(.*)",
        ["Para brindarte una atencion al cliente mas satisfactoria por favor visita nuestra pagina web www.ejemplo.com o"
         "contactanos al número telefonico 89560820"]
    ],
]
def bot():
    print("Bienvenido soy el bot asistente,¿en qué puedo ayudarte?")
    chat = Chat(pares)
    chat.converse()
bot()
