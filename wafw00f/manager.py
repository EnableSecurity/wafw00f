#!/usr/bin/env python3
'''
Copyright (C) 2026, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

import os
import importlib.util

def load_plugins():
    here = os.path.abspath(os.path.dirname(__file__))
    plugin_dir = os.path.join(here, 'plugins')

    plugin_dict = {}

    # Iterate over all files in the plugin directory
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            plugin_name = filename[:-3]  # Remove the .py extension
            plugin_path = os.path.join(plugin_dir, filename)

            # Load the plugin module
            spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
            plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin_module)

            # Store the loaded plugin in the dictionary
            plugin_dict[plugin_name] = plugin_module

    return plugin_dict
