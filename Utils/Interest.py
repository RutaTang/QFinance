class Interest():
    def __init__(self, init_principle, rate, time, interest=None, final_principle=None):
        """

        :param init_principle: initial capital
        :param rate: interests Rates
        :param interest:
        :param final_principle:
        :param time:
        """
        self.init_principle = init_principle
        self.rate = rate
        self.interest = interest
        self.final_principle = final_principle
        self.time = time

    def SimpleInterestF(self):
        """
        Calculate simple interest (final value)
        Formula: Interest = Price * rate * time
        :return: None
        """
        self.interest = self.init_principle * self.rate * self.time
        self.final_principle = self.init_principle * (1 + self.rate * self.time)

    def SimpleInterestI(self):
        """
        Calculate simple interest (initial value)
        :return: None
        """
        self.init_principle = self.final_principle/(1+self.rate*self.time)


