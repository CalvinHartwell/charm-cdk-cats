#!/usr/bin/env python3
import sys
sys.path.append('lib')
import yaml

import os
from ops.charm import CharmBase
from ops.main import main

class CDKCats(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.start, self)

    def on_start(self, event):
        # Deploy Container
        path = os.getcdw() + "/src/cdk-cats-manifest.yaml"
        with open(path, 'r') as stream:
            try:
                response = yaml.safe_load(stream)
                self._apply_spec(response)
            except yaml.YAMLError as exc:
                pass


if __name__ == "__main__":
    main(CDKCats)
