import { useEffect, useState } from 'react';
import chime_logo from '../assets/chime_logo.png';
import '../styles/App.css';
import Dropdown from './Dropdown'

function App() {

  const LOCAL_SERVER = 'http://localhost:8000';

  const [scale, setScale] = useState('calm');
  const [color, setColor] = useState('brown');
  
  useEffect(() => { // fetch scale setting and send to Python
    async function fetchScaleSetting() {
      const scaleSetting = {
        scale: scale,
      }
      const settings = {
        method: "POST",
        body: JSON.stringify(scaleSetting),
        headers: {
          "Content-Type": "application/json",
        },
      }
      const res = await fetch(`${LOCAL_SERVER}/scale`, settings)
      const data = await res.json();
      console.log(data);
    }
    fetchScaleSetting();
    
  }, [scale])  // set mode based on scale
  
  useEffect(() => {
    const brown = '#783c23';
    const red = '#8e1001';
    const purple = '#25016a';

    if (scale === 'calm') setColor(brown)
    if (scale === 'reflective') setColor(purple)
    if (scale === 'hopeful') setColor(red) 
    console.log(color);
    document.body.style.backgroundColor = color;
  }, [scale])

  const handleSelect = (e) => {
    console.log(e.target.value);
    setScale(e.target.value);
  };

  return (
    <>
      <div className="App">
        <img src={chime_logo} className="chime-logo" alt="logo" />
        <div className="Dropdown">
          <Dropdown 
            scale={scale}
            setScale={setScale}
            // action="http://localhost:8000/scale"
          />
        </div>
      </div>
    </>
  );
}

export default App;


// BELOW CODE WORKS BUT REPLACED BY ABOVE!

  //   const scaleSetting = {
  //     scale: 'scale',
  //   }
  //   const settings = {
  //     method: "POST",
  //     body: JSON.stringify(scaleSetting),
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //   }

  //   const res = await fetch(`${LOCAL_SERVER}/scale`, settings)
  //   const data = await res.json();

  //   console.log(data);
  // }, [scale])  // set mode based on scale

  // END CODE THAT WORKS


  // useEffect(() => {
  //   if (scale) {
  //     // if user location exists
  //     switch (mode) {
  //       case 'calm':
  //         postScale('calm');
  //         break;
  //       case 'reflective':
  //         postScale('reflective');
  //         break;
  //       case 'hopeful':
  //         postScale('hopeful');
  //         break;
  //       default:
  //         break;
  //     }
  //   }
  //   // eslint-disable-next-line react-hooks/exhaustive-deps
  // }, [scale, mode]);
