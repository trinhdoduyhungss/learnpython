class Doc:
    def __init__(self, total):
        self.total = total
    def get_book_with_total(self):
        f = open("data_doc.txt", "r")
        text = f.read()
        for i,idx in enumerate(text):
            if self.total == i:
                print(idx)


class ItemDoc:
    def __init__(self, name, auth, series, species):
        self.name = name
        self.auth = auth
        self.series = series
    def add_doc(self):
        f = open("data_doc.txt","a+")
        name_add = str(self.name)
        auth_add = str(self.auth)
        series_add = str(self.series)
        f.write( 'Name : '+name_add+', author : '+auth_add + ', series : '+ series_add +'\n')
        print("Đã add")

#test_doc = ItemDoc("Tokuda book","Tokuda","4.0", "book")
#test_doc.add_doc()
test_get = Doc(1).get_book_with_total()