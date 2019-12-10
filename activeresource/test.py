from pyactiveresource.activeresource import ActiveResource


class Campaign(ActiveResource):
    # ActiveResource Documentation: https://github.com/Shopify/pyactiveresource
    _site = 'https://api.bns.re/v3/foxx/campaign'
    _headers = {'authorization': 'xxx'}

    @classmethod
    def _collection_path(cls, prefix_options=None, query_options=None):
        return f"{cls._prefix(prefix_options)}/{cls._query_string(query_options)}"

    @classmethod
    def list(cls, **kwargs):
        return cls._find_every(**kwargs)[0].data


campaigns = Campaign.list()
