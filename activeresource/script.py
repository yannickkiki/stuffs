from pyactiveresource.activeresource import ActiveResource


class BeansActiveResource(ActiveResource):

    @classmethod
    def _element_path(cls, id_, prefix_options=None, query_options=None, action=None):
        prefix = cls._prefix(prefix_options)
        path = f"{prefix}/{cls._plural}/{id_}"
        if action:
            path += f"/{action}"
        return path + cls._query_string(query_options)

    @classmethod
    def _collection_path(cls, prefix_options=None, query_options=None):
        prefix = cls._prefix(prefix_options)
        path = f"{prefix}/{cls._plural}"
        return path + cls._query_string(query_options)

    @classmethod
    def retrieve(cls, id_, **kwargs):
        return cls._find_single(id_, **kwargs)

    @classmethod
    def list(cls, **kwargs):
        return cls._find_every(**kwargs)[0].data

    def delete(self):
        url = self._element_path(self.id, self._prefix_options)
        return self.klass.connection.delete(url, self.klass.headers)

    def to_json(self, root=False):
        return super().to_json(root=root)


class Foxx(BeansActiveResource):
    _site = 'https://api.bns.re/v3/foxx'
    _headers = {'authorization': 'xxx'}


class Campaign(Foxx):
    _plural = 'campaign'

    def schedule(self, data=None):
        url = self._element_path(self.id, self._prefix_options, action='schedule')
        return self.klass.connection.post(url, self.klass.headers, data=data)


# List campaigns
campaigns = Campaign.list(offset=0, limit=3)  # campaigns[0].name

# Retrieve campaign
campaign_retrieved = Campaign.retrieve('cp_0wfzuivyy50x')  # campaign.name

# Create campaign
campaign_created = Campaign.create({
    'name': 'ActiveResourceFirst',
    'uid': 'rule:foxx:campaign_announcement'
})

# Update Campaign
campaign_created.name = 'ActiveResourceOh'
campaign_created.save()

# Delete Campaign
campaign_created.delete()

# Schedule campaign
campaign_created.schedule(data={})
