# autoKS

An easy-to-used Python package to process knowledge structure data automatically, including:
- Convert a variety of forms of data (e.g., concept map, essay/summary) into a graph
- Calculate graph-based features
- Similarity comparison

## Installation

Windows:

`py -m pip install --upgrade autoKS`

Unix/macOS:

`python3 -m pip install --upgrade autoKS`

## Import

```
import autoKS as ks
```

## Quickstart

### Step 1: load data

For concept map data in proposition format, it should be arranged in a way like this: 

```
beeswax	minerals
bees	figure 8
nectar	bees
water	beeswax
......
```

Use `cmap2graph` to load a concept map data in propositions format, and convert it into a `networkx` graph

```
bees_student = ks.cmap2graph('D:/py_project/KS_test/different_formats/bees_student_cmap_en.txt', data_type='pairs')
```

For text data, we can load it from a string object directly

The content is too much so I only show you the beginning and the end of this text

```
text = "Bees make honey to survive. ......Some of the main sources of nectar are fruit trees, clover and flowering trees. "

text_en = text_en.replace('honeycomb', 'hive')  # replace synonym: honeycomb --> hive

keyterms = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
            'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
            'bees', 'evaporation', 'dry', 'fruit trees']
```

Now we can convert it into a `networkx` graph by using function `text2graph`

```
bees_text = ks.text2graph(text, keyterms, read_from_file=False)
```

### Step 2: Do some calculations

For example, we can calculate Tversky's simialrity between graph `bees_student` and `bees_text`, by using funciton`calc_tversky`

```
ks.calc_tversky(bees_en, bees_student_en, comparison='propositional', detailed=True)
```

### Step 3: Visualzation

Use funciton `draw_html` to show graph, it would draw graph using `D3.js`, and dispaly by `pywebview`

```
ks.draw_html(bees_student)
```

results:

![alt text](https://github.com/weiziqian1996/autoKS/blob/main/ks_draw_bees_student_en.png)
