


class BasicMisc(BasicItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.family = kwargs.get('family', 'books')
        self.effect = kwargs.get('effect', ('permanent', 1))
