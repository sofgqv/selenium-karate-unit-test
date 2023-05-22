import logo from './logo.svg';
import './App.css';
import {useState} from 'react';

function App() {

  const [data, setData] = useState('');
  const [err, setErr] = useState('');
  const [state, setState] = useState({
    member1: '',
    member2: '',
    member3: '',
    member4: '',
    member5: '',
    member6: ''
  });
  

  const handleClick = async () => {
    try {
      console.log(state)
      setData(state);
    } catch (err) {
      setErr(err.message);
    }
  };

  function handleChange(evt) {
    const value = evt.target.value;
    setState({
          ...state,
          [evt.target.name]: value
        });
  }

  return (
    <div className="App">
      <div>
        Test Me !
        <div>
          Member 1: <input 
              name = "member1"
              type="text" 
              value = {state.member1}
              onChange={handleChange}
          />
          Member 2: <input
              name = "member2"
              type="text" 
              value = {state.member2}
              onChange={handleChange}
          />
          Member 3: <input
              name = "member3"
              type="text" 
              value = {state.member3}
              onChange={handleChange}
          />
          Member 4: <input
              name = "member4"
              type="text" 
              value = {state.member4}
              onChange={handleChange}
          />
          Member 5: <input
              name = "member5"
              type="text" 
              value = {state.member5}
              onChange={handleChange}
          />
          Member 6: <input
              name = "member6"
              value = {state.member6}
              type="text" 
              onChange={handleChange}
          />
        </div>
        <button type="button" onClick={handleClick}>
          Click Me
        </button>
        <div>
        {data.member1} {data.member2} {data.member3} {data.member4} {data.member5} {data.member6}
        </div>
      </div>
    </div>
  );
}

export default App;
