from scraper import guardian_dataset
import pandas

articles = guardian_dataset.loadGuardian()

for article in range(0, len(articles)):
    dataset =[]

    for word in articles[article]:
        try:
            vec = guardian_dataset.w2v[word]
            dataset.append({'word':word, 'stop':0})
        except KeyError:
            pass
    df = pandas.DataFrame(dataset)
    with open('phrase_dataset/article' + str(article)+".csv", 'w')as f:
        f.write(df.to_csv())