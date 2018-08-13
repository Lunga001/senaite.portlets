# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from senaite.portlets.testing import SENAITE_PORTLETS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that senaite.portlets is properly installed."""

    layer = SENAITE_PORTLETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if senaite.portlets is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'senaite.portlets'))

    def test_browserlayer(self):
        """Test that ISenaitePortletsLayer is registered."""
        from senaite.portlets.interfaces import (
            ISenaitePortletsLayer)
        from plone.browserlayer import utils
        self.assertIn(ISenaitePortletsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SENAITE_PORTLETS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['senaite.portlets'])

    def test_product_uninstalled(self):
        """Test if senaite.portlets is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'senaite.portlets'))

    def test_browserlayer_removed(self):
        """Test that ISenaitePortletsLayer is removed."""
        from senaite.portlets.interfaces import \
            ISenaitePortletsLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISenaitePortletsLayer, utils.registered_layers())
