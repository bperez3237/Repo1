import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
import CostCodeList from './components/CostCodeList';

function App() {

  return (
    <div className="App">
      <header>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
      <CostCodeList />
    </div>
  );
}

export default App;
