# Análisis de Señales EMG y ECG

Este informe presenta el análisis de las señales EMG y ECG capturadas, utilizando distintos tipos de filtros (FIR, Butterworth, y Chebyshev). Para cada señal, se muestra su análisis en el dominio del tiempo, el dominio de la frecuencia, y la transformada corta de Fourier (STFT). También se incluye el análisis de los filtros aplicados a las señales mediante el diagrama de polos y ceros, y el diagrama de Bode (magnitud y fase).

## 1. Señal EMG - Bíceps Braquial en Reposo

### Análisis de la Señal
#### Gráfica en el Dominio del Tiempo
La siguiente gráfica muestra la señal original de EMG en reposo y la señal filtrada con los tres filtros (FIR, Butterworth, Chebyshev) en el dominio del tiempo. La señal fue capturada con una frecuencia de muestreo de 1000 Hz.

![image](https://github.com/user-attachments/assets/505bbe5a-ad65-48fd-b9c9-6e464b70f41f)
![image](https://github.com/user-attachments/assets/b4d0b085-fec7-415f-ba4d-5c617b1ff424)
![image](https://github.com/user-attachments/assets/c7ec01c5-18d4-4bbd-81d1-93f71f70327c)
![image](https://github.com/user-attachments/assets/61ec7efd-c9a0-427d-ac66-d156626a3c5c)

#### Gráfica en el Dominio de la Frecuencia
Se presenta el espectro de frecuencia de la señal original y filtrada, calculado mediante la Transformada de Fourier.

![image](https://github.com/user-attachments/assets/8d299c32-e908-4feb-b7e3-fd97e4e847ed)
![image](https://github.com/user-attachments/assets/33507ffe-a838-489e-9448-2e8d186c3bff)
![image](https://github.com/user-attachments/assets/442cfa78-b96a-4461-850e-72c94bb5d4cb)![image](https://github.com/user-attachments/assets/be72b3a0-1878-49e0-b40a-545d74daccb7)

#### Transformada Corta de Fourier (STFT)
A continuación se muestra la STFT de la señal original y filtrada, para observar cómo varía el contenido en frecuencia a lo largo del tiempo.

![image](https://github.com/user-attachments/assets/ab9da237-5d88-43cb-8145-5d8c7684fde8)
![image](https://github.com/user-attachments/assets/1817853d-5a48-43fc-93f7-937a18e9e66b)
![image](https://github.com/user-attachments/assets/b5fa78cd-9c9e-4163-b86b-f2efc25694d7)
![image](https://github.com/user-attachments/assets/a16cf5ec-a91b-4769-aedc-dda7157c6b85)

### Análisis del Filtro
#### Diagrama de Polos y Ceros
El diagrama de polos y ceros para los tres filtros (FIR, Butterworth, y Chebyshev) se presenta a continuación. Este diagrama es crucial para verificar la estabilidad del filtro.

![image](https://github.com/user-attachments/assets/4866496b-768d-40c9-b635-4af84e2beaf7)
![image](https://github.com/user-attachments/assets/552bde08-db53-4827-ba74-2a01b6939598)
![image](https://github.com/user-attachments/assets/d0ea18e1-b4d8-4e1a-b104-cfb9cace7c39)

#### Diagrama de Bode (Magnitud y Fase)
El diagrama de Bode permite observar cómo los filtros afectan la magnitud y la fase de la señal en las distintas frecuencias.

![image](https://github.com/user-attachments/assets/8700a792-54f2-43d5-af8f-86af2b85a532)
![image](https://github.com/user-attachments/assets/d9127ff6-b1db-44bd-ab78-a6f7d4d64211)
![image](https://github.com/user-attachments/assets/4cbc667f-6e3e-4f51-9bfb-3a2a9ce478e3)

---

## 2. Señal EMG - Bíceps Braquial Oposición Leve

### Análisis de la Señal
#### Gráfica en el Dominio del Tiempo
Se presenta la señal EMG durante una leve oposición del bíceps braquial y su versión filtrada con los tres filtros.

![image](https://github.com/user-attachments/assets/e6881a62-4118-4a1d-9315-e96dc5f26c06)
![image](https://github.com/user-attachments/assets/f3e46d0d-016c-4d17-a654-19a5d2f938f7)
![image](https://github.com/user-attachments/assets/aa8dcbff-3ff9-45d8-b675-d700738313f6)
![image](https://github.com/user-attachments/assets/94f11ded-be63-4cc2-a6fa-ca8765ed8eb0)

#### Gráfica en el Dominio de la Frecuencia
La Transformada de Fourier revela las frecuencias presentes en la señal original y filtrada.
![image](https://github.com/user-attachments/assets/378d7abf-f179-4466-b890-f036460579cf)
![image](https://github.com/user-attachments/assets/c076929c-e6f0-4bf8-bc8c-0df4290bad12)
![image](https://github.com/user-attachments/assets/1cadd7cf-3acd-4c67-b412-8db514ef7d3a)
![image](https://github.com/user-attachments/assets/2efe9307-935f-4a8d-976a-b553d146f7ac)

#### Transformada Corta de Fourier (STFT)
Se visualiza cómo varían las frecuencias de la señal a lo largo del tiempo.
![image](https://github.com/user-attachments/assets/c580e19f-a685-4d87-bc87-2a96ac82dbdd)
![image](https://github.com/user-attachments/assets/97968f50-d624-4892-b2be-44c515585379)
![image](https://github.com/user-attachments/assets/963c4d0d-e76c-430d-99a2-a7b5ec17d987)
![image](https://github.com/user-attachments/assets/a9584056-0507-422c-a3ea-f35723767721)

### Análisis del Filtro
#### Diagrama de Polos y Ceros
Se muestra la distribución de polos y ceros para los filtros aplicados.

![image](https://github.com/user-attachments/assets/006ecb8b-0d91-433f-ac71-66036bb9356c)
![image](https://github.com/user-attachments/assets/b8df511f-cdcf-4801-926d-a70f9049ff99)
![image](https://github.com/user-attachments/assets/33f15d3a-9ced-4473-9641-1bd36f25969f)

#### Diagrama de Bode (Magnitud y Fase)
Este diagrama ayuda a analizar el comportamiento de los filtros en frecuencia y fase.

![image](https://github.com/user-attachments/assets/5ba5f2bd-3f50-4598-af3a-520ce2304840)
![image](https://github.com/user-attachments/assets/b65529d5-c2b6-4c73-86b3-d5e2e136944b)
![image](https://github.com/user-attachments/assets/e7017782-10f9-4db1-a957-3faf309fc906)

---

## 3. Señal EMG - Bíceps Braquial Oposición Fuerte

### Análisis de la Señal
#### Gráfica en el Dominio del Tiempo
Se muestra la señal durante una contracción fuerte del bíceps, junto con las señales filtradas.

![image](https://github.com/user-attachments/assets/dc4cc763-b911-43e2-b388-e122ae811ab8)
![image](https://github.com/user-attachments/assets/5f824bd9-d50d-47df-90b3-a0a6d1d87f59)
![image](https://github.com/user-attachments/assets/eafd09c2-f7bb-43e6-913e-38d8374cae19)
![image](https://github.com/user-attachments/assets/837e7ddd-fef4-42ea-a98c-f978d016ea0d)

#### Gráfica en el Dominio de la Frecuencia
Se presenta el análisis de frecuencias de la señal mediante la Transformada de Fourier.

![image](https://github.com/user-attachments/assets/c54b83bf-5b59-40b5-9e0a-a7088ee97f23)
![image](https://github.com/user-attachments/assets/a390ba02-bd31-48bd-933a-f0f0b289b86a)
![image](https://github.com/user-attachments/assets/f300cd32-f611-43d3-89cd-537725841849)
![image](https://github.com/user-attachments/assets/cebea846-d0ab-414f-baa2-e1e006de3aa8)

#### Transformada Corta de Fourier (STFT)
La STFT permite observar la variación en frecuencia de la señal a lo largo del tiempo.

![image](https://github.com/user-attachments/assets/db596a10-185c-4772-a5dd-be083427f993)
![image](https://github.com/user-attachments/assets/08012e61-eb46-4bdc-8941-1eebd4851551)
![image](https://github.com/user-attachments/assets/835ef83f-6d19-45f0-98f6-c8cdae140906)
![image](https://github.com/user-attachments/assets/e2915fb1-33ee-49d8-835f-087f9be8c9ca)

### Análisis del Filtro
#### Diagrama de Polos y Ceros
Se analiza la estabilidad de los filtros mediante el diagrama de polos y ceros.

![image](https://github.com/user-attachments/assets/f4fbf86e-a720-47a6-997e-f010f8a88d81)
![image](https://github.com/user-attachments/assets/d95a74fe-90f4-40c6-8e23-2987eff376b0)
![image](https://github.com/user-attachments/assets/381be441-d4f9-4d21-9008-a69feeca1675)

#### Diagrama de Bode (Magnitud y Fase)
El diagrama de Bode permite visualizar la respuesta en frecuencia y fase de los filtros.

![image](https://github.com/user-attachments/assets/3091ff0f-320c-4c67-87da-e04c6eb9ac52)
![image](https://github.com/user-attachments/assets/8875ee27-bb2f-4144-a078-6adaa3d00859)
![image](https://github.com/user-attachments/assets/f1542e75-dbd3-49bd-910f-b8879d0c5926)

---

## 4. Señal ECG - Estado Basal

### Análisis de la Señal
#### Gráfica en el Dominio del Tiempo
Se presenta la señal ECG en estado basal, junto con las señales filtradas.

![image](https://github.com/user-attachments/assets/419d1b34-a1c8-4185-b237-7ea9c25835a8)
![image](https://github.com/user-attachments/assets/2cecffc0-3d47-42ff-9330-d66b3aec2cfa)
![image](https://github.com/user-attachments/assets/402191b5-997a-4b43-9a4c-2d503060d328)
![image](https://github.com/user-attachments/assets/7f07ee7e-2f62-4205-99f4-d58076345cb2)

#### Gráfica en el Dominio de la Frecuencia
Se visualiza el análisis de frecuencia de la señal mediante la Transformada de Fourier.

![image](https://github.com/user-attachments/assets/32fca7ed-b404-4e96-8389-382a84de8f4b)
![image](https://github.com/user-attachments/assets/9b36a412-51ec-436f-9cef-df888506e072)
![image](https://github.com/user-attachments/assets/7f031c38-7987-40b5-820b-3910f747ff68)
![image](https://github.com/user-attachments/assets/2905a61f-5186-474d-947c-97a010026e89)

#### Transformada Corta de Fourier (STFT)
Se analiza la variación en frecuencia a lo largo del tiempo mediante la STFT.

![image](https://github.com/user-attachments/assets/e7e4c76c-20be-447c-94df-36afdd0487d0)
![image](https://github.com/user-attachments/assets/a0246439-b4d2-4b16-877b-27478aa38d75)
![image](https://github.com/user-attachments/assets/99b7a49b-bb7f-4ccc-8afd-11a1aa182932)
![image](https://github.com/user-attachments/assets/f8b32df0-73ef-491a-b81a-d02154396936)

### Análisis del Filtro
#### Diagrama de Polos y Ceros
Análisis de los polos y ceros de los filtros aplicados.

![image](https://github.com/user-attachments/assets/016426b5-5ca7-4059-9121-699aa439ed0d)
![image](https://github.com/user-attachments/assets/8b919363-a7fa-4d28-af02-1ca2cc0a0773)
![image](https://github.com/user-attachments/assets/9ef7b0bf-59f8-416c-80ac-f0a910f91d2b)

#### Diagrama de Bode (Magnitud y Fase)
El diagrama de Bode permite visualizar cómo el filtro afecta a la señal.

![image](https://github.com/user-attachments/assets/99d9b84a-308f-4b70-8973-49da029ce1d5)
![image](https://github.com/user-attachments/assets/2a29389d-3345-47c9-86a8-d9e4b6575ef1)
![image](https://github.com/user-attachments/assets/1c1d25f4-58f8-4719-b275-ffba5190a07f)

---

## 5. Señal ECG - Estado con Respiración

### Análisis de la Señal
#### Gráfica en el Dominio del Tiempo
Se presenta la señal ECG durante la respiración y sus versiones filtradas.

![image](https://github.com/user-attachments/assets/8f1c9b93-45af-455a-b099-19cbd8748040)
![image](https://github.com/user-attachments/assets/d9d1741a-2df6-4124-93f8-0ad0ffc9a512)
![image](https://github.com/user-attachments/assets/9e9226b8-984b-49f9-9536-f41b33dc2c39)
![image](https://github.com/user-attachments/assets/262982a9-81b0-4c2f-b22e-1527279e057a)


#### Gráfica en el Dominio de la Frecuencia
Transformada de Fourier para el análisis de las frecuencias presentes.

![image](https://github.com/user-attachments/assets/d910674c-276f-4c24-8758-528677a4801b)
![image](https://github.com/user-attachments/assets/0a1403a2-c82f-4191-9d96-34a1e2e6b004)
![image](https://github.com/user-attachments/assets/fc12a922-9429-4833-87d2-9d0b4d1d3a42)
![image](https://github.com/user-attachments/assets/c20d11e6-a917-4ee7-9dbb-4b8a837ef0fc)


#### Transformada Corta de Fourier (STFT)
Visualización de la variación en frecuencia a lo largo del tiempo.

![image](https://github.com/user-attachments/assets/14009423-c3b4-490a-b79e-9388fb3f1ed9)
![image](https://github.com/user-attachments/assets/b6da7315-30b0-4308-a988-421109dfa505)
![image](https://github.com/user-attachments/assets/bf96f7a1-4b0b-4f76-93a1-d6a8d6ca0ffc)
![image](https://github.com/user-attachments/assets/ffacf8dc-5dfd-422e-acb5-a46e90e52cf8)


### Análisis del Filtro
#### Diagrama de Polos y Ceros
Diagrama de polos y ceros de los tres filtros aplicados.

![image](https://github.com/user-attachments/assets/d98f81a7-ccfe-4db0-94e5-2684d09e87f4)
![image](https://github.com/user-attachments/assets/d9f1f515-7cdc-4aaf-9b55-51842e97956b)
![image](https://github.com/user-attachments/assets/11283908-5051-4b94-9a98-34ac7810bbb8)

#### Diagrama de Bode (Magnitud y Fase)
Diagrama de Bode de la señal ECG filtrada.

![image](https://github.com/user-attachments/assets/eed74531-768d-41ca-ac8c-0491b857280e)
![image](https://github.com/user-attachments/assets/8c8f66ee-f032-44a6-bea2-d5931efdb19c)
![image](https://github.com/user-attachments/assets/7dd4101c-3d04-4a41-aeb6-a6b8cb1ae149)

---

## 6. Señal ECG - Estado sin Respiración

### Análisis de la Señal
#### Gráfica en el Dominio del Tiempo
Se presenta la señal ECG en ausencia de respiración y sus versiones filtradas.

![image](https://github.com/user-attachments/assets/25c6aa0f-f28a-458f-8216-26b46d6aab82)
![image](https://github.com/user-attachments/assets/73e20f06-00bd-4ffb-b371-fd8220246579)
![image](https://github.com/user-attachments/assets/4c2553e9-7087-4cb2-a1be-ad398c2e1074)
![image](https://github.com/user-attachments/assets/24450663-61f6-4e56-a6dd-e6a1f5497c93)

#### Gráfica en el Dominio de la Frecuencia
Se presenta el espectro de frecuencias mediante la Transformada de Fourier.

![image](https://github.com/user-attachments/assets/a6db5f71-c7c3-4feb-ac0b-18e714fc5f95)
![image](https://github.com/user-attachments/assets/e251c6f9-1e14-42c8-af1b-f6ad4909248c)
![image](https://github.com/user-attachments/assets/3542958b-8b20-4964-96bd-6f48cfd27fd4)
![image](https://github.com/user-attachments/assets/8695bc9c-6028-4fdc-b359-4e7dc50c8b57)

#### Transformada Corta de Fourier (STFT)
Se analiza la variación en frecuencia de la señal a lo largo del tiempo.

![image](https://github.com/user-attachments/assets/3d310acd-1178-43c0-ad22-7947b37e49fa)
![image](https://github.com/user-attachments/assets/a221587d-274f-4593-8ca8-46ed064e6012)
![image](https://github.com/user-attachments/assets/92d533a9-4837-486d-baa4-bd4f65d369f5)
![image](https://github.com/user-attachments/assets/8fcb6765-b5c6-4753-96f2-4377a7632c11)

### Análisis del Filtro
#### Diagrama de Polos y Ceros
Se muestran los polos y ceros de los filtros aplicados.

![image](https://github.com/user-attachments/assets/374f400f-84b6-4098-acd8-79161cc3f46e)
![image](https://github.com/user-attachments/assets/9b304f6d-9924-4ef5-80e0-be64903644c2)
![image](https://github.com/user-attachments/assets/dc83cff7-3cd3-4068-bc96-d4e32b9e7dc3)

#### Diagrama de Bode (Magnitud y Fase)
El diagrama de Bode permite analizar la respuesta del filtro en magnitud y fase.

![image](https://github.com/user-attachments/assets/23e5db46-c1c2-4bea-8536-91f4de977974)
![image](https://github.com/user-attachments/assets/ff1ebf3b-a216-43da-b076-deae7e2688ce)
![image](https://github.com/user-attachments/assets/7139f254-332b-4a3e-ba8f-d1b6d040c531)

---

## Justificación de los Filtros Aplicados

### Diferencias entre Señales EMG y ECG

Las señales **ECG** (Electrocardiograma) y **EMG** (Electromiograma) son señales biomédicas con características diferentes, lo que afecta las decisiones de filtrado:

- **Frecuencia**: Las señales ECG tienen frecuencias más bajas (entre 0.05 Hz y 100 Hz) que las señales EMG, las cuales típicamente oscilan entre 20 Hz y 500 Hz debido a la actividad muscular.
- **Ruido**: Las señales EMG suelen estar más expuestas a interferencias electromagnéticas, lo que justifica la necesidad de filtros que eliminen ruido sin afectar las frecuencias útiles. Las señales ECG, por otro lado, pueden estar afectadas por ruido de red y artefactos de movimiento, especialmente en registros largos.

A continuación, se justifica la selección de los filtros **FIR**, **Butterworth** y **Chebyshev Tipo I** para las señales EMG y ECG, junto con los parámetros específicos utilizados para cada señal.

---

### 1. Señal EMG - Bíceps Braquial en Reposo

#### Filtro FIR (Finite Impulse Response)
- **Frecuencia de corte**: Se utilizaron frecuencias de corte de **20 Hz a 450 Hz** para eliminar el ruido de baja frecuencia (como el movimiento) y las componentes de alta frecuencia (interferencias electromagnéticas).
- **Número de coeficientes (101)**: El número de coeficientes se seleccionó para proporcionar una buena precisión sin sobrecargar el procesamiento computacional.
- **Justificación**: El filtro FIR fue elegido debido a su **fase lineal**, que es crucial para no distorsionar la forma de la señal EMG en reposo, donde los picos de activación muscular deben preservarse para un análisis preciso de la actividad.

#### Filtro Butterworth (IIR)
- **Frecuencia de corte**: **20 Hz a 450 Hz**.
- **Orden 5**: Proporciona una atenuación suave en la banda de paso, permitiendo que las frecuencias importantes de la señal EMG permanezcan intactas.
- **Justificación**: El filtro Butterworth es adecuado para eliminar el ruido sin introducir distorsiones graves en la amplitud de la señal. Es computacionalmente más eficiente que el FIR y mantiene las características generales de la señal en reposo.

#### Filtro Chebyshev Tipo I (IIR)
- **Frecuencia de corte**: **20 Hz a 450 Hz**.
- **Orden 5 con ondulación de 5 dB**: El filtro Chebyshev atenua rápidamente las frecuencias fuera de la banda de paso, lo que es útil para eliminar interferencias de alta frecuencia.
- **Justificación**: Aunque introduce ondulaciones en la banda de paso, el filtro Chebyshev es eficaz para eliminar interferencias electromagnéticas que suelen afectar las señales EMG en reposo.

---

### 2. Señal EMG - Bíceps Braquial Oposición Leve

#### Filtro FIR (Finite Impulse Response)
- **Frecuencia de corte**: Se utiliza el mismo rango de **20 Hz a 450 Hz**. Durante una leve contracción muscular, las frecuencias útiles se encuentran dentro de este intervalo.
- **Número de coeficientes (101)**: Permite una transición suave entre la banda de paso y la banda de rechazo, asegurando una separación precisa de las frecuencias útiles.
- **Justificación**: El filtro FIR se utiliza por su **fase lineal**, lo que garantiza que no se distorsione la temporalidad ni la forma de los picos de activación muscular durante la leve contracción.

#### Filtro Butterworth (IIR)
- **Frecuencia de corte**: **20 Hz a 450 Hz**.
- **Orden 5**: Proporciona una atenuación suave en la banda de paso y asegura que las frecuencias importantes se mantengan.
- **Justificación**: El filtro Butterworth es útil para eliminar ruido de alta frecuencia, siendo eficiente y manteniendo las características principales de la señal muscular.

#### Filtro Chebyshev Tipo I (IIR)
- **Frecuencia de corte**: **20 Hz a 450 Hz**.
- **Orden 5 con ondulación de 5 dB**: Este filtro atenua rápidamente las frecuencias fuera de la banda de paso, eliminando eficazmente interferencias no deseadas.
- **Justificación**: Ideal para eliminar ruidos electromagnéticos más agresivos que pueden afectar la señal EMG durante una contracción leve.

---

### 3. Señal EMG - Bíceps Braquial Oposición Fuerte

#### Filtro FIR (Finite Impulse Response)
- **Frecuencia de corte**: **20 Hz a 450 Hz**. Las señales EMG durante una contracción fuerte pueden contener frecuencias más altas, pero este rango es adecuado para eliminar ruido y preservar la señal muscular relevante.
- **Número de coeficientes (101)**: Este número de coeficientes asegura una buena transición sin complejidad computacional excesiva.
- **Justificación**: Se utiliza el FIR para preservar la fase y la forma de la señal muscular durante una contracción fuerte, donde la fase lineal es crucial para analizar la actividad muscular sin distorsión.

#### Filtro Butterworth (IIR)
- **Frecuencia de corte**: **20 Hz a 450 Hz**.
- **Orden 5**: Proporciona una atenuación suave en la banda de paso sin alterar las frecuencias importantes de la señal.
- **Justificación**: El filtro Butterworth es eficiente para eliminar interferencias externas durante contracciones musculares fuertes, manteniendo las características generales de la señal EMG.

#### Filtro Chebyshev Tipo I (IIR)
- **Frecuencia de corte**: **20 Hz a 450 Hz**.
- **Orden 5 con ondulación de 5 dB**: Este filtro proporciona una atenuación rápida en la banda de rechazo, útil para eliminar interferencias electromagnéticas.
- **Justificación**: Ideal para eliminar ruidos de alta frecuencia de manera agresiva durante una fuerte contracción, sin sacrificar la calidad de la señal en la banda de paso.

---

### 4. Señal ECG - Estado Basal

#### Filtro FIR (Finite Impulse Response)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**. Este rango de frecuencias es adecuado para señales ECG, ya que preserva las ondas cardíacas (ondas P, QRS, T) y elimina componentes de baja frecuencia (movimiento del paciente) y alta frecuencia (ruido de red).
- **Número de coeficientes (101)**: Proporciona una transición suave, permitiendo que la señal ECG no sea afectada por interferencias de alta y baja frecuencia.
- **Justificación**: El FIR fue elegido para garantizar que la señal no se vea distorsionada en términos de fase, lo que es crucial para el análisis clínico de las ondas cardíacas.

#### Filtro Butterworth (IIR)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**.
- **Orden 5**: Proporciona una atenuación suave de las frecuencias fuera de la banda de interés.
- **Justificación**: El Butterworth es ideal para señales ECG porque permite mantener la amplitud de las ondas importantes y eliminar ruido de alta frecuencia.

#### Filtro Chebyshev Tipo I (IIR)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**.
- **Orden 5 con ondulación de 5 dB**: Este filtro atenua rápidamente las frecuencias no deseadas fuera de la banda de paso.
- **Justificación**: Aunque introduce ondulaciones en la banda de paso, el Chebyshev es adecuado para eliminar rápidamente ruido de red o interferencias electromagnéticas que pueden afectar las señales ECG en estado basal.

---

### 5. Señal ECG - Estado con Respiración

#### Filtro FIR (Finite Impulse Response)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**, adecuado para preservar las frecuencias cardíacas mientras se eliminan interferencias debidas al movimiento del paciente.
- **Número de coeficientes (101)**: Permite una transición suave entre las frecuencias útiles y el ruido.
- **Justificación**: El FIR garantiza que la fase de la señal ECG no se vea afectada, lo que es esencial para un análisis preciso de las ondas cardíacas, especialmente en la presencia de ruido debido a la respiración.

#### Filtro Butterworth (IIR)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**.
- **Orden 5**: Proporciona una atenuación suave en la banda de paso.
- **Justificación**: El filtro Butterworth es ideal para eliminar ruido de baja frecuencia debido a la respiración, preservando las características esenciales de la señal ECG.

#### Filtro Chebyshev Tipo I (IIR)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**.
- **Orden 5 con ondulación de 5 dB**: Permite una atenuación rápida fuera de la banda de paso.
- **Justificación**: Adecuado para eliminar ruidos

 electromagnéticos que pueden afectar la señal ECG durante la respiración, aunque introduce ondulaciones en la banda de paso.

---

### 6. Señal ECG - Estado sin Respiración

#### Filtro FIR (Finite Impulse Response)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**. Este rango es adecuado para eliminar el ruido de baja y alta frecuencia sin afectar las ondas cardíacas.
- **Número de coeficientes (101)**: Proporciona una buena precisión sin añadir complejidad computacional excesiva.
- **Justificación**: El FIR asegura que la señal ECG no sea distorsionada en términos de fase, lo que es fundamental para el análisis detallado de las ondas cardíacas.

#### Filtro Butterworth (IIR)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**.
- **Orden 5**: Mantiene la atenuación suave de las frecuencias fuera de la banda de interés.
- **Justificación**: El Butterworth es útil para eliminar ruido de alta frecuencia, asegurando que las características de la señal ECG no se vean alteradas.

#### Filtro Chebyshev Tipo I (IIR)
- **Frecuencia de corte**: **0.5 Hz a 40 Hz**.
- **Orden 5 con ondulación de 5 dB**: Asegura una atenuación rápida de las frecuencias no deseadas fuera de la banda de paso.
- **Justificación**: El Chebyshev es eficaz para eliminar interferencias electromagnéticas, aunque puede introducir ondulaciones en la banda de paso, es útil para eliminar rápidamente ruidos externos.

---
# Código PYTHON
## Señales EMG y ECG
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, butter, cheby1, freqz, spectrogram

# Cargar la señal desde el archivo .txt correspondiente
data = np.loadtxt(r'D:\Señales ECG\Señal EMG - bicep braquial en reposo.txt', skiprows=4)
emg_reposo = data[:, 5] 
fs = 1000  # Frecuencia de muestreo en Hz

# --- Parámetros de los filtros ---
cutoff_frequencies = [20, 450]  # Frecuencias de corte para la señal EMG (en Hz)
numtaps_fir = 101  # Número de coeficientes del filtro FIR
butter_order = 5  # Orden del filtro Butterworth (IIR)
cheby_order = 5  # Orden del filtro Chebyshev (IIR)
ripple = 5  # Ondulación para el filtro Chebyshev (IIR)

# --- Filtro FIR ---
filtro_fir = firwin(numtaps_fir, cutoff_frequencies, pass_zero=False, fs=fs)
emg_fir_filtered = lfilter(filtro_fir, 1.0, emg_reposo)

# --- Filtro IIR Butterworth ---
b_butter, a_butter = butter(butter_order, [20 / (fs / 2), 450 / (fs / 2)], btype='band')
emg_butter_filtered = lfilter(b_butter, a_butter, emg_reposo)

# --- Filtro IIR Chebyshev Tipo I ---
b_cheby, a_cheby = cheby1(cheby_order, ripple, [20 / (fs / 2), 450 / (fs / 2)], btype='band')
emg_cheby_filtered = lfilter(b_cheby, a_cheby, emg_reposo)

# --- Función para realizar la Transformada de Fourier ---
def plot_frequency_spectrum(signal, fs, title):
    N = len(signal)
    f_signal = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, 1/fs)
    
    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:N//2], np.abs(f_signal)[:N//2], color='green')
    plt.title(title)
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud')
    plt.grid(True)
    plt.show()

# --- Función para realizar la STFT (Transformada Corta de Fourier) ---
def plot_stft(signal, fs, title):
    f, t, Sxx = spectrogram(signal, fs, nperseg=256)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.title(title)
    plt.ylabel('Frecuencia [Hz]')
    plt.xlabel('Tiempo [s]')
    plt.colorbar(label='Potencia [dB]')
    plt.show()

# --- Gráficas para la señal original ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(emg_reposo)) / fs, emg_reposo, color='blue')
plt.title("Señal Original EMG - Reposo (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(emg_reposo, fs, "Espectro de Frecuencia de la Señal Original - EMG Reposo")

# STFT (Transformada Corta de Fourier)
plot_stft(emg_reposo, fs, "STFT - Señal Original EMG Reposo")

# --- Gráficas para la señal filtrada con Filtro FIR ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(emg_fir_filtered)) / fs, emg_fir_filtered, color='green')
plt.title("Señal Filtrada con Filtro FIR - EMG Reposo (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(emg_fir_filtered, fs, "Espectro de Frecuencia - Filtro FIR (EMG Reposo)")

# STFT (Transformada Corta de Fourier)
plot_stft(emg_fir_filtered, fs, "STFT - Filtro FIR (EMG Reposo)")

# --- Gráficas para la señal filtrada con Filtro IIR Butterworth ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(emg_butter_filtered)) / fs, emg_butter_filtered, color='orange')
plt.title("Señal Filtrada con Filtro Butterworth (IIR) - EMG Reposo (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(emg_butter_filtered, fs, "Espectro de Frecuencia - Filtro Butterworth (EMG Reposo)")

# STFT (Transformada Corta de Fourier)
plot_stft(emg_butter_filtered, fs, "STFT - Filtro Butterworth (EMG Reposo)")

# --- Gráficas para la señal filtrada con Filtro IIR Chebyshev ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(emg_cheby_filtered)) / fs, emg_cheby_filtered, color='red')
plt.title("Señal Filtrada con Filtro Chebyshev (IIR) - EMG Reposo (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(emg_cheby_filtered, fs, "Espectro de Frecuencia - Filtro Chebyshev (EMG Reposo)")

# STFT (Transformada Corta de Fourier)
plot_stft(emg_cheby_filtered, fs, "STFT - Filtro Chebyshev (EMG Reposo)")
# --- Diagrama de Polos y Ceros ---
def plot_pole_zero(b, a, title):
    z, p, _ = tf2zpk(b, a)
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros', color='blue')
    plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos', color='red')
    plt.title(title)
    plt.xlabel("Parte Real")
    plt.ylabel("Parte Imaginaria")
    plt.grid(True)
    plt.legend()
    plt.show()

# --- Diagrama de Bode ---
def plot_bode(b, a, fs, title):
    w, h = freqz(b, a, worN=2000)
    plt.figure(figsize=(10, 6))

    # Magnitud
    plt.subplot(2, 1, 1)
    plt.plot(w * fs / (2 * np.pi), 20 * np.log10(abs(h)), color='green')
    plt.title(title + " - Magnitud")
    plt.ylabel("Magnitud [dB]")
    plt.grid(True)

    # Fase
    plt.subplot(2, 1, 2)
    plt.plot(w * fs / (2 * np.pi), np.angle(h), color='purple')
    plt.title(title + " - Fase")
    plt.ylabel("Fase [radianes]")
    plt.xlabel("Frecuencia [Hz]")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# --- Análisis del filtro FIR ---
# FIR tiene solo ceros, ya que es un filtro de respuesta finita
plot_pole_zero(filtro_fir, [1], "Diagrama de Polos y Ceros - Filtro FIR")
plot_bode(filtro_fir, [1], fs, "Diagrama de Bode - Filtro FIR")

# --- Análisis del filtro IIR Butterworth ---
plot_pole_zero(b_butter, a_butter, "Diagrama de Polos y Ceros - Filtro Butterworth")
plot_bode(b_butter, a_butter, fs, "Diagrama de Bode - Filtro Butterworth")

# --- Análisis del filtro IIR Chebyshev ---
plot_pole_zero(b_cheby, a_cheby, "Diagrama de Polos y Ceros - Filtro Chebyshev")
plot_bode(b_cheby, a_cheby, fs, "Diagrama de Bode - Filtro Chebyshev")

----------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, butter, cheby1, freqz, spectrogram, tf2zpk

# Cargar la señal desde el archivo .txt correspondiente
data = np.loadtxt(r'D:\Señales ECG\Señal ECG - Estado basal.txt', skiprows=4)
ecg_basal = data[:, 5] 
fs = 1000  # Frecuencia de muestreo en Hz para señales ECG

# --- Parámetros de los filtros para ECG ---
cutoff_frequencies = [0.5, 40]  # Frecuencias de corte para la señal ECG (en Hz)
numtaps_fir = 101  # Número de coeficientes del filtro FIR
butter_order = 5  # Orden del filtro Butterworth (IIR)
cheby_order = 5  # Orden del filtro Chebyshev (IIR)
ripple = 5  # Ondulación para el filtro Chebyshev (IIR)

# --- Filtro FIR ---
filtro_fir = firwin(numtaps_fir, cutoff_frequencies, pass_zero=False, fs=fs)
ecg_fir_filtered = lfilter(filtro_fir, 1.0, ecg_basal)

# --- Filtro IIR Butterworth ---
b_butter, a_butter = butter(butter_order, [0.5 / (fs / 2), 40 / (fs / 2)], btype='band')
ecg_butter_filtered = lfilter(b_butter, a_butter, ecg_basal)

# --- Filtro IIR Chebyshev Tipo I ---
b_cheby, a_cheby = cheby1(cheby_order, ripple, [0.5 / (fs / 2), 40 / (fs / 2)], btype='band')
ecg_cheby_filtered = lfilter(b_cheby, a_cheby, ecg_basal)

# --- Función para realizar la Transformada de Fourier ---
def plot_frequency_spectrum(signal, fs, title):
    N = len(signal)
    f_signal = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, 1/fs)
    
    plt.figure(figsize=(10, 4))
    plt.plot(freqs[:N//2], np.abs(f_signal)[:N//2], color='green')
    plt.title(title)
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud')
    plt.grid(True)
    plt.show()

# --- Función para realizar la STFT (Transformada Corta de Fourier) ---
def plot_stft(signal, fs, title):
    f, t, Sxx = spectrogram(signal, fs, nperseg=256)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.title(title)
    plt.ylabel('Frecuencia [Hz]')
    plt.xlabel('Tiempo [s]')
    plt.colorbar(label='Potencia [dB]')
    plt.show()

# --- Gráficas para la señal original ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(ecg_basal)) / fs, ecg_basal, color='blue')
plt.title("Señal Original ECG - Estado Basal (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(ecg_basal, fs, "Espectro de Frecuencia de la Señal Original - ECG Estado Basal")

# STFT (Transformada Corta de Fourier)
plot_stft(ecg_basal, fs, "STFT - Señal Original ECG Estado Basal")

# --- Gráficas para la señal filtrada con Filtro FIR ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(ecg_fir_filtered)) / fs, ecg_fir_filtered, color='green')
plt.title("Señal Filtrada con Filtro FIR - ECG Estado Basal (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(ecg_fir_filtered, fs, "Espectro de Frecuencia - Filtro FIR (ECG Estado Basal)")

# STFT (Transformada Corta de Fourier)
plot_stft(ecg_fir_filtered, fs, "STFT - Filtro FIR (ECG Estado Basal)")

# --- Gráficas para la señal filtrada con Filtro IIR Butterworth ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(ecg_butter_filtered)) / fs, ecg_butter_filtered, color='orange')
plt.title("Señal Filtrada con Filtro Butterworth (IIR) - ECG Estado Basal (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(ecg_butter_filtered, fs, "Espectro de Frecuencia - Filtro Butterworth (ECG Estado Basal)")

# STFT (Transformada Corta de Fourier)
plot_stft(ecg_butter_filtered, fs, "STFT - Filtro Butterworth (ECG Estado Basal)")

# --- Gráficas para la señal filtrada con Filtro IIR Chebyshev ---
# Dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(np.arange(len(ecg_cheby_filtered)) / fs, ecg_cheby_filtered, color='red')
plt.title("Señal Filtrada con Filtro Chebyshev (IIR) - ECG Estado Basal (Dominio del Tiempo)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Dominio de la frecuencia (Transformada de Fourier)
plot_frequency_spectrum(ecg_cheby_filtered, fs, "Espectro de Frecuencia - Filtro Chebyshev (ECG Estado Basal)")

# STFT (Transformada Corta de Fourier)
plot_stft(ecg_cheby_filtered, fs, "STFT - Filtro Chebyshev (ECG Estado Basal)")

# --- Diagrama de Polos y Ceros ---
def plot_pole_zero(b, a, title):
    z, p, _ = tf2zpk(b, a)
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros', color='blue')
    plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos', color='red')
    plt.title(title)
    plt.xlabel("Parte Real")
    plt.ylabel("Parte Imaginaria")
    plt.grid(True)
    plt.legend()
    plt.show()

# --- Diagrama de Bode ---
def plot_bode(b, a, fs, title):
    w, h = freqz(b, a, worN=2000)
    plt.figure(figsize=(10, 6))

    # Magnitud
    plt.subplot(2, 1, 1)
    plt.plot(w * fs / (2 * np.pi), 20 * np.log10(abs(h)), color='green')
    plt.title(title + " - Magnitud")
    plt.ylabel("Magnitud [dB]")
    plt.grid(True)

    # Fase
    plt.subplot(2, 1, 2)
    plt.plot(w * fs / (2 * np.pi), np.angle(h), color='purple')
    plt.title(title + " - Fase")
    plt.ylabel("Fase [radianes]")
    plt.xlabel("Frecuencia [Hz]")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# --- Análisis del filtro FIR ---
# FIR tiene solo ceros, ya que es un filtro de respuesta finita
plot_pole_zero(filtro_fir, [1], "Diagrama de Polos y Ceros - Filtro FIR")
plot_bode(filtro_fir, [1], fs, "Diagrama de Bode - Filtro FIR")

# --- Análisis del filtro IIR Butterworth ---
plot_pole_zero(b_butter, a_butter, "Diagrama de Polos y Ceros - Filtro Butterworth")
plot_bode(b_butter, a_butter, fs, "Diagrama de Bode - Filtro Butterworth")

# --- Análisis del filtro IIR Chebyshev ---
plot_pole_zero(b_cheby, a_cheby, "Diagrama de Polos y Ceros - Filtro Chebyshev")
plot_bode(b_cheby, a_cheby, fs, "Diagrama de Bode - Filtro Chebyshev")

