class Query(object):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return 'query {{ {key} {{ {values} }}}}'.format(
            key=list(self.kwargs.keys())[0],
            values=' '.join(list(self.kwargs.values())[0]),
        )
