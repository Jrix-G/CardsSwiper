const addCard = require('./addCard');

const newCard = {
  title: "Nouvelle carte",
  response: "Réponse de la nouvelle carte",
  date: new Date().toLocaleDateString('fr-FR')
};

addCard(newCard);