from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class CharmyMcinterfaceProvides(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:http}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.available')

    @hook('{provides:http}-relation-{broken,departed}')
    def broken(self):
        self.remove_state('{relation_name}.available')

    def test(self, data):
        self.set_remote(data=data)
