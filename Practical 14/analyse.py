import xml.dom.minidom as xdm
import xml.sax as xs
import time

# define the pathway of sax to parse .xml file
class GOHandler(xs.ContentHandler):
    
    def __init__(self):
        self.current = ""
        self.ns = ""
        self.id = ""
        self.name = ""
        self.is_a = 0
        self.max = {
            "molecular_function": {"count": 0, "id": "", "name": ""},
            "biological_process": {"count": 0, "id": "", "name": ""},
            "cellular_component": {"count": 0, "id": "", "name": ""}
        }
    
    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "term":
            # Reset all relevant fields for new <term>
            self.ns = ""
            self.id = ""
            self.name = ""
            self.is_a = 0
        elif tag == "is_a":
            self.is_a += 1
    
    def characters(self, content):
        if self.current == "namespace": self.ns += content.strip()
        elif self.current == "id": self.id += content.strip()
        elif self.current == "name": self.name += content.strip()
    
    def endElement(self, tag):
        if tag == "term":
            if self.ns in self.max and self.is_a > self.max[self.ns]["count"]:
                self.max[self.ns] = {
                    "count": self.is_a,
                    "id": self.id,
                    "name": self.name[:20] + "..." if len(self.name) > 20 else self.name
                }
            self.current = ""


def dom_analyze(file):
    start = time.time()
    dom = xdm.parse(file)
    terms = dom.getElementsByTagName("term")
    max = {
        "molecular_function": {"count": 0, "id": "", "name": ""},
        "biological_process": {"count": 0, "id": "", "name": ""},
        "cellular_component": {"count": 0, "id": "", "name": ""}
    }
    
    for term in terms:
        ns = term.getElementsByTagName("namespace")[0].firstChild.data
        if ns in max:
            id = term.getElementsByTagName("id")[0].firstChild.data
            name = term.getElementsByTagName("name")[0].firstChild.data
            is_a = len(term.getElementsByTagName("is_a"))
            if is_a > max[ns]["count"]:
                max[ns] = {
                    "count": is_a,
                    "id": id,
                    "name": name
                }
    
    return max, time.time() - start

def sax_analyze(file):
    start = time.time()
    parser = xs.make_parser()
    handler = GOHandler()
    parser.setContentHandler(handler)
    parser.parse(file)
    return handler.max, time.time() - start

def print_result(data, api, time):
    print(f"\n{api} API ({time:.2f}s):")
    print(f"{'Namespace':<20} {'ID':<12} {'Name':<32} Count")
    for ns in data:
        print(f"{ns:<20} {data[ns]['id']:<12} {data[ns]['name']:<35} {data[ns]['count']}")

if __name__ == "__main__":
    file = "/Users/wsr/Desktop/IBI1_2024-25/Practical 14/go_obo.xml"
    
    dom, t1 = dom_analyze(file)
    sax, t2 = sax_analyze(file)
    
    print_result(dom, "DOM", t1)
    print_result(sax, "SAX", t2)
    
    if t2 > t1: print("SAX is slower than DOM")
    elif t1>t2: print("SAX is faster than DOM")
    else: print("The two ways are equaled")