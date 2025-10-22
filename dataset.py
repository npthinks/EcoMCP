import pandas as pd


df = pd.read_csv("nutrition_cf - Sheet5.csv", sep = ";")

def clean_region(value):
    if pd.isna(value):
        return None
    parts = [p.strip().capitalize() for p in str(value).split(",") if p.strip()]
    parts = sorted(set(parts))
    return ", ".join(parts)

df["Region"] = df["Region"].apply(clean_region)

region_list = list(df.Region.unique())
print(isinstance(region_list, list))
id_dict = {value : (i+1) * 10000 for i,value in enumerate(region_list)}
    
df["ID"] = df["Region"].map(id_dict)
df["ID"] = df.groupby("Region").cumcount() + 1
df["ID"] = df.apply(lambda row: id_dict[row["Region"]] + row["ID"], axis=1)

df.to_json("NutritionIndia.json",orient = "records", indent = 4)

