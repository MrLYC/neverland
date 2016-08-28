# encoding: utf-8

import os
import inspect
import re
import importlib

from ycyc.ycollections.tagmaps import TagMaps

Targets = TagMaps()


def target_auto_load():
    from mountain.targets import BaseTarget

    target_path = os.path.dirname(
        inspect.getsourcefile(BaseTarget)
    )
    module_regex = re.compile(r"^(?P<name>\w+)\.pyc?$")
    for f in os.listdir(target_path):
        if not os.path.isfile(os.path.join(target_path, f)):
            continue
        match = module_regex.match(f)
        if not match:
            continue

        match_dict = match.groupdict()
        name = match_dict.get("name")
        if not name or name.startswith("_"):
            continue
        importlib.import_module("%s.%s" % (BaseTarget.__module__, name))

    for cls in BaseTarget.__subclasses__():
        Targets[cls.name] = cls
