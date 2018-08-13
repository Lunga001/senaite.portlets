# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import senaite.portlets


class SenaitePortletsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=senaite.portlets)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.portlets:default')


SENAITE_PORTLETS_FIXTURE = SenaitePortletsLayer()


SENAITE_PORTLETS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_PORTLETS_FIXTURE,),
    name='SenaitePortletsLayer:IntegrationTesting'
)


SENAITE_PORTLETS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_PORTLETS_FIXTURE,),
    name='SenaitePortletsLayer:FunctionalTesting'
)


SENAITE_PORTLETS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_PORTLETS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SenaitePortletsLayer:AcceptanceTesting'
)
