import os
import glob
import spacy
from tqdm import tqdm
from lxml import etree as ET

# Load the spaCy Spanish model
nlp = spacy.load("es_core_news_md")


# Annotate every paragraph
def annotate_paragraph(p_element):
    text = "".join(p_element.itertext()).strip()
    if not text:
        return
    doc = nlp(text)
    p_element.clear()
    for token in doc:
        w = ET.SubElement(p_element, "w")
        w.text = token.text
        w.set("pos", token.pos_)
        w.set("lemma", token.lemma_)
        if token.ent_type_:
            w.set("ner", token.ent_type_)


# Processing xml
def process_xml(path):
    parser = ET.XMLParser(remove_blank_text=True)
    tree = ET.parse(path, parser)
    root = tree.getroot()

    ns = {"tei": "http://www.tei-c.org/ns/1.0"}
    paragraphs = root.xpath(".//tei:text//tei:body//tei:p", namespaces=ns)

    if not paragraphs:
        print(f"Not found paragraphs in: {path}")
        return

    for p in paragraphs:
        annotate_paragraph(p)

    output_path = path.replace(".xml", "_annotated.xml")
    tree.write(output_path, encoding="utf-8", pretty_print=True, xml_declaration=True)
    print(f"Saved at: {output_path}")


# Look for documents that end with .xml in the spa folder
ruta = "/Users/lauravargas/Desktop/Digital Humanities/ProjectDH/Annotation and Processing/Selected/spa/*.xml"
archivos = glob.glob(ruta)

print(f"Found {len(archivos)}  XML files to process\n")

for archivo in tqdm(archivos):
    process_xml(archivo)
