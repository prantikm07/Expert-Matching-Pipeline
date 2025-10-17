import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class Matcher:
    def __init__(self, mentors_csv, model='all-MiniLM-L6-v2'):
        self.df = pd.read_csv(mentors_csv)
        assert {'mentor_name', 'mentor_description'}.issubset(self.df.columns)
        self.embed = SentenceTransformer(model)
        self.vec = self.embed.encode(self.df['mentor_description'].tolist(), batch_size=32)
    def match(self, topic, desc, k=5):
        inp = f"{topic}. {desc}"
        v = self.embed.encode([inp])
        sim = cosine_similarity(v, self.vec)[0]
        self.df['score'] = sim * 100
        return self.df[['mentor_name','mentor_description','score']].sort_values('score',ascending=False).head(k).reset_index(drop=True)
    def batch(self, mentees_csv, out_csv, k=5):
        mentees = pd.read_csv(mentees_csv)
        out = []
        for i, row in mentees.iterrows():
            res = self.match(row.get('topic',''),row['description'],k)
            res['mentee_id'],res['mentee_name'],res['mentee_topic'],res['mentee_desc'] = row.get('mentee_id',i),row.get('mentee_name',''),row.get('topic',''),row['description']
            out.append(res)
        pd.concat(out).to_csv(out_csv,index=False)
