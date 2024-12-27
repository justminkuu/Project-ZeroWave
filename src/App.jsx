import React from "react";
import './styles.css'; 

function App() {
  return (
    <div>
      <head>
        <title>Project ZeroWave</title>
        <meta name="description" content="Sustainability and climate change project" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body>
        <div className="main-container">
          <h1>Welcome to Project ZeroWave</h1>
          <p>This project aims to address sustainability and climate change.</p>
          <button className="btn-primary">Learn More</button>
        </div>
      </body>
    </div>
  );
}

export default App;
