const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const app = express();
const PORT = 3001;

app.use(cors());

app.use(express.json());

app.post('/addCard', (req, res) => {
  const newCard = req.body;
  const filePath = path.join(__dirname, '..', 'cards', 'src', 'datas', 'cards.json');

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading JSON file:', err);
      return res.status(500).send('Error reading file');
    }

    let cards;
    try {
      cards = data ? JSON.parse(data) : [];
    } catch (parseErr) {
      console.error('Error parsing JSON file:', parseErr);
      return res.status(500).send('Error parsing file');
    }

    cards.push(newCard);

    fs.writeFile(filePath, JSON.stringify(cards, null, 2), 'utf8', (writeErr) => {
      if (writeErr) {
        console.error('Error writing JSON file:', writeErr);
        return res.status(500).send('Error writing file');
      }

      res.status(201).json(newCard);
    });
  });
});

app.get('/loadCards', (req, res) => {
  const filePath = path.join(__dirname, '..', 'cards', 'src', 'datas', 'cards.json');

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading JSON file:', err);
      return res.status(500).send('Error reading file');
    }

    let cards;
    try {
      cards = data ? JSON.parse(data) : [];
    } catch (parseErr) {
      console.error('Error parsing JSON file:', parseErr);
      return res.status(500).send('Error parsing file');
    }

    res.status(200).json(cards);
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});