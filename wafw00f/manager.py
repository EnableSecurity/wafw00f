#!/usr/bin/env python


import os
from functools import partial

from pluginbase import PluginBase


def load_plugins():
    here = os.path.abspath(os.path.dirname(__file__))
    get_path = partial(os.path.join, here)
    plugin_dir = get_path('plugins')

    plugin_base = PluginBase(
        package='wafw00f.plugins', searchpath=[plugin_dir]
    )
    plugin_source = plugin_base.make_plugin_source(
        searchpath=[plugin_dir], persist=True
    )

    plugin_dict = {}
    for plugin_name in plugin_source.list_plugins():
        plugin_dict[plugin_name] = plugin_source.load_plugin(plugin_name)

    return plugin_dict
