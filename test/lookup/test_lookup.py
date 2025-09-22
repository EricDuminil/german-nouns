import pytest

from german_nouns.lookup import Nouns

# TODO: https://de.wiktionary.org/wiki/Verzeichnis:Deutsch/Komposita_mit_%C3%9Cberl%C3%A4nge
# "Donaudampfschifffahrtsgesellschaftskapitän" -> ['Donaudampfschifffahrtsgesellschaft', 'Kapitän'] :/

test_words = [
    (
        "Faktencheck",
        [
            {
                "flexion": {
                    "nominativ singular": "Faktencheck",
                    "nominativ plural": "Faktenchecks",
                    "genitiv singular": "Faktenchecks",
                    "genitiv plural": "Faktenchecks",
                    "dativ singular": "Faktencheck",
                    "dativ plural": "Faktenchecks",
                    "akkusativ singular": "Faktencheck",
                    "akkusativ plural": "Faktenchecks",
                },
                "lemma": "Faktencheck",
                "pos": ["Substantiv"],
                "genus": "m",
            }
        ],
    ),
    (
        "Krüge",
        [
            {
                "flexion": {
                    "nominativ singular": "Krug",
                    "nominativ plural": "Krüge",
                    "genitiv singular": "Kruges",
                    "genitiv singular*": "Krugs",
                    "genitiv plural": "Krüge",
                    "dativ singular": "Krug",
                    "dativ singular*": "Kruge",
                    "dativ plural": "Krügen",
                    "akkusativ singular": "Krug",
                    "akkusativ plural": "Krüge",
                },
                "lemma": "Krug",
                "pos": ["Substantiv"],
                "genus": "m",
            }
        ],
    ),
    (
        "Heidelberg",
        [{"flexion": {}, "lemma": "Heidelberg", "pos": ["Substantiv", "Toponym"]}],
    ),
]

test_articles = [
    ("Das", "Ende"),
    ("Das", "Feedback"),
    ("Das", "Formular"),
    ("Das", "Geld"),
    ("Das", "Kabel"),
    ("Das", "Konzept"),
    ("Das", "Körpergewicht"),
    ("Das", "Meeting"),
    ("Das", "Projekt"),
    ("Das", "Quartier"),
    ("Das", "Radler"),
    ("Das", "Seil"),
    ("Das", "T-Shirt"),
    ("Das", "Teil"),  # : etwas Losgelöstes, für ein einzelnes Stück."
    ("Das", "Thema"),
    ("Das", "Ticket"),
    ("Das", "Tool"),
    ("Das", "Treffen"),
    ("Das", "Vertrauen"),
    ("Der", "Akzent"),
    ("Der", "Bericht"),
    ("Der", "Beton"),
    ("Der", "Code"),
    ("Der", "Einfluss"),
    ("Der", "Geruch"),
    ("Der", "Kalender"),
    ("Der", "Schloss"),
    ("Der", "Teil#"),  # : Untermenge eines Ganzen"
    ("Der", "Verein"),
    ("Der", "Wechsel"),
    ("Der", "Workflow"),
    ("Der", "Workshop"),
    ("Der", "Überblick"),
    ("Die", "Band"),
    ("Die", "Butter"),
    ("Die", "Konferenz"),
    ("Die", "Nutella"),
]

ARTICLES = {
        'f': 'Die',
        'm': 'Der',
        'n': 'Das'
}


compound_test_words = [
    ("Faktencheck", ["Fakt", "Check"]),
    ("Dreiergespann", ["Dreier", "Gespann"]),
    ("Falkenstein", ["Falke", "Stein"]),
    ("Vermögensbildung", ["Vermögen", "Bildung"]),
    ("Nichtpersonalmaskulinum", ["Personalmaskulinum"]),
    ("Berichterstattung", ["Bericht", "Erstattung"]),
    ("Ersatzlieferungen", ["Ersatz", "Lieferung"]),
    ("Transfergesellschaft", ["Transfer", "Gesellschaft"]),
    ("Dampfwalze", ["Dampf", "Walze"]),
    ("Einkommensteuer", ["Einkommen", "Steuer"]),
    ("Einkommensverteilung", ["Einkommen", "Verteilung"]),
    ("Ertragsteuer", ["Ertrag", "Steuer"]),
    ("Ertragssteigerung", ["Ertrag", "Steigerung"]),
    ("Körperschaftsteuer", ["Körperschaft", "Steuer"]),
    ("Körperschaftsstatus", ["Körperschaft", "Status"]),
    ("Verkehrszeichen", ["Verkehr", "Zeichen"]),
    ("Versicherungsteuer", ["Versicherung", "Steuer"]),
    ("Versicherungspolice", ["Versicherung", "Police"]),
]


# Loading nouns is expensive, so only do it once per test
@pytest.fixture(scope="module")
def nouns():
    return Nouns()


class TestLookup:
    @pytest.mark.parametrize("test_input,expected", test_words)
    def test_lookup(self, test_input, expected, nouns):
        result = nouns[test_input]

        assert result == expected

    @pytest.mark.parametrize("test_input,expected", compound_test_words)
    def test_parse_compound(self, test_input, expected, nouns):
        result = nouns.parse_compound(test_input)

        assert result == expected

    @pytest.mark.parametrize("expected, word", test_articles)
    def test_parse_articles(self, expected, word, nouns):
        article = ARTICLES[nouns[word][0]['genus']]
        assert article == expected
