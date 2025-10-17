from models.matcher import Matcher

def test_match():
    m = Matcher('data/raw/mentors.csv')
    out = m.match("ml", "deep learning")
    assert type(out).__name__=="DataFrame"
    assert out.shape[0]>0

def test_batch():
    m = Matcher('data/raw/mentors.csv')
    m.batch('data/raw/mentees.csv','data/processed/batch_results.csv')

if __name__=="__main__":
    test_match()
    test_batch()
    print("Tests passed")
