import stanza

# stanza.download('zh')
nlp = stanza.Pipeline('zh-hans')
doc = nlp("贝拉克·奥巴马出生于夏威夷。")
doc.sentences[0].print_dependencies()
