
class Router(object):
    print("class calls")

    def __init__(self, model, modelId, serialno):
        self.model = model
        self.modelId = modelId
        self.serialno = serialno

    def display_Fun(self):
        print(self.model, self.serialno, self.modelId)

C1 = Router('code', 'boss', '2156')
print(C1.display_Fun(), '\n')
print(C1.modelId)
print(C1.serialno)
print(C1.model)

