"""CSV -> site/data/5b.json. Run after adding rows to data/5b_clean.csv."""
import pandas as pd, json
df=pd.read_csv("data/5b_clean.csv")
df=df[df.ticker.str.startswith("ASX:",na=False)]
out={}
for t,g in df.sort_values(["ticker","quarter_end"]).groupby("ticker"):
    qs=[]
    for _,r in g.iterrows():
        d={k:(None if pd.isna(v) else (round(v,4) if isinstance(v,float) else v)) for k,v in r.items()}
        notes=[n.strip() for n in str(r.get("extraction_flags") or "").split(";") if n.strip() and n.strip()!="nan" and not n.strip().lower().startswith("ticker ")]
        if isinstance(r.get("cleaning_notes"),str) and r["cleaning_notes"]: notes.append("Cleaned: "+r["cleaning_notes"])
        d["notes"]=notes
        qs.append(d)
    n=qs[0]["company_name"].replace(" (HAR)","")
    out[t]={"name":n.title() if n.isupper() else n,"quarters":qs}
json.dump({"companies":out},open("site/data/5b.json","w"),separators=(",",":"))
print(len(out),"companies,",sum(len(c["quarters"]) for c in out.values()),"filings")
