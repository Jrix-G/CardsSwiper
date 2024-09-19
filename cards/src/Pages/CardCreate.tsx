import React, { useState, useEffect } from 'react';

const CardCreate = () => {
  const [title, setTitle] = useState('');
  const [response, setResponse] = useState('');
  interface Card {
    id: number;
    title: string;
    response: string;
    date: string;
  }
  
  const [cards, setCards] = useState<Card[]>([]);

  useEffect(() => {
    const fetchCards = async () => {
      try {
        const res = await fetch('http://localhost:3001/loadCards');
        const data = await res.json();
        setCards(data);
      } catch (error) {
        console.error('Error fetching cards:', error);
      }
    };

    fetchCards();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    let id = Math.floor(Math.random() * 1000000000) + 1;

    const newCard = {
        id, 
        title,
        response,
        date: new Date().toLocaleDateString('fr-FR')
    };

    try {
      await fetch('http://localhost:3001/addCard', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newCard),
      });

      setTitle('');
      setResponse('');

      setCards((prevCards) => [...prevCards, newCard]);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Create a New Card</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Title:</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="response">Response:</label>
          <input
            type="text"
            id="response"
            value={response}
            onChange={(e) => setResponse(e.target.value)}
            required
          />
        </div>
        <button type="submit">Create Card</button>
      </form>

      <h2>Existing Cards</h2>
      <ul>
        {cards.map((card, index) => (
          <li key={index}>
            <strong>{card.title}</strong>: {card.response} (Created on: {card.date})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CardCreate;