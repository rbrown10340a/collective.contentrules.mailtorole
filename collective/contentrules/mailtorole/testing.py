# -*- coding: utf-8 -*-

from zope.configuration import xmlconfig

from plone.testing import z2
from Products.Five import fiveconfigure
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import applyProfile


class TestMailToRoleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        fiveconfigure.debug_mode = True
        import collective.contentrules.mailtorole
        xmlconfig.file('configure.zcml',
                       collective.contentrules.mailtorole,
                       context=configurationContext)
        z2.installProduct(app, 'collective.contentrules.mailtorole')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.contenttypes:default')
        portal.portal_workflow.setDefaultChain("simple_publication_workflow")
        # quickInstallProduct(portal, 'rt.lastmodifier')
        # setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])
        # acl_users = portal.acl_users
        # acl_users.userFolderAddUser('user1', 'secret', ['Member'], [])
        # member = portal.portal_membership.getMemberById('user1')
        # member.setMemberProperties(mapping={"fullname": "User 1"})
        # setRoles(portal, 'user1', ['Member', 'Contributor', 'Editor', 'Reviewer'])


MAILTOROLE_FIXTURE = TestMailToRoleLayer()
MAILTOROLE_INTEGRATION_TESTING = \
    IntegrationTesting(
        bases=(MAILTOROLE_FIXTURE, ),
        name="MailToRole:Integration"
    )
