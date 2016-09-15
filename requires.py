from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class CharmyMcinterfaceRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:http}-relation-{joined,changed}')
    def changed(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.available')

    @hook('{requires:http}-relation-{departed,broken}')
    def broken(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.available')

    def test(self, data):
        return data
