Introduction
============

This is a bare-bones experimental Proof-Of-Concept to demo how the existing
portlet machinery in Plone can be used to build a flexible grid-based layout
system that allows for code-driven run-time layout personalization.

This PoC currently has two features:

- A custom ReversePortletRetriever reorders the sequence of portlets.

This is currently hacked via overrides.zcml and ought to use some
more elegant component registration instead that finds a way to hook
into the portletmanager adapter factory.

- A custom GridPortletRenderer wraps portlets in a div with markup
  that indicates the priority of the portlet.

This currently does not actually do any positioning. But it demonstrates
that this would be easily feasible.

Roadmap
-------

* Tests.

* Possibly override plone.app.portlets.portletcontext to strip out implicit
  acquisition from the portlet config. Which also is a potential performance
  issue.

* Expand the retriever ordening logic with a pluggable personalization system.

* Expand the renderer into an actual grid positioning system plus the possibility
  to render portlets in multiple modes (e.g. a blown-up "hero" mode).

* Replace #content-core rendering with a portlet based rendering and drop all
  content except for one portlet manager. I.e. replace the main layout logic
  for a page with the portlet-defined layout engine prototyped here.

Not On The Roadmap
------------------

* What's not on this roadmap is editing layouts and reordering portlets.
  Coders can provide layouts. Portlets can be ordered by humans or code already.

