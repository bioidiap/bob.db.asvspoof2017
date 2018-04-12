.. vim: set fileencoding=utf-8 :
.. Fri 3 Feb 11:51:35 CEST 2016

.. image:: http://img.shields.io/badge/docs-v1.1.0-yellow.png
   :target: https://www.idiap.ch/software/bob/docs/bob/bob.db.asvspoof2017/v1.1.0/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/bob/bob.db.asvspoof2017/master/index.html
.. image:: https://gitlab.idiap.ch/bob/bob.db.asvspoof2017/badges/v1.1.0/build.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof2017/commits/v1.1.0
.. image:: https://gitlab.idiap.ch/bob/bob.db.asvspoof2017/badges/v1.1.0/coverage.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof2017/commits/v1.1.0
.. image:: https://img.shields.io/badge/gitlab-project-0000c0.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.asvspoof2017
.. image:: http://img.shields.io/pypi/v/bob.db.asvspoof2017.png
   :target: https://pypi.python.org/pypi/bob.db.asvspoof2017


=========================================
 ASVspoof2017 Database Interface for Bob
=========================================

This package is part of the signal-processing and machine learning toolbox
Bob_. It contains a Bob-based access API for the ASVspoof2017_ Database. The
database is used in Automatic Speaker Verification Spoofing and Countermeasures
Challenge (ASVspoof 2017). Genuine speech is collected from 10
speakers for training set and 8 speakers for development set.
Presentation attacks are then generated from the genuine data using a number
of different replay attacks using different devices recorded in different environments.

Installation
------------

Complete Bob's `installation`_ instructions. Then, to install this package,
run::

  $ conda install bob.db.asvspoof2017


Contact
-------

For questions or reporting issues to this software package, contact our
development `mailing list`_.


.. Place your references here:
.. _bob: https://www.idiap.ch/software/bob
.. _installation: https://gitlab.idiap.ch/bob/bob/wikis/Installation
.. _mailing list: https://groups.google.com/forum/?fromgroups#!forum/bob-devel
.. _asvspoof2017: http://www.spoofingchallenge.org/