import { useState } from 'react'
import './App.css'

function App () {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [registrationMessage, setRegistrationMessage] = useState(null)

  const handleRegistration = async (event) => {
    event.preventDefault() // Prevent the default form submission behavior

    try {
      console.log('Submitting registration form...') // Add a debugging statement

      const response = await fetch('http://localhost:5000/user', {
        method: 'POST',
        body: JSON.stringify({
          username,
          password
        }),
        headers: {
          'Content-Type': 'application/json'
        }
      })

      const res = await response.json()

      console.log('Registration successful:', res.username)

      // Update the state to show the registration message
      setRegistrationMessage(`User ${res.username} registered successfully!`)

      // Reset the form fields
      setUsername('')
      setPassword('')
    } catch (error) {
      // Handle registration error
      setRegistrationMessage('Registration failed. Please try again.') //
    }
  }

  return (
    <div>
      <h1>Registration Page</h1>
      <form onSubmit={handleRegistration}>
        <label>Username:</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <br />
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <br />
        <button type="submit">Register</button>
      </form>

      {registrationMessage && <p>{registrationMessage}</p>}
    </div>
  )
}

export default App
