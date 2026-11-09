from flask import Flask, render_template, request  # <-- AJOUTÉ : ", request" pour lire l'URL

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    # LIT le paramètre "nom" dans l'adresse, ou utilise "visiteur" par défaut
    nom_utilisateur = request.args.get("nom", "visiteur")
    # ENVOIE ce nom au fichier HTML
    return render_template("accueil.html", nom=nom_utilisateur)


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------

@app.route("/contact")
def contact():
    return "Pour me contacter, envoyez un e-mail à : ramitsm95@exemple.com"

# La nouvelle route pour l'exercice 9 a été insérée ici 👇
@app.route("/erreur-test")
def erreur_test():
    from flask import abort
    abort(404)

# La nouvelle route pour l'exercice 10 a été insérée ici 👇
@app.route("/qui-suis-je")
def qui_suis_je():
    navigateur = request.headers.get("User-Agent")
    return f"<h1>Voici votre signature numerique :</h1><p>{navigateur}</p>"

# La toute dernière route pour l'exercice 11 a été insérée ici 👇
@app.route("/api/meteo")
def api_meteo():
    from flask import jsonify
    donnees = {
        "ville": "Paris",
        "temperature": 18.5,
        "conditions": "Ensoleille",
        "humidite": 62
    }
    return jsonify(donnees)

# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
