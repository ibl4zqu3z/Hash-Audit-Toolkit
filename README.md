# Hash Audit Toolkit

Herramienta en Python para análisis, verificación y auditoría controlada de hashes en entornos autorizados.

---

## Descripción

Hash Audit Toolkit es una utilidad CLI orientada a profesionales de seguridad que necesitan analizar hashes, verificar integridad de datos y detectar debilidades en el almacenamiento de contraseñas sin recurrir a técnicas ofensivas de cracking masivo.

---

## Objetivos del proyecto

- Identificar algoritmos hash probables a partir de longitud y formato
- Generar hashes de texto de forma controlada
- Validar coincidencias frente a hashes esperados
- Auditar hashes con wordlists autorizadas
- Verificar integridad de ficheros
- Exportar resultados en JSON
- Proporcionar una CLI clara, documentada y extensible

---

## Características principales

- Identificación de hash por patrón y longitud
- Soporte para `md5`, `sha1`, `sha224`, `sha256`, `sha384` y `sha512`
- Verificación opcional contra un hash esperado
- Auditoría controlada mediante diccionarios autorizados
- Exportación de informes JSON con `--report`
- Salida consistente en formato JSON
- Ayuda integrada con `--help`
- Arquitectura modular preparada para crecer

---

## Estructura del proyecto

```text
hash-audit-toolkit/
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
├── .gitignore
├── hash_audit/
│   ├── __init__.py
│   ├── cli.py
│   ├── detector.py
│   ├── verifier.py
│   ├── auditor.py
│   ├── filehash.py
│   ├── reporter.py
│   └── utils.py
├── wordlists/
│   └── demo.txt
├── examples/
│   ├── sample_hashes.txt
│   └── sample_report.json
└── tests/
    ├── test_detector.py
    ├── test_verifier.py
    └── test_auditor.py
```

---

## Instalación

### Linux / macOS

```bash
git clone https://github.com/TU_USUARIO/hash-audit-toolkit.git
cd hash-audit-toolkit
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows

```powershell
git clone https://github.com/TU_USUARIO/hash-audit-toolkit.git
cd hash-audit-toolkit
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> `requirements.txt` se mantiene mínimo porque el proyecto usa librería estándar.

---

## Ayuda integrada

La herramienta incorpora ayuda en tres niveles.

### Ayuda general

```bash
python main.py --help
```

### Ayuda por comando

```bash
python main.py identify --help
python main.py verify --help
python main.py audit --help
python main.py filehash --help
```

---

## Comandos disponibles

### `identify`

Identifica algoritmos hash probables a partir de la longitud y el patrón hexadecimal del valor proporcionado.

#### Sintaxis

```bash
python main.py identify <hash>
```

#### Ejemplo

```bash
python main.py identify 5f4dcc3b5aa765d61d8327deb882cf99
```

#### Salida esperada

```json
{
  "hash": "5f4dcc3b5aa765d61d8327deb882cf99",
  "length": 32,
  "possible_algorithms": [
    "MD5"
  ],
  "notes": [
    "MD5 es débil para contraseñas."
  ]
}
```

#### Argumentos

- `hash_value`: hash a identificar

---

### `verify`

Genera el hash de un texto utilizando el algoritmo indicado. También puede comparar el resultado con un hash esperado.

#### Sintaxis

```bash
python main.py verify --text "<texto>" --algorithm <algoritmo> [--expected <hash>]
```

#### Ejemplos

```bash
python main.py verify --text "hola123" --algorithm sha256
python main.py verify --text "hola123" --algorithm md5 --expected 6d48c98f40391c180df3f27b8c63b3fc
```

#### Argumentos y opciones

- `--text`: texto de entrada
- `--algorithm`: algoritmo hash a utilizar  
  Valores permitidos: `md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`
- `--expected`: hash esperado para comparación opcional

---

### `audit`

