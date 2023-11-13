const register = async ({ username, password }) => {
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
  return response
}

export default { register }
