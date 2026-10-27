from collections import Counter
from flask import Flask, redirect, render_template, request, session, url_for
from langdetect import detect, DetectorFactory
import spacy
from translations import TRANSLATIONS

DetectorFactory.seed = 0

app = Flask(__name__)
app.secret_key = "temporal_secret_key"

nlp_models = {
    "es": spacy.load("es_core_news_sm"),
    "en": spacy.load("en_core_web_sm"),
    "fr": spacy.load("fr_core_news_sm"),
    "it": spacy.load("it_core_news_sm"),
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form.get("text", "")
        language = request.form.get("language", "en")

        session["language"] = language

        nlp = nlp_models.get(language, nlp_models["en"])
        t = TRANSLATIONS.get(language, TRANSLATIONS["en"])

        if user_text.strip():
            doc = nlp(user_text)

            tokens = [token for token in doc if not token.is_space]
            words = [token for token in tokens if not token.is_punct]
            sentences = list(doc.sents)

            num_words = len(words)
            has_verbs = any(token.pos_ in ("VERB", "AUX") for token in doc)

            warnings = []

            if num_words < 10 or not has_verbs:
                warnings.append(t.get("not_a_sentence_warning", "El texto debe tener al menos 10 palabras y una estructura oracional válida con verbos."))

            detected_lang = language
            try:
                raw_detected = detect(user_text)
                detected_lang = raw_detected[:2].lower()
            except Exception:
                pass

            if detected_lang != language and detected_lang in nlp_models:
                warnings.append(t["lang_mismatch_warning"])

            if warnings:
                session["diagnoses"] = warnings
                session["metrics"] = None
                session["frequent_words"] = []
                session["user_text"] = user_text
                return redirect(url_for("index"))

            unique_words = set([token.text.lower() for token in words])
            lexical_richness = len(unique_words) / num_words if num_words > 0 else 0
            
            has_punctuation = any(token.is_punct and token.text in '.!?' for token in doc)
            if has_punctuation and len(sentences) > 0:
                num_sentences = len(sentences)
            else:
                num_sentences = max(1, len(user_text.split(',')))

            average_sentence_length = num_words / num_sentences

            meaningful_words = [
                token.text.lower() for token in doc 
                if not token.is_stop and not token.is_punct and not token.is_space and len(token.text) > 1
            ]
            most_common_words = Counter(meaningful_words).most_common(5)

            session["metrics"] = {
                "words": num_words,
                "richness": round(lexical_richness, 2),
                "length": round(average_sentence_length, 1),
            }
            
            session["frequent_words"] = most_common_words

            diagnoses = []
            if lexical_richness > 0.6:
                diagnoses.append(t["rich_style"])
            else:
                diagnoses.append(t["mod_style"])

            if average_sentence_length > 25:
                diagnoses.append(t["complex_syntax"])
            else:
                diagnoses.append(t["agile_syntax"])

            session["diagnoses"] = diagnoses
            session["user_text"] = user_text

        return redirect(url_for("index"))

    metrics = session.pop("metrics", None)
    diagnoses = session.pop("diagnoses", None)
    frequent_words = session.pop("frequent_words", [])
    user_text = session.pop("user_text", "")

    selected_language = session.get("language", "en")
    t = TRANSLATIONS.get(selected_language, TRANSLATIONS["en"])

    return render_template(
        "index.html",
        metrics=metrics,
        diagnoses=diagnoses,
        frequent_words=frequent_words,
        user_text=user_text,
        selected_language=selected_language,
        t=t,
    )


if __name__ == "__main__":
    app.run(debug=True)