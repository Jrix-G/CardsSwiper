import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Latex from 'react-latex';

interface Card {
  title: string;
  response: string;
}

const Home = () => {
  const [cards, setCards] = useState<Card[]>([]);
  const [currentCardIndex, setCurrentCardIndex] = useState(0);
  const [userResponse, setUserResponse] = useState('');
  const [showAnswer, setShowAnswer] = useState(false);
  const [correctAnswers, setCorrectAnswers] = useState<number[]>([]);

  const loadCards = async () => {
    try {
      const response = await fetch('http://localhost:3001/loadCardsToDo');
      const data = await response.json();
      setCards(data);
      setCorrectAnswers(new Array(data.length).fill(0));
    } catch (error) {
      console.error('Error fetching cards:', error);
    }
  };

  useEffect(() => {
    loadCards();
  }, []);

  const handleInputChange = (value: string) => {
    setUserResponse(value);
  };

  const handleCheckAnswer = () => {
    console.log(userResponse.replace(/\\\\/g, '\\').toLowerCase(), cards[currentCardIndex].response.toLowerCase())
    if (userResponse.replace(/\\\\/g, '\\').toLowerCase() === cards[currentCardIndex].response.toLowerCase()) {
      const newCorrectAnswers = [...correctAnswers];
      newCorrectAnswers[currentCardIndex] += 1;
      setCorrectAnswers(newCorrectAnswers);
      alert('Correct answer!');
    } else {
      alert('Incorrect answer. Try again.');
    }
  };

  const handleShowAnswer = () => {
    setShowAnswer(true);
  };

  const handleNextCard = () => {
    setShowAnswer(false);
    setUserResponse('');
    setCurrentCardIndex((prevIndex) => (prevIndex + 1) % cards.length);
  };

  if (cards.length === 0) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <div>
        <h2>
          <Latex>{cards[currentCardIndex].title}</Latex>
        </h2>
        <input
          type="text"
          value={userResponse}
          onChange={(e) => handleInputChange(e.target.value)}
        />
        <button onClick={handleCheckAnswer}>Submit Answer</button>
        <button onClick={handleShowAnswer}>Show Answer</button>
        {showAnswer && (
          <p>
            <Latex>{cards[currentCardIndex].response}</Latex>
          </p>
        )}
        <p>Correct answers: {correctAnswers[currentCardIndex]}</p>
        <button onClick={handleNextCard}>Next Card</button>
      </div>
      <div>
        <Link to="/cardCreate">
          <button>Create New Card</button>
        </Link>
      </div>
    </div>
  );
};


export default Home;