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

## Quickstart

Import

```
import autoKS as ks
```

Step 1: load data

For concept map data in proposition format, it should be arranged in a way like this: 

```
beeswax	minerals
bees	figure 8
nectar	bees
water	beeswax
......
```

Load propositions data of concept map, `bees_student` is a `networkx` graph

```
bees_student = ks.cmap2graph('D:/py_project/KS_test/different_formats/bees_student_cmap_en.txt', data_type='pairs')
```

For text data, we can load it from a string object directly

The content is too much so I only show you the beginning and the end of this text

```
text = "Bees make honey to survive. ......Some of the main sources of nectar are fruit trees, clover and flowering trees. "
```

Now we can convert it into a `networkx` graph by use function `text2graph`

```
text_en = text_en.replace('honeycomb', 'hive')  # replace synonym: honeycomb --> hive
keyterms = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
            'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
            'bees', 'evaporation', 'dry', 'fruit trees']
bees_text = ks.text2graph(text, keyterms, read_from_file=False)
```

Step 2: do some calculations

For example, we can calculate Tversky's simialrity between graph `bees_student` and `bees_text`, by using `calc_tversky` easily

```
ks.calc_tversky(bees_en, bees_student_en, comparison='propositional', detailed=True)

### 0.1224
```

Step 3: Visualzation

```
ks.draw_html(bees_student, show=False)
ks.draw_html(bees_text)
```

results:


