class calculator:
    def __init__(self, vector) -> None:
        self.vector = vector

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        product = 0
        for e, v in enumerate(v1):
            product += v1[e] * v2[e]
        print(product)

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        product = []
        for e, v in enumerate(v1):
            product.append(v1[e] + v2[e])
        print(product)

    def sous_vec(v1: list[float], v2: list[float]) -> None:
        product = []
        for e, v in enumerate(v1):
            product.append(v1[e] - v2[e])
        print(product)
