class Step(object):

    def __init__(self, description: str):
        self.description = description

    def __enter__(self):
        print(f"{type(self).__name__} {self.description}")

    def __exit__(self, ex_type, value, traceback):
        if ex_type:
            print(f"{type(self).__name__} {self.description} - Failed")


class And(Step):
    pass


class Given(Step):
    pass


class When(Step):
    pass


class Then(Step):
    pass
