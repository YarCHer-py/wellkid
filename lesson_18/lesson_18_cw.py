class Fruit():
    def __init__(self, name, weight, vkus):
        self.name = name
        self.weight = weight
        self.vkus = vkus
banana = Fruit("banana" , 500 , 10)
mandarin = Fruit('mandarin', 350 , 7)
print(banana.name,banana.weight,banana.vkus)
print(mandarin.name,mandarin.weight,mandarin.vkus)