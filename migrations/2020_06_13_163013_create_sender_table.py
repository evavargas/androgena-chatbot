from orator.migrations import Migration


class CreateSenderTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('sender') as table:
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('sender')
