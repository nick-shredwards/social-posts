import { useState, useEffect } from 'react'
import './App.css'

import Login from './Login.jsx'

function App() {
  const [count, setCount] = useState(0)
  const [user, setUser] = useState(null)
  const [messages, setMessages] = useState([])
  const [newMessage, setNewMessage] = useState('')
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (user) {
      fetchMessages()
    }
  }, [user])

  async function fetchMessages() {
    setLoading(true)
    try {
      const res = await fetch('http://127.0.0.1:8000/api/messages')
      const data = await res.json()
      setMessages(data)
    } catch (err) {
      // handle error
    }
    setLoading(false)
  }

  async function handlePostMessage(e) {
    e.preventDefault()
    if (!newMessage.trim()) return
    try {
      await fetch('http://127.0.0.1:8000/api/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: user.userId, message: newMessage })
      })
      setNewMessage('')
      fetchMessages()
    } catch (err) {
      // handle error
    }
  }

  if (!user) {
    return <Login onLogin={setUser} />
  }

  return (
    <div className="main-layout">
      <div className="logout-container">
        <button className="logout-btn" onClick={() => setUser(null)}>
          Logout
        </button>
      </div>
      <aside className="sidebar">
        <h1>Welcome, {user.username}</h1>
        <p className="app-desc">
          Social Posts is a fun message board where people can post their thoughts and see what others are sharing. Join the conversation!
        </p>
      </aside>
        <section className="feed">
          <h2>Feed</h2>
          {loading ? (
            <div>Loading feed...</div>
          ) : (
            <ul style={{ listStyle: 'none', padding: 0 }}>
              {messages.map(msg => (
                <li key={msg.id} style={{ marginBottom: '1em', borderBottom: '1px solid #eee', paddingBottom: '0.5em' }}>
                  <strong>{msg.username}</strong>: {msg.message}
                </li>
              ))}
            </ul>
          )}
          <form className="post-form" onSubmit={handlePostMessage}>
            <input
              type="text"
              value={newMessage}
              onChange={e => setNewMessage(e.target.value)}
              placeholder="What's on your mind?"
              className="post-input"
            />
            <button className="post-btn" type="submit">Post</button>
          </form>
        </section>
      </div>
  )
}

export default App