Audita un hash comparándolo con una wordlist autorizada. Puede inferir el algoritmo por longitud o recibirlo explícitamente. También permite exportar un informe JSON.

#### Sintaxis

```bash
python main.py audit --hash <hash> --wordlist <ruta> [--algorithm <algoritmo>] [--report <fichero.json>]
```

#### Ejemplos

```bash
python main.py audit --hash 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist wordlists/demo.txt
python main.py audit --hash 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist wordlists/demo.txt --algorithm md5
python main.py audit --hash 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist wordlists/demo.txt --report informe.json
```

#### Argumentos y opciones

- `--hash`: hash objetivo
- `--wordlist`: ruta a la wordlist autorizada
- `--algorithm`: algoritmo hash si se conoce
- `--report`: ruta para guardar un informe JSON

#### Ejemplo de informe

```json
{
  "status": "match",
  "summary": "Coincidencia encontrada en la wordlist autorizada.",
  "hash": "5f4dcc3b5aa765d61d8327deb882cf99",
  "algorithm": "md5",
  "matched_plaintext": "password",
  "checked_candidates": 2,
  "risk": "high",
  "recommendations": [
    "Restablecer la contraseña.",
    "Usar Argon2, bcrypt o scrypt.",
    "Aplicar sal única por credencial.",
    "Revisar reutilización de credenciales en el entorno auditado."
  ]
}
```

---

### `filehash`

Calcula el hash de un fichero para verificación de integridad.

#### Sintaxis

```bash
python main.py filehash <ruta_fichero> [--algorithm <algoritmo>]
```

#### Ejemplos

```bash
python main.py filehash documento.pdf
python main.py filehash documento.pdf --algorithm sha512
```

#### Argumentos y opciones

- `filepath`: ruta del fichero
- `--algorithm`: algoritmo hash  
  Valor por defecto: `sha256`

---

## Resumen rápido de argumentos

### `identify`
- `hash_value`

### `verify`
- `--text`
- `--algorithm`
- `--expected`

### `audit`
- `--hash`
- `--wordlist`
- `--algorithm`
- `--report`

### `filehash`
- `filepath`
- `--algorithm`

---

## Flujo de uso recomendado

### 1. Identificación inicial del hash

```bash
python main.py identify 5f4dcc3b5aa765d61d8327deb882cf99
```

### 2. Verificación del comportamiento del algoritmo

```bash
python main.py verify --text "password" --algorithm md5
```

### 3. Auditoría controlada con wordlist autorizada

```bash
python main.py audit --hash 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist wordlists/demo.txt --report informe.json
```

### 4. Verificación de integridad de ficheros

```bash
python main.py filehash README.md --algorithm sha256
```

---

## Casos de uso legítimos

- Auditorías internas de seguridad
- Revisión de políticas de contraseñas
- Verificación de integridad de ficheros
- Demostraciones educativas en laboratorios controlados
- Revisión de implementaciones criptográficas
- Validación técnica de hallazgos en informes de seguridad

---

## Enfoque de seguridad

Este proyecto ayuda a detectar:

- Uso de MD5 o SHA1
- Contraseñas débiles presentes en diccionarios controlados
- Riesgo de reutilización de credenciales
- Falta de algoritmos modernos para almacenamiento de contraseñas

No está diseñado para:

- fuerza bruta masiva
- cracking distribuido
- optimización GPU
- acceso a bases de datos filtradas
- automatización ofensiva contra terceros

---

## Futuras mejoras

- Soporte para formatos bcrypt y Argon2
- Detección de hashes con prefijos estructurados
- Exportación también en Markdown
- API REST con FastAPI
- Mejoras de formato en informes y métricas

---

## Aviso de uso ético

Este proyecto debe utilizarse únicamente en:

- entornos autorizados
- auditorías legítimas
- formación técnica
- laboratorios controlados

---

## Autor

Isaac Blázquez  
Pentester | Seguridad Web | Auditorías técnicas

---

## Licencia

MIT License
