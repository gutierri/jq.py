*****
jq.py
*****

jq.py is a simple jq-like for Pythonists

like jq, jq.py does the processing of JSON structures, but using dot notation
and native list features to process queries.


example:

.. code-block:: sh

   $ echo '{"results": [{"x": "1"},{"y":"2"}]}' | jq.py -q "results[0]"
   {
    "x": "1"
   }

   $ echo '{"body": {"title": "my title"}}' | jq.py -q "body.title"
   "my title"

for more information and documentation: ``jq.py --help``

installation
############

from source

.. code-block:: sh

   $ curl -o ~/.local/bin/jq.py https://raw.github.com/gutierri/jq.py/main/jq.py

from git

.. code-block:: sh

   $ python3 -m pip install git+https://github.com/gutierri/jq.py.git#egg=jq.py

license
#######
jq.py is free software, licensed under the GNU General Public License,
which can be found in the file COPYING.
