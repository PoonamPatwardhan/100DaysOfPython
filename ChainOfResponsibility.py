class Chain:
    def __init__(self, chain = None):
        pass

    def calculate(self, request):
        pass

class Numbers:

    def __init__(self, number1, number2, calculation):
        self.number1 = number1;
        self.number2 = number2;
        self.calc = calculation;

class AddNumbers(Chain):
    def __init__(self, nextChainInstance = None):
        self.nextInChain = nextChainInstance

    def calculate(self, request):
        if (request.calc == "Add"):
            print("Addition: {} + {} = {}".format(request.number1, request.number2, request.number1 + request.number2));
        else:
            self.nextInChain.calculate(request);


class  SubNumbers(Chain):
    def __init__(self, nextChainInstance):
        self.nextInChain = nextChainInstance

    def calculate(self, request):
        if (request.calc == "Subtract"):
            print("Addition: {} - {} = {}".format(request.number1, request.number2, request.number1 - request.number2));
        else:
            self.nextInChain.calculate(request);


class DivideNumbers(Chain):
    def __init__(self, nextChainInstance):
        self.nextInChain = nextChainInstance

    def calculate(self, request):
        if (request.calc == "Divide"):
            print("Addition: {}/{} = {}".format(request.number1, request.number2, request.number1/request.number2));
        else:
            self.nextInChain.calculate(request);


if __name__ == '__main__':
    add = AddNumbers();
    divide = DivideNumbers(add);
    sub = SubNumbers(divide);

    numberRequest = Numbers(4, 5, "Mult");

    sub.calculate(numberRequest);







