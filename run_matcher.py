from models.matcher import Matcher

def main():
    m = Matcher('data/raw/mentors.csv')
    while True:
        t = input("topic: ")
        d = input("desc: ")
        if not t and not d: 
            break
        df = m.match(t, d)        
        for idx, (_, row) in enumerate(df.iterrows(), start=1):
            print(f"{idx}. {row.mentor_name} ({row.score:.2f}%): {row.mentor_description[:80]}")



if __name__ == "__main__":
    import sys
    if len(sys.argv)==1:
        main()
    elif sys.argv[1]=="batch":
        Matcher('data/raw/mentors.csv').batch('data/raw/mentees.csv','data/processed/batch_results.csv')
        print("Batch matches saved to data/processed/batch_results.csv")
