# LABORATORIO 5: – USO DE BITalino PARA ECG

### Tabla de contenidos

------------

1. [Introducción](#introduccion)
2. [Objetivos](#objetivos)
3. [Materiales y equipos](#materiales-y-equipos)
4. [Procedimiento](#procedimiento)
5. [Resultados](#resultados)
   1. [Conexión usada](#conexion-usada)
   2. [Video de la señal](#video-de-la-señal)
   3. [Ploteo de la señal en Python](#ploteo-de-la-señal-en-python)
6. [Referencias](#referencias)

## Introducción
El electrocardiograma (ECG) es una prueba diagnóstica fundamental en la medicina que registra la actividad eléctrica del corazón. Utilizando electrodos colocados en la piel, el ECG mide los impulsos eléctricos que desencadenan cada latido cardíaco, proporcionando un gráfico que muestra el ritmo, la frecuencia y la forma de las ondas eléctricas. Esta información es crucial para detectar diversas afecciones cardíacas, como arritmias, infartos y enfermedades del músculo cardíaco. El ECG es una herramienta no invasiva, rápida y ampliamente utilizada en entornos clínicos para evaluar la salud cardiovascular y guiar decisiones terapéuticas.

El presente laboratorio se centra en el uso de la placa de desarrollo Bitalino para capturar señales de electrocardiograma (ECG) de interés. Esta innovadora herramienta nos brinda la capacidad de registrar y analizar la actividad eléctrica del corazón de manera no invasiva y en tiempo real. A lo largo de esta experiencia práctica, se busca adquirir conocimientos sobre la obtención y el análisis de señales ECG, además de familiarizarse con los procedimientos y protocolos necesarios para la utilización de los electrodos de ECG.

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/C.png" width="500" height="266"></p>
</p>
Fig 1. Señales ECG con los diferentes intervalos y segmentos que la componen [1].

## Objetivos

- Adquirir señales biomédicas de ECG usando el BiTalino
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales ECG del software OpenSignals (r)evolution.
- Interpretar el significado clínico de las señales ECG y observar posibles errores en la toma de datos.
  
## Materiales y equipos

- BITalino (r)evolution kit
- Electrodos ECG
- Computadora con Bluetooth
- Software OpenSignals
- Entorno de desarrollo Python

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/D.png" width="900" height="266"></p>
</p>

## Procedimiento

### 4.1. Conexión del OpenSignals:

La conexión correcta de la PC con la placa BITalino, el reconocimiento del modelo en la aplicación OpenSignals, junto con la configuración de la entrada A2 del BITalino para la medición del ECG.

### 4.2. Revisión de las Guías de laboratorio de BITalino:

La guía: “HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) [2]” posee como contenido la ubicación de electrodos recomendadas siendo, la elegida, la siguiente:

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/A.png" width="300" height="266"></p>
</p>
Fig 2. Colocación de electrodos para la 1era derivación: IN+ (izquierda - rojo) e IN- (derecha - negro) en las muñecas y la REF (blanco) en la cresta ilíaca [1].

<p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/B.png" width="500" height="266"></p>
</p>
Fig 3. Colocación de los electrodos en el estudiante elegido junto con la conexión con el BITalino.

### 4.3. Preparación del estudiante:

Se debe asegurar que las zonas correspondientes a la ubicación de los electrodos estén libres de obstrucciones, como prendas o accesorios, y que estén limpias para garantizar un contacto adecuado con los electrodos.

### 4.4. Registro de la señal ECG:

Una vez puestos los electrodos superficiales en las zonas descritas se empieza a registrar las señales tres veces en diferentes momentos, cada ocasión se repite con una configuración de derivación distinta.

- **Estado Basal:**
Estado de reposo evaluado donde el estudiante se mantiene calmado y relajado.

[Ver video 1](https://youtu.be/eoxMC3BR_5U)

- **Estado de pausa respiratoria (durante y después):**
El estudiante mantiene la respiración durante 10 segundos, mientras se registra su ECG en ese intervalo. Al concluir, se realiza un nuevo registro del ECG para observar las variaciones posteriores al ejercicio de contención de la respiración. Se repite este proceso tres veces, siendo seis registros en total.

[Ver video 2](https://youtu.be/8n2kfjqa50U)

[Ver video 3](https://youtu.be/anY9URw1vs4)

- **Estado después de una actividad física:**
Durante 5 minutos aproximadamente, el estudiante realiza ejercicios aeróbicos intensos hasta llegar al cansancio. En nuestro caso, el estudiante subió y bajó escaleras durante ese periodo de tiempo. Se busca registrar cada derivación lo más rápido posible para que no disipe el efecto del cansancio sobre el ECG.

[Ver video 4](https://youtu.be/AYHTVNsGHok)

[Ver video 5](https://youtu.be/aCMujE-tHtw)

### 4.5. Simulación - ProSim4:

Finalmente se puede observar señales patrón gracias al ProSim 4, un simulador de signos vitales portátil diseñado para realizar pruebas rápidas que, en este caso se dieron para simular el ECG en diferentes frecuencias cardiacas que fueron registradas con la aplicación OpenSignals.

   - Simulación de 60lpm - Estado basal
   - Simulación de 120lpm - Empieza a agitarse
   - Simulación de 150lpm - Haciendo ejercicio
   - Simulación de 90lpm - Reponiéndose

[Ver video 6](https://youtu.be/D4N19q_PkfQ)

## Resultados

### 5.1. Ploteo de la señal en Python

Para el análisis de la señal obtenida, se utilizó Python para filtrar las señales usando Mediana (Reduce el ruido [3]), Butterworth (0.05Hz - 150Hz), Notch (60Hz) y visualizar la señal:

- Estados de reposo
   - 1ra derivación
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Estado basal I dev.png" width="700" height="266"></p>
        </p>
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT Señal Original Estado basal I dev.png" width="700" height="266"></p>
        </p>
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltradaIderi_estadoBasal.png" width="700" height="266"></p>
       </p>
     Al observar la señal filtrada obtenida de la primera derivación ECG de una persona en reposo (estado basal), se denotan los picos repetitivos pertenecientes a los complejos QRS, los cuales representan la despolarización de los ventrículos. No obstante, aunque los picos QRS son más visibles y más limpios después del proceso de filtrado de la señal, los picos R presentaron excesivamente una menor amplitud que los picos S, lo cual puede deberse a múltiples factores como la colocación de los electrodos, la anatomía individual, o las características eléctricas del corazón del individuo. También, se puede relacionar con una activación ventricular más prolongada o un eje eléctrico inclinado hacia la izquierda, lo cual no necesariamente es patológico.
Asimismo, la gráfica de la transformada rápida de Fourier (FFT) para la señal muestra que la mayor parte de la actividad se concentra en frecuencias bajas (entre 0 y 50 Hz), lo cual es esperable en una señal de ECG para un estado de reposo. Se debe tener en cuenta que mayormente no se deberían encontrar frecuencias superiores de 40 Hz, ya que al estar en reposo, no debería haber frecuencias elevadas asociadas a la actividad muscular intensa o movimiento, por lo que es posible que el resto de frecuencias  se deban a interferencias electromagnéticas, como el ruido de la red eléctrica. De la misma manera, las ondas P y T no son claramente identificables, lo que puede deberse a la atenuación de estas señales de baja amplitud durante el proceso de filtrado. 

   - 2da derivación
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Estado basal II dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT Señal Original Estado basal II dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltradaIIderi_estadoBasal.png" width="700" height="266"></p>
        </p>
     Al analizar la señal filtrada del estado basal para la II derivación se pueden contemplar todos los componentes de las fases del ciclo cardíaco, siendo el complejo QRS más prominente. En comparación de la gráfica para la I derivación, en esta señal, el pico R es uno de los picos con mayor amplitud y notoriedad, debido a la orientación del vector de activación del ventrículo izquierdo, que es dominante en la  II derivación. Del mismo modo, se presenta una separación regular entre los picos R, lo que indica un ritmo cardíaco normal en reposo. 
Para el caso de la onda P y T, se puede observar que ambas son deflexiones de menor tamaños y menos prominentes que el complejo QRS. En caso de la onda P, es posible identificarla como la primera deflexión positiva significativa de cada ciclo antes del complejo QRS, lo que representa una despolarización de las aurículas adecuada. Sin embargo, el tamaño y la forma de la onda P, suelen ser más pequeños debido a que la activación auricular no es tan intensa como la ventricular. Mientras que la onda T aparece como una deflexión positiva suave tras el complejo QRS, representando la repolarización de los ventrículos, al presentar la forma más cercana a la ideal, se puede inferir que no se presentan alteraciones en la recuperación eléctrica de los ventrículos.

   - 3ra derivación
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Estado basal III dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT Señal Original Estado basal III dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltradaIIIderi_estadoBasal.png" width="700" height="266"></p>
        </p>
      En esta señal ECG filtrada para la III derivación, los electrodos fueron colocados de manera específica: el de referencia en la muñeca derecha, el negativo, en la muñeca izquierda, y el positivo, en la cresta iliaca. De esta manera, esta configuración permite capturar el potencial eléctrico generado por el corazón en un eje que va principalmente desde la muñeca izquierda hacia la pierna izquierda, proporcionando una perspectiva oblicua del eje cardíaco. Debido a lo anterior, el pico R del complejo QRS es visible pero con menor amplitud en comparación con la II derivación, lo cual es previsible, debido a que la derivación no está alineada directamente con el vector principal de despolarización ventricular. Asimismo, las ondas P y T aparecen menos definidas debido a la orientación y la menor amplitud intrínseca de estas ondas en la dirección captada por esta derivación, y por el proceso de filtrado que podría haber reducido aún más su visibilidad. 

- ECG durante la conteción de respiración
   - Sin Respiración (1ra derivación)
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Estado sin respiración.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT_Original_Estado sin respiración.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltradaIderi_Sinrespira.png" width="700" height="266"></p>
        </p>
        Al examinar la señal del ECG, se observa que la amplitud del pico S es inusualmente mayor que la del pico R, lo cual podría atribuirse a la colocación de los electrodos y a la orientación del eje eléctrico del corazón. Asimismo, para este caso, la señal fue obtenida mientras la persona aguantaba la respiración, por lo que al visualizar la señal se dificulta el identificar las ondas P y T, ya que al no respirar, la ausencia de movimiento respiratorio reduce las fluctuaciones mecánicas y eléctricas inducidas por el diafragma y los músculos intercostales.Aún así, cabe destacar que el tamaño normal de la distancia de los intervalos RR sugiere que el ritmo es regular, lo que indica un funcionamiento adecuado del sistema de conducción cardíaco. 

   - Post-Respiración (1ra derivación)
     - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(1ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Respiracion_1d_24.png" width="700" height="266"></p>
        </p>
        En el ECG, se puede observar un intervalo RR de 0.75 segundos. Al comparar esta distancia con la del estado basal, podemos indicar que mantener la respiración por un tiempo de 20 segundos no influye en el aumento de la frecuencia cardiaca. 
        
   - Sin Respiración (2da derivación)
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Estado sin respiración II dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT Señal Original Estado sin respiración II dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltradaIIderi_Sinrespira.png" width="700" height="266"></p>
        </p> 
        La señal de ECG en II derivación para una persona que aguanta la respiración muestra complejos QRS bien definidos que corresponden a los picos altos y estrechos, indicando una fuerte actividad eléctrica ventricular. Mientras que, las ondas P y T son visibles como pequeñas oscilaciones antes y después de cada complejo QRS, reflejando la despolarización auricular y la repolarización ventricular, respectivamente. Aunque, cuando una persona aguanta la respiración, se puede esperar una menor variabilidad en la línea de base de la señal, ya que la variabilidad respiratoria afecta menos al ritmo cardíaco; en la señal observada, se aprecia un patrón relativamente regular del complejo PQRST, indicando un ritmo cardíaco constante. 
   - Post-Respiración (2da derivación)
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(2da_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Respiracion_2d_24.png" width="700" height="266"></p>
        </p>
        En el ECG, se puede observar un intervalo RR de 0.70 segundos.
      
   - Sin Respiración (3ra derivación)
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Estado sin respiración III dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT Señal Original Estado sin respiración III dev.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltradaIIIderi_Sinrespira.png" width="700" height="266"></p>
        </p>    
        En la señal de ECG en III derivación para cuando una persona mantiene la respiración, se pueden identificar los componentes típicos del ciclo cardíaco. En caso de la onda P, se mantiene como pequeñas deflexiones positivas que corresponden a la despolarización auricular, aunque puede no ser claramente visible en esta derivación, puede visualizarse justo antes del complejo QRS. En caso de este último, el complejo QRS es el componente más prominente en la señal, donde la onda R tiene una amplitud significativamente mayor que la onda S, lo cual indica una fuerte actividad eléctrica de los ventrículos y sugiere una buena captura del evento de despolarización ventricular. Aunque en la derivación III esta configuración de mayor R que S puede ser un hallazgo normal, también podría estar asociado con condiciones específicas como la hipertrofia ventricular izquierda, por lo que se recomienda evaluarlo en conjunto con otros datos clínicos. En caso de la onda T sigue al complejo QRS, indicando una repolarización ventricular adecuada, con amplitud y morfología normales. Por último, la línea de base se mantiene estable, con ligeras fluctuaciones típicas y la frecuencia cardíaca se mantiene constante debido a la reducción de la variabilidad por la falta de respiración.
   - Post-Respiración (3ra derivación)
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Estado_con_respiración_(3ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Respiracion_3d_24.png" width="700" height="266"></p>
        </p>
        En el ECG, se puede observar un intervalo RR de 0.75 segundos. Al comparar esta distancia con la del estado basal, podemos indicar que mantener la respiración por un tiempo de 20 segundos seguidamente no influye en el aumento de la frecuencia cardiaca. Esto se puede deber a que la persona participe acostumbra a ejercitarse seguidamente.
        
- Estado de ejercicio
   - 1ra derivación
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(1ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_1d_24.png" width="700" height="266"></p>
        </p>
        A comparación del estado basal, en el que solo se ven 3 complejos QRS, en un estado ejercitado, en la 1ra derivación, se ve como hay 4 complejos QRS en un tiempo de 2 a 4 segundos y aparecen cada 0.5 segundos aproximadamente.
        
   - 2da derivación
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(2da_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_2d_24.png" width="700" height="266"></p>
        </p>
        A comparación del estado basal, en la 2ra derivación, los complejos QRS y aparecen cada 0.45 segundos aproximadamente en un tiempo de 2 a 4 segundos. Es decir, se acorta la distancia el intervalo RR
        
   - 3ra derivación
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_(3ra_derivación)_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Ejercicio_3d_24.png" width="700" height="266"></p>
        </p>
        A comparación del estado basal, en la 3ra derivación, los complejos QRS y aparecen cada 0.5 segundos aproximadamente en un tiempo de 2 a 4 segundos.
        
- Simulaciones
   - 60 bpm
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Simulacion 60 bpm.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT Señal Original Simulación 60 bpm.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltrad60bpm.png" width="700" height="266"></p>
        </p>     
   - 90 bpm
     - Imagenes obtenidas
       <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Señal Original Simulacion 90 bpm.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/FFT Señal Original Simulacion 90 bpm.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/SeñalFiltrad90bpm.png" width="700" height="266"></p>
        </p>
      Interpretaciones de 60 y 90 bpm: Las señales electrocardiográficas (ECG) presentadas corresponden a simulaciones de frecuencias cardíacas de 60 bpm y 90 bpm realizadas con el dispositivo ProSim. En el caso de una frecuencia cardiáca de 60 bpm, el corazón está trabajando en condiciones normales de reposo, con tiempo suficiente para que las aurículas y ventrículos se despolaricen y repolaricen de manera eficiente, asegurando un suministro constante de sangre oxigenada al cuerpo.  Mientras que, a 90 bpm, el corazón está trabajando más rápido, lo que suele ocurrir en situaciones de mayor demanda metabólica, como ejercicio físico, estrés o una mayor actividad simpática, por lo que el ciclo cardíaco es más corto, y tanto la despolarización como la repolarización deben ocurrir más rápidamente para mantener un flujo sanguíneo adecuado. Finalmente, al comparar las dos señales filtradas, se observa que la señal a 60 bpm tiene ciclos cardíacos más espaciados, lo que permite una mejor diferenciación de los componentes PQRST. En cambio, en la señal a 90 bpm, los ciclos son más cortos y los elementos de la señal se encuentran más próximos entre sí, lo que reduce la claridad en la separación de las ondas, especialmente entre la onda T y el complejo QRS del siguiente ciclo. 

   - 120 bpm
      - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_120_bpm_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/S120_24.png" width="700" height="266"></p>
        </p>
        En el ECG del intervalo de 2 a 4 segundos, se puede observar un intervalo RR de 0.5 segundos. Esto podria indicar que en el estado de ejercicio, la persona alcanzo 120 bpm. Además, al ser una simulación se pueden ver mejor las caracteristicas del ECG.
        
   - 150 bpm
     - Imagenes obtenidas
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_original.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_filtrada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_original_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/Simulación_a_150_bpm_fft_senal_filtrada_enfocada.png" width="700" height="266"></p>
        </p>
      - Interpretaciones
        <p align="center"><img src="/ISB/Laboratorios/Lab5 - Adquisición de señal ECG/Imagenes/ECG/S150_24.png" width="700" height="266"></p>
        </p>
        En el ECG del intervalo de 2 a 4 segundos, se puede observar un intervalo RR de 0.4 segundos. Este rango es 0.1 segundos menor al del ECG a 120 bpm, lo cual puede indicar que a mayor bpms, mas corto es el intervalo RR. Además, al ser una simulación se pueden ver mejor las caracteristicas del ECG.
     

## Referencias
[1] D. J. Nelson, A. Alvarez, E. Dugarte, and G. Álvarez, “Técnicas de procesamiento de la señal ECGAR aplicadas en el prototipo DIGICARDIAC.” https://ve.scielo.org/scielo.php?script=sci_arttext&pid=S0798-04772015000100007
[2] “BITalino Lab Guides (Home Guides).” https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/
[3] J. Cheng, Q. Zou y Y. Zhao, “ECG signal classification based on deep CNN and BiLSTM”, BMC Med. Inform. Decis. Making, vol. 21, n.º 1, diciembre de 2021. Accedido el 21 de septiembre de 2024. [En línea]. Disponible: https://doi.org/10.1186/s12911-021-01736-y
