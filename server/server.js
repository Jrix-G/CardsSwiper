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

  // Ensure that the backslashes are properly formatted
  // This replaces four backslashes with two
  newCard.title = newCard.title.replace(/\\\\/g, '\\');
  newCard.response = newCard.response.replace(/\\\\/g, '\\');

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

app.get('/loadCardsToDo', (req, res) => {
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

    const today = new Date();
    const oneMonthAgo = new Date();
    oneMonthAgo.setMonth(today.getMonth() - 1);

    console.log('Today:', today);
    console.log('One month ago:', oneMonthAgo);

    const convertDate = (dateStr) => {
      console.log('Original date string:', dateStr);
      const [day, month, year] = dateStr.split('/');

      console.log(`Day: ${day}, Month: ${month}, Year: ${year}`);

      const isoDate = `${year}-${month}-${day}`;
      const parsedDate = new Date(isoDate);

      console.log('Converted date:', parsedDate);

      return parsedDate;
    };

    const recentCards = cards.filter(card => {
      const cardDate = convertDate(card.date);

      if (isNaN(cardDate.getTime())) {
        console.error('Invalid Date for card:', card);
      }

      console.log('Card date:', cardDate, 'One month ago:', oneMonthAgo, 'Today:', today);

      return cardDate >= oneMonthAgo && cardDate <= today;
    });

    console.log('Recent cards:', recentCards);

    res.status(200).json(recentCards);
  });
});




app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});