import { useState } from 'react'
import registerService from '../services/register.js'

const RegistrationPage = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [registrationMessage, setRegistrationMessage] = useState(null)

  const handleRegister = async (event) => {
    event.preventDefault() // Prevent the default form submission behavior

    console.log(`Registering with username: ${username} and password: ${password}`)

    try {
      const response = await registerService.register({ username, password })
      const message = await response.json()
      if (!response.ok) {
        // Handle registration error
        setRegistrationMessage(message.message)
        return
      }

      // Update the state to show the registration message
      setRegistrationMessage(`User ${username} registered successfully!`)

      // Reset the form fields
      setUsername('')
      setPassword('')
    } catch (error) {
      console.log(error)
      setRegistrationMessage('Registration failed. Please try again.')
    }
  }

  return (
    <main>
      <h1>Registration Page</h1>
      <form
        onSubmit={handleRegister}
      >
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={({ target }) => setUsername(target.value)}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={({ target }) => setPassword(target.value)}
          />
        </div>
        <button type="submit">Register</button>
      </form>
      {registrationMessage && <p>{registrationMessage}</p>}
    </main>
  )
}

export default RegistrationPage
