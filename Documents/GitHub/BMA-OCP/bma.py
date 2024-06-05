from pykml import parser
import pandas as pd

with open('/Users/tententgc/Documents/GitHub/BMA-OCP/bma-1.kml', 'r', encoding="utf-8") as f:
   root = parser.parse(f).getroot()
   
places = []
for place in root.Document.Folder.Placemark:
    data = {item.get("name"): item.text for item in
            place.ExtendedData.SchemaData.SimpleData}
    coords = place.Polygon.outerBoundaryIs.LinearRing.coordinates.text.strip()
    data["Coordinates"] = coords
    places.append(data)
df = pd.DataFrame(places)
print(df)