from Acquisition import aq_inner
from zope.schema.vocabulary import SimpleVocabulary

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode


def RolesVocabularyFactory(context):
    """ Vocabulary Factory for Roles in the Plone Site
    """

    # context is the content rule object which is stored in the plone site

    pmemb = getToolByName(aq_inner(context), 'portal_membership')
    roles = sorted(pmemb.getPortalRoles())

    sane_roles = [(safe_unicode(role).encode('ascii', 'replace'),
                   safe_unicode(role)) for role in roles]
    return SimpleVocabulary.fromItems(sane_roles)
