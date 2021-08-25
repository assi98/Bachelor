# TDAT3001 Bacheloroppgave Dataingeniør 2021
## Systemdokumentasjon

### Introduksjon
Dokumentet er skrevet i forbindelse med faget TDAT3001 Bacheloroppgave Dataingeniør våren 2021. Hensikten med dokumentet er å gi en beskrivelse av systemet som er laget, og inneholder dermed informasjon på kode og avhengigheter som er benyttet.

Lenke til vårt GitHub Repository: https://gitlab.stud.idi.ntnu.no/asbjorfk/vehicle-parts-detection
___

### Prosjektstruktur

 * frame_extraction.py - inneholder kode for genereing av frames ut fra en video
 * generate_train_and_valid_data.py - inneholder kode som forenkler prosessen med innedeling av trenings- og valideringsdata i Darknet.

Kjør følgende kommando for installasjon av nødvendige biblioteker:
> pip install -r requirements.txt
___

### Installasjon og kjøring

De viktigste eksterne avhengighetene/programvarebibliotekene som har blitt brukt i prosjektet er listet nedenfor:

* [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet) - Rammeverk for trening av YOLO-modeller. 
* [tzutalin/labelImg](https://github.com/tzutalin/labelImg) - Program brukt for labeling av frames.
* [theAIGuysCode/yolo4-custom-functions](https://github.com/theAIGuysCode/yolov4-custom-functions) - Repository med kode for å konvertere modeller fra Darknet til TensorFlow. Repoet inneholder også kode for deteksjon på biler og video. Modifikasjoner er gjort for å tegne ground truth bokser, og kan brukes ved å klone vår fork av repoet: [our-yolo-custom-functions](https://gitlab.stud.idi.ntnu.no/miafo/our-yolo-custom-functions). Prosessen med å installere nødvendige biblioteker, samt konvertering av modell, gjøres på tilsvarende måte som for den originale koden. Dersom det er ønskelig å benytte vår kode for tegning av ground truth bokser må følgende kommando brukes:

> python detect.py --weights ./checkpoints/yolov4-tiny-416 --size 416 --model yolov4 --images ./data/test-data.txt --tiny --output ./detections/ --dont_show --ground_truth

* [theAIGuysCode/yolov4-deepsort](https://github.com/theAIGuysCode/yolov4-deepsort) - Repository med kode for konvertering av Darknet-modeller til TensorFlow, samt implementasjon av objektsporingsalgoritmen DeepSORT. Dette repositoriet ble brukt som sjekk på hvordan de trente YOLO-modellene fungerte med sporing. 
 * [protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf/releases?fbclid=IwAR12YGQMJ77evhzfdu2_h2YdZecCu7EHYUCXDx9Zc1iHh-DjETO_exycIfU) - Repository med kode brukt i forbinelse med trening av SSD, og er nødvendig for å konfigurere modeller og trene parametre.
* [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) - Repository med kode for trening av objektdetekteringsmodeller med TensorFlow.  Brukt i forbindelse med trening av SSD-modeller.

 

