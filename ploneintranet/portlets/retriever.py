import random
from zope.component import adapts
from zope.interface import implements
from zope.interface import Interface

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRetriever
from plone.portlets.retriever import PortletRetriever

from ploneintranet.portlets.interfaces import IPloneintranetPortletsEnabled
from ploneintranet.portlets.interfaces import IPortletManager


class ReversePortletRetriever(PortletRetriever):
    """A silly proof of concept that reorders portlets."""

    implements(IPortletRetriever)
    adapts(Interface, IPortletManager)

    def getPortlets(self):
        """Just reverses the actual portlet sequence.
        You can imagine more funky prioritization going on here."""

        assignments = PortletRetriever.getPortlets(self)
        if random.choice((True, False)):
            assignments.reverse()
        return assignments
