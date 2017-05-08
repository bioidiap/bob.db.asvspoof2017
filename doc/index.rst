.. vim: set fileencoding=utf-8 :
.. @author: Pavel Korshunov <Pavel.Korshunov@idiap.ch>
.. @date:   Fri 3 Feb 15:06:22 CEST 2017

.. _bob.db.asvspoof2017:

=================================
 ASVspoof2017 Database Interface
=================================

ASVspoof2017 Protocols
----------------------

ASVspoof2017_ database provides one protocols::

    * competition - protocol used in Automatic Speaker Verification Spoofing and Countermeasures Challenge (ASVspoof
    2017). It includes training and development sets with labels and an anonymized evaluation set.

The protocol is supported by `bob.db.asvspoof2017` DB interface for Bob_.


Getting the data
----------------

The original data and the description of protocols can be downloaded directly from ASVspoof2017_.


Using this interface 
--------------------

Once the interface package is installed, SQL database file need to be downloaded using the following command:

.. code-block:: sh

    $ bob_dbmanage.py asvspoof2017 download


This interface can be used to directly query and access the database protocols and samples, or/and in verification `bob.bio.` and PAD `bob.pad.` frameworks of Bob toolkit.

The database filelist can be queried via the following command line:

.. code-block:: sh

    $ bob_dbmanage.py asvspoof2017 dumplist --help

To use the database in verification experiments within `bob.bio.` framework, a `bob.bio.database` entry point need to be defined in the `setup.py` file of the package that would run these experiments as so, as follows:

.. code-block:: python

        'bob.bio.database': [
            'asvspoof2017             = bob.path.to.config.file:database',
	]

To use the database in experiment within `bob.pad.` framework, a `bob.pad.database` entry point need to be defined in the `setup.py` file of the package that would run these experiments as so, as follows:

.. code-block:: python

        'bob.pad.database': [
            'asvspoof2017             = bob.path.to.config.file:database',
	]

The config file (other ways to defined the database are also available in Bob_, please see database API documentation) would then initialize the `database` with the path to the directory where the actual database sample are located, see the following
example for a `bob.bio.` package:

.. code-block:: python

    import bob.bio.base.database
    asvspoof2017_input_dir = "PATH_TO_DATA"
    database = bob.bio.base.database.ASVspoof2017BioDatabase(
	    protocol = 'competition-licit',
	    original_directory=asvspoof2017_input_dir,
	    original_extension=".wav",
	    training_depends_on_protocol=True,
	)

Similarly, for PAD experiments, an entry point `bob.pad.database` should be defined in `setup.py` and `bob.pad.db.ASVspoofPadDatabase` should be defined in the config file.

Specifying `bob.bio.database` and/or `bob.pad.database` entry points ensures that the verification and/or PAD frameworks can find and use the database.


.. _bob: https://www.idiap.ch/software/bob
.. _ASVspoof2017: http://www.spoofingchallenge.org/
.. _idiap: http://www.idiap.ch


