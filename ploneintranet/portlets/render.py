from zope.component import adapts
from zope.interface import implements
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserView

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletManagerRenderer
from plone.portlets.manager import PortletManagerRenderer

from ploneintranet.portlets.interfaces import IPloneintranetPortletsEnabled


class GridPortletRenderer(PortletManagerRenderer):
    """A portlet renderer that marks up portlet renderings with
    grid css classes.
    """
    implements(IPortletManagerRenderer)
    adapts(Interface, IPloneintranetPortletsEnabled, IBrowserView, IPortletManager)

    def render(self):
        renderings = []
        i = 0
        portlets = self.portletsToShow()
        for p in portlets:
            i += 1
            klass = "foobar-%s" % i  # just a PoC, do something more fancy here
            rendered = p['renderer'].render()
            renderings.append('<div class="%s">%s</div>' % (klass, rendered))
        # obviously an ugly hack to highlight the concept
        # would be grid positioning classes etc in a production implementation
        styles = """
<style type="text/css">
.foobar-1 {background-color: #eeaaaa; font-weight: bold; }
.foobar-2 { background-color: #aaaaee; }
</style>"""
        return styles + '\n'.join(renderings)
