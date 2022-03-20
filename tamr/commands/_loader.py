import tanjun
from . import basic

@tanjun.as_loader
def load(client: tanjun.abc.Client):
    client.add_component(basic.COMPONENT.copy())