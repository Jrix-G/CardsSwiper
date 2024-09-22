import React, { useState, useEffect } from 'react';
import '../Styles/addcards.css';
import Latex from 'react-latex';

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
      <div className='create-new-card'>
        <div className='create-new-card-div'>
          <div className='create-new-card-div-second'>
            <h1 className='main-text-gradient-card-create'>Create A New Card</h1>
            <div className='form-card-creation'>
              <form onSubmit={handleSubmit}>
                <div>
                  <div className="wave-group wave-group-one">
                    <input 
                      type="text"
                      id="title"
                      value={title}
                      className='input'
                      onChange={(e) => setTitle(e.target.value)}
                      required 
                    />
                    <span className="bar"></span>
                    <label className="label">
                      <span className="label-char" style={{ '--index': 0 } as React.CSSProperties}>C</span>
                      <span className="label-char" style={{ '--index': 1 } as React.CSSProperties}>a</span>
                      <span className="label-char" style={{ '--index': 2 } as React.CSSProperties}>r</span>
                      <span className="label-char" style={{ '--index': 3 } as React.CSSProperties}>d</span>
                    </label>
                  </div>
                </div>
                <div>
                  <div className="wave-group wave-group-second">
                    <input 
                      type="text"
                      id="title"
                      value={response}
                      className='input'
                      onChange={(e) => setResponse(e.target.value)}
                      required 
                    />
                    <span className="bar"></span>
                    <label className="label">
                      <span className="label-char" style={{ '--index': 0 } as React.CSSProperties}>R</span>
                      <span className="label-char" style={{ '--index': 1 } as React.CSSProperties}>e</span>
                      <span className="label-char" style={{ '--index': 2 } as React.CSSProperties}>s</span>
                      <span className="label-char" style={{ '--index': 3 } as React.CSSProperties}>p</span>
                      <span className="label-char" style={{ '--index': 4 } as React.CSSProperties}>o</span>
                      <span className="label-char" style={{ '--index': 5 } as React.CSSProperties}>n</span>
                      <span className="label-char" style={{ '--index': 6 } as React.CSSProperties}>s</span>
                      <span className="label-char" style={{ '--index': 7 } as React.CSSProperties}>e</span>
                    </label>
                  </div>
                </div>
                <button type="submit" className='create-card-button'>Create Card</button>
              </form>
            </div>
          </div>
        </div>
      </div>

      <h2>Existing Cards</h2>
      <ul>
        {cards.map((card, index) => (
          <li key={index}>
            <strong><Latex>{card.title}</Latex></strong>: <Latex>{card.response}</Latex> (Created on: {card.date})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CardCreate;