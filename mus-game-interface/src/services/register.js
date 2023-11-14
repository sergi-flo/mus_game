const register = async ({ username, password }) => {
  const csrfToken = document.cookie.split('; ').filter(row => row.startsWith('csrftoken=')).map(c => c.split('=')[1])[0]

  const response = await fetch('http://localhost:5000/user', {
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify({
      username,
      password
    }),
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    }
  })
  return response
}

export default { register }
