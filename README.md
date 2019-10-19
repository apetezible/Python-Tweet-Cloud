# Python Tweet-Cloud

## Abstract
Como parte de este proyecto, Escribiré un programa que procese una lista de trinos de Twitter y genere una
nube de palabras a partir de ellos.

## Introducción
Para concluír mi estudio de Python básico, necesitaba proponer un proyecto que sintetisaze todos los conceptos aprehendidos en ese intervalo de tiempo. Propongo entonces este proyecto que reunirá un conjunto de Tweets, extraerá sus palabras y finalmente las ordenará de acuerdo con su freciencia.

## Métodos
En "process_tweets.py" se procesarán los Tweets de "tweets.txt", para obtener las palabras y frecuencias apropiadas que se dibujarán en la nube. La función "get_tweet_text()" Recibe una línea del archivo "tweets.txt" y obtiene el texto del trino, el cual devuelve como una cadena de caracteres. La función "read_stopwords()" Lee las stop words del archivo 'stopwords.txt' y retorna una lista con las palabras. La función "clean_line()" elimina todos los caracteres no alfabéticos, excepto ' ', '@' y '#', de la linea. Cambia los caractertes en mayúscula a minúscula. La función "process_tweet_text()" recibe el texto del tweet y lo procesa: Elimina cualquier carácter no alfabético, excepto ' ', '@' y '#'; lo convierte a minúsculas; lo separa en palabras; filtra todas las palabras que son stop words; devuelve las palabras restantes como una lista. La función "process_tweet_file()" recibe el nombre del archivo que contiene los tweets. Lo procesa para obtener todos los textos de los trinos. Extrae las palabras de él y cuenta sus frecuencias. Devuelve el resultado como un diccionario, donde las claves son las palabras y los valores son las frecuencias de palabras. La función "print_statistics()" recibe un diccionario con frecuencias de palabras e imprime las estadísticas. La función "write_words(word_freqs, file_name)" escribe las palabras junto con sus frecuencias, una palabra por línea con las palabras y las frecuencias separadas por un espacio.
En "word_cloud.py" se procesarán las frecuecias y palabras comprendidas en el archivo "words.txt", para dibujar en HTML las palabras en una nube. La función "read_words()" lee un archivo con palabras y frecuencias y almacena los datos como una lista de pares. La función "get_top_words()" recibe una lista de palabras y frecuencias y devuelve las top n palabras más frecuentes con sus respectivas frecuencias. La función "get_top_hashtags()" recibe una lista de palabras y frecuencias y devuelve los top n hashtags más frecuentes con sus respectivas frecuencias. La "función get_top_users()" recibe una lista de palabras y frecuencias y devuelve los top n usuarios más frecuentes con sus respectivas frecuencias. La función "generate_cloud(words, scale, file_name) genera una página HTML que muestra una nube de palabras a partir de la lista de palabras. El código HTML de salida se escribe en file_name. El archivo se puede abrir con el browser. El parámetro de escala controla el tamaño de las palabras.
