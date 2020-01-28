import sys
sys.path.append('lib')

from ops.charm import CharmBase
from ops.main import main

class CDKCats(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.start, self.on_start)

     def on_start(self, event):
        # Handle the event here.

if __name__ == "__main__":
    main(CDKCats)
