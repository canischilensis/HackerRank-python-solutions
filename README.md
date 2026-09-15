# 🐍 HackerRank Python Solutions

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![HackerRank](https://img.shields.io/badge/HackerRank-Python-2EC866?logo=hackerrank&logoColor=white)
![Progreso](https://img.shields.io/badge/resueltos-9%2F115-blue)

Soluciones en **Python 3** a los desafíos del dominio [**Python** de HackerRank](https://www.hackerrank.com/domains/python).

Cada directorio del repositorio corresponde a un **subdominio** de HackerRank (Introduction, Basic Data Types, Strings, etc.), y dentro de él hay un archivo `.py` por cada desafío resuelto.

---

## 📑 Tabla de contenidos

- [Progreso general](#-progreso-general)
- [Estructura del repositorio](#-estructura-del-repositorio)
- [Cómo ejecutar las soluciones](#-cómo-ejecutar-las-soluciones)
- [Convenciones](#-convenciones)
- [Desafíos por subdominio](#-desafíos-por-subdominio)
  - [Introduction](#introduction)
  - [Basic Data Types](#basic-data-types)
  - [Strings](#strings)
  - [Sets](#sets)
  - [Math](#math)
  - [Itertools](#itertools)
  - [Collections](#collections)
  - [Date and Time](#date-and-time)
  - [Errors and Exceptions](#errors-and-exceptions)
  - [Classes](#classes)
  - [Built-Ins](#built-ins)
  - [Python Functionals](#python-functionals)
  - [Regex and Parsing](#regex-and-parsing)
  - [XML](#xml)
  - [Closures and Decorators](#closures-and-decorators)
  - [Numpy](#numpy)
  - [Debugging](#debugging)
- [Recursos](#-recursos)
- [Autor](#-autor)

---

## 📊 Progreso general

**9 de 115 desafíos resueltos** (7.8 %)

| # | Subdominio | Directorio | Desafíos | 🟢 | 🟡 | 🔴 | Resueltos | Progreso |
|:-:|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | [Introduction](#introduction) | [`introduction/`](./introduction/) | 7 | 6 | 1 | 0 | 7 | `██████████` 100 % |
| 2 | [Basic Data Types](#basic-data-types) | [`basic-data-types/`](./basic-data-types/) | 6 | 6 | 0 | 0 | 2 | `███░░░░░░░` 33 % |
| 3 | [Strings](#strings) | `strings/` | 14 | 12 | 2 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 4 | [Sets](#sets) | `sets/` | 13 | 12 | 1 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 5 | [Math](#math) | `math/` | 7 | 4 | 3 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 6 | [Itertools](#itertools) | `itertools/` | 7 | 4 | 2 | 1 | 0 | `░░░░░░░░░░` 0 % |
| 7 | [Collections](#collections) | `collections/` | 8 | 5 | 3 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 8 | [Date and Time](#date-and-time) | `date-and-time/` | 2 | 1 | 1 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 9 | [Errors and Exceptions](#errors-and-exceptions) | `errors-and-exceptions/` | 2 | 2 | 0 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 10 | [Classes](#classes) | `classes/` | 2 | 1 | 1 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 11 | [Built-Ins](#built-ins) | `built-ins/` | 6 | 4 | 2 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 12 | [Python Functionals](#python-functionals) | `python-functionals/` | 3 | 1 | 2 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 13 | [Regex and Parsing](#regex-and-parsing) | `regex-and-parsing/` | 17 | 13 | 2 | 2 | 0 | `░░░░░░░░░░` 0 % |
| 14 | [XML](#xml) | `xml/` | 2 | 2 | 0 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 15 | [Closures and Decorators](#closures-and-decorators) | `closures-and-decorators/` | 2 | 2 | 0 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 16 | [Numpy](#numpy) | `numpy/` | 15 | 15 | 0 | 0 | 0 | `░░░░░░░░░░` 0 % |
| 17 | [Debugging](#debugging) | `debugging/` | 2 | 0 | 2 | 0 | 0 | `░░░░░░░░░░` 0 % |
| | **Total** | | **115** | **90** | **22** | **3** | **9** | `█░░░░░░░░░` 7 % |

> 🟢 Fácil · 🟡 Media · 🔴 Difícil

---

## 📁 Estructura del repositorio

```text
HackerRank-python-solutions/
├── introduction/
│   ├── arithmetic-operators.py
│   ├── loops.py
│   ├── print-function.py
│   ├── python-division.py
│   ├── python-if-else.py
│   ├── say-hello-world.py
│   └── write-a-function.py
├── basic-data-types/
│   └── list-comprehesions.py
├── README.md
└── lists.py
```

A medida que se avance con nuevos subdominios se irán creando sus directorios con los siguientes nombres:

| Subdominio | Directorio |
|---|---|
| Introduction | [`introduction/`](./introduction/) |
| Basic Data Types | [`basic-data-types/`](./basic-data-types/) |
| Strings | `strings/` |
| Sets | `sets/` |
| Math | `math/` |
| Itertools | `itertools/` |
| Collections | `collections/` |
| Date and Time | `date-and-time/` |
| Errors and Exceptions | `errors-and-exceptions/` |
| Classes | `classes/` |
| Built-Ins | `built-ins/` |
| Python Functionals | `python-functionals/` |
| Regex and Parsing | `regex-and-parsing/` |
| XML | `xml/` |
| Closures and Decorators | `closures-and-decorators/` |
| Numpy | `numpy/` |
| Debugging | `debugging/` |

---

## 🚀 Cómo ejecutar las soluciones

Requisitos: **Python 3** (y **NumPy** para el subdominio `numpy`).

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd HackerRank-python-solutions

# Ejecutar una solución e ingresar los datos por teclado
python3 introduction/loops.py

# O pasar la entrada de ejemplo por la entrada estándar
echo "5" | python3 introduction/loops.py
printf '1\n1\n1\n2\n' | python3 basic-data-types/list-comprehesions.py
```

Al igual que en HackerRank, las soluciones leen los datos desde la **entrada estándar** (`input()`) y escriben el resultado en la **salida estándar** (`print()`).

---

## 📐 Convenciones

- **Directorios:** nombre del subdominio en minúsculas y separado por guiones (`kebab-case`), p. ej. `basic-data-types/`.
- **Archivos:** nombre del desafío en `kebab-case` con extensión `.py`, p. ej. `python-if-else.py`.
- **Enlaces:** cada desafío en las tablas enlaza a su enunciado en HackerRank; la columna *Solución* enlaza al archivo del repositorio.
- **Estado:** ✅ resuelto · ⬜ pendiente.

---

## 🧩 Desafíos por subdominio

### Introduction

Primeros pasos: `print`, entrada estándar, condicionales, bucles y funciones.

📂 Directorio: [`introduction/`](./introduction/) · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-introduction) · ✅ **7/7** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Say "Hello, World!" With Python](https://www.hackerrank.com/challenges/py-hello-world/problem) | 🟢 Fácil | 5 | [`say-hello-world.py`](./introduction/say-hello-world.py) | ✅ |
| 2 | [Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem) | 🟢 Fácil | 10 | [`python-if-else.py`](./introduction/python-if-else.py) | ✅ |
| 3 | [Arithmetic Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem) | 🟢 Fácil | 10 | [`arithmetic-operators.py`](./introduction/arithmetic-operators.py) | ✅ |
| 4 | [Python: Division](https://www.hackerrank.com/challenges/python-division/problem) | 🟢 Fácil | 10 | [`python-division.py`](./introduction/python-division.py) | ✅ |
| 5 | [Loops](https://www.hackerrank.com/challenges/python-loops/problem) | 🟢 Fácil | 10 | [`loops.py`](./introduction/loops.py) | ✅ |
| 6 | [Write a function](https://www.hackerrank.com/challenges/write-a-function/problem) | 🟡 Media | 10 | [`write-a-function.py`](./introduction/write-a-function.py) | ✅ |
| 7 | [Print Function](https://www.hackerrank.com/challenges/python-print/problem) | 🟢 Fácil | 20 | [`print-function.py`](./introduction/print-function.py) | ✅ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Basic Data Types

Listas, tuplas, diccionarios y comprensiones de listas.

📂 Directorio: [`basic-data-types/`](./basic-data-types/) · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-basic-data-types) · ✅ **2/6** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem) | 🟢 Fácil | 10 | [`list-comprehesions.py`](./basic-data-types/list-comprehesions.py) | ✅ |
| 2 | [Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 3 | [Nested Lists](https://www.hackerrank.com/challenges/nested-list/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 4 | [Finding the percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 5 | [Lists](https://www.hackerrank.com/challenges/python-lists/problem) | 🟢 Fácil | 10 | [`lists.py`](./lists.py) | ✅ |
| 6 | [Tuples](https://www.hackerrank.com/challenges/python-tuples/problem) | 🟢 Fácil | 10 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Strings

Manipulación, formateo, alineación y validación de cadenas de texto.

📂 Directorio: `strings/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-strings) · ✅ **0/14** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [sWAP cASE](https://www.hackerrank.com/challenges/swap-case/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 3 | [What's Your Name?](https://www.hackerrank.com/challenges/whats-your-name/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 4 | [Mutations](https://www.hackerrank.com/challenges/python-mutations/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 5 | [Find a string](https://www.hackerrank.com/challenges/find-a-string/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 6 | [String Validators](https://www.hackerrank.com/challenges/string-validators/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 7 | [Text Alignment](https://www.hackerrank.com/challenges/text-alignment/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 8 | [Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 9 | [Designer Door Mat](https://www.hackerrank.com/challenges/designer-door-mat/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 10 | [String Formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 11 | [Alphabet Rangoli](https://www.hackerrank.com/challenges/alphabet-rangoli/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 12 | [Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 13 | [The Minion Game](https://www.hackerrank.com/challenges/the-minion-game/problem) | 🟡 Media | 40 | — | ⬜ |
| 14 | [Merge the Tools!](https://www.hackerrank.com/challenges/merge-the-tools/problem) | 🟡 Media | 40 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Sets

Conjuntos y sus operaciones: unión, intersección, diferencia y subconjuntos.

📂 Directorio: `sets/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-sets) · ✅ **0/13** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Introduction to Sets](https://www.hackerrank.com/challenges/py-introduction-to-sets/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [No Idea!](https://www.hackerrank.com/challenges/no-idea/problem) | 🟡 Media | 50 | — | ⬜ |
| 3 | [Symmetric Difference](https://www.hackerrank.com/challenges/symmetric-difference/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 4 | [Set .add()](https://www.hackerrank.com/challenges/py-set-add/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 5 | [Set .discard(), .remove() & .pop()](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 6 | [Set .union() Operation](https://www.hackerrank.com/challenges/py-set-union/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 7 | [Set .intersection() Operation](https://www.hackerrank.com/challenges/py-set-intersection-operation/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 8 | [Set .difference() Operation](https://www.hackerrank.com/challenges/py-set-difference-operation/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 9 | [Set .symmetric_difference() Operation](https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 10 | [Set Mutations](https://www.hackerrank.com/challenges/py-set-mutations/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 11 | [The Captain's Room](https://www.hackerrank.com/challenges/py-the-captains-room/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 12 | [Check Subset](https://www.hackerrank.com/challenges/py-check-subset/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 13 | [Check Strict Superset](https://www.hackerrank.com/challenges/py-check-strict-superset/problem) | 🟢 Fácil | 10 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Math

Números complejos, enteros grandes, `divmod`, potencias y geometría.

📂 Directorio: `math/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-math) · ✅ **0/7** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Polar Coordinates](https://www.hackerrank.com/challenges/polar-coordinates/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [Find Angle MBC](https://www.hackerrank.com/challenges/find-angle/problem) | 🟡 Media | 10 | — | ⬜ |
| 3 | [Triangle Quest 2](https://www.hackerrank.com/challenges/triangle-quest-2/problem) | 🟡 Media | 20 | — | ⬜ |
| 4 | [Mod Divmod](https://www.hackerrank.com/challenges/python-mod-divmod/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 5 | [Power - Mod Power](https://www.hackerrank.com/challenges/python-power-mod-power/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 6 | [Integers Come In All Sizes](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 7 | [Triangle Quest](https://www.hackerrank.com/challenges/python-quest-1/problem) | 🟡 Media | 20 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Itertools

Producto cartesiano, permutaciones, combinaciones y `groupby`.

📂 Directorio: `itertools/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-itertools) · ✅ **0/7** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [itertools.product()](https://www.hackerrank.com/challenges/itertools-product/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [itertools.permutations()](https://www.hackerrank.com/challenges/itertools-permutations/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 3 | [itertools.combinations()](https://www.hackerrank.com/challenges/itertools-combinations/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 4 | [itertools.combinations_with_replacement()](https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 5 | [Compress the String!](https://www.hackerrank.com/challenges/compress-the-string/problem) | 🟡 Media | 20 | — | ⬜ |
| 6 | [Iterables and Iterators](https://www.hackerrank.com/challenges/iterables-and-iterators/problem) | 🟡 Media | 40 | — | ⬜ |
| 7 | [Maximize It!](https://www.hackerrank.com/challenges/maximize-it/problem) | 🔴 Difícil | 50 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Collections

`Counter`, `defaultdict`, `namedtuple`, `OrderedDict` y `deque`.

📂 Directorio: `collections/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-collections) · ✅ **0/8** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [collections.Counter()](https://www.hackerrank.com/challenges/collections-counter/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [DefaultDict Tutorial](https://www.hackerrank.com/challenges/defaultdict-tutorial/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 3 | [Collections.namedtuple()](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 4 | [Collections.OrderedDict()](https://www.hackerrank.com/challenges/py-collections-ordereddict/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 5 | [Word Order](https://www.hackerrank.com/challenges/word-order/problem) | 🟡 Media | 50 | — | ⬜ |
| 6 | [Collections.deque()](https://www.hackerrank.com/challenges/py-collections-deque/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 7 | [Company Logo](https://www.hackerrank.com/challenges/most-commons/problem) | 🟡 Media | 30 | — | ⬜ |
| 8 | [Piling Up!](https://www.hackerrank.com/challenges/piling-up/problem) | 🟡 Media | 50 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Date and Time

Módulos `calendar` y `datetime`, zonas horarias y diferencias de tiempo.

📂 Directorio: `date-and-time/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-date-time) · ✅ **0/2** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Calendar Module](https://www.hackerrank.com/challenges/calendar-module/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [Time Delta](https://www.hackerrank.com/challenges/python-time-delta/problem) | 🟡 Media | 30 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Errors and Exceptions

Manejo de excepciones con `try` / `except`.

📂 Directorio: `errors-and-exceptions/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=errors-exceptions) · ✅ **0/2** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Exceptions](https://www.hackerrank.com/challenges/exceptions/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [Incorrect Regex](https://www.hackerrank.com/challenges/incorrect-regex/problem) | 🟢 Fácil | 20 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Classes

Programación orientada a objetos y sobrecarga de operadores.

📂 Directorio: `classes/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-classes) · ✅ **0/2** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Classes: Dealing with Complex Numbers](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem) | 🟡 Media | 20 | — | ⬜ |
| 2 | [Class 2 - Find the Torsional Angle](https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem) | 🟢 Fácil | 20 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Built-Ins

Funciones integradas: `zip`, `eval`, `input`, `sorted`, `any`, `all`.

📂 Directorio: `built-ins/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-built-ins) · ✅ **0/6** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Zipped!](https://www.hackerrank.com/challenges/zipped/problem) | 🟢 Fácil | 10 | — | ⬜ |
| 2 | [Input()](https://www.hackerrank.com/challenges/input/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 3 | [Python Evaluation](https://www.hackerrank.com/challenges/python-eval/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 4 | [Athlete Sort](https://www.hackerrank.com/challenges/python-sort-sort/problem) | 🟡 Media | 30 | — | ⬜ |
| 5 | [Any or All](https://www.hackerrank.com/challenges/any-or-all/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 6 | [ginortS](https://www.hackerrank.com/challenges/ginorts/problem) | 🟡 Media | 40 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Python Functionals

Programación funcional: `map`, `filter`, `reduce` y `lambda`.

📂 Directorio: `python-functionals/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-functionals) · ✅ **0/3** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Map and Lambda Function](https://www.hackerrank.com/challenges/map-and-lambda-expression/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 2 | [Validating Email Addresses With a Filter](https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem) | 🟡 Media | 20 | — | ⬜ |
| 3 | [Reduce Function](https://www.hackerrank.com/challenges/reduce-function/problem) | 🟡 Media | 30 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Regex and Parsing

Expresiones regulares con `re` y parseo de HTML.

📂 Directorio: `regex-and-parsing/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-regex) · ✅ **0/17** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Detect Floating Point Number](https://www.hackerrank.com/challenges/introduction-to-regex/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 2 | [Re.split()](https://www.hackerrank.com/challenges/re-split/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 3 | [Group(), Groups() & Groupdict()](https://www.hackerrank.com/challenges/re-group-groups/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 4 | [Re.findall() & Re.finditer()](https://www.hackerrank.com/challenges/re-findall-re-finditer/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 5 | [Re.start() & Re.end()](https://www.hackerrank.com/challenges/re-start-re-end/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 6 | [Regex Substitution](https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem) | 🟡 Media | 20 | — | ⬜ |
| 7 | [Validating Roman Numerals](https://www.hackerrank.com/challenges/validate-a-roman-number/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 8 | [Validating phone numbers](https://www.hackerrank.com/challenges/validating-the-phone-number/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 9 | [Validating and Parsing Email Addresses](https://www.hackerrank.com/challenges/validating-named-email-addresses/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 10 | [Hex Color Code](https://www.hackerrank.com/challenges/hex-color-code/problem) | 🟢 Fácil | 30 | — | ⬜ |
| 11 | [HTML Parser - Part 1](https://www.hackerrank.com/challenges/html-parser-part-1/problem) | 🟢 Fácil | 30 | — | ⬜ |
| 12 | [HTML Parser - Part 2](https://www.hackerrank.com/challenges/html-parser-part-2/problem) | 🟢 Fácil | 30 | — | ⬜ |
| 13 | [Detect HTML Tags, Attributes and Attribute Values](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem) | 🟢 Fácil | 30 | — | ⬜ |
| 14 | [Validating UID](https://www.hackerrank.com/challenges/validating-uid/problem) | 🟢 Fácil | 40 | — | ⬜ |
| 15 | [Validating Credit Card Numbers](https://www.hackerrank.com/challenges/validating-credit-card-number/problem) | 🟡 Media | 40 | — | ⬜ |
| 16 | [Validating Postal Codes](https://www.hackerrank.com/challenges/validating-postalcode/problem) | 🔴 Difícil | 80 | — | ⬜ |
| 17 | [Matrix Script](https://www.hackerrank.com/challenges/matrix-script/problem) | 🔴 Difícil | 100 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### XML

Recorrido y análisis de documentos XML con `ElementTree`.

📂 Directorio: `xml/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=xml) · ✅ **0/2** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [XML 1 - Find the Score](https://www.hackerrank.com/challenges/xml-1-find-the-score/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 2 | [XML2 - Find the Maximum Depth](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem) | 🟢 Fácil | 20 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Closures and Decorators

Clausuras y decoradores.

📂 Directorio: `closures-and-decorators/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=closures-and-decorators) · ✅ **0/2** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Standardize Mobile Number Using Decorators](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem) | 🟢 Fácil | 30 | — | ⬜ |
| 2 | [Decorators 2 - Name Directory](https://www.hackerrank.com/challenges/decorators-2-name-directory/problem) | 🟢 Fácil | 30 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Numpy

Arreglos, álgebra lineal y operaciones matemáticas con NumPy.

📂 Directorio: `numpy/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=numpy) · ✅ **0/15** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Arrays](https://www.hackerrank.com/challenges/np-arrays/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 2 | [Shape and Reshape](https://www.hackerrank.com/challenges/np-shape-reshape/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 3 | [Transpose and Flatten](https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 4 | [Concatenate](https://www.hackerrank.com/challenges/np-concatenate/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 5 | [Zeros and Ones](https://www.hackerrank.com/challenges/np-zeros-and-ones/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 6 | [Eye and Identity](https://www.hackerrank.com/challenges/np-eye-and-identity/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 7 | [Array Mathematics](https://www.hackerrank.com/challenges/np-array-mathematics/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 8 | [Floor, Ceil and Rint](https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 9 | [Sum and Prod](https://www.hackerrank.com/challenges/np-sum-and-prod/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 10 | [Min and Max](https://www.hackerrank.com/challenges/np-min-and-max/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 11 | [Mean, Var, and Std](https://www.hackerrank.com/challenges/np-mean-var-and-std/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 12 | [Dot and Cross](https://www.hackerrank.com/challenges/np-dot-and-cross/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 13 | [Inner and Outer](https://www.hackerrank.com/challenges/np-inner-and-outer/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 14 | [Polynomials](https://www.hackerrank.com/challenges/np-polynomials/problem) | 🟢 Fácil | 20 | — | ⬜ |
| 15 | [Linear Algebra](https://www.hackerrank.com/challenges/np-linear-algebra/problem) | 🟢 Fácil | 20 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

### Debugging

Encontrar y corregir errores en código existente.

📂 Directorio: `debugging/` · 🔗 [Ver en HackerRank](https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-debugging) · ✅ **0/2** resueltos

| # | Desafío | Dificultad | Puntos | Solución | Estado |
|:-:|---|:-:|:-:|---|:-:|
| 1 | [Words Score](https://www.hackerrank.com/challenges/words-score/problem) | 🟡 Media | 10 | — | ⬜ |
| 2 | [Default Arguments](https://www.hackerrank.com/challenges/default-arguments/problem) | 🟡 Media | 30 | — | ⬜ |

<p align="right"><a href="#-hackerrank-python-solutions">⬆️ Volver arriba</a></p>

---

## 📚 Recursos

- [Dominio Python en HackerRank](https://www.hackerrank.com/domains/python)
- [Documentación oficial de Python 3](https://docs.python.org/es/3/)
- [Tutorial oficial de Python (español)](https://docs.python.org/es/3/tutorial/)
- [Documentación de NumPy](https://numpy.org/doc/stable/)
- [Módulo `re` — expresiones regulares](https://docs.python.org/es/3/library/re.html)
- [Módulo `itertools`](https://docs.python.org/es/3/library/itertools.html)
- [Módulo `collections`](https://docs.python.org/es/3/library/collections.html)

---

## 👤 Autor

**Jubaea chilensis**

> ⚠️ Estas soluciones se publican con fines de aprendizaje. Se recomienda intentar resolver cada desafío por cuenta propia antes de revisar la solución.
