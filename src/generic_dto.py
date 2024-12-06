from dataclasses import dataclass

@dataclass
class GenericDTO:
    pass

    def __init__(self, *args, **kwargs):  ## TODO this allows all types of arguments, therefore ignoring the problem
        pass
        print(self.__dict__)
        self.__dict__.update(kwargs)
        print(self.__dict__)
        print()
