from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

Listmotos = [{"Id": 0,"Modelo":"M1000RR","Marca":"BMW","Precio":200000000,"Img":"https://www.soymotero.net/sites/default/files/styles/max_width_800px/public/2020-09/bmw_m1000rr_ok.jpg?itok=7nr2tSsA","Descripcion":"Primera moto M de BMW, fruto del perfeccionamiento de la S1000RR por su departamento Motorsport: llantas de carbono, bielas y escape de titanio, alerones, y muchos detalles que llevan el peso a solo 169 kg en seco y la potencia a 212 CV. Una superdeportiva muy especial."},
{"Id": 1,"Modelo":"H2R","Marca":"KAWASAKI","Precio": 150000000,"Img":"https://static.turbosquid.com/Preview/2016/04/21__02_04_35/Kawasaki_Ninja_H2R_Supercharged_2015_0000.jpgae38e956-defd-49f2-8e9c-637b53d31eacDefaultHQ.jpg","Descripcion":"La Kawasaki Ninja H2R es una moto exclusiva de circuito con un empuje que bien podría recordar a una MotoGP. Su preparación hace que rinda tranquilamente 310 cv de potencia, pero que incluso con Ram Air llega a los brutales 326 cv... ¡De locos! Sin embargo, el resto de la moto no desmerece el desarrollo realizado en el propulsor. Distintas divisiones del gigante Kawasaki Heavy Industries colaboraron para realizar distintas partes de la moto (Compresores, Aeroespacial, etc) incidiendo en su aerodinámica, materiales o incluso su pintura especial."},
{"Id": 2,"Modelo":"AGUNSTA BRUTALE 1000","Marca":"MV","Precio":14000000,"Img":"https://www.motofichas.com/images/phocagallery/MV_Agusta/brutale-1000-2019/01-mv-agusta-brutale-1000-rr-2020-estatica-rojo.jpg","Descripcion":"La MV Agusta Brutale 1000 RR es una naked de 1000 totalmente radical, con un motor explosivo de nada menos que 208 CV de potencia a 13.450 rpm. Es la maxinaked más radical del momento, que deriva de forma directa de la deportiva F4 1000."},
{"Id": 3,"Modelo":"Panigale","Marca":"Ducati","Precio":14000000,"Img":"https://img.motoryracing.com/noticias/portada/32000/32864-n.jpg","Descripcion":"La Ducati Panigale V4 es una deportiva que deriva directamente de la Desmosedici de MotoGP, una moto muy avanzada tecnológicamente con un explosivo motor capaz de rendir 214 CV. Lanzada en 2018, la Panigale V4 se renueva en 2020 adquiriendo gran parte de las componentes que incorpora la Panigale V4 R, en especial el paquete aerodinámico con los alerones que hacen que la moto tenga un comportamiento más eficaz a alta velocidad. La Panigale V4 S es sólo 5,5 kg más pesada que la 1299 Panigale S, una cifra que habla por sí sola del gran trabajo de los italianos con la Desmosedici Stradale. Estas cifras no se hubieran conseguido usando un tradicional chasis perimetral de ahí que los ingenieros se decantaran por llevar a cabo una evolución del monocasco de MotoGP, usando el motor de elemento autoportante. Este diseño ofrece una mejor absorción de las irregularidades en curva así como una superior agilidad y precisión en la conducción, lo que supone menos fatiga para el piloto. El chasis también cambia en 2020 y pasa a ser como el de la Panigale V4 R."},
{"Id": 4,"Modelo":"RSV4 RR","Marca":"Aprilia","Precio":14000000,"Img":"https://www.motofichas.com/images/phocagallery/Aprilia/RSV4_RR_2017/02-aprilia-rsv4-1000-rr-2019-negra-estatica.jpg","Descripcion":"La Aprilia RSV4 RR es la superbike de la marca italiana, una deportiva realmente equipada y dorada de un motor que ofrece unas prestaciones casi de carreras: 201 CV de potencia y 115 Nm de par. Se mantiene sin variaciones técnicas desde 2017, y sólo en 2019 se han introducido nuevos colores. La moto destaca por su electrónica tan avanzada, contando con el sistema patentado APRC (Aprilia Performance Ride Control) de cuarta evolución que incluye un nuevo acelerador Ride-by-Wire bastante más ligero que el anterior. El APRC incluye control de tracción con ocho modos seleccionables a través de un joystick fácilmente manipulable, un sistema anti Wheelie de tres niveles, un control de salidas con otros tres niveles, un sistema de cambio de marcha (Aprilia Quick Shift) para subir y bajar de marcha sin necesidad de usar el embrague y sin desacelerar, un limitador de velocidad (para el pit lane o para usar en carretera) y un sistema de velocidad crucero sin necesidad de usar el acelerador. El APRC afecta a los frenos, pues la nueva RSV4 RR cuenta con un avanzado ABS en curva, de la marca Bosch, que resulta igualmente útil en carretera como en circuito. El sistema ayuda igualmente en el tren trasero, limitando el levantamiento de la rueda trasera cuando se realizan fuertes frenadas. Este ABS en curva cuenta con tres mapas que se combinan con otros tres mapas del motor (Sport, Track y Race). Todas estas opciones se visualizan a través de su instrumentación TFT, con diferente luz dependiendo de si es de día o de noche, que es compatible con el sistema de conectividad Aprilia Mia que permite conectar la moto al smartphone via Bluetooth tanto para realizar las tareas habituales del teléfono a través de la pantalla, como para configurar los ajustes de la moto y tomar datos sobre tiempos en circuito. El chasis y el basculante de aluminio son regulables como en las motos de competición en lo que se refiere al ángulo de dirección, posición del subchasis que sustenta el asiento del piloto, altura trasera o el pivote del basculante."},
{"Id": 5,"Modelo":"Ninja ZX-10R","Marca":"Kawasaki","Precio":14000000,"Img":"https://www.motofichas.com/images/cache/01-kawasaki-ninja-zx-10r-krt-2020-estudio-verde-739-a.jpg","Descripcion":"La Kawasaki Ninja ZX-10R 2020 continúa destilando aroma de superbikes y siendo una de las referencias indiscutibles de la categoría a pesar de no recibir más cambios que los estéticos en 2020 tras su profunda renovación el año anterior. Destaca por ser heredera directa de mucha de la tecnología aplicada por Kawasaki en el Mundial de Superbikes que lleva dominando con mano de hierro en los últimos años gracias al talento de Jonathan Rea. Y como homenaje, se ofrecen los colores KRT (Kawasaki Racing Team) como la única opción disponible en la versión básica. Además, Kawasaki también lanza la versión SE (Special Edition) en 2020. Los ingenieros de Kawasaki cada vez importan más elementos usados en competición a una moto que es el fiel reflejo de la usada en el Mundial de Superbikes. Un buen ejemplo es el sistema de válvulas que permite lograr unas prestaciones de vértigo mientras que la fiabilidad no se ve comprometida a altas revoluciones. En lugar de usar el accionamiento mediante taqués, al hacerlo por balancines se provoca un ahorro de un 20 en la masa. Esto además posibilita el uso de perfiles de leva más agresivos, un factor que incide directamente en la potencia que alcanza esta montura. El recubrimiento en los balancines DLC (Carbono como diamante) mitiga además su desgaste. "}]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/motos', methods=['GET'])
def usuarios():
    return jsonify({"datos": Listmotos}), 200


@app.route('/motoid', methods=['GET'])
def usuario_id():
    id = request.headers.get('id')
    motosid = Listmotos[int(id)]
    return jsonify({"InfoMotos": motosid}), 200


if __name__ == '__main__':
    app.run()
