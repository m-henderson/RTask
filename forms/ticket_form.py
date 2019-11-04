from models.ticket import Ticket
from wtforms_alchemy import ModelForm
from wtforms import SubmitField

class TicketForm(ModelForm):
    class Meta():
        model = Ticket
        button_map = SubmitField()
