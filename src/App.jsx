import { useState } from 'react'
import './App.css'

import Login from './Login.jsx'

function App() {
  const [count, setCount] = useState(0)
  const [user, setUser] = useState(null)

  if (!user) {
    return <Login onLogin={setUser} />
  }

  return (
    <>
      <div className="logout-container">
        <button className="logout-btn" onClick={() => setUser(null)}>
          Logout
        </button>
      </div>
      <h1>Welcome, {user.username}</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
    </>
  )
}

export default App
