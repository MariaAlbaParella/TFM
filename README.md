# Detecció d’àrees cerebrals alterades en TEA, mitjançant segmentació automatitzada i aprenentatge profund d’imatges MRI

Aquest repositori conté el codi en python desenvolupat pel projecte de final del Master de Bioinformàtic i Bioestadística de la UOC i la UB.

La finalitat d’aquest projecte és detectar diferencies estructurals i patrons anòmals de desenvolupament cerebral en persones dins el trastorn de l’espectre autista (TEA), un trastorn del neurodesenvolupament sense causes específiques conegudes i sense biomarcadors objectius robusts. L’estudi s’aborda des d’una perspectiva neurocientífica amb el doble objectiu d’identificar possibles biomarcadors que puguin esdevenir dianes per a teràpies personalitzades i de desenvolupar un model d’intel·ligència artificial capaç de discriminar entre individus TEA i Control per facilitar el diagnòstic. Per dur a terme l’anàlisi es fan servir imatges de ressonància magnètica (RMI) del projecte [ABIDE II](https://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html). La segmentació de les regions cerebrals s’ha realitzat amb [Synthseg](https://www.pnas.org/doi/10.1073/pnas.2216399120), una eina basada en xarxes neuronals convolucionals integrada dins el paquet FreeSurfer.

## 🧪 Laboratoris:

Per a aquest projecte s'han seleccionat les dades dels següents laboratoris:


<table style="background:white;">
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/9310d54d-18f3-4211-80c3-26aa7bb9b9e5" height="120"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/2be25ba8-35f1-4d7d-a95b-84b8cdc70595" height="120"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/de2cc907-bf16-4f5e-abe0-591a650139bf" height="120"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/17346de4-f60e-4d0e-8f5a-51406e3b3849" height="120"></td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/ad60d5ab-cd9a-499e-abeb-1bcda00822cc" height="120"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/19227e4f-3743-4111-a6dc-c356fcc04a42" height="120"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/8d654f14-4d31-46e5-bf35-04769e351e24" height="120"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/7e16a2c3-421a-4d35-9719-0ee0cbd2a9c0" height="120"></td>
  </tr>
</table>



Les dades es poden descarregar a través de la plataforma [NITRC](http://www.nitrc.org/), per poder accedir-hi, cal registrar-se com a usuari a la plataforma.



## 📁 Organització del codi

## 🐍 Script inicial

### `0_Organitzacio_dades.py`

Script de Python pensat per executar-se en mode local. Serveix per estructurar les dades descarregades del projecte **ABIDE II**:

- Extreu els arxius `anat.nii.gz` ubicats a `\\session_1\\anat_1\\` de cada subjecte.
- Identifica cada imatge segons l’ID del subjecte.
- Trasllada totes les imatges a una mateixa carpeta per automatitzar el processament posterior.



<img width="1105" height="303" alt="estructurar dades" src="https://github.com/user-attachments/assets/c116a7bb-ad8c-4518-881a-888d310e1faa" />


Aquest arxiu nomès fa falta si es vol executar les dades desde zero:

1. descarregar dades dels laboratoris
2. estructurar i renombrar arxius
3. executar segmentacions amb *mri_synthseg* (executar la seqüència de processat amb freesurfer).

---

### 📂 Carpeta `CSV/`

Conté tots els arxius necessaris per al correcte funcionament dels scripts:

| Arxiu | Descripció |
|-------|------------|
| **ABIDEII_Composite_Phenotypic.csv** | Dades fenotípiques de tots els subjectes i laboratoris d’ABIDE II. |
| **qc.csv** | Puntuacions de control de qualitat retornades per *mri_synthseg*. |
| **Vol.csv** | Volums de les regions cerebrals retornats per *mri_synthseg*. |
| **Dataset_to_Check_qc.csv** | Vinculació entre `qc.csv` i `ABIDEII_Composite_Phenotypic.csv`. |
| **Dataset_to_Check_vol.csv** | Vinculació entre `vol.csv` i `ABIDEII_Composite_Phenotypic.csv`. |
| **volums.csv** | Arxiu resultant després d’eliminar imatges incorrectes. |
| **harmonized_data.csv** | Volums de les regions cerebrals harmonitzades. |
| **harmonized_ICV_data.csv** | Volum intracranial total harmonitzat. |

---

### Seqüència de processat amb FreeSurfer

Els passos seguits per executar la comanda `recon-all` de FreeSurfer per al subjecte amb **ID = 29057** són:

#### 1. Configurar l’entorn de treball de FreeSurfer

```bash
export FREESURFER_HOME="/Applications/freesurfer/7.4.1"
source $FREESURFER_HOME/SetUpFreeSurfer.sh
```

#### 2. Establir la ruta de ```SUBJECTS_DIR

```bash
export SUBJECTS_DIR=/Documents/TFM/test
```

#### 3. Executar segmentacions

```bash
mri_synthseg --i ABIDE_RAW \
  --o ABIDE_DATA \
  --qc qc_T1 \
  --vol vol_T1.csv
```
Paràmetres:

- `--i`: carpeta amb arxius a processar
- `--o`: carpeta de sortida
- `--qc`: puntuacions de control de qualitat en CSV
- `--vol`: volums regionals en CSV

---

## 📓 Notebooks de Google Colab

Els notebooks estant pensats per executar-se desde colab i poder reproduir els anàlisis sense modificar rutes, cal copiar la carpeta CSV a la mateixa carpeta del drive on s'estigui executant l'script.

A la carpeta csv hi ha tots els arxius generats, es poden executar els colabs de manera saltada (es pot anar directe al 5 si interessa)

### 1️⃣ **1_Dataset_Treball.ipynb**

Vincula els arxius generats per *mri_synthseg* amb les dades fenotípiques d’ABIDE II.

**Entrada:**
- `ABIDEII_Composite_Phenotypic.csv`
- `qc.csv`
- `Vol.csv`

**Sortida:**
- `Dataset_to_Check_qc.csv`
- `Dataset_to_Check_vol.csv`

---

### 2️⃣ **2_QC_Dataset_Treball.ipynb**

Control de qualitat de les dades i eliminació d’imatges incorrectes.

**Entrada:**
- `Dataset_to_Check_qc.csv`
- `Dataset_to_Check_vol.csv`

**Sortida:**
- `Volums.csv`

---

### 3️⃣ **3_Harmonitzar_Dataset.ipynb**

Executa la harmonització per eliminar l’efecte de diferents escàners i protocols d’adquisició.

**Entrada:**
- `Volums.csv`

**Sortida:**
- `harmonized_data.csv`
- `harmonized_ICV_data.csv`

---

### 4️⃣ **4_Analysis.ipynb**

Anàlisi estadístic corresponent a la fase de *tècniques clàssiques*.

**Entrada:**
- `harmonized_data.csv`
- `harmonized_ICV_data.csv`

---

### 5️⃣ **Avaluacio_Algoritmes.ipynb**

Avaluació de diferents algoritmes de *Machine Learning* i selecció del més prometedor.

**Entrada:**
- `harmonized_data.csv`

---

### 6️⃣ **5_Analysis_ML.ipynb**

Ajust del model de *Machine Learning* seleccionat.

**Entrada:**
- `harmonized_data.csv`

---

### 7️⃣ **6_CatBoost_OneOut.ipynb**

Validació de la capacitat de generalització del model mitjançant el mètode **Leave-One-Group-Out**.

**Entrada:**
- `harmonized_data.csv`






