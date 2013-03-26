====================================
 Migrations and initial development
====================================

Hint from http://regebro.wordpress.com/2013/01/25/non-obvious-beginners-hint-for-development-with-django-and-south/

Using Django and South for initial development, that is when you are
continuously changing your schema to find the right one.

Instead of making new migration steps for every change, first make an
initial migration step::

  python [yourproject]/manage.py schemamigration [yourapp] --initial

Then, each time you need to change the schema, instead of making a new
migration, update the first initial one::

  python [yourproject]/manage.py schemamigration [yourapp] --initial --update

This well first back out the old initial migration, in practice
clearing the app database, and then regenerate the initial
migration. When you run the migration, it will create a new empty
database::

  python [yourproject]/manage.py migrate [yourapp]

That means you have to recreate the test data. You can do that by
making test/demo data once, and dump it::

  python [yourpoject]/manage.py dumpdata [yourapp] --indent=4 [yourproject]/[yourapp]/fixtures/test_data.json

After you change the schema, you will have to update the schema in the
``test_data.json`` file as well, but then you can load it into the
database::

  python [yourproject]/manage.py loaddata test_data

As an addition bonus, you now have fixture data for your tests!

You can keep using ``--initial --update`` until you start installing a
staging server. At that point you need to have proper migrations as
people will put data into the staging server. It might not be real
production data, but they might get annoyed if it disappears. Then you
can use ``--update`` for all the schema changes you do between two
releases, so all the changes in one release only need one upgrade
step.
