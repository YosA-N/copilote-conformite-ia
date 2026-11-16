"""Guard of the remote mode: a question that holds personal data is never sent to the API.

Only simple, documented regular expressions, on four kinds of data that are easy to recognise: an e-mail
address, a French phone number, an IBAN and a French social security number (NIR). Names, situations
or health facts are NOT detected: this is a safety net, not a guarantee, as the README says.
In local mode nothing leaves the computer, so nothing is blocked.

The guard lives in the core: rag.answer_question calls refuse_personal_data() first, before the search and
before any call to the API, so every entry point (scripts/ask.py, a web interface…) is protected without
having to think of it. An entry point only has to show the PersonalDataError it receives.
"""

import re
from typing import Protocol

PERSONAL_DATA = {
    # user@example.org, prenom.nom+tag@sous.domaine.fr
    "une adresse e-mail": re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"),
    # 06 12 34 56 78, 06.12.34.56.78, 0612345678, +33 6 12 34 56 78, +33612345678
    "un numéro de téléphone": re.compile(r"(?<![\d/])(?:\+33\s?[1-9]|0[1-9])(?:[\s.-]?\d{2}){4}(?![\d/])"),
    # FR76 3000 6000 0112 3456 7890 189 (two letters, two digits, then 11 to 30 letters or digits, spaces allowed)
    "un IBAN": re.compile(r"\b[A-Z]{2}\d{2}(?:\s?[A-Z0-9]{4}){2,7}(?:\s?[A-Z0-9]{1,4})?\b"),
    # 1 85 05 78 006 084 36 : sex, year, month (01-12 or 20-99 when unknown), département (2 digits or 2A/2B),
    # commune, order number, and the optional 2-digit key
    "un numéro de sécurité sociale": re.compile(
        r"(?<!\d)[12]\s?\d{2}\s?(?:0[1-9]|1[0-2]|[2-9]\d)\s?(?:\d{2}|2[AB])\s?\d{3}\s?\d{3}(?:\s?\d{2})?(?!\d)"
    ),
}


def personal_data_found(text: str) -> list[str]:
    """The kinds of personal data found in the text, in a fixed order; empty when none is found."""
    return [kind for kind, pattern in PERSONAL_DATA.items() if pattern.search(text)]


class PersonalDataError(ValueError):
    """The question holds personal data and the model is remote: nothing was sent. str() is the message to show."""

    def __init__(self, kinds: list[str], provider: str):
        super().__init__(refusal_message(kinds, provider))
        self.kinds = kinds
        self.provider = provider


class RemoteOrLocal(Protocol):
    remote: bool
    provider: str


def refuse_personal_data(question: str, chat_model: RemoteOrLocal) -> None:
    """Raise PersonalDataError when the model is remote and the question holds personal data; nothing otherwise."""
    if not getattr(chat_model, "remote", False):
        return
    kinds = personal_data_found(question)
    if kinds:
        raise PersonalDataError(kinds, getattr(chat_model, "provider", "l'API distante"))


def refusal_message(kinds: list[str], provider: str) -> str:
    """Why the question was not sent, and what to do; the data itself is never repeated."""
    found = " et ".join(kinds) if len(kinds) <= 2 else ", ".join(kinds[:-1]) + " et " + kinds[-1]
    return (
        f"La question contient {found} : en mode distant, rien n'a été envoyé à {provider}. "
        "Reformulez-la sans ces données (par exemple « un client » plutôt que ses coordonnées), "
        "ou passez en mode local avec --backend ollama."
    )
