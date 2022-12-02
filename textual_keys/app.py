"""Provides the main application class."""

##############################################################################
# Python imports.
from importlib.metadata import version

##############################################################################
# Textual imports.
from textual.app        import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets    import Header, Footer, Label
from textual.events     import Key

##############################################################################
# Local imports.
from . import __version__

##############################################################################
class TextualKeys( App[ None ] ):
    """Textual key event display application."""

    CSS = """
    #titles {
        dock: top;
        height: 1;
    }

    #titles Label {
        width: 1fr;
        background: $primary;
        border-left: solid $primary-lighten-2;
        padding-left: 1;
        text-style: bold;
    }

    .event {
        height: auto;
    }

    .event Label {
        border-left: solid $primary-lighten-2;
        padding-left: 1;
    }

    .zebra-on {
        background: $surface-lighten-2;
    }

    .zebra-off {
        background: $surface-lighten-1;
    }

    .event Label {
        width: 1fr;
    }
    """

    TITLE = "Textual Keys"
    """str: The title of the application."""

    SUB_TITLE = f"v{__version__} (Textual v{version( 'textual' )})"
    """str: The subtitle for the application."""

    def __init__( self ) -> None:
        """Initialise the app."""
        super().__init__()
        self.zebra = False

    def compose( self ) -> ComposeResult:
        """Compose the layout of the application.

        Returns:
            ComposeResult: The result of laying out the app's display.
        """
        yield Header()
        yield Vertical(
            Horizontal(
                Label( "Bindable Name" ),
                Label( "Printable Character" ),
                Label( "Aliases" ),
                id="titles"
            ),
            Vertical( id="keys" )
        )
        yield Footer()

    def on_key( self, event: Key ) -> None:
        """Handle a keyboard event.

        Args:
            event (Key): The keyboard event to handle.
        """
        self.query_one( "#keys", Vertical ).mount(
            Horizontal(
                Label( event.key ),
                Label( event.char if event.char is not None and event.is_printable else "" ),
                Label( "\n".join( event.key_aliases ) ),
                classes=f"event zebra-{'on' if self.zebra else 'off'}"
            ),
            before=0
        )
        self.zebra = not self.zebra

### app.py ends here
