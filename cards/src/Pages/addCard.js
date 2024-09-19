const fs = require('fs');
const path = require('path');

const addCard = (newCard) => {
  const cardsFilePath = path.join(__dirname, 'datas', 'cards.json');

  fs.readFile(cardsFilePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Failed to read cards file:', err);
      return;
    }

    const cards = JSON.parse(data);
    cards.push(newCard);

    fs.writeFile(cardsFilePath, JSON.stringify(cards, null, 2), (err) => {
      if (err) {
        console.error('Failed to write to cards file:', err);
      } else {
        console.log('Card added successfully');
      }
    });
  });
};

module.exports = addCard;