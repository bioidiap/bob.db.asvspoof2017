.. vim: set fileencoding=utf-8 :
.. @author: Pavel Korshunov <Pavel.Korshunov@idiap.ch>
.. @date:   Fri 3 Feb 15:06:22 CEST 2017

.. _bob.db.asvspoof2017:

===============================
ASVspoof2017 Database Interface
===============================

ASVspoof2017 Protocols
----------------------

ASVspoof2017_ database provides one protocols::

	* competition - protocol used in Automatic Speaker Verification Spoofing and Countermeasures Challenge (ASVspoof 2017) that currently includes only training and development data.

The protocol is supported by `bob.db.asvspoof2017` DB interface for Bob_.


Getting the data
----------------

The original data and the description of protocols can be downloaded directly from ASVspoof2017_.


Using this interface 
--------------------

Once the interface package is installed, SQL database file need to be downloaded using the following command:

.. code-block:: sh

    $ .bin/bob_dbmanage.py asvspoof2017 download


This interface can be used to directly query and access the database protocols and in PAD `bob.pad.voice` framework of Bob toolkit.

The database filelist can be queried via the following command line:

.. code-block:: sh

    $ .bin/bob_dbmanage.py asvspoof2017 dumplist --help

To use the database in experiment within `bob.pad.` framework, a `bob.pad.database` entry point need to be defined in the `setup.py` file of the package that would run these experiments as so, as follows:

.. code-block:: python

        'bob.pad.database': [
            'asvspoof2017             = bob.path.to.config.file:database',
	]

The config file (other ways to defined the database are also available in Bob_, please see database API documentation) would then initialize the `database` with the path to the directory where the actual database sample are located, as follows:

.. code-block:: python

	import bob.pad.voice.database
	asvspoof2017_input_dir = "PATH_TO_DATA"
	database = bob.pad.voice.database.ASVspoof2017BioDatabase(
	    protocol = 'competition',
	    original_directory=asvspoof2017_input_dir,
	    original_extension=".wav",
	    training_depends_on_protocol=True,
	)

Specifying `bob.pad.database` entry point ensures that the PAD frameworks can find and use the database.


.. _bob: https://www.idiap.ch/software/bob
.. _ASVspoof2017: http://www.spoofingchallenge.org/
.. _idiap: http://www.idiap.ch


