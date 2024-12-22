class csvHandler:
    def __init__(self, directory):
        self.dir = directory

    def insertDataInCsv(self, data):
        print(f"Inserindo {data} in {self.dir}")
    
    def ReadCsv(self):
        print(f"read data in {self.dir}")

csvHandler = csvHandler("o/caminho/para/o/.csv")
csvHandler.insertDataInCsv("22-12-2024")
csvHandler.ReadCsv()