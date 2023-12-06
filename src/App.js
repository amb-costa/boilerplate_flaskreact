import logo from './logo.svg';
import './App.css';

function App() {
  // this is already connected to the RESTful API on app.py
  const funct = async () =>{
    const resp = await fetch("/maintest/",{
      method: 'GET',
      headers: {
        "Content-Type" : "application/json"
      }
    })
    const data = await resp.json()
    console.log(data)
  }

  funct()
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
