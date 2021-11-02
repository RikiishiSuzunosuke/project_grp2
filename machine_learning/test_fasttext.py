import fasttext as ft


model = ft.train_supervised('train_data.txt', label_prefix = '__label__', neg = 10, dim = 200,  epoch = 40, loss = 'hs')
#minCount = 2 登場回数が２回未満の単語を無視するオプション
model.save_model('model.bin')

print(model.predict('時間'))

#results = model.test('train_data.txt')
#print(results)
#テストデータとlabelの一致の割合が見える

