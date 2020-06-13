from orator.migrations import Migration


class CreateSenderTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('sender') as table:
            table.string('id_sender',20)
            table.primary('id_sender')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('sender')
