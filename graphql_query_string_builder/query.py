class Query(object):
    def __init__(self, auto_camel_case=True, **kwargs):
        self.auto_camel_case = auto_camel_case

    def _camel_case_string(self, s):
        parts = s.split('_')
        if len(parts) == 1:
            return s
        first_part = parts[0]
        rest = parts[1:]
        camel = [r.title() for r in rest]
        return ''.join([first_part] + camel)

    def render_query_string(self, **kwargs):
        query_parameters = dict(kwargs)
        assert len(query_parameters) == 1  # TODO Switch this to a better exception
        key = list(kwargs.keys())[0]
        value = list(kwargs.values())[0]
        if self.auto_camel_case:
            # TODO Camel case values too
            key = self._camel_case_string(key)
        return str(QueryStringBuilder(key=key, value=value))


class QueryStringBuilder(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return 'query {{ {key} {{ {values} }}}}'.format(
            key=self.key,
            values=' '.join(self.value),
        )
