import pandas as pd

# Beispiel-Daten
data = {
    "Name": ["Anna", "Ben", "Clara", "David"],
    "Alter": [25, 32, 29, 41],
    "Stadt": ["Berlin", "München", "Köln", "Hamburg"]
}

df = pd.DataFrame(data)

# Speichern als Parquet-Datei
df.to_parquet("beispiel.parquet", engine="pyarrow", index=False)

print("Parquet-Datei erfolgreich gespeichert.")
