from orator.migrations import Migration


class CreateMessagesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('messages') as table:
            table.string('id_message',20)
            table.primary('id_message')
            table.string('id_sender',20).unsigned()
            table.foreign('id_sender').references('id_sender').on('sender')
            table.string('time',20)
            table.text('text')


            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('messages')
