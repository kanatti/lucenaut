from textual.app import App
from textual.widgets import DataTable
from lucenaut_cli.ffi import get_segment_metadata

class LucenautApp(App):
    def compose(self):
        table = DataTable()
        table.add_columns("Segment", "Doc Count", "Codec", "Compound")

        segments = get_segment_metadata("path/to/index")
        for seg in segments:
            table.add_row(
                seg["name"],
                str(seg["doc_count"]),
                seg["codec"],
                "Yes" if seg["is_compound"] else "No"
            )
        yield table

def main():
    app = LucenautApp()
    app.run()

