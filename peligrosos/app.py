import web
import json
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

urls = ('/upload', 'Upload')

class Upload():
    def POST(self):
        datos={}
        x = web.input(myfile={})
        filedir = 'static' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
            datos["Mensaje"]="Archivo recibido"
        else:
            datos["Error"]="Archivo no recibido"
            datos["Mensaje"]="Archivo recibido"
        np.set_printoptions(suppress=True)
        model = tensorflow.keras.models.load_model('static/keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open('static/'+ filename)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        image.show()
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)

        for i in prediction:
            if i[0] > 0.7:
                resultado = "Es una boa"
                datos["Tipo de animal"]=resultado                
                datos["Descripcion"]="La boa constrictora (Boa constrictor) es una especie de serpiente de la familia Boidae, y de la subfamilia Boinae. Actualmente, es la única especie del genero Boa."
                datos["Habitat"]="A la boa podemos encontrarla en lugares humedos de algunos bosques y en lugares con muy poca cantidad de agua como ambientes aridos y en desiertos, en sabanas y tambien en terrenos de cultivo."
                datos["Tip"]="No es recomendable vivir cerca de una de ellas porque pueden escaparse y enrollarse en niños y mujeres embarazadas."
                datos["Consejo"]="A pesar de su intimidante aspecto, es inofensiva ya que ademas de no poseer veneno no cuenta con colmillos y no atacara al hombre a no ser que este la amenace."                              
            elif i[1] > 0.7:
                resultado = "Es una cobra"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="Estos temibles reptiles son animales oviparos, es decir, se reproducen por huevos. Para sobrevivir se alimentan de aves y pequenos mamiferos, sobre todo ratones, a los que muerden e inyectan, a traves de los colmillos, un veneno mortal."
                datos["Habitat"]="Habitan en zonas tropicales y deserticas del sur de Asia y Africa"
                datos["Tip"]="No te le acerques porque te mata"
                datos["Consejo"]="Si te muerde una serpiente venenosa, llama inmediatamente al 911 o al numero local de emergencias, especialmente si la zona mordida cambia de color, comienza a hincharse o duele; Alejate del radio de ataque de la serpiente, Quedate quieto y manten la calma para ayudar a disminuir la propagación del veneno, Quitate las joyas y la ropa ajustada antes de que comiences a hincharte, Colocate, si es posible, de manera tal que la mordedura este a la altura del corazon o por debajo, Limpia la herida con agua y jabon. Cubrela con un aposito limpio y seco."     
            elif i[2] > 0.7:
                resultado = "Es una coralillo"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="La coral ratonera, falsa coral o culebra real coralillo (Lampropeltis triangulum) es una especie de reptil de la familia Colubridae. Habita en casi toda America, desde el sur de Canada hasta Ecuador, Colombia y Venezuela, pasando por Estados Unidos, Mexico y Centroamerica"
                datos["Habitat"]="Al ser animales de sangre fria, acostumbran a poblar zonas tropicales que le brinden el calor necesario para sobrevivir."
                datos["Consejo"]="Si te muerde una serpiente venenosa, llama inmediatamente al 911 o al numero local de emergencias, especialmente si la zona mordida cambia de color, comienza a hincharse o duele; Alejate del radio de ataque de la serpiente, Quedate quieto y manten la calma para ayudar a disminuir la propagación del veneno, Quitate las joyas y la ropa ajustada antes de que comiences a hincharte, Colocate, si es posible, de manera tal que la mordedura este a la altura del corazon o por debajo, Limpia la herida con agua y jabon. Cubrela con un aposito limpio y seco."     
                datos["Consejo"]="El cuadro clínico de una persona infectada con el veneno de la serpiente coral se caracteriza por padecimientos muy discretos. Las personas experimentan un leve dolor que desaparece en breve tiempo, y la zona infectada se muestra como un simple rasguno. Sin embargo, al cabo de unas horas, las patologias se agravan, la vision se vuelve borrosa, la garganta se entumece y comenzamos a experimentar sensaciones de asfixia."     
            elif i[3] > 0.7:
                resultado = "Es un alacran"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="Scorpiones es un orden de artropodos aracnidos depredadores conocidos comunmente como escorpiones o alacranes. Se caracterizan por un contar con un par de pinzas de agarre y una cola estrecha y segmentada, a menudo formando una reconocible curva hacia delante sobre la espalda y siempre rematada con un aguijon"
                datos["Habitat"]="Su habitat se localiza mayormente, en regiones aridas o deserticas, aunque algunas especies estan adaptadas a regiones humedas, tropicales y subtropicales. La mayoria prefiere terrenos arenosos, secos y pedregosos o tierras aridas y secas de las montanas."
                datos["Tip"]="Revisar y sacudir prendas de vestir, y calzados, Sacudir la ropa de cama antes de acostarse o acostar un bebe o nino, Tener precaucinn cuando se examinan cajones o estantes, Evitar caminar descalzo en zonas donde se conozca la presencia de alacranes."
                datos["Consejo"]="Si estas solo/a llama a alguien que pueda auxiliarte, No pierdas de vista al alacran y de ser posible atrapalo, Lava la zona afectada con agua y jabon, Manten la zona elevada, No manipules la herida (picar, rascar, apretar, etc)"     
            elif i[4] > 0.7:
                resultado = "Es una viuda negra"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="La viuda negra del sur (Latrodectus mactans) es una especie de arana araneomorfa de la familia Theridiidae.1 Tambien se conoce como arana del trigo, arana capulina, viuda negra, y mico-mico (en el sur de Bolivia)."
                datos["Habitat"]="Se encuentra principalmente en el este de Estados Unidos, en Mexico y en Venezuela. Su habitat es terrestre, suele vivir cerca de la tierra y en puntos abrigados y oscuros. Sin embargo, tambien prepara sus cuevas sobre plantas. La tela de la viuda se puede encontrar en hendiduras debajo de piedras, en plantas, en grietas o agujeros, en terraplenes de suciedad y en graneros."
                datos["Tip"]="El veneno de esta arana es peligroso, raramente llega a ser letal. Si es correcta y puntualmente tratada, la victima se recupera totalmente"
                datos["Consejo"]="La picadura de las aranas viuda negra rara vez es mortal, pero es importante obtener atencion medica lo antes posible porque puede causar algunos trastornos. Con la ayuda de un adulto, lava bien la picadura con agua y jabon. Luego aplica un cubito de hielo sobre la picadura para reducir la extension del veneno."     
            elif i[5] > 0.7:
                resultado = "Es un cien pies"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="Los ciempies tienen un cuerpo alargado y plano formado por 21 segmentos o anillos (metameros), con un par de patas en cada uno de ellos. Pueden llegar a medir desde unos cuantos milimetros, en los Lithobiomorpha y Geophilomorpha, hasta los 30 cm en los Scolopendromorpha."
                datos["Habitat"]="Muchos ciempies viven en el suelo y en la hojarasca, mientras que los que cazan libremente en el suelo son estrictamente nocturnos y pasan el dia escondidos bajo troncos y piedras donde pueden mantenerse humedos"
                datos["Tip"]="La mayoria de las mordeduras de los cienpies no causan danos significantes a la persona."
                datos["Consejo"]="Las mordeduras de cienpies deben tratarse lavandolas fuertemente con agua y jabon. Una compresa fria puede ser utilizada por intervalos de 10 minutos para reducir la hinchazon del sitio."     
            elif i[6] > 0.7:
                resultado = "Es una tarantula"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="La tarantula es una arana peluda de la familia de los aracnidos, que tambien incluye a los acaros, las garrapatas y los escorpiones. Pueden medir hasta unas 12 pulgadas de largo (unos 30 cm.) "
                datos["Habitat"]="Las tarantulas se pueden encontrar en Africa, Asia, Medio Oriente, America del Sur y Central, Mexico y el suroeste de los Estados Unidos. Algunas viven en el desierto, pero muchas viven en las selvas lluviosas. Algunas tarantulas construyen sus hogares bajo rocas o troncos, o bajo la corteza de los arboles."                
                datos["Tip"]="Las tarantulas no suelen ser mortales para los seres humanos en la mayoria de los casos pero si puedes no te acerques "
                datos["Consejo"]="Si crees que te ha picado una tarantula, lava la picadura con agua y jabon. Si la picadura te produce mucho dolor, puedes pedirle a un adulto que te de un medicamento para el dolor. Poner hielo sobre la picadura tambien ayuda a aliviar el dolor."
            elif i[7] > 0.7:
                resultado = "Es un sapo bufo"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="Bufo es un genero de anfibios anuros de la familia Bufonidae que incluye, entre otros, al sapo europeo comun. Se distribuye por las regiones templadas de Eurasia, norte de Africa, Oriente Medio, Japon y la zona norte del sudeste asiatico."
                datos["Habitat"]="El sapo bufo se encuentra en altitudes de hasta 2500 metros en la parte sur de su area de distribucion. Se encuentra principalmente en zonas boscosas con coniferas, caducifolios y bosques mixtos, especialmente en lugares humedos."
                datos["Tip"]="Se le denomina Bufo porque sus glandulas cutaneas contienen bufotenina y 5-MeO-DMT, que son dos sustancias psicodelicas que durante las secreciones de su piel tienen propiedades alucinogenas."
                datos["Consejo"]="Pero cuidado! Porque este anfibio tambien contiene un veneno, situado en sus patas traseras, capaz de paralizar e incluso causar la muerte en el momento que es ingerido."     
            elif i[8] > 0.7:
                resultado = "Es una rana Arlequin"
                datos["Tipo de animal"]=resultado
                datos["Descripcion"]="Atelopus varius o sapo pintado es una especie de anfibios de la familia Bufonidae. Estan amenazadas de extincion por la perdida de su habitat natural"
                datos["Habitat"]="A. varius habita en zonas de baja montaaa en la cordilleras de Costa Rica y el oeste de Panama, tanto en la vertiente del Atlantico como en la del Pacifico"
                datos["Tip"]="Dejala esta en peligro de extincion"
                datos["Consejo"]="No te acerques"     
            else:
                resultado = "No se encontro coincidencias:"
                datos["Tipo de animal"]=resultado
        return json.dumps(datos)
        

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()

