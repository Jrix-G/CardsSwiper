import React, { useEffect, useState } from 'react';
import Slider from 'react-slick';
import { Link } from 'react-router-dom';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

interface Card {
  title: string;
  response: string;
}

const Home = () => {
  const [cards, setCards] = useState<Card[]>([]);

  useEffect(() => {
    fetch('http://localhost:3001/Pages/datas/cards.json')
      .then(response => response.json())
      .then(data => setCards(data))
      .catch(error => console.error('Error fetching cards:', error));
  }, []);

  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <div>
      <h1>Cards Swiper</h1>
      <Slider {...settings}>
        {cards.map((card, index) => (
          <div key={index}>
            <h2>{card.title}</h2>
            <p>{card.response}</p>
          </div>
        ))}
      </Slider>
      <Link to="/cardCreate">
        <button>Create New Card</button>
      </Link>
    </div>
  );
};

export default Home;
