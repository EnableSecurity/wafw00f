"""Tests for the plugin manager."""

import pytest
from wafw00f.manager import load_plugins


class TestLoadPlugins:
    """Tests for the load_plugins function."""

    def test_load_plugins_returns_dict(self):
        """Verify load_plugins returns a dictionary."""
        plugins = load_plugins()
        assert isinstance(plugins, dict)

    def test_load_plugins_not_empty(self):
        """Verify plugins are loaded."""
        plugins = load_plugins()
        assert len(plugins) > 0

    def test_plugins_have_name_attribute(self):
        """Verify each plugin has a NAME attribute."""
        plugins = load_plugins()
        for name, plugin in plugins.items():
            assert hasattr(plugin, 'NAME'), f"Plugin {name} missing NAME attribute"

    def test_plugins_have_is_waf_function(self):
        """Verify each plugin has an is_waf function."""
        plugins = load_plugins()
        for name, plugin in plugins.items():
            assert hasattr(plugin, 'is_waf'), f"Plugin {name} missing is_waf function"
            assert callable(plugin.is_waf), f"Plugin {name} is_waf is not callable"

    def test_known_plugins_loaded(self):
        """Verify some known plugins are loaded."""
        plugins = load_plugins()
        known_plugins = ['cloudflare', 'fastly', 'awswaf', 'anubis']
        for plugin_name in known_plugins:
            assert plugin_name in plugins, f"Expected plugin {plugin_name} not found"

    def test_plugin_names_are_strings(self):
        """Verify plugin keys are strings."""
        plugins = load_plugins()
        for name in plugins.keys():
            assert isinstance(name, str)
