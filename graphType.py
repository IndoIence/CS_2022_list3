from dataclasses import dataclass
@dataclass
class GraphType:
    name: str
    k_val: list
    func: any

    def make_new(self, n, param):
        if self.name == 'ER':
            return self.func(n=n, p=(param / n))
        elif self.name == 'BAR':
            return self.func(n=n, m=2 * param)
        elif self.name == 'WS':
            return self.func(n=n, k=param, beta=0.01)
        else:
            raise ValueError("No supported graph type found")