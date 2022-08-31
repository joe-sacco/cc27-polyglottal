import { useEffect, useState } from 'react';
import chime_logo from '../assets/chime_logo.png';
import '../styles/App.css';
import Dropdown from './Dropdown'

function App() {

  const [scale, setScale] = useState('calm');

  // axios post req here
  
  return (
    <>
      <div className="App">
      <img src={chime_logo} className="chime-logo" alt="logo" />
      <div className="Dropdown">
        <Dropdown 
          scale={scale}
          setScale={setScale}
        />
      </div>
      
      </div>
    </>
  );
}

export default App;


//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>

